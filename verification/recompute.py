#!/usr/bin/env python3
"""Recalculate JSONL only; no API client, experiment-module imports, or network access."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import random
import statistics

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--log', required=True, type=Path, help='Path to the original runs.jsonl.')
parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parent)
parser.add_argument('--bootstrap-reps', type=int, default=100000)
args = parser.parse_args()
if args.bootstrap_reps < 1000:
    parser.error('--bootstrap-reps must be at least 1000.')
raw = args.log.read_bytes()
rows = []
for line, text in enumerate(raw.decode('utf-8').splitlines(), 1):
    if text.strip():
        r = json.loads(text)
        r['_line'] = line
        rows.append(r)

def mean(values):
    return sum(map(Fraction, values)) / len(values)

def bootstrap_ci(values):
    """Percentile interval of task-resampled medians; not a power calculation."""
    rng = random.Random(20260906)
    values = [float(v) for v in values]
    samples = sorted(statistics.median(rng.choices(values, k=len(values)))
                     for _ in range(args.bootstrap_reps))
    return [samples[int(.025 * len(samples))], samples[int(.975 * len(samples))]]

def exact_tests(differences):
    """Exact two-sided sign and signed-rank tests, dropping zero differences."""
    differences = [d for d in differences if d != 0]
    n = len(differences)
    if n == 0:
        return {'n_nonzero': 0, 'sign_p': None, 'wilcoxon_p': None}
    npos = sum(d > 0 for d in differences)
    nneg = n - npos
    sign_p = min(1., 2 * sum(math.comb(n, k) for k in range(min(npos, nneg) + 1)) / 2**n)
    sorted_abs = sorted(abs(d) for d in differences)
    ranks = [mean([i + 1 for i, a in enumerate(sorted_abs) if a == abs(d)])
             for d in differences]
    positive_rank_sum = sum(rank for d, rank in zip(differences, ranks) if d > 0)
    rank_total = sum(ranks)
    observed = min(positive_rank_sum, rank_total - positive_rank_sum)
    distribution = {Fraction(0): 1}
    for rank in ranks:
        following = Counter()
        for total, count in distribution.items():
            following[total] += count
            following[total + rank] += count
        distribution = following
    p = sum(count for total, count in distribution.items()
            if min(total, rank_total - total) <= observed) / 2**n
    return {'n_nonzero': n, 'increases': npos, 'decreases': nneg,
            'sign_p': sign_p, 'wilcoxon_W_min': float(observed), 'wilcoxon_p': p}

def cost_summary(rs):
    n_input = sum(r['input_tokens'] for r in rs)
    n_cached = sum(r['cached_tokens'] for r in rs)
    n_output = sum(r['output_tokens'] for r in rs)
    fresh_cost = (n_input - n_cached) * Fraction(10, 1000000)
    cached_cost = n_cached * Fraction(1, 1000000)
    output_cost = n_output * Fraction(50, 1000000)
    return {'records': len(rs), 'input_tokens': n_input, 'cached_tokens': n_cached,
            'output_tokens': n_output, 'reasoning_tokens': sum(r['reasoning_tokens'] for r in rs),
            'fresh_input_usd': float(fresh_cost), 'cached_input_usd': float(cached_cost),
            'output_usd': float(output_cost), 'estimated_usd': float(fresh_cost + cached_cost + output_cost),
            'rates_usd_per_million': {'input': 10, 'cached_input': 1, 'output': 50}}

def arm_summary(rs):
    return {arm: {'records': len(rr), 'raw_call_median': statistics.median(r['reasoning_tokens'] for r in rr),
                  'raw_call_mean': float(mean([r['reasoning_tokens'] for r in rr])),
                  'tasks': len({r['task'] for r in rr}),
                  'per_task_repetitions': dict(Counter(r['task'] for r in rr)),
                  'saved_correct': sum(r['correct'] for r in rr)}
            for arm in sorted({r['arm'] for r in rs})
            for rr in [[r for r in rs if r['arm'] == arm]]}

def contrast(rs, hi, lo, field='reasoning_tokens', aggregate=mean):
    cells = defaultdict(list)
    for r in rs:
        cells[r['task'], r['arm']].append(int(r[field]))
    tasks = sorted({r['task'] for r in rs})
    differences = {t: aggregate(cells[t, hi]) - aggregate(cells[t, lo]) for t in tasks}
    ds = list(differences.values())
    return {'high_arm': hi, 'low_arm': lo, 'field': field, 'aggregation': aggregate.__name__,
            'task_differences': {t: float(v) for t, v in differences.items()},
            'median_task_difference': float(statistics.median(ds)),
            'mean_task_difference': float(mean(ds)), 'median_bootstrap_95ci': bootstrap_ci(ds),
            **exact_tests(ds)}

result = {'input_sha256': hashlib.sha256(raw).hexdigest(), 'records': len(rows),
          'bootstrap_reps': args.bootstrap_reps, 'bootstrap_seed': 20260906,
          'waves': {}, 'contrasts': {}, 'scope': 'Saved records; no response-text regrading or billing reconciliation.'}
for wave in sorted({r['wave'] for r in rows}):
    rs = [r for r in rows if r['wave'] == wave]
    result['waves'][wave] = {'line_range': [min(r['_line'] for r in rs), max(r['_line'] for r in rs)],
                             **cost_summary(rs), 'arms': arm_summary(rs)}
result['all_costs'] = cost_summary(rows)
result['main_costs'] = cost_summary([r for r in rows if r['wave'] in ('main', 'main2')])
result['main_plus_smoke_arm_medians'] = arm_summary([r for r in rows if r['wave'] in ('main', 'smoke')])
result['main2_plus_smoke2_arm_medians'] = arm_summary([r for r in rows if r['wave'] in ('main2', 'smoke2')])
for wave, pairs in [('main', [('D_monitored','A_bare'), ('D_monitored','C_logged'),
                             ('C_logged','A_bare'), ('B_placebo','A_bare')]),
                    ('main2', [('RD_rule_monitored','RC_rule_logged'),
                              ('RD_rule_monitored','R0_rule'), ('RC_rule_logged','R0_rule')])]:
    rs = [r for r in rows if r['wave'] == wave]
    for hi, lo in pairs:
        result['contrasts'][f'{wave}:{hi}-{lo}'] = contrast(rs, hi, lo)
    control, treatment = pairs[1] if wave == 'main' else pairs[0]
    result['waves'][wave]['review_minus_logging_input_tokens'] = sorted({
        r['input_tokens'] - next(q['input_tokens'] for q in rs if q['task'] == r['task'] and q['arm'] == treatment)
        for r in rs if r['arm'] == control})
rs = [r for r in rows if r['wave'] == 'main2']
result['contrasts']['main2:min_reasoning'] = contrast(rs, 'RD_rule_monitored', 'RC_rule_logged', aggregate=min)
result['contrasts']['main2:compliant'] = contrast(rs, 'RD_rule_monitored', 'RC_rule_logged', field='compliant')
rule_rows = [r for r in rs if r['arm'] != 'A0_bare']
result['rule_records'] = {arm: {'n': len(ar), 'saved_compliant': sum(r['compliant'] for r in ar),
                              'saved_concealed': sum(r['concealed'] for r in ar),
                              'tasks': dict(Counter(r['task'] for r in ar))}
                          for arm in ['R0_rule','RC_rule_logged','RD_rule_monitored']
                          for ar in [[r for r in rule_rows if r['arm'] == arm]]}
result['violation_rows'] = [{k: r[k] for k in ['_line','task','arm','rep','steps_found','steps_dup','self_report','concealed']}
                            for r in rule_rows if not r['compliant']]
result['binomial_zero_formulas'] = {
    'rule_of_three_36': 3/36,
    'one_sided_95_upper_36': 1 - .05**(1/36),
    'two_sided_95_upper_36': 1 - .025**(1/36),
    'one_sided_95_upper_12_independent_clusters': 1 - .05**(1/12),
    'one_sided_95_upper_3_for_one_task': 1 - .05**(1/3),
    'probability_zero_36_when_p_15pct': .85**36,
    'miss_10pct_event_in_five_trials': .9**5,
    'assumption': 'Independent Bernoulli trials; common p, or a separately justified fixed-design average rate.'}
result['brief_ci_arithmetic_not_power'] = {
    'v1_8_3_div_53': 8.3/53, 'v1_4_8_div_53': 4.8/53,
    'v2_20_8_div_191': 20.8/191, 'v2_3_9_div_191': 3.9/191,
    'hypothetical_sign_p_12_same_sign_arbitrarily_small_nonzero_differences': 2/(2**12)}
result['provenance_fields'] = {key: dict(Counter(str(r.get(key)) for r in rows))
                               for key in ['model','effort','rt_used_source','visible_token_method','status']}
result['duplicate_job_keys'] = len(rows) - len({(r['wave'],r['task'],r['arm'],r['rep'],r['effort']) for r in rows})
result['duplicate_response_ids'] = len(rows) - len({r['response_id'] for r in rows})
args.output_dir.mkdir(parents=True, exist_ok=True)
output = args.output_dir/'results.json'
output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(f'Saved {output}; {len(rows)} records, main estimated cost ${result["main_costs"]["estimated_usd"]:.5f}.')

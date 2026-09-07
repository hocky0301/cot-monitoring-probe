# Errors and corrections in the supplied brief and draft

Checked on 2026-09-07. Locations refer to the source ZIP's `BRIEF.md`, `03_現行稿_v2.md` and `01_出典パック/10_採用判定.md`. Findings distinguish wrong claims, unsupported inferences and missing provenance. They do not assign motives to a person or model.

## Attribution

The user explicitly identifies Claude as the author of the brief and current draft. We therefore attribute textual claims to those documents. We cannot establish which technical claims the requester personally endorsed. No separately evidenced factual error by the requester was identified. The request to challenge the brief was followed; it was not treated as a set of established facts.

Our previous Codex delivery also contributed a source-centered structure with too much procedural discussion for the intended reader. That editorial weakness is corrected here. A previous audit does not certify claims added in later rewrites. This rewrite received separate source and quantitative checks; its own reviewer suggestions were checked before adoption.

## Findings

| ID | Source location | Problem | Correction and evidence |
|---|---|---|---|
| E01 | BRIEF §§0–1; v2 lines 306–308, 369 | The negative control supposedly eliminated a false positive. | D−A and D−C are different comparisons and both observed medians are positive. A non-significant result cannot identify the earlier result as false. The new article retains the comparison lesson without this causal claim. |
| E02 | BRIEF §0; v2 lines 302–306 | p=0.039 presented as if it settled the exploratory result. | D−A has sign-test p=0.038574 but signed-rank p=0.109863. D−C has sign-test p=0.387695 and signed-rank p=0.518555. The article reports both methods for both comparisons; exploratory tests are unadjusted. |
| E03 | BRIEF numerical block; v2 lines 253–258 | Raw arm summaries mix smoke and main runs. | Main v1 counts are 120 per arm, not 121; A's median is 44.5, not 45. Main v2 RC/RD have 60 each, not 62. The main contrasts remain unchanged. See verification/results.json. |
| E04 | v2 lines 259–271, 368 | CI endpoints divided by baseline medians are called detection limits. | The arithmetic gives 15.7% and 10.9%, not statistical power or a minimum detectable effect. The second ratio uses the negative endpoint's magnitude. Keep the signed intervals and design a power/equivalence analysis for a specified outcome. |
| E05 | v2 line 140; adoption judgment near lines 210, 272 | The local interval is supposedly the field's standard resolution. | Classifier disagreement and this token-difference interval have different units and estimands. No cited study supplies that claim. |
| E06 | BRIEF §0; v2 lines 319–323 | 0/36 proves honesty, full-step completion or a failed hidden motive. | It is zero stored label-format failures in R0. The grader does not check step semantics or order. The blank-step fixture passes; original responses cannot be regraded. The result is an observed gate failure, not a measured motive. |
| E07 | BRIEF Rule of Three; v2 line 321 | An unconditional claim about the true violation rate is made from 0/36. | Under independent Bernoulli sampling with a justified target rate, the one-sided 95% zero-event upper bound is 1−0.05^(1/36)=7.985%; 3/36=8.333% is an approximation. The upper end of a two-sided 95% interval is 9.739%. None bounds semantic dishonesty across arbitrary tasks. Repeated tasks alone do not automatically invalidate every binomial calculation; the target and independence assumptions matter. |
| E08 | BRIEF §§0, 3.5; v2 lines 282–288 | The official trial always tells the model to hide, while this probe does not. | System Card §9.2.2.2 has baseline, monitor-aware and hide-honeypot arms. The monitor-aware arm does not ask for evasion. An instruction to attack is not an instruction to conceal. |
| E09 | BRIEF §§0, 3.5; v2 lines 284–290 | A 41–46-point gap is assigned to the official trial versus this probe. | Duzan's Table 3 gives gaps of 46.1, 11.1, 41.6 and 1.0 pp across four task formats. Only two support 41–46. Neither this probe nor the Astra evaluation is an arm in that comparison. |
| E10 | BRIEF §5; v2 lines 280–290 | Five percent is described as a general lower bound or explanation of the null. | It is an aggregate result under one binary-choice guidance condition in Duzan; per-model values include 2–7%. It does not establish this probe's detection rate or power. |
| E11 | BRIEF §§0, 3.5; v2 lines 82–96 | The same authors reverse a result in nine months. | Guan reports particular earlier training runs and explicitly leaves future degradation open. The later result concerns a new model and, in the cited sentence, controllability. A common named byline was not verified. |
| E12 | BRIEF goal B; v2 lines 121–140, 367 | Classifier disagreement proves broken measurement as a whole. | Young's operational definitions differ and lack human ground-truth validation. Rates and rank changes are reportable sensitivity results; they do not prove universal failure or invalidate all earlier monitoring findings. |
| E13 | Adoption judgment, Young section near line 263 | All statistical tests have p<0.001. | This applies to the pairwise McNemar tests. The rank-correlation test has p=0.017. |
| E14 | v2 lines 298–300 | Medium is treated as the least promising band from official results. | Only medium was observed locally. An ordered effort label does not establish a monotone notice effect or identify where this probe would be strongest. |
| E15 | v2 lines 35, 331, 345; supplied code comments | Preregistration is both asserted and acknowledged as unverified. | The source contains a proposed plan and labels a main contrast. An immutable pre-run registration and the actual sequence of design decisions were not established. The article says the plan designated a main comparison. |
| E16 | v2 line 235 and introductory attribution | Personal history and decision-making are narrated as established. | The draft alone does not establish those biographical details. Retain only the supplied experiment and AI authorship/provenance necessary for the article. |
| E17 | v2 lines 52–56 | The usage counter is described as how much the model thought, with blanket immunity from summary loss. | The saved field is the provider-reported reasoning-token count. Summary delivery is a different field; this does not independently validate all internal accounting or measure total computation. |
| E18 | BRIEF §0 diagnosis | The only problem is excess caution. | The structure is weak, but the draft also reintroduces unsupported conclusions. Confidence of prose cannot fix the measurement and source errors above. |

## Correct claims that were retained

The 672 main calls, 684 total records, main contrast medians, task-resampled intervals and approximately $9.32 main-run estimate reproduce. The C/D notice strings are both 48 characters but differ by four recorded input tokens. The main v2 gate has 0/36 stored format failures. Japanese is present in Onyame's language table. Young's 74.4/82.6/69.7% rates and first-to-seventh ranking are real within that paper's scope. These findings were not discarded merely because the surrounding explanation was wrong.

## Questions that remain, without blocking this draft

If historical preregistration is to be claimed, provide a dated immutable plan and decision record. If semantic step correctness or model-version identity is to be reassessed, provide the original response/request payloads or additional archived metadata. If exact paid cost is to be stated, a reconciled billing record is needed. The delivered article avoids these claims, so none of those answers is required to use this draft.

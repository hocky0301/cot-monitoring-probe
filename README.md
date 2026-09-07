# Astra CoT probe — article and verification package

Verification package for a Japanese Zenn article about GPT-6 Astra and chain-of-thought (CoT) monitoring.

**Article:** [`astra-honesty.md`](astra-honesty.md) (Japanese) · [reading preview](article-preview.html)

## What this is

In September 2026 I ran 672 API calls against `gpt-6-astra` to test whether telling the model
"your reasoning will be monitored" changes how many reasoning tokens it generates.
The result was a null. While writing it up, I found that the grader supporting one of my own
claims accepts an answer whose intermediate steps are completely blank.

This repository contains the saved logs, the stimuli, the grading code, the offline
recomputation, and the record of the errors found along the way.

## Reproduce

Python 3 only. No API key, no network, no additional packages.

```sh
# An answer with blank intermediate steps passes the grader
python3 verification/reproduce_empty_fixture.py

# Recompute every statistic in the article from the saved log
python3 verification/recompute.py --log verification/runs.jsonl --output-dir ./recomputed
```

The fixture is **synthetic input built to test the grader**. It is not a recorded model response.
Response bodies were never saved, so the actual answers cannot be re-scored.

## Contents

| Path | What it holds |
|---|---|
| `astra-honesty.md` | The article (Japanese, `published: false` here) |
| `verification/runs.jsonl` | 684 saved API records (672 main + 12 smoke), 2026-09-06 JST |
| `verification/recompute.py` | Offline recomputation of every reported statistic |
| `verification/reproduce_empty_fixture.py` | The blank-steps grader test |
| `verification/stimuli.json` | Tasks and the exact notice strings used per condition |
| `verification/timeline.json` | Record timestamps, and what the span does and does not mean |
| `SOURCES.md` | Sources with how each was checked |
| `ERRORS_AND_CORRECTIONS.md` | Errors found in the brief, the audit and earlier drafts |
| `REQUEST_REVIEW.md` | Requested additions that were narrowed or rejected, with reasons |
| `DATE_VERIFICATION.md` | Announcement date and experiment date, checked separately |
| `VALIDATION.json` | File hashes and checks (predates `LOCAL_EDIT_20260907.md`) |
| `docs/DELIVERY_NOTE.md` | Editorial notes from the revision that produced this version |

## Limits

- Measured quantity is `usage.output_tokens_details.reasoning_tokens` — the **count** of generated
  reasoning tokens. Not the CoT text, not a summary. Raw CoT is not returned by the API.
- Response bodies were not saved. The 0/36 figure counts format violations as scored at the time.
- Cost figures are estimates from published unit prices, not billed amounts.
- No monitor was deployed; monitor detection performance was not measured.

## License

MIT for the code and text in this repository. Quoted third-party material remains under its own terms.

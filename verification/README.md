# Offline evidence for the article rewrite

`evidence_report.md` explains which claims can support a reader-centered article. `results.json` contains fresh calculations from the newly supplied log. `source_evidence.json` records the source hashes, literal notices, and synthetic grading fixtures. `stimuli.json` contains the literal task and prompt configuration extracted from the supplied source, not archived request payloads. `runs.jsonl` is byte-identical to the supplied 684-row log.

`verification.json` confirms agreement with the earlier audit and with the original bootstrap's 10,000-resample, seed20260906 primary intervals at article precision. `source_evidence.json` includes both the numbered999 fixture and the exact empty-line fixture used in the article, clearly marked synthetic.

The portable recalculation needs only the original JSONL and the Python standard library:

```sh
python3 recompute.py --log ./runs.jsonl --output-dir ./recomputed
```

It never imports the experiment runner and contains no API interface. It does not execute requests, regenerate responses, independently recover the missing response text, or reconcile billing. Bootstrap defaults to 100,000 task resamples, seed 20260906. Prices are the original code's assumptions: $10/M input, $1/M cached input, and $50/M output.

The current primary dataset contains 672 main-run records. All 684 records include 12 preliminary calls. Keep these scopes separate when quoting medians, counts, and costs.


## Blank-step example in the narrative revision

Run `python3 reproduce_empty_fixture.py` from this directory to reproduce the synthetic empty-step example. `fixture_reproduction.json` records the output and the optional AST comparison with the supplied original runner. Four constants and `grade_v2` match the original executable AST, ignoring the translated docstring and source locations. The original API runner was never imported. This tests the grader; it does not reconstruct any original model answer.

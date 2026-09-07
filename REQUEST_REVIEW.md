# Review of the new expansion request

The newly supplied request was checked against the System Card and the existing evidence package on September 7, 2026. The request's quoted passages are useful inputs, not automatic validation of the conclusions attached to them.

| Request | Decision and implementation |
|---|---|
| Add the three-generation example from Table 9 | Added after the empty-answer scene and the contradictory draft wording. The passage describes visible behavior: deliberation about compliance, a move to mostly symbolic calculation, and immediate alternating case. It does not invent an argument with the model or assert an inferred escape intention. Correctness of the three examples is attributed to OpenAI's caption. |
| Reproduce Astra's alternating-case output | Included a nine-word opening excerpt. The supplied excerpt omits its first word, `SuRvIvAl`, and normalizes some spacing; it is not an exact complete transcription. The short excerpt was checked directly against the live card. A full trace is unnecessary to show the change in writing. |
| Add 1.7%, 16.1%, and 60.9% | Added with the 750–1,250-token band and QA scope beside the numbers. They concern adherence to reasoning-text constraints, not answer accuracy or successful monitor evasion. The single examples use the same reasoning effort; the aggregate rates compare a length band. |
| Describe the evaluation as more than 13,000 tasks | Retained in the appendix as suite size. Published results are restricted to three QA datasets and eight instruction types. The card does not report the number of examples in this particular length bin, so 13,000 is not used as the rates' denominator. |
| Say capability improvement directly becomes a safety regression | Rejected as a general conclusion. The card treats control of reasoning text as an early warning for monitoring and evasion capability. The article explains the tension specifically for oversight that depends on reading CoT, not overall safety or ordinary-use dishonesty. |
| Connect short CoT to the 672 local observations | Accepted. The former draft put too much distance between the official concern and the useful local measure. The article now makes their common length axis explicit. |
| Treat the local counter as exactly the same causal variable and measurement as the official study | Narrowed. The API records generated reasoning-token usage; exact counting and aggregation equivalence with the official plots is not established. The local intervention is a notice string, and token length is an outcome. It compares the same requested model, while the official central comparison is Astra versus Sol. Local monitor outcomes were never measured. |
| Treat longer-CoT recovery as proof that making a response longer restores monitoring | Rejected. The official discussion includes comparisons by length and residual environment differences. It does not establish that intervention as a universal remedy. |
| Explain CoT, reasoning tokens and negative controls on first use | Added short definitions. The intended negative control is the non-monitoring sentence B. The recorded-only condition C is a separate comparator and is not renamed as the negative control. |
| Describe the empty-answer moment more closely | Added the construction order: labels, blank step contents, the no-omission self-report, the final answer, and submission to the grader. It remains explicitly synthetic; no unrecorded surprise, time pressure or original model response is invented. |
| Give a 30-second action | Delivered a one-command offline reproduction using existing Python code, plus one specific adaptation for a reader's grader. No human completion time is claimed. The default command reproduces the result; it does not redo the optional source-AST comparison on each run. |
| Preserve the ending, details block and explicit attribution of overclaims | Preserved the final two statements exactly. Existing methods and limits stay collapsed. The article names Claude's draft and the request passed along by the author without falsely saying the author personally wrote the Claude-authored brief. |

## Material moved or omitted

The detailed honeypot monitoring example moved from the main story to the existing appendix so the new three-generation scene and the length connection could carry the argument. Its scope and 100% full-context recall in that setting remain available. The two named environments with residual length-matched differences are also in the appendix. The suite inventory remains there rather than interrupting the numerical comparison.

The main text does not reproduce the entire Table 9 trace, introduce a new checklist, claim a new API experiment, or assert a new model capability measurement. No required addition was dropped for lack of time.

## Source locations

- [System Card](https://deploymentsafety.openai.com/gpt-6-astra/vision): §§9.1.2–9.1.3 for length and information; §9.2.1, Table 9 and Table 10 for controllability; §9.2.2.2 for the retained honeypot example.
- [Reasoning guide](https://developers.openai.com/api/docs/guides/reasoning): reasoning-token usage and unavailable raw reasoning text.
- Local evidence: `verification/results.json`, `verification/source_evidence.json`, `verification/reproduce_empty_fixture.py` and the original saved `verification/runs.jsonl`.

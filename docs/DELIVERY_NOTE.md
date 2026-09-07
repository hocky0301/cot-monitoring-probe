# Astra article — expanded narrative revision

Read [the Japanese article](astra-honesty.md) or [the reading preview](article-preview.html).

The article now connects three observed scenes: an empty answer passes the local grader; three model generations handle the same reasoning-text constraint differently; and a model can become easier to direct while creating concerns for text-based monitoring. The official discussion of shorter reasoning is connected to the local API token counts without claiming a reproduction of the official causal explanation.

The existing title and final two statements are preserved. The opening now places 672 main observations and the estimated $9.32 cost on September 6 (JST), three days after the published announcement date of September 3; timestamp details are in the appendix. Numerical methods, conditions and limitations remain in a collapsed appendix. The main text gives one offline command for reproducing the empty-answer result, then invites readers to try removing intermediate work from a valid answer in their own grader.

## Package

- `astra-honesty.md`: Japanese Zenn article; `published: false`; one inline Mermaid diagram.
- `article-preview.html`: self-contained Japanese preview with a rendered diagram and collapsible methods appendix.
- `EDITORIAL_DECISIONS.md`: narrative decisions for this revision.
- `REQUEST_REVIEW.md`: accepted additions and corrections to claims in the expansion request.
- `DATE_VERIFICATION.md` and `verification/timeline.json`: announcement date, independently recomputed record times, and the distinction between record span and runtime.
- `SOURCES.md`: verified sources, including the newly used System Card example.
- `RESEARCH_MAP.md` and `ERRORS_AND_CORRECTIONS.md`: retained research and correction records from the previous delivery.
- `verification/`: original saved responses, extracted stimuli, offline recomputation, grader evidence and its reproduction.
- `VALIDATION.json`: checks and file hashes for this revision.

## Verify the central example

```sh
python3 verification/reproduce_empty_fixture.py
```

This exercises the extracted grading function with a synthetic answer containing blank intermediate steps. The fixture is not an observed Astra response. Actual response bodies were not saved, so their intermediate calculations cannot be recovered or rescored.

To recalculate the saved numerical observations:

```sh
python3 verification/recompute.py --log verification/runs.jsonl --output-dir ./recomputed
```

Both commands run offline with Python's standard library. No additional paid experiment was performed.

## Status and language

This is a local draft. The supplied inputs and previous delivery remain intact. No publication, repository upload, video upload or X post occurred. The reading preview is not a verified live Zenn rendering.

The Zenn article and its reading preview are Japanese. Repository documentation, new comments and supporting reports are English. Literal source quotations and experimental inputs keep their original language. The continuing media policy is an English 4–5 minute introduction video with English subtitles or narration, unlisted on YouTube, and English X copy. Those media are not part of this article revision.

Before external publication, attach a public download or repository URL for this verification package. The article currently names the included files because no public evidence URL has been supplied.

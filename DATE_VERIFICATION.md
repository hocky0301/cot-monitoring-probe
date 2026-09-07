# Date and timestamp verification

Checked on September 7, 2026. The opening now combines the September 3 announcement, September 6 JST main experiment, 672 main observations and estimated cost of $9.32 in one sentence. The title, front matter, closing statements and pre-existing numerical evidence are unchanged.

## Public date

[OpenAI's safety overview](https://openai.com/index/safety-overview-gpt-6-astra/) displays September 3, 2026 and announces the release. The [System Card](https://deploymentsafety.openai.com/gpt-6-astra/vision) separately displays the same publication date. These are first-party sources for the article's date anchor.

The [launch page](https://openai.com/index/gpt-6-astra/) describes limited initial access and broader availability over the coming days. It does not provide an exact general API availability start time. The article does not use that event as its starting point. The request's additional September 1 and September 4 chronology is unnecessary for the selected anchor and is not reproduced as a newly verified timeline.

“Three days” refers to the difference between the published date label and the JST experiment date. It does not mean an exact 72-hour interval across time zones.

## Saved observations

All 684 records fall on September 6, 2026 JST under both `ts` and `iso`. The main subset is selected by `wave` equal to `main` or `main2`.

| Subset | Records | First `ts`, JST | Last `ts`, JST | Span in seconds |
|---|---:|---|---|---:|
| All, including smoke runs | 684 | 17:17:03.746200 | 19:15:22.226791 | 7,098.480591 |
| Main runs only | 672 | 17:23:30.498003 | 19:15:22.226791 | 6,711.728788 |

The request's 7,098 seconds agrees with the all-record span rounded to whole seconds. Its description as execution duration is too strong. In the original runner, the API request begins at line 598; elapsed request time and `now` are obtained at lines 615–616 after the request returns. The saved `ts` uses that value at line 668, while `iso` is generated separately. The difference between those fields is at most about 1.04 milliseconds in these records.

The timestamps therefore describe completed-response records. They do not establish the first request's start time, continuous active execution, or preparation and analysis time. There are substantial gaps between waves. At the user's request, the article omits time ranges and durations, retaining the verified experiment date. The detailed timestamp audit remains in this supporting report and the saved data.

The full precision, both timestamp fields, per-wave ranges and log hash are in `verification/timeline.json`. `verification/results.json` remains unchanged and supplies the $9.32296 main-run estimate; no billing statement was checked.

The unverified two-day ChatGPT/Codex usage account is not added. No new API experiment, productivity claim or publication is made.

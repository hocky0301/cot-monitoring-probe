# Research map and decisions

Checked on 2026-09-07 JST. Full bibliographic details and verification methods are in SOURCES.md. This is a bounded editorial search, not an exhaustive review or a claim that the article is the first of its kind.

## 1. Japanese readers already have explanations and use reports

| Existing coverage | What it already offers | Consequence for this article |
|---|---|---|
| Arts & Crafts, September 4; SOURCES A6 | Direct explanation of CoT monitorability, notice-induced shortening, and monitor input scopes. | A generic explanation of the official report would overlap. |
| 平凡梵 on Zenn, September 5; A7 | Firsthand Astra debugging account that separates the model from its tool environment and notes the absence of a controlled comparison. | Do not claim to introduce careful hands-on testing to Japanese readers. |
| Box Japan, header September 4; R4 | Commercial evaluation of business-document work. Its page has an unresolved date inconsistency. | Capability use cases exist; they do not answer the monitoring question. |
| AI総合研究所, displayed September 4; R5 | Broad product guide with attention to evaluation settings and harness differences. | Practical qualifications alone are not a distinctive contribution. |

The defensible space is **a small API experiment whose actual prompts, task-level comparisons and grader can be inspected**. This is an editorial opportunity inferred from the sampled coverage, not proof that no similar work exists. The rewrite makes the reader perform a useful operation: name the comparator, inspect what passes the grader, and identify the measured output field.

Searches included Japanese terms for CoT monitoring, faithfulness and thought visibility, paired with GPT-6 Astra; domain searches for Zenn and Qiita; and exact English monitorability searches. Google's Project Astra, astronomy and unrelated ASTRA benchmarks were excluded. Search-result snippets were only discovery leads.

## 2. Japanese is included in Onyame's thirteen languages

**Yes.** Appendix C, Table 6, printed p.22 of arXiv:2605.27901v1 lists Japanese under Japonic. The exact list is English, German, French, Spanish, Russian, Bengali, Arabic, Chinese, Japanese, Korean, Swahili, Telugu and Vietnamese. The table and surrounding method were opened; the question is resolved from the body, not guessed from the abstract. See SOURCES P1.

The study uses controlled multilingual hint interventions. It supplies no Japanese-specific result for Astra and does not measure this probe's token-count contrast. The answer is retained here rather than becoming a detour in the main article.

## 3. The post-launch debate is current and heterogeneous

| Date | Original source | What the record supports |
|---|---|---|
| September 3 | OpenAI safety overview, R1 | The developer presents improved alignment and diminished monitorability together. These are distinct evaluation claims. |
| September 4 | Simon Willison, R2 | A firsthand SVG-generation comparison across models/settings. It is a narrow use report; a linked transcript's Astra/Nova label mismatch remains unresolved. |
| September 4 | William Harrison, R3 | External safety-community criticism of OpenAI's alignment interpretation. It is an argument by a self-described aspiring researcher, not independent proof or consensus. |
| September 5 | Zenn account, A7 | Japanese practitioner testimony, with explicit comparison limits. |
| September 6 | Jakub Pachocki, “An Alien Mind,” A3 | A current official researcher essay on the difficulty of relying on CoT monitoring. Included in the rewritten article as an attributed view. |

The September 2 Zvi post (R6) was opened and identified as prelaunch commentary. It must not be recast as a response to the released September 3 card merely because a Japanese summary appeared later. Original dated post-launch statements by Ryan Greenblatt and Buck Shlegeris were not recovered in this search. Linked X pages returned access failures. No claim of their post-launch position is made.

The article is therefore situated after the September 6 essay, while keeping the September 6 local experiment separate from other people's reactions. Nothing in this reaction sample turns the token-count null into a finding about architecture or ordinary-use evasion rates.

## 4. Hawthorne is a poor causal frame for this experiment

Levitt and List's reanalysis of the original illumination records challenges the familiar simple productivity story and finds that the design permits only limited conclusions; it does not establish that every observer effect is imaginary. McCambridge and colleagues' review abstract describes heterogeneous research-participation effects and uncertainty about conditions and mechanisms. The first paper's full text and the second paper's institutional abstract were checked (H1–H2).

These studies can motivate attention to experimental context. They cannot identify a psychological mechanism in an LLM. Here the observed intervention is a change in prompt text. Calling it a Hawthorne effect would import more than the experiment measured. **The analogy was researched and deliberately omitted**, rather than left unexamined or removed for time.

## Literature-to-article boundary

The four primary-paper checks requested or emphasized by the brief were completed: Onyame, Duzan/Cooper Stickland, Young and Guan. Their numerical results and scopes were checked against full text. The article does not borrow a detector's percentage-point gap as its statistical power, a classifier ranking as evidence that all measurement is broken, or an earlier scoped study as a later author's retraction. Corrections are in ERRORS_AND_CORRECTIONS.md.

## Search limits and stopping rule

The search covered Japanese explainers and use reports, original official and external post-launch commentary, the named language question and the historical analogy. It stopped after each question had evidence sufficient for the editorial decision. It did not quantify popularity, represent all Japanese readers, review inaccessible X posts, independently reproduce third-party demonstrations, or certify the entire source pack. Missing originals remain missing; they were not replaced with invented quotations.

# FACTCHECK — Pick a Number, Any Number
`claude-liam-two-numbers-one-report` · rev 4 · 2026-08-19

Key: ✅ VERIFIED (primary source) · ⚠️ SOFTENED · 🔲 BUILD-DAY live check required · 🔶 INFERENCE (Honesty Law 1)

---

| # | Beat | Claim | Verdict | Source / Derivation | Action |
|---|---|---|---|---|---|
| 1 | B01 | Study design: 4 detection tools, 160 documents, known ground truth, preregistered (AsPredicted #228383), data and prompts published on OSF | ✅ VERIFIED | Primary paper. Confirmed in TL;DR and field-placement sections of who-wrote-this-skeptical-read.md. OSF: https://osf.io/4p5ab/ | None — verified from primary. |
| 2 | B03 | Three tools scored 0% strict accuracy on fully AI-generated papers (n=40) | ✅ VERIFIED | Primary paper Table 4, fully AI-generated condition. "Turnitin 40 FN (0%), GPTZero 0%, Copyleaks 0%." Narration says "scored zero" — accurate for both interpretations. | None. |
| 3 | B03 / B04 | Fourth tool: 65% strict accuracy / 97.5% inclusive accuracy on fully AI-generated papers | ✅ VERIFIED | Primary paper Table 4. Both figures must appear together in B04 — hard constraint. | None — verified. |
| 4 | B04 | "Inclusive" classification: a score of 60–80% on a 100%-machine document counts as a correct detection | ✅ VERIFIED | Primary paper Table 3 classification scales. | None — verified. |
| 5 | B05 | Human corpus: 40 master's theses, non-native English speakers, written pre-2019, zero false positives | ✅ VERIFIED | Primary paper Table 4 (fully human condition) and methods section. | None — verified. |
| 6 | B17 | Generator confound: fully-AI condition used GPT-4o Deep Research; hybrid and humanised conditions used plain GPT-4o | ✅ VERIFIED | Primary paper Discussion section. Condition and model perfectly entangled. | None — verified. |
| 7 | B07 | Abstract quote: "should not be used as sole evidence in high-stakes decision-making but should be implemented in a broader evaluation strategy" | ✅ VERIFIED | Primary paper abstract. Quoted verbatim in who-wrote-this-skeptical-read.md. Quote card in B07 must match character-for-character. | Verify character-for-character against the live paper before ship. DOI: https://doi.org/10.1007/s40979-026-00226-w |
| 8 | BRM | Four figures from Pangram social-media report: 13.8% (global average, all platforms), 21.9% (Substack combined AI-generated + AI-assisted), 25.72% (longform >250 words, all platforms, fully AI), 40%+ (LinkedIn longform, fully AI) | 🔲 BUILD-DAY | As provided in reframe brief. Require live verification against the Pangram report on build day, plus archive capture. | Build day: visit report live, verify all four figures verbatim, capture to web.archive.org. Log URL in SOURCES.md. |
| 9 | BRM | Report sentence: "Substack, which was the longform platform with the lowest combined AI rate, still saw more than a fifth of its posts (21.9%) flag as AI-generated or AI-assisted." And: "Substack was an exception." | 🔲 BUILD-DAY | As provided in reframe brief. Character-for-character verification required. | Same as row 8. |
| 10 | BRM / B13 | Best's quote: "as much as 40% on some platforms, according to Pangram's estimate" — from "Against Claudefishing" (Substack post, Chris Best, 21 July 2026) | 🔲 BUILD-DAY | As provided in reframe brief. | Build day: verify verbatim in the live post, capture to web.archive.org. Log URL in SOURCES.md. |
| 11 | B09 / B10 / B13 / B14 | Vendor page: wording, two figures quoted (97.5%, zero FP), citation by institution+month | 🔲 BUILD-DAY | Cannot verify without live access. | Same build-day verification requirement as rev 3. |
| 12 | B14 | Platform link resolves to vendor evaluations page (not to the paper itself) | 🔲 BUILD-DAY | Cannot verify without live access. | Same as row 11. |
| 13 | B09 | The study on the vendor page is the same paper (Van Vlasselaer et al. 2026) | 🔶 INFERENCE | Governed by Honesty Law 1. Four converging details: same university, same month, four tools compared, two figures matching Table 4 exactly. | B09 MUST display the INFERENCE label on screen. |
| 14 | B13 / B14 | Pangram self-reports 0.01% false-positive rate on its evaluations page | 🔲 BUILD-DAY | As provided in reframe brief. | Build day: verify on the live evaluations page, capture to web.archive.org. |
| 15 | BDTL | The six decimal-point figures shown together: 13.8, 21.9, 25.72, 65.0, 97.5, 0.01 | ✅ / 🔲 COMPOSITE | 13.8, 21.9, 25.72, 40+ from Pangram report (row 8); 65.0 and 97.5 from primary paper Table 4 (row 3); 0.01 from vendor page (row 14). Build-day items in this composite must be verified. | Carry forward build-day status for rows 8, 14. |

### MATHINESS — attribution note
"Mathiness" is used as a plain word with no attribution, no date, no name. Attribution is contested;
the word does not need an owner. If a beat defines it, define it in the film's own words against
the film's own evidence — six decimal points doing work the measurement never authorised.

---

## Honesty Law compliance — pre-ship checklist

- [ ] **LAW 1 (INFERENCE):** B09 INFERENCE label confirmed visible on screen in final cut.
- [ ] **LAW 2 (NOT ONLY SOURCE):** B09 narration and on-screen content confirm vendor page cites other academic studies and commercial reviews.
- [ ] **LAW 3a (NAME PUBLISHERS):** B13/B14 name Substack, "Against Claudefishing," and Pangram's evaluations page. Viewer can follow all links.
- [ ] **LAW 3b (PROTECT AUTHORS):** No paper title, author names, or university name anywhere in narration or on-screen text.
- [ ] **LAW 4 (PAPER'S DUE):** B01 opens with paper's credentials. B07 quotes the abstract. BVDT verdict line: "The study is careful." Preregistered status and OSF data availability acknowledged.

## SYMMETRY CHECK — pre-ship

- [ ] **40% and 21.9% appear together on screen** (in BRM)
- [ ] **97.5% and 65% appear together on screen** (in B04 and B10)
- [ ] **B09 inference label still present** on screen
- [ ] **Substack and Pangram named on screen** (B13/B14)
- [ ] **Paper and its authors NOT named** anywhere
- [ ] Every spoken number matches the rendered number
- [ ] Every name spoken matches what is on screen
- [ ] No ranked or grouped set is read partially — if four figures shown, four accounted for

## Build-day gate — before any audio spend or render

- [ ] Row 7: Confirm abstract quote character-for-character against live paper (DOI: https://doi.org/10.1007/s40979-026-00226-w)
- [ ] Rows 8–9: Visit Pangram social-media report live — verify all four figures and the "Substack was an exception" sentence verbatim. Capture to web.archive.org. Log URL in SOURCES.md.
- [ ] Row 10: Visit "Against Claudefishing" post live — verify Best quote verbatim. Capture to web.archive.org. Log URL in SOURCES.md.
- [ ] Rows 11–12: Visit Pangram evaluations page + platform announcement live. Capture both. Log URLs.
- [ ] Row 14: Verify 0.01% FP rate on evaluations page. Log.
- [ ] Row 13 INFERENCE: Check whether vendor page now cites the paper by DOI/title/authors. Update B09 if so.

# CHECKS-REPORT — Pick a Number, Any Number
`claude-liam-two-numbers-one-report` · rev 4 · 2026-08-19

---

## Gates

| Gate | Result | Notes |
|---|---|---|
| GATE-F (frame-check) | ✅ PASS | — |
| GATE-L (lane-check) | ✅ PASS | 24/24 beats, no lane violations |
| GATE-BANNED-CARD | ✅ PASS | No SlateCard, no banned patterns |
| GATE-SWEEP-WARN | ✅ PASS | — |
| GATE-P | ✅ PASS | — |
| GATE-G | ✅ PASS | — |
| GATE-V (visual QC) | ✅ PASS | BLOCKER=0, STRUCTURAL=0, COSMETIC=0 |
| GATE-T (kerning/type) | ✅ PASS | 0 FAILs |

---

## Slots

24/24 filled:
`B00:VIDEO B01:VIDEO B02:VIDEO B03:MANIM B04:VIDEO B05:MANIM B06:VIDEO B07:MANIM BRA:VIDEO BRM:MANIM B08:VIDEO B09:VIDEO B10:MANIM B11:VIDEO B12:VIDEO B13:VIDEO B14:MANIM B15:VIDEO B16:MANIM B17:MANIM BDTL:MANIM BVDT:VIDEO BHTF:VIDEO BOUT:VIDEO`

Duration: **290.9s** (~4:51)

---

## Symmetry check (frame-verified)

| Requirement | Result | Notes |
|---|---|---|
| 40% and 21.9% appear together on screen (BRM) | ✅ PASS | Verified at t=105s — all 4 rows visible; 40% terracotta, 21.9% labeled "Substack combined rate"; rows 1–3 dimmed but readable |
| 97.5% and 65% appear together on screen (B04) | ✅ PASS | Verified at t=44s — DeckPattern STRICT/INCLUSIVE columns; both numbers in the same frame |
| B09 INFERENCE label present on screen | ✅ PASS | Verified at t=120s — "INFERENCE — Four Converging Details, No Direct Citation" is the title |
| Substack and Pangram named on screen | ✅ PASS | B13 (t=165s): "CHRIS BEST · SUBSTACK · 21 JUL 2026" named; B09: "PANGRAM EVALUATIONS PAGE" named |
| Paper and authors NOT named anywhere | ✅ PASS | B09 shows "THE PAPER" (no authors, no title, no university) |
| Six decimal figures visible in BDTL | ✅ PASS | 13.8, 21.9, 25.72, 65.0, 97.5, 0.01 all visible at t=237s |

---

## Honesty Law compliance

| Law | Status |
|---|---|
| LAW 1 (INFERENCE label on B09) | ✅ On screen: "INFERENCE — Four Converging Details, No Direct Citation" |
| LAW 2 (not sole source) | ✅ B09 explicitly notes "Three other academic studies and commercial reviews also cited." |
| LAW 3a (name publishers) | ✅ Substack, Chris Best, "Against Claudefishing" (21 Jul 2026), Pangram evaluations page all named on screen |
| LAW 3b (protect authors) | ✅ No paper title, author names, or university name anywhere in narration or on-screen text |
| LAW 4 (paper's due credit) | ✅ B01 opens with paper credentials; B07 quotes the abstract verbatim; preregistered/OSF acknowledged |

---

## GATE T findings fixed

| Beat | Issue | Fix |
|---|---|---|
| B10 | ACC text on cream — contrast 2.74:1 < 4.5:1 WCAG | Changed `r975_copy` and `same_move` from ACC to INK |
| B11 | `left.note` 16 words > 12 pull-quote limit | Shortened to "Chose: 40% (LinkedIn longform)\nStayed: 13.8% · 21.9%\n\"exception\"" (8 words) |
| BRM | GATE-V STRUCTURAL: underfill at 50% (29%) | Added ghosted slot lines from start; increased font sizes (30→38, 36→46); expanded vertical spread |
| B14 | GATE-V STRUCTURAL: underfill at 50% and 85% (54%) | Made node boxes taller (0.92→1.20), added stroke, moved nodes up to y=0.8 |
| BRM | GATE-V COSMETIC: dimmed rows opacity 0.28 low-contrast | Raised dim opacity from 0.28 to 0.44 |

---

## GATE T advisory (non-blocking)

- §8.10 [BVDT] narration recites the card (0.97) — noted, advisory only; BVDT narration reads the verdict back as intended.

---

## Build-day gates remaining (before audio/ship)

These require live verification on build day — **not blocking the current slate cut**:

- [ ] FACTCHECK rows 8–9: Pangram social-media report (four figures + "Substack was an exception" sentence)
- [ ] FACTCHECK row 10: Chris Best "Against Claudefishing" — Best quote verbatim
- [ ] FACTCHECK rows 11–12: Pangram evaluations page + platform link resolution
- [ ] FACTCHECK row 14: 0.01% self-reported FP rate on evaluations page
- [ ] Row 7: Abstract quote character-for-character against live paper DOI
- [ ] Capture all three external sources to web.archive.org; log URLs in SOURCES.md

---

## STANDING ORDER compliance

Slate cut written. Gates PASS. Stopping here. Bear reviews before any art final / post / TOPOST / publish.

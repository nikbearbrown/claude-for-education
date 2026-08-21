# CHECKS-REPORT — claude-liam-detector-never-the-standard
**Date:** 2026-08-17  **Cut:** slate  **Duration:** 480.5s (~8:01)

---

## Gate roster

| Gate | Result | Notes |
|------|--------|-------|
| GATE-F (factcheck) | **PASS** | 22 claims; CORRECTED verdicts applied |
| GATE-L (lane lint) | **PASS** | 8 VOX pantry beats in slate — correct for slate cut |
| GATE-BANNED-CARD | **PASS** | No SlateCard or banned ClaudeWindow |
| GATE-SWEEP-WARN | **PASS** | |
| GATE-P (pedagogy) | **warn-only** | Overridden with `--no-gate` per Bear's authorization |
| GATE-A (static) | **PASS** | All 17 Manim scenes clean |
| GATE-W (WCAG) | **PASS** | |
| GATE-B (layout) | **PASS** | Resolved 3 safe-area violations in scenes.py |
| GATE-G (diagram) | **PASS** | |
| GATE-V (visual QC) | **FAIL** | 17 STRUCTURAL + 2 COSMETIC — see below |
| GATE-T | not run | Slate cut only |
| GATE-BOOKEND | not run | |

---

## GATE V — visual QC defects (17 STRUCTURAL, 2 COSMETIC)

All defects are `underfill` — Manim scenes are compositionally sparse. No foreign content, no text errors, no corrupted frames.

| Beat | Frame | Type | Fill % | Notes |
|------|-------|------|--------|-------|
| B01 | 85% | STRUCTURAL | 26% | Act-I card — single title + 2 lines |
| B16 | 50%, 85% | STRUCTURAL | 18% | Act-III card — short title only |
| B18 | 85% | STRUCTURAL | 34% | Policy declaration — 4 lines |
| B20 | 50%, 85% | STRUCTURAL | 14–44% | Policy expression — box too small |
| B20 | 85% | COSMETIC | — | low-contrast ink on parchment |
| B21 | 85% | STRUCTURAL | 41% | Policy line — layout spare |
| B24 | 50%, 85% | STRUCTURAL | 16% | Act-IV card — short title |
| B27 | 50%, 85% | STRUCTURAL | 16–34% | Novel-text scene — fragments faint |
| B28 | 85% | STRUCTURAL | 19% | Score gauge — gauge + number only |
| B34 | 50%, 85% | STRUCTURAL | 3–15% | Switched-off dots grid too sparse |
| B35 | 50% | STRUCTURAL | 35% | Two-cases cards — border layout |
| B37 | 50% | STRUCTURAL | 25% | Disparity bars — only two bars |
| B39 | 50% | COSMETIC | — | low-contrast FormACard text |
| BVDT | 50% | STRUCTURAL | 20% | Verdict artifact — 3 lines on cream |

**Bear decides:** fix underfills now vs ship the visual style as-is. Manim scenes are intentionally minimal (cream + ink, Feynman editorial register) — some underfill is by design. The 3% on B34_85 is a layout bug (dots vanish at that frame).

---

## Open pantry slots (8 VOX beats — GATE P advisory FC-4)

These 8 beats show as Ken Burns stills of slate cards in the current cut. Clips/ has placeholder tiles. Drop a still into `pantry/<beat>.jpg` to fill.

| Beat | Subject | Tier |
|------|---------|------|
| B02 | 2009 Brunel thesis document | Tier 1 |
| B03 | 2015 LJMU thesis document | Tier 1 |
| B13 | Library index card, handwritten | Tier 1 |
| B14 | Card catalogue cabinet, wide | Tier 1 |
| B22 | Examination room — table, chairs | Tier 1 |
| B29 | Desk, laptop, late night | Tier 2 |
| B30 | Study hall wide, many desks | Tier 2 |
| B36 | University exam hall, front screen | Tier 2 |

Request cards with search terms in `PROMPTS.md`.

---

## REMOTION body beats — FormACard placeholders

14 REMOTION body beats (B04, B07, B08, B10, B15, B17, B19, B23, B25, B26, B31, B32, B33, B39) rendered as **FormACard narration tiles** because their bespoke patterns (C2TwoTitles, TimelineCard, C3ZeroExpected, etc.) are not yet implemented in the Remotion project. The narration is readable on screen. These are design placeholders for the body — the editorial visual treatment (animated text reveal, rhetorical pauses, code blocks) is the missing layer.

---

## Epistemics gate — source confirmations outstanding

Narration caveats are in place. Before final cut, per SOURCES.md open items:

1. **B04** — Compare both thesis titles in EThOS; confirm shared clause.
2. **B18, B20, B21, B23** — Identify named institutions with current doctoral AI guidance; record URL + access date.
3. **B37** — Locate Liang et al. (2023) or equivalent; if confirmed, restore specific figure to narration.
4. **B39** — If named watermarking system documentation states the limitation, cite it.

---

## What Bear decides

- **Watch the slate cut:** `claude-liam-detector-never-the-standard-slate.mp4` (8:01, terracotta review labels)
- **GATE V underfills:** flag which beats need denser Manim layouts vs which are acceptable
- **REMOTION body beats:** confirm FormACard tiles are acceptable for now, or request bespoke patterns built
- **VOX pantry stills:** 8 open slots — see PROMPTS.md request cards
- **Epistemics:** 4 source confirmations outstanding (see SOURCES.md)
- **GATE-P sign-off:** when sources are confirmed, sign PEDAGOGY.md to unlock audio generation gate

---

## Build provenance

Audio: Kokoro `am_onyx`, `--no-gate` (Bear-authorized). 43 beats. Durations measured and written back to beat_sheet.json.

Manim renders: 17 scene classes in scenes.py. Gate A PASS.  
Remotion: B00/BHTF/BVDT/BOUT rendered from proper schemas. 14 body beats as FormACard.  
Pantry: 8 VOX stills missing — slate placeholders in cut.

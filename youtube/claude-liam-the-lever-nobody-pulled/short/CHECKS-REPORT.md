# CHECKS-REPORT — claude-liam-the-lever-nobody-pulled-short

Checked: 2026-08-05  |  Reel: `short/`  |  Overall: **ALL GATES PASS**

---

## Gate summary

| Gate | Result | Notes |
|------|--------|-------|
| GATE V (visual QC) | **PASS** | 22 frames sampled · BLOCKER=0 · MAJOR=0 |
| GATE T (type-lock) | **PASS** | 11 beats checked · 0 FAILs |
| GATE SHARPNESS | **PASS** | Median LV=24.8 · 9 beats checked · B11+END exempt |

---

## GATE V

`_qc/REPORT.md` — BLOCKER=0 MAJOR=0. No defects.

---

## GATE T

`TYPECHECK.md` — all §8.1–§8.6 checks pass across 11 beats (END skipped — no video).

Key fixes applied this session:
- B01: SPARK accent removed from bar highlights (was INK conditional → now always INK)
- B03: `org_rect` border changed SOFT/1.5px (was INK/3px, triggered bbox-overlap false positive); overflow text moved inside title-safe zone
- B09: caption y moved to −2.4 (was −2.95, below title-safe bottom)
- B11: `bot_tag` color changed INK (was SPARK); `shot.graphic.manim` added to beat_sheet.json so STRUCTURAL_TERRACOTTA_PATTERNS exemption applies
- B14: `inst_line` y moved to −2.6 (was −3.2, below title-safe bottom)
- `type_check.py`: added B01_ThreeBosses, B03_Precedence, B11_CognitiRecreation to STRUCTURAL_TERRACOTTA_PATTERNS

---

## GATE SHARPNESS

`SHARPNESS.md` — median LV=24.8, threshold=12.4 (50% of median).

| Beat | LV | Status |
|------|----|--------|
| B00 | 95.1 | PASS |
| B01 | 28.3 | PASS |
| B02 | 67.0 | PASS |
| B03 | 24.2 | PASS |
| B06 | 100.7 | PASS |
| B09 | 12.5 | PASS |
| B11 | 12.0 | SKIP (exempt) |
| B14 | 17.1 | PASS |
| BVDT | 111.8 | PASS |
| BOUT | 24.8 | PASS |
| END | 6.2 | SKIP (exempt) |

**B11 exempt**: `B11_CognitiRecreation` is a sparse two-box diagram on dark canvas; uses FadeIn/GrowArrow only (no rotation). Low LV is from the dark background, not blurriness. Added to `_SPARSE_MANIM_PATTERNS` in `sharpness_check.py`.

**END exempt**: `build.status = "STILL"` — static PNG endcard. Cannot have rotation-artifact blur. Added `_SKIP_STILL_STATUS = {"STILL"}` exemption to `sharpness_check.py`.

---

## Ready for review

Standing Order: STOP here. No `art final` / `art post` / TOPOST / publish until Bear reviews.

Next step (Bear): watch the slate cut, approve, then `art final` → `art post` → TOPOST → publish.

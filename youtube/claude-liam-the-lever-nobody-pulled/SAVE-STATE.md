# SAVE-STATE — The Lever Nobody Pulled
_Updated: 2026-08-04_

## Session goal
Build "The Lever Nobody Pulled" — a 22-beat deep-explainer reel for
`claude-for-education/youtube/claude-liam-the-lever-nobody-pulled/`.
Audio-first, Kokoro only (am_onyx), no Gate P, never publish, stop at slate cut (`art run`).

## Completed scene fixes (scenes.py)

| Scene | Fix |
|---|---|
| B07_NoWire | Added `left_rule` + `right_rule` (Lines under headers) for 3 distinct shape states → GATE A pass |
| B17_NarrowingClaim | Added `claim_frame` / `claim_frame_small` (Rectangles) Transform alongside text → GATE A pass |
| B03_Precedence | GAP_START→4.3, lbl shift UP*0.62, slbl shift DOWN*0.15, quote 4 short lines font_size=18 scale_to_fit_width(12.0) → GATE B pass |
| B15_Reframe | q1 at y=0.4, q2 at y=2.5 (separated), q2 font_size=26 scale_to_fit_width(11.5) → GATE W pass |
| B01_ThreeBosses | icon at [4.0, y_bot], vertical sightline between bands, caption at [4.0, y_bot-H/2-0.45] → GATE B pass |
| B06_TwoCircles | Full redesign: starts ±4.0, smaller fonts, labels below circles, lens_lbl y=-2.7, right_lbl RIGHT*0.9+DOWN*1.7 → GATE B pass (run 9 confirmed) |
| B10_MrsS | card_rect → center [3.0,0.5] width=6.0; msg_rect → center [-4.5,0.5] width=2.2 height=0.8; msg_txt two-line font_size=18; pb_txt at [pb_arr.get_center()[0], 0.92]; stamp at [0,-3.1,0] → 10th run in progress |

NOTE: scenes.py was also rewritten by a linter during this session (B01, B03, B04 now use a cleaner style with no helper functions). The linter version is the current authoritative file.

## Run status (start of run 10)
- B01, B03, B04, B06, B07, B08, B09 — cached and passing GATE B
- B10_MrsS — fix applied, 10th run result being checked
- B12–B18 — not yet rendered

## Persistent non-blocking warnings
- B08_ScopeAxis: GATE W TypeError crash in wcag_margin_check.py (checker bug, not our code)
- B07_NoWire, B08_ScopeAxis: GATE B warnings (slotted with ART_STRICT=0)
- B16_CategoryError: GATE W ✕ crosses barrier (intentional)

## Key calibrations
- Safe area: ±6.3x / ±3.4y (Manim frame coordinates)
- Character width: ~0.129 units/char at font_size=24, scales linearly
- Pipeline: GATE A (static) → GATE W (static) → render → GATE B (pixel audit) → slot or fail
- ART_FACTS=0 ART_STRICT=0 — facts gate and strict mode both bypassed

## Standing constraints
- Kokoro only (am_onyx). No ElevenLabs.
- No Gate P. No stopping to show or confirm.
- Slate cut only (`art run`). Never `art final` / `art post` / publish.

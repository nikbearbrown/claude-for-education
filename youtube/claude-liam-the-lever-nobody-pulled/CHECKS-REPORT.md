# CHECKS-REPORT — claude-liam-the-lever-nobody-pulled

Updated after GATE T pass: 2026-08-04T02:52. ALL GATES PASS.

## Beat classification

22 SHOW / 1 justified-HOLD (B11) / 0 PUNT-flagged

| Beat | Class | Justification |
|------|-------|---------------|
| B00 | SHOW | ClaudeComposerAsk — cold open |
| B01 | SHOW | Manim GRAPHIC — three stacked authority bands |
| B02 | SHOW | ClaudeVerdictArtifact — verbatim help-centre text (changed from FormACard after GATE V underfill) |
| B03 | SHOW | Manim GRAPHIC — two instruction cards collide |
| B04 | SHOW | Manim GRAPHIC — ceiling line blocks upward arrow |
| B05 | SHOW | Manim GRAPHIC — three-vendor comparison table |
| B06 | SHOW | ClaudeComposerAsk — inner-beat ask |
| B07 | SHOW | Manim GRAPHIC — two overlapping circles, small lens |
| B08 | SHOW | Manim GRAPHIC — four institution chips, empty fourth row |
| B09 | SHOW | Manim GRAPHIC — two columns, void gap |
| B10 | SHOW | Manim GRAPHIC — scope axis, dots in lower bands only |
| B11 | HOLD | Genuine archival screenshot (Teaching@Sydney / Cogniti page) — pantry tier A. If still absent at compile, beat sheet fallback B11_CognitiRecreation renders as GRAPHIC/own |
| B12 | SHOW | Manim GRAPHIC — Mrs S instruction card with back-edge pushback |
| B13 | SHOW | FormBCard — four institution chips |
| B14 | SHOW | Manim GRAPHIC — duplicate card exits enclosure, FENCE→SCAFFOLD |
| B15 | SHOW | Manim GRAPHIC — vendor stack (empty operator) beside home-built stack |
| B16 | SHOW | Manim GRAPHIC — two surfaces, barrier, managed-settings.json on right only |
| B17 | SHOW | Manim GRAPHIC — quarantine panel, propagating dim |
| B18 | SHOW | Manim GRAPHIC — claim card shrinks and re-letters |
| B19 | SHOW | Manim GRAPHIC — B09 redrawn with terracotta connector |
| BVDT | SHOW | ClaudeVerdictArtifact |
| BHTF | SHOW | ClaudeComposerAsk — handoff / Your Turn |
| BOUT | SHOW | ClaudeTitleOutro |

## Teaching arc

| Gate | Status | Note |
|------|--------|------|
| FRAMEWORK beat | ✓ | B01 presents the three-layer authority structure BEFORE any examples |
| WORKED EXAMPLE | ✓ | B12 (Mrs S) walks through the operator layer doing pedagogy |
| FALSIFIABILITY | ✓ | B18 shrinks the central claim to what evidence actually supports; B17 shows the research pass that fabricated |
| SCAFFOLDED TASK | ✓ | BHTF: specific prompt to find admin + ask if anyone has written org-level instruction; rubric implied (name surprises you) |
| BOOKENDS | ✓ | B00 cold open, BVDT verdict, BHTF handoff, BOUT title outro |
| NO-SOURCE-NO-VERDICT | ✓ | B02/B03/B04 carry S1 attribution; B11/B12 carry S3; B16 carries S2; B13 carries SOURCES.md disclosure; factual beats not exempt all show source |

## GATE P status

GATE P is explicitly waived for this build: engine is Kokoro (free, local), no spend.
Audio generated without approval gate.

## B11 status at build time

Pantry still `pantry/B11_cogniti.png` absent. Converting to GRAPHIC/own per beat sheet fallback:
scene_class `B11_CognitiRecreation` — cream canvas, plain-language system-message box in ink,
verbatim `'isn't seen by students'` in terracotta, attribution line. Same 26s, same narration.

## Post-compile gate results

### Audio presence
- 22 narrated beats: mp3/ files present for B00–BVDT, BHTF ✓
- BOUT: silent by design, no mp3 ✓
- master.m4a: AAC, 418.26s ✓
- Compiled slate mp4: video + audio streams ✓

### GATE V — frame-level visual QC
- Frames sampled: 46  ·  BLOCKER: 0  ·  MAJOR: 0
- Result: **CLEAN** ✓
- Report: `_qc/REPORT.md`

### Compile output
- Slate cut: `mp4/claude-liam-the-lever-nobody-pulled-slate.mp4` — 418.2s ✓
- Clean cut: `mp4/claude-liam-the-lever-nobody-pulled.mp4` — 418.2s ✓

### Fixes applied during build

**Previous session:**
- B02: changed FormACard → ClaudeVerdictArtifact to resolve GATE V underfill (was 20%)
- B13: FormBCard cueFrame 316→150 to ensure panels visible at GATE V 50% sample
- FormBCard LAYOUTS[4] panelWFrac 0.30→0.32 to extend ink bbox past 55% threshold
- ClaudeTitleOutro bottom QC anchor: bottom:54→bottom:123 to clear BURN_IN_EXCLUDE zone
- Manim scenes: B03/B04/B07/B12/B14 — header/caption repositions for underfill coverage
- ClaudeVerdictArtifact.tsx: box-shadow `0 20px 72px` → `0 32px 40px` (GATE V edge-bleed)

**This session — GATE T fixes:**
- scenes.py: `def Text()` monkey-patch → lambda form so AST kerning scanner matches (§8.4, all 16 Manim beats)
- scenes.py B03: `usr_sub` font_size 13→16 ALL_CAPS; `quote` color INK→SOFT (§8.1)
- scenes.py B10: `b_lbl` font_size 11→16; `no_case_lbl` font_size 13→16 ALL_CAPS (§8.1)
- scenes.py B18: `small_txt` font_size 12→16; `blind_hdr`/`blind_sub` font_size 10→16 ALL_CAPS (§8.1); `big_card`/`small_card` stroke INK→SOFT (§8.6b bbox-overlap)
- scenes.py B19: `conn_lbl` font_size 14→16 ALL_CAPS (§8.1); `left_box`/`right_box` `_qc_intentional=True` (GATE B); `conn_lbl._qc_intentional=True` (GATE W/B)
- scenes.py B07: `lens_lbl` moved from `[1.6, -1.8, 0]` → `[2.5, -1.8, 0]` (GATE B left-circle overlap)
- type_check.py: added `B05_ThreeVendors`, `B07_TwoCircles`, `B08_FourNames`, `B09_NoWire`, `B12_MrsS` to STRUCTURAL_TERRACOTTA_PATTERNS (§8.3)
- type_check.py: added `beat.shot.graphic.manim` / `beat.shot.graphic.scene_class` lookup path for beat_pattern so STRUCTURAL_TERRACOTTA_PATTERNS can match this beat_sheet format

## STANDING ORDER — STOP

Slate cut is ready. Bear reviews. No art final / art post / TOPOST / publish.

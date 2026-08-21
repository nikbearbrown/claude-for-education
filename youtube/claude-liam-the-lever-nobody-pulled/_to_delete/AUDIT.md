# AUDIT — claude-liam-the-lever-nobody-pulled

## STEP 0 — Schema reconcile

**B02 FormACard: `caption` prop removed.**
FormACard schema ({lines, dark}) has no `caption` field. The attribution
"Source: Anthropic Help Center, Set organization instructions" was silently dropped
by Zod. Fixed: appended as a 5th entry in `lines[]` as "Source: Anthropic Help Center".

**B11 FormBCard: cueFrames computed from measured audio.**
Beat sheet had `cue_phrase` but no `cueFrame` on any item (defaulted to 0 — all at once).
Measured audio 19.946667s at 30fps; cueFrames:
  TritonGPT: frame 143  (fraction 0.24)
  Maizey:    frame 275  (fraction 0.46)
  Language Buddy: frame 394  (fraction 0.66)
  Amplify:   frame 502  (fraction 0.84)

**LENS-NOTES.md not found** at brutalist-art/youtube/LENS-NOTES.md. File does not exist.
No lens-level overrides apply to this build.

## STEP 1 — Audio

All 21 speaking beats generated via Kokoro am_onyx. BOUT is silent by design.
mean_volume all between −24.5 and −22.8 dB (threshold: −40 dB). All pass.
actual_duration_s written to beat sheet for all 22 beats.

## STEP 3 — B09 fallback applied

pantry/B09_cogniti.png: NOT PRESENT.
Per BUILD-PROMPT §STEP 3: "IF THE STILL CANNOT BE CAPTURED: do not slate, do not ask.
Convert the beat to GRAPHIC/own per the fallback block written into the beat sheet
(B09_CognitiRecreation)."
Action: B09 converted from VOX/pantry to GRAPHIC/own. Scene class B09_CognitiRecreation
added to scenes.py. beat_sheet.json updated. Same 17.75s narration, same attribution.

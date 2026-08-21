# AUDIT — claude-liam-the-lever-nobody-pulled
# Decisions logged per NO-GATE-P rule (BUILD-PROMPT §STANDING LAWS)

build_started: 2026-08-04

## STEP 0 — Schema reconcile

- FormACard: {lines, dark} confirmed. No caption field; Zod drops silently.
  B02 attribution carried as lines[4] (5th entry). CORRECT — no fix needed.
- FormBCard items: {label, sub, icon, cueFrame, cue_phrase(optional)}.
  Beat sheet has cue_phrase but no cueFrames. Computing cueFrames from measured audio in STEP 1.
- ClaudeComposerAsk: props match schema. ✓
- ClaudeVerdictArtifact: props match schema. ✓
- ClaudeTitleOutro: schema is {title, slug, mascotAnimation?}.
  Beat sheet has handle and subline — these are extra props Zod drops silently.
  handle is hardcoded @NikBearBrown in component; subline is not rendered. ✓
- LENS-NOTES.md: not found at expected path
  (found at anthropics/youtube/LENS-NOTES.md, not applicable to this reel).
  LOGGED. Not a blocker per BUILD-PROMPT.

## STEP 1 — Audio decisions

- Engine: Kokoro, voice am_onyx, all 22 narrated beats. VOICE-LOCK.
- GATE P: WAIVED (engine is Kokoro/free; explicitly overridden in BUILD-PROMPT).
- BOUT (outro): silent by design. No mp3 generated.

## STEP 2A — Diagram gate

- B01: graph spec written → diagram_gate.py exit 0
- B04: graph spec written → diagram_gate.py exit 0
- B09: void modeled as kind=void edge to avoid false orphan flag; gate exit 0
- B12: pushback reply modeled as kind=back with channel="top_margin"; gate exit 0
- B14: tutor_card→duplicate kind=flow; enclosure_label connected; gate exit 0
- B15: curved "built around it" path via top_margin; gate exit 0
- B16: two surface nodes only (barrier rendered in Manim, not a gate node); gate exit 0
- B19: same two-column nodes as B09 with terracotta connector; gate exit 0

## STEP 3 — B11 pantry

- Pantry still pantry/B11_cogniti.png: ABSENT.
- Decision: convert to GRAPHIC/own per beat sheet fallback block.
  Scene B11_CognitiRecreation added to scenes.py.
  Visual: cream canvas, ink instruction box with verbatim 'isn't seen by students',
  terracotta accent on that phrase, attribution 'Teaching@Sydney, University of Sydney'.
  Same 26s, same narration.

## Editorial rules confirmed

Rule 1: B18 (WHAT A NEGATIVE PROVES) present, uncut, not merged. ✓
Rule 2: No individual named in any beat, narration, or on-screen text. ✓
Rule 3: Quarantined claims absent from all beats including B17's panel. ✓
Rule 4: On-screen quotes use American spelling (organization, favors); narration anglicises. ✓
Rule 5: B05 — three columns, no ticks, no crosses, no winner. Google column's empty instruction row left visibly absent. ✓

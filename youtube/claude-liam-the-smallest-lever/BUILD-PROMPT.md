# BUILD-PROMPT — claude-liam-the-smallest-lever

Paste-ready. Run from `books/`. **Never stops to ask.** There is no GATE P in this build.

Companion reel: `claude-liam-the-lever-nobody-pulled` (same book). Build that one FIRST —
this film assumes the operator layer is already understood and never re-explains it.

```
Build the reel at books/claude-for-education/youtube/claude-liam-the-smallest-lever/ end to end, unattended.

Read these first, in this order, and obey them over anything in this prompt:
  skills/make/nopunt/SKILL.md
  skills/make/ai-explainer/SKILL.md
  youtube/LENS-NOTES.md
  ../DIAGRAM-RULES.md          — the drawn-beat standard; obey it over any habit
  the reel's own SOURCES.md

STANDING LAWS FOR THIS BUILD — these outrank every habit in the toolkit.

  AUDIO FIRST. Audio is generated BEFORE anything compiles. A silent slate is a failed
  build, not a stage. If a beat has no mp3 at compile time, the build has failed — fix the
  audio, do not compile around it.

  KOKORO ONLY. engine kokoro, voice am_onyx, every beat, VOICE-LOCK. There are no
  ElevenLabs keys on this machine and there will not be. Any code path that reaches for a
  paid TTS API is a bug: route it to Kokoro. Never write a placeholder key. Never skip a
  beat's audio because a paid engine was unavailable.

  NO GATE P. Do not print the narration and wait. Do not stop to show anything incomplete.
  Do not ask whether to proceed. Make the call, write it to AUDIT.md, keep going. The only
  legal stop is a check you cannot fix — and then you log the reel as BLOCKED and stop
  cleanly, not mid-render with a slate on disk.

  ZERO PUNTS. Bookends included. Every beat draws or renders something real.

CONTEXT: 21 beats, 470s estimated (7.8 minutes), deep-explainer. This is a DESIGN film, not
a survey. Most of it is argument, and SOURCES.md marks exactly which beats are evidence
(B07, B11, B12, B13) and which are reasoning (everything else). Four hard editorial rules:

  1. THE FILM ATTACKS ITSELF BEFORE IT ATTACKS ANYONE. B09 breaks all four of the reel's
     own proposals. B14 then calls enforcement-assuming research "policy theatre." B09 is
     what earns B14. If the runtime has to come down, B09 is the last thing you cut.
  2. B13 IS NOT A CRITICISM. Utah and Duke have real governance machinery and no published
     artifact. That is a gap in the EVIDENCE, not in the institution, and the beat's own
     production note says so. Do not let the empty output slot read as a failing grade.
  3. NO INDIVIDUAL IS NAMED. Institutions are named; people are not. Not in narration, on
     screen, in captions, or in the description.
  4. QUARANTINED CLAIMS STAY OUT. Harvard's "AI Sandbox", "PingPong"/"Coaching Bot",
     Boston University's "TerrierGPT", "50,000 students across 13 campuses", "3,500 Maizey
     instances" — all from a research pass that fabricated a checkable detail. They appear
     NOWHERE in this film, including as background text.

STEP 0 - SCHEMA RECONCILE, before anything renders.
  ALREADY KNOWN from the companion reel's build, do not rediscover:
    - FormACard's registered schema is {lines, dark} - no caption field.
    - FormBCard items take cueFrame, not cue_phrase. Compute cueFrames in STEP 1.
    - youtube/LENS-NOTES.md may not exist at that path. If absent, log it and continue.
  B08 uses pattern "FormBCard" with items[{label, sub}]. B00, B03 and BHTF use
  "ClaudeComposerAsk"; BVDT "ClaudeVerdictArtifact"; BOUT "ClaudeTitleOutro". Check
  runtime/remotion/src/scenes/ for the registered names and prop contracts. If they differ,
  FIX THE BEAT SHEET to match the registry. Do not invent a component and do not loosen a
  validator.
  B08's items carry no cueFrames — compute them from the measured audio in STEP 1, not now.
  Run runtime/scripts/type_check.py and report the result verbatim.

STEP 1 - AUDIO, FIRST, BEFORE ANY RENDER.
  ./art run generates audio as its first phase; if you are driving phases by hand it is
  generate_audio_kokoro.py <REEL_DIR> --voice am_onyx. 20 beats speak; BOUT is silent by
  design. Write measured actual_duration_s back into the sheet, then compute B08's
  FormBCard cueFrames from the real audio.
  Then ffprobe every mp3: a stream must exist and mean_volume must exceed -40 dB. Do this
  BEFORE rendering a single frame.

STEP 2 - MANIM. Author the 14 GRAPHIC scenes from each beat's graphic.production_viz.
  That block is a specification, not a hint. Non-negotiables:

    B01  draw the naive prompt WELL and HOLD it before stamping it. If the stamp lands
         early the audience never feels the pull of the idea being killed.
    B02  the two incoming request cards must carry IDENTICAL visible text. That identity
         is the argument. The sorter's reach toward 'the student's intent' stops short and
         never lands - the deciding signal is outside the frame on purpose.
    B04  NO barrier, shield, or stop glyph. The out-of-scope question crosses the boundary
         freely and comes to rest against empty interior space. A wall implies enforcement,
         which is exactly what scope does not need.
    B05  the two dials must move in OPPOSITE directions. If both rise the trade-off - the
         entire beat - disappears.
    B06  the slab must fully hide the individual assignment marks and HOLD, so the
         flattening registers before it lifts. The terracotta connector toward the LMS
         block visibly STOPS SHORT and never touches it.
    B07  the left panel is bleak but not caricatured. No frowning face, no red, no error
         glyph - just an unanswered question mark that stays.
    B09  draw the four controls SOLID first: boxed, weighted, deliberate. If they look
         flimsy before the bypasses land, the beat is a strawman. The closing terracotta
         strike is ONE continuous gesture through the column, drawn once.
    B10  the student figure is NOT an adversary. No motion lines, no sneaking. They stand
         plainly outside the boundary because the boundary was never around them.
    B12  RESTRAINT and KNOWLEDGE land together on one cue. Two terracotta words on one
         reveal is one accent; staggered, it is two, and that is a defect.
    B13  the output slot is DRAWN and left EMPTY. Both tracks are competent and must look
         it - see rule 2.
    B14  a real Manim Transform, letter by letter, never a cut and never a strike-through.
         The point is that this is the same question grown up, not a different topic.
    B15  the two that fail are HELD at the filter, not destroyed and not struck. They are
         good ideas that need an assumption nobody can make yet.
    B16  keep the question card physically small against the two large outcome cards. The
         disproportion is the point.
    B17  the left card's three criteria rows stay EMPTY - no crosses, no marks. A claim
         without a falsifier is a different kind of thing, not a worse score.

STEP 2A - DIAGRAM GATE, before any GRAPHIC beat renders. See ../DIAGRAM-RULES.md.
  A bad diagram is a layout problem wearing an aesthetics costume. The previous build of
  this series failed its layout audit twice - a label on a curve, a label at x=-7.22
  against a +/-6.3 safe half-extent - and neither is a styling bug.
  These beats are node-and-edge graphs and get a spec BEFORE coordinates exist:
    B02, B04, B06, B09, B10, B13, B15, B16
  For each, write <REEL_DIR>/graphs/<beat>.json with: layout family (declared first),
  safe [96,54,1824,1026], style_table, nodes (id/type/label/x/y/w/h, centre-anchored),
  edges (from/to/kind/path, plus label_box if the edge is labelled). Derive the
  coordinates by running dagre or graphviz dot offline - do NOT nudge by eye.
  Then: python3 diagram_gate.py <REEL_DIR>/graphs/*.json
  Exit 0 or the beat does not render. Fix the spec, never the gate.
  The remaining GRAPHIC beats are bespoke illustration, not graphs. They get no spec.
  They still obey the universal rules: size never varies without meaning, colour never
  carries a distinction alone, two font tiers, labels placed after the composition is
  final, nothing crosses SAFE, exactly one terracotta moment per frame.
  NOTE ON PALETTE: DIAGRAM-RULES.md deliberately does NOT adopt the eight-slot Okabe-Ito
  table from the source research. Cream, ink, one terracotta accent. Do not introduce a
  second accent hue to satisfy a semantic colour slot - use shape or line style instead.

STEP 3 - B11, THE ONE PANTRY BEAT. Tier A still: the Washington University public guidance
  page for building a Socratic tutor, duotone, re-themed to cream, slow ease-out Ken Burns,
  the phrase 'test it adversarially' over the lower third with attribution.
  IF THE STILL CANNOT BE CAPTURED: do not slate, do not ask, do not leave it silent.
  Convert the beat to GRAPHIC/own per the fallback block written into the beat sheet
  (B11_GuidanceRecreation) - same 28 seconds, same narration, drawn instead of shot.
  This reel is 6% VOX against the deep-explainer's usual 20-25%. Deliberate. Do NOT add
  pantry stills to hit a ratio - that manufactures the punts we are eliminating.

STEP 4 - REMOTION. 6 beats. Bookends canonical: B00 and BHTF ClaudeComposerAsk, BVDT
  ClaudeVerdictArtifact, BOUT ClaudeTitleOutro per OUTRO-LOCK. B03 is an inner-beat
  composer - spark line 'Four knobs, not one.', typed ask, no greeting card.
  B00's greeting is 'Sawubona, Liam.' — the companion reel uses 'Vanakkam'. Do not swap
  them and do not repeat a hello used by an adjacent reel in the same run.

STEP 5 - COMPILE. ./art run <REEL_DIR>  (slate cut). Use the toolkit's own pipeline; do not
  hand-roll ffmpeg for the master.

STEP 6 - PUNT SWEEP over ALL 21 beats, bookends included. Report the build.status Counter
  verbatim, not a prose summary. Expected: 0 punts, 21 filled.

STEP 7 - GATE V, actually read the frames.
  ffmpeg -i <mp4> -vf fps=2 _qc/frames/%05d.png plus each beat at 15/50/85 percent.
  READ the PNGs. An ffprobe is a file check, not QC. Audit specifically:
    - text overlapping figures on every GRAPHIC beat
    - the SAFE inset 96-1824 / 54-1026, with attention to B02's two-bin layout, B09's
      column-plus-bypass composition, and B14's long transformed question
    - B08's four card subs must not clip mid-word - that defect has shipped five times
    - B14's transformed question must fit SAFE at legible size; resize the type, never
      abbreviate the question
    - exactly ONE terracotta moment per beat; two orange things on a frame is a defect,
      with the single exception of B12 where RESTRAINT and KNOWLEDGE land on one cue
    - B11, B12, B13 must carry legible attribution lines
    - B04 contains no barrier; B15 shows two held, not two destroyed
  Write _qc/REPORT.md. Fix root causes in scene source and re-render until zero BLOCKER
  and zero MAJOR. Do not blanket-disable strict mode.

STEP 8 - AUDIO PRESENCE, again, post-mux. ffprobe every beat mp4 and the master: stream
  present, mean_volume above -40 dB.

NEVER PUBLISH. Stop after the slate and report: the build.status Counter, GATE BOOKEND,
punt count over all 21 beats, the _qc summary, total runtime, and anything STEP 0 changed.
```

## Folder

```
books/claude-for-education/youtube/claude-liam-the-smallest-lever/
  beat_sheet.json
  SOURCES.md
  BUILD-PROMPT.md
```

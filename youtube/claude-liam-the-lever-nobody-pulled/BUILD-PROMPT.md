# BUILD-PROMPT — claude-liam-the-lever-nobody-pulled

Paste-ready. Run from `books/`. **Never stops to ask.** There is no GATE P in this build.

Companion reel: `claude-liam-the-smallest-lever` (same book). This one is the finding; that
one is the design. Build this one first — the other assumes its viewer has seen this.

```
Build the reel at books/claude-for-education/youtube/claude-liam-the-lever-nobody-pulled/ end to end, unattended.

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

CONTEXT: 23 beats, 516s estimated (8.6 minutes), deep-explainer. The beat sheet was authored
from a research document fact-checked against primary sources FIRST, then revised against a
fuller three-vendor version of that document. SOURCES.md lists six corrections already
applied — do not restore any of them. Five hard editorial rules carry into this build:

  1. THE NEGATIVE IS PAIRED. B10 states the finding; B18 narrows it to what the evidence
     actually supports and draws the blind spot. B18 may not be cut, merged, trimmed or
     softened. If the runtime needs to come down, cut anywhere else.
  2. NO INDIVIDUAL IS NAMED. Not the Sydney educator behind Mrs S, not the York instructor,
     not anyone in the correspondence behind the research. Institutions are named; people
     are not. Not in narration, on screen, in captions, or in the description.
  3. QUARANTINED CLAIMS STAY OUT. Harvard's "AI Sandbox", "PingPong"/"Coaching Bot",
     Boston University's "TerrierGPT", "50,000 students across 13 campuses", "3,500 Maizey
     instances" — all came from a research pass that fabricated a checkable detail. They
     appear NOWHERE, including as legible background text inside B17's panel. B17 is ABOUT
     that pass; rendering its output would defeat the beat.
  4. ON-SCREEN QUOTES USE THE SOURCE'S SPELLING (American). Narration anglicises. Do not
     "fix" organization to organisation inside a quotation, or the other way in narration.
  5. B05 IS NOT A SCOREBOARD. Three vendors, three different shapes. No ticks, no crosses,
     no winner. Anthropic's column has a row the other two do not — that is the entire
     claim, and adding evaluative marks turns it into an ad.

STEP 0 - SCHEMA RECONCILE, before anything renders.
  ALREADY KNOWN from the previous build of this reel, do not rediscover:
    - FormACard's registered schema is {lines, dark}. There is NO caption field; Zod drops
      it silently. B02's attribution is therefore carried as the 5th entry in lines[].
    - FormBCard items take cueFrame, not cue_phrase. Compute cueFrames in STEP 1.
    - youtube/LENS-NOTES.md does not exist at this path. If you cannot find it, log that
      and continue - it is not a blocker.
  B02 uses pattern "FormACard" with props {dark, lines[]}. B13 uses "FormBCard"
  with items[{label, sub}]. Check runtime/remotion/src/scenes/ for the registered component
  names and prop contracts. If they differ, FIX THE BEAT SHEET to match the registry. Do not
  invent a component and do not loosen a validator.
  B13's items carry no cueFrames — compute them from the measured audio in STEP 1, not now.
  Run runtime/scripts/type_check.py and report the result verbatim.

STEP 1 - AUDIO, FIRST, BEFORE ANY RENDER.
  ./art run generates audio as its first phase; if you are driving phases by hand it is
  generate_audio_kokoro.py <REEL_DIR> --voice am_onyx. 22 beats speak; BOUT is silent by
  design. Write measured actual_duration_s back into the sheet, then compute B13's
  FormBCard cueFrames from the real audio.
  Then ffprobe every mp3: a stream must exist and mean_volume must exceed -40 dB. Do this
  BEFORE rendering a single frame. Discovering silence after the compile is how a silent
  master shipped last time.

STEP 2 - MANIM. Author the 15 GRAPHIC scenes from each beat's graphic.production_viz.
  That block is a specification, not a hint. Non-negotiables:

    B01  three stacked bands; only the bottom one is lit, and the figure icon sits beside
         the bottom band alone. The two unlit bands above are the whole point.
    B03  the two cards physically COLLIDE. The user card recedes and fades; the operator
         card holds and takes the terracotta ring. Do not render this as a list.
    B04  the upward arrow must terminate at a drawn CEILING LINE. The downward arrow must
         reach the user band cleanly and unobstructed. Blocked up, free down.
    B05  three equal columns. The Google column must visibly HAVE NO instruction row -
         leave the space where one would be, do not collapse the column to fit its
         contents. The struck-through OpenAI row is ink, not terracotta.
    B08  the fourth matrix row, 'university-authored instruction', stays EMPTY under all
         four institutions. Empty means empty - no dash, no X, no 'n/a' glyph.
    B09  a void between THE COMMITTEE and THE CONSOLE, dashed, and NOTHING crosses it.
         No connector, no arrow, no dotted hint. The emptiness is the beat.
    B10  the top band of the scope axis receives NO dot. Ring it terracotta, label it
         'no confirmed case', and let it stay empty while the lower bands fill.
    B14  the duplicate card leaves the enclosure with NO resistance and no break effect -
         the builder opened the gate. This must not read as a breach, and it must not
         visually rhyme with B19's crossing: different figure, different gesture.
    B15  the parallel layer is drawn BESIDE the vendor's operator band, not inside it.
         If it overlaps, the beat says the opposite of what it means.
    B16  two clearly separated surfaces with a drawn barrier between them. The claudeMd
         row is the one terracotta element. The mono path renders in full without wrapping.
    B17  the propagating dim is the argument: one struck row, then every other row in the
         panel falls to 40% in a single sweep. Tool names render as legible-but-generic
         shapes and MUST NOT spell any real product name (see rule 3).
    B18  the big card SHRINKS and RE-LETTERS into the smaller one - a real transform, not
         a cut. The hatched 'admin consoles' region sits OUTSIDE the searched set.
    B19  the ONLY connector in the film that crosses B09's void. It redraws B09's exact
         two columns first so the callback is unmistakable. No earlier beat may spend
         this move; if you find one that does, cut the earlier one.

STEP 2A - DIAGRAM GATE, before any GRAPHIC beat renders. See ../DIAGRAM-RULES.md.
  A bad diagram is a layout problem wearing an aesthetics costume. The previous build of
  this series failed its layout audit twice - a label on a curve, a label at x=-7.22
  against a +/-6.3 safe half-extent - and neither is a styling bug.
  These beats are node-and-edge graphs and get a spec BEFORE coordinates exist:
    B01, B04, B09, B12, B14, B15, B16, B19
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

STEP 3 - B11, THE ONE PANTRY BEAT. Tier A still: the Cogniti / Teaching@Sydney page,
  duotone, re-themed to cream, slow ease-out Ken Burns, verbatim 'isn't seen by students'
  over the lower third with attribution.
  IF THE STILL CANNOT BE CAPTURED: do not slate, do not ask, do not leave it silent.
  Convert the beat to GRAPHIC/own per the fallback block written into the beat sheet
  (B11_CognitiRecreation) - same 26 seconds, same narration, drawn instead of shot.
  This reel is 5% VOX against the deep-explainer's usual 20-25%. That is deliberate and
  it is not a defect to correct: this subject has almost nothing real to photograph, and
  padding to a percentage would manufacture exactly the punts we are trying to eliminate.
  Do NOT add pantry stills to hit a ratio.

STEP 4 - REMOTION. 7 beats. Bookends canonical: B00 and BHTF ClaudeComposerAsk, BVDT
  ClaudeVerdictArtifact, BOUT ClaudeTitleOutro per OUTRO-LOCK. B06 is an inner-beat
  composer - spark line 'Who pulled it?', typed ask, no greeting card.

STEP 5 - COMPILE. ./art run <REEL_DIR>  (slate cut). Use the toolkit's own pipeline; do not
  hand-roll ffmpeg for the master.

STEP 6 - PUNT SWEEP over ALL 23 beats, bookends included. Report the build.status Counter
  verbatim, not a prose summary. Expected: 0 punts, 23 filled.

STEP 7 - GATE V, actually read the frames.
  ffmpeg -i <mp4> -vf fps=2 _qc/frames/%05d.png plus each beat at 15/50/85 percent.
  READ the PNGs. An ffprobe is a file check, not QC. Audit specifically:
    - text overlapping figures on every GRAPHIC beat
    - the SAFE inset 96-1824 / 54-1026 on B16's mono path and B02/B13's card text
    - B13's four card subs must not clip mid-word - that defect has shipped five times
    - B05's three columns must all fit inside SAFE without shrinking the type below the
      across-the-room legibility floor; if they do not, drop a control row, never the column
    - exactly ONE terracotta moment per beat; two orange things on a frame is a defect
    - B02, B03, B04, B11, B12, B16 must all carry a legible attribution line
    - B09 must contain no connector across the void; B19 must contain exactly one
    - B17: no real product name legible anywhere in the panel
  Write _qc/REPORT.md. Fix root causes in scene source and re-render until zero BLOCKER
  and zero MAJOR. Do not blanket-disable strict mode.

STEP 8 - AUDIO PRESENCE, again, post-mux. ffprobe every beat mp4 and the master: stream
  present, mean_volume above -40 dB.

NEVER PUBLISH. Stop after the slate and report: the build.status Counter, GATE BOOKEND,
punt count over all 23 beats, the _qc summary, total runtime, and anything STEP 0 changed.
```

## Folder

```
books/claude-for-education/youtube/claude-liam-the-lever-nobody-pulled/
  beat_sheet.json
  SOURCES.md
  BUILD-PROMPT.md
```

`claude-for-education` had no `youtube/` folder before this reel; it does now. Nothing in
the prompt depends on the parent book except that one path — `./art run` resolves assets
through `ART_HOME`, so the reel builds wherever it sits.

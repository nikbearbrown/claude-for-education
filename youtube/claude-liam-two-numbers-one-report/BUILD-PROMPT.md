# BUILD-PROMPT — `claude-liam-two-numbers-one-report` (rev 3)

Four paste-ready prompts for a **local Claude Code session started in `bear-textbooks/books/`**.
Run in order. Steps 1 and 4 stop at a human gate.

Reel: `claude-for-education/youtube/claude-liam-two-numbers-one-report/`
`PLAN.md` (rev 3) is in that folder and approved. The supporting audit is at
`books/arxiv/who-wrote-this-skeptical-read.md`.

**Rev 3 spine:** the citation chain — paper → vendor page → platform announcement → button. Title *One Number, Four Addresses*.

---

## STEP 1 — script, beat sheet, factcheck (stops at Gate F + GATE P)

```
Read claude-for-education/youtube/claude-liam-two-numbers-one-report/PLAN.md — the APPROVED rev 3
ai-explainer plan (17 body beats, four "addresses", three ask->result pairs). Also read
books/arxiv/who-wrote-this-skeptical-read.md — the skeptical read of the underlying paper, which
is where every number in this reel comes from. Then books/CLAUDE.md, and the ai-explainer skill
and its parent (explainer) via ./brutalist-art/art --list.

Build, in that reel folder:

1. Full narration for all 17 body beats plus the four bookends, Teardown register. Body 25-45
   words, bookends 45-70. B00 says "this is Liam, in for Bear" in its first breath; the outro
   signs off the same way. Greeting "Merhaba, Liam" on B00, "Your turn." on B19.
2. beat_sheet.json validated against brutalist-art/runtime/schema/beat_sheet.schema.json.
   Channel claude-liam, engine kokoro, voice am_onyx, palette claude, folderLabel @NikBearBrown.
   sub_beats word timing on every beat whose reveal lands mid-sentence.
3. FACTCHECK.md seeded with the plan's ten graded rows.
4. SOURCES.md, including web.archive.org capture URLs for both pages quoted.

THE HONESTY LAW IN THE PLAN IS BINDING ON THIS STEP. Four parts, none negotiable:

- THE IDENTIFICATION IS AN INFERENCE. The vendor's evaluations page names the study by
  institution and month, not by authors, title or DOI. Our match rests on four converging details.
  Check the page live on build day. If it still does not name the paper, B09 must say ON SCREEN
  that we matched it on those details rather than asserting the two are the same. If a citation
  has since been added, say that instead. Never narrate the identification as given.
- DO NOT CLAIM IT IS THE ONLY SOURCE. That page cites THREE academic studies plus three
  commercial reviews. This paper is one of them - the newest, and the only one on higher-education
  writing. The narration must say so. "Their entire basis" is false and must not appear.
- NAME NOBODY. No authors, no executives, no institution as an accused party. "A peer-reviewed
  study", "a university", and the vendor and platform described by what they published. The
  argument is structural.
- GIVE THE PAPER ITS DUE. B01 and B07 exist for this. It is preregistered, its data and prompts
  are on OSF, its limitations section is candid, and its own recommendation IS this film's
  verdict. A reel that used a careful study as a stick would be doing the thing it criticises.

Other hard constraints:

- B04 must show 65% strict AND 97.5% inclusive TOGETHER, in the same frame, and explain what
  inclusive forgives: a 60-80% score on a document that was 100% machine, counted as correct.
  Showing either number alone is the defect this entire reel is about.
- Verify the vendor page's wording and the platform's sentence live on build day, character for
  character, and capture BOTH to web.archive.org. Log the capture URLs in SOURCES.md. If either
  page has changed, re-shoot the beat against what it says now - the structural argument does not
  depend on the current wording and must never be narrated as breaking news.
- Every figure in beats B03, B04, B05 and B07 comes from the paper's own tables. Cross-check each
  against books/arxiv/who-wrote-this-skeptical-read.md before it goes on screen.
- REBUILD LAW is absolute: B03, B09, B13 and B15 are native animated Remotion/Manim rebuilds on
  the cream stage. NO screenshot of any page, paper, table or product appears in this reel at any
  resolution, for any reason.
- ILLUSTRATE LAW: Claude UI only on B00, B02, B08, B12, B18, B19, B20.
- Strip the datable: no model names, no product version numbers, no "as of" phrasing.
- Do not generate audio. Do not compile.

Then present the narration on an animated slate for GATE P, plus every FACTCHECK row that did not
verify. Wait for my sign-off.
```

---

## STEP 2 — audio (after GATE P sign-off) — unchanged from rev 2

```
GATE P is signed off for claude-for-education/youtube/claude-liam-two-numbers-one-report.

Generate narration with Kokoro am_onyx (free — no ElevenLabs), measure real durations, write them
back to beat_sheet.json, and run align so the word clock exists for on-word reveals.

Report total runtime and flag any beat more than 30% off the ~10s planning estimate. Fix by
rewriting narration and regenerating that beat, never by hand-editing timings.
```

---

## STEP 3 — build the visuals and compile

```
Audio is locked for claude-for-education/youtube/claude-liam-two-numbers-one-report.

Build every visual slot per the plan's beat table:

- Manim: B03 (rebuilt accuracy table, four tools), B05 (the human corpus and its date), B07 (the
  "sole evidence" quote card, verbatim), B10 (the two figures the vendor page takes), B14 (the
  link graph - claim resolves to vendor page, not to paper), B16 (the four-address chain), B17
  (what fell off at each hop).
- C2 rhetorical patterns: B01, B04 (the 65/97.5 divergence - this is the reel's key figure, give
  it the most care), B06, B11. Retint pattern constants to the Claude stage: cream #F2F0E9, ink
  #3D3929, accent #D97757, warn #A44A32 - log the retint as a decision.
- C3 concept illustrations: B09 (rebuilt vendor page), B13 (rebuilt announcement), B15 (the
  button). Start from runtime/remotion/src/illustrations/ rather than authoring new motion math.

Render Remotion only via runtime/scripts/remotion_scenes.py, foreground, --concurrency=1. Never
hand-roll npx remotion render and never background it.

Then compile:

  ./brutalist-art/art run claude-for-education/youtube/claude-liam-two-numbers-one-report

One terracotta moment per beat. NBB logo bug lower-right inside title-safe on every beat. Fill the
canvas: if a graphic would still fit at half size with room to spare, it was built too small.
```

---

## STEP 4 — visual QC and final (stops for my review) — unchanged from rev 2

```
Run the VISUAL QC LAW pass on
claude-for-education/youtube/claude-liam-two-numbers-one-report per
CLAUDE-CODE-VISUAL-QC-CHECK.md:

Sample frames at >=2 fps with ffmpeg, plus each beat at ~15/50/85% of its span from the beat
sheet. Actually READ the PNGs - the mp4 probe is a file check and does not count as QC. Audit the
nine-point rubric including CANVAS FILL. Log defects and fixes to _qc/REPORT.md, fix root causes
in scene source, re-render until zero BLOCKER and zero MAJOR remain.

Also run GATE T type-lock - TYPECHECK.md with no FAIL.

Then produce the clean master:

  ./brutalist-art/art final claude-for-education/youtube/claude-liam-two-numbers-one-report

Do NOT stage to TOPOST. Do NOT publish. Report the master path, the runtime, and the QC results.
```

---

## Notes

- No `./art keys` needed — entirely free build (Kokoro, Manim, Remotion).
- No pantry, no SHOPPING.md, no human media. Fully machine-buildable after GATE P.
- Companion reel: `claude-liam-detector-never-the-standard` (deep-explainer, greeting `Namaste`). Its Act V should take its numbers from the same paper — the secondary roundup statistics come out of both films.
- Publishing is out of scope: master stays in the reel folder.

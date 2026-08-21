# BUILD-PROMPT — `claude-liam-detector-never-the-standard` (rev 3)

Five paste-ready prompts for a **local Claude Code session started in `bear-textbooks/books/`**.
Run in order. Each stops at a human gate. Do not merge them.

Reel: `claude-for-education/youtube/claude-liam-detector-never-the-standard/`
`PLAN.md` (rev 3) is in that folder and is approved. Everything derives from it.

**Rev 3 framing:** no real person, no real case. The subject is a hypothetical researcher accused of having a background chapter too close to another's.

---

## STEP 1 — script, beat sheet, factcheck (stops at Gate F + GATE P)

```
Read claude-for-education/youtube/claude-liam-detector-never-the-standard/PLAN.md — it is the
APPROVED rev 3 deep-explainer plan (42 body beats, five acts, four vox runs). Also read
books/CLAUDE.md and books/AGENTS.md, then the deep-explainer skill and its parents (ai-explainer,
explainer) via ./brutalist-art/art --list.

Build, in that reel folder:

1. Full narration for all 42 body beats plus the bookends, Teardown register (Feynman x MKBHD).
   Body beats 25-45 words; bookend beats 45-70. B00's first breath says "this is Liam, in for
   Bear"; the outro signs off the same way. Greeting "Namaste, Liam" on B00, "Your turn." on the
   handoff.
2. beat_sheet.json validated against brutalist-art/runtime/schema/beat_sheet.schema.json, with the
   lane assignment, shot blocks, vox_run ids and handoff blocks exactly as the plan specifies:
   R1 A02->A03, R2 B05->B06, R3 C09->C10, R4 E04->E05. Channel claude-liam, engine kokoro, voice
   am_onyx, palette claude, folderLabel @NikBearBrown. Author sub_beats word timing on every beat
   whose reveal must land mid-sentence.
3. FACTCHECK.md — claim | verdict | source | fix, seeded with the plan's eight graded rows.
4. SOURCES.md, including web.archive.org capture URLs for every vendor page quoted.

THE EDITORIAL LAW IN THE PLAN IS BINDING ON THIS STEP. Four parts, none negotiable:

- NO REAL PERSON, NO REAL CASE. No name, no photograph, no real thesis, no real institution, and
  no repetition of any live or unadjudicated allegation about any individual. If a draft line
  starts to resemble a recognisable real case, rewrite it. The researcher is hypothetical and
  stays hypothetical.
- NO RECIPE. Act III shows that the loop exists and closes. It does NOT walk through it as
  instructions — no settings, no ordering tips, no "this is what worked," and no on-screen
  demonstration of a passage going from flagged to clean. The affordance is the argument; the
  procedure is not the content.
- NO ASSERTED SUCCESS RATE. Do not claim, and do not test, whether a given rewrite defeats a given
  checker. What is documented and narratable: the two pairs sit adjacent in one strip, both are
  free, and each product's own marketing states its purpose. Write C05 and C11 in terms of what
  the products are FOR, never in terms of a measured outcome.
- NAME THE LINE PLAINLY. D08 cannot be softened, shortened, or moved later in the cut. A clean
  score is not compliance; inserting an unreviewed section is a breach whether or not the number
  is green.

Other hard constraints:

- Verify the four vendor marketing strings (C04, C08) live on build day, character for character,
  and capture each page to web.archive.org. If the nav has been reorganised, re-shoot the beat
  against what it says then — the structural argument does not depend on the current wording, and
  must never be narrated as breaking news.
- The vendor beats judge the MARKET, not one company. Include the line noting the same
  detector/evasion pairing exists across the category.
- FACTCHECK rows 5, 6 and 7 are graded WEAK or MEDIUM in the plan. Verify each against a primary
  source or cut the specific and keep the pattern. E06 currently ships with NO number by design —
  add one only if it comes from the primary study itself, never from a summary.
- Policy quotes (D03, D05, D06) and the examiner instruction (D08) must come from the
  institutions' own pages, not news write-ups.
- Strip the datable: no model names, no version numbers, no "as of" phrasing. The watermark is a
  mechanism, not a product.
- Do not generate audio. Do not compile. Stop when the four files exist.

Then present: the lane histogram recomputed from the actual beat sheet, every FACTCHECK row that
did NOT verify, and the narration on an animated slate for GATE P. Wait for my sign-off.
```

---

## STEP 2 — audio (only after you sign off GATE P)

```
GATE P is signed off for claude-for-education/youtube/claude-liam-detector-never-the-standard.

Generate narration with Kokoro (am_onyx, free — no ElevenLabs, no nbb, no Slurm round trip),
measure the real durations, write them back to beat_sheet.json, and run the align step so the word
clock exists for on-word reveals.

Report the measured total runtime and the per-act breakdown, and flag any beat whose measured
duration is more than 30% off the plan's ~10s estimate. Do not fix timings by hand — if a beat is
wrong, rewrite its narration and regenerate that beat's audio.

Stop at audio lock. Do not write SHOPPING.md yet.
```

---

## STEP 3 — Gate D2: pantry search and shopping list (only after audio lock)

```
Audio is locked for claude-for-education/youtube/claude-liam-detector-never-the-standard.

Run the Tier-0 library pass first. For each of the 9 vox beats — A02, A03, B05, B06, C09, C10,
D07, E04, E05 — search the toolkit still stock:

  python3 brutalist-art/runtime/scripts/pantry_search.py "<terms>"

LOOK at the candidates; do not match on filename. Copy real matches in with
--copy claude-for-education/youtube/claude-liam-detector-never-the-standard --beat <BID>.

All nine slots are Tier 1 — generic and illustrative. There are no Tier 2 or Tier 3 entries in
this reel and none may be introduced: nothing may depict a real person, a real document, or a real
institution. If a candidate still is a recognisable real place or person, reject it.

Run-mates must come from the same visual stock: B05 with B06, C09 with C10, E04 with E05.

Then write SHOPPING.md from the LOCKED durations, one entry per still still missing, tier-tagged.
Matched entries pre-checked with their library id. Motion assets ask for more duration than needed
so conform trims rather than stretches.

Do not compile yet.
```

---

## STEP 4 — Gate D1: the slate previz

```
Compile the full-length slate previz for
claude-for-education/youtube/claude-liam-detector-never-the-standard:

  ./brutalist-art/art run claude-for-education/youtube/claude-liam-detector-never-the-standard

Real audio, real Manim and Remotion beats, slates in every unfilled vox slot, --review burn-in.
Render Remotion only via runtime/scripts/remotion_scenes.py, foreground, --concurrency=1 — never
hand-roll npx remotion render and never background it.

Verify by LOOKING at frames and at qc-sheet.png, not by reading the log. Then tell me the output
path and the runtime, and list every slot still on a slate. This is a previz — do not describe it
as a cut.
```

---

## STEP 5 — pantry fill, QC, final

```
I have dropped stills into
claude-for-education/youtube/claude-liam-detector-never-the-standard/pantry/.

Intake them with the pantry command word (treat, rename, seat on the Claude cream stage:
desaturate ~80%, contrast ~1.15, film grain, warm-ink vignette, terracotta as the one accent).
Set shot.focus per beat toward the subject of that beat's sentence. Fill the .source.txt sidecars.
Recompile — only changed slots.

Then run the VISUAL QC LAW pass per CLAUDE-CODE-VISUAL-QC-CHECK.md (sample frames at >=2 fps plus
each beat at ~15/50/85% of its span, actually READ the PNGs, audit the nine-point rubric including
CANVAS FILL, log to _qc/REPORT.md, fix root causes in scene source, re-render until zero BLOCKER
and zero MAJOR). Also run GATE T type-lock — TYPECHECK.md with no FAIL.

Then produce the clean master:

  ./brutalist-art/art final claude-for-education/youtube/claude-liam-detector-never-the-standard

Do NOT stage to TOPOST and do NOT publish. Report the master path and the QC results.
```

---

## Notes

- `./art keys` is not needed — entirely free build (Kokoro, Manim, Remotion).
- The nbb voice is unavailable from any sandboxed session (port 22 blocked); this reel is Kokoro by design.
- Companion reel: `claude-liam-two-numbers-one-report` (ai-explainer). Keep the world-language greetings distinct — this one takes `Namaste`, that one takes `Merhaba`.
- Publishing is out of scope. Master stays in the reel folder.

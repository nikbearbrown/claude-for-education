# PLAN — `claude-liam-detector-never-the-standard` (rev 3)

**Skill:** deep-explainer · **Book:** `claude-for-education` · **Channel:** `claude-liam`
**Target:** `claude-for-education/youtube/claude-liam-detector-never-the-standard/`
**Voice:** Kokoro `am_onyx` (free) · **Register:** Teardown · **Greeting:** `Namaste, Liam`
**Working title:** *The Detector Was Never the Standard*

**Rev 3 — the framing changed.** No real person appears in this film. No real thesis, no real institution, no real case. The subject is a **hypothetical researcher accused of having their background chapter sit too close to someone else's** — the most common shape this accusation takes. Every argument the earlier draft made survives; the man does not appear in it.

**What this buys.** The reel no longer rests on a single pseudonymous, unreviewed overlap analysis — that material is gone entirely, along with the FACTCHECK problem it created. Nothing here asserts guilt about anyone, and no unadjudicated allegation is repeated.

---

## The argument

A researcher is accused of background research too close to another's. The instrument that produced the accusation measures one thing: whether a run of this text already exists somewhere else. It never measured whether credit was owed — we let it stand in for that.

And now the same market that sells the instrument sells, one tab away, the thing that clears it. Scan, hit, next tab, reword, re-scan. Detector flags it, humanizer launders it, re-scan. Free, no account, same page.

**The landing:** the loop produces a clean score and breaches the actual rule anyway — because what the rules turn on is whether you reviewed the work and can defend it, and no number on that page has ever read that. Passing the check was never compliance. The detector was never the standard.

---

## Act map

| Act | Beats | Job |
|---|---|---|
| **I — The Accusation** | 7 | A hypothetical researcher; what the report showed; why that shape is the common one |
| **II — The Instrument** | 7 | What a similarity score measures, and what we made it stand for |
| **III — The Loop** | 11 | The tab strip; both adjacent pairs; the loop closes; the score goes clean and nothing changed |
| **IV — The Rules** | 8 | What 2026 policy says; the loop passes the check and breaches the rule regardless |
| **V — What's Left** | 9 | Detection collapse; watermarking answers the wrong question; the vendors already pivoted |

**Body beats: 42.** Bookends and the closing block exempt.

## Lane histogram

```
VOX       █████████                     9   21.4%   target 20–25%   PASS
MANIM     ██████████████               14   33.3%   target 25–40%   PASS
REMOTION  ████████████████             16   38.1%   target 30–45%   PASS
CARD      ███                           3    7.1%   remainder       PASS
```

Consecutive-lane lint: no run of 3+ same-lane beats outside a vox run. **PASS.**
**Duration estimate:** 42 × ~10 s ≈ 7:00, plus bookends ≈ 1:35 → **~8:35**. In the 5–10 band. Measured audio is the only clock.

---

## Beat plan

### B00 — COLD OPEN · `ClaudeComposerAsk` · greeting `Namaste, Liam`
Ask: *"If a researcher's background chapter is flagged as too close to someone else's, what has actually been proven?"* Output lands answered. "…this is Liam, in for Bear." 45–70 words.

### ACT I — THE ACCUSATION

| ID | Lane | Beat |
|---|---|---|
| A01 | CARD | "I. The Accusation" |
| A02 | VOX **R1 b1** | A researcher. A finished thesis. Their own fieldwork, their own data, their own findings. And a background chapter written in the last weeks before a deadline that would not move. |
| A03 | VOX **R1 b2** | Someone runs it against an earlier work on the same subject, and the report comes back with matches. |
| A04 | REMOTION C2 | Note what is and is not alleged. Not the results. Not the method. The background — the part that summarises what everyone else already said. |
| A05 | MANIM | What a report like that shows: runs of text appearing in both documents, listed, highlighted, counted. |
| A06 | MANIM | And the shape it usually takes — dense in the review chapter, near zero in the methodology and the data. |
| A07 | REMOTION | That shape is not exotic. It is the single most common form this accusation takes, in every discipline that requires you to survey a literature before adding to it. |

### ACT II — THE INSTRUMENT

| ID | Lane | Beat |
|---|---|---|
| B01 | REMOTION spark-line | "II. The Instrument" |
| B02 | MANIM | A similarity score measures one thing. Does a run of this text already exist in some other document. That is the entire question it asks. |
| B03 | REMOTION C3 | Between two independently written documents the expected number of long identical runs is not "small." It is zero. Prose does not collide at that length by accident. |
| B04 | MANIM | So the mechanism is honest: sort every position in every text, find the repeats, report them. |
| B05 | VOX **R2 b1** | Before it was software it was a cabinet. Every word of every book, indexed by where it appeared. |
| B06 | VOX **R2 b2** | Same mechanism, more shelves. |
| B07 | REMOTION | What it reports is collision. It has never reported whether credit was owed — that requires knowing what was cited, what was quoted, what was understood. We let a collision count stand in for all three. |

### ACT III — THE LOOP

| ID | Lane | Beat |
|---|---|---|
| C01 | CARD | "III. The Loop" |
| C02 | REMOTION C3 · **rebuilt tab strip** | Here is the product strip of a mainstream writing-tools site. Six tabs. Free. No account. |
| C03 | MANIM | The first pair. A plagiarism checker — and one tab away, a paraphrasing tool. |
| C04 | REMOTION C3 · copy side by side | Read what each promises. The checker: ensure every word is your own. The rewriter, one tab across: quickly reword sentences for essays. |
| C05 | MANIM | Which closes a loop. Scan. See a hit. Move one tab. Reword the passage. Scan again. |
| C06 | REMOTION C2 | And nothing about that is a workaround or an exploit. It is two advertised products used for their advertised purposes, in the order the navigation puts them in. |
| C07 | MANIM | The second pair, further along the same strip. An AI detector — and one tab away, an AI humanizer, which names the models whose output it launders. |
| C08 | REMOTION C3 | And read who the detector is sold to. A score shows how much of your work appears to be written with AI "so you can submit it with peace of mind." Not the institution's instrument. The writer's pre-flight check. |
| C09 | VOX **R3 b1** | A desk, late. |
| C10 | VOX **R3 b2** | Pull back — every desk. |
| C11 | REMOTION | Run the loop and the number goes clean. Now ask what changed about the work. The same passage says the same thing, standing on the same source, credited to nobody. |

### ACT IV — THE RULES

| ID | Lane | Beat |
|---|---|---|
| D01 | CARD | "IV. The Rules" |
| D02 | REMOTION C2 | Which raises the question nobody in this argument gets asked. Is a researcher in 2026 expected to write all of this by hand, because hand is purer? |
| D03 | MANIM quote | One university permits generative AI and requires it declared on the thesis declaration form — explicitly including drafting ideas and planning or structuring written material. |
| D04 | REMOTION | Structuring your writing with a model is a disclosure item, not an offence. Purity is not the standard anywhere in this. |
| D05 | MANIM quote | Another permits students to rewrite, rephrase and paraphrase their own work to improve how it reads. Assistance in expressing your ideas. |
| D06 | MANIM quote · **the hinge** | And prohibits one thing by name: inserting unreviewed AI-generated sections — with literature reviews given as the example. |
| D07 | VOX | A room, two examiners, a table. |
| D08 | REMOTION C3 | So run the loop and you get a clean score and a breach. The rule turns on whether you reviewed it and can defend it. Examiners at that same institution are told not to run detection software at all. |

### ACT V — WHAT'S LEFT

| ID | Lane | Beat |
|---|---|---|
| E01 | REMOTION spark-line | "V. What's Left" |
| E02 | MANIM isotype | More than fifty universities have switched AI writing detection off. |
| E03 | MANIM | One found its tool marking entirely human writing as machine-generated. Another ran thousands of misconduct cases in a single year and dismissed many of them on investigation. |
| E04 | VOX **R4 b1** | A hall of desks. |
| E05 | VOX **R4 b2** | A screen at the front of it. |
| E06 | MANIM | The false-positive burden did not fall evenly — it fell hardest on writers whose first language is not English. The instrument had a demographic. |
| E07 | MANIM | Then watermarking. Split the vocabulary, seeded by the words just written. Nudge one half. Count how many landed marked. Compare to chance. A z-score, a p-value. Elegant, and honest about itself. |
| E08 | REMOTION | It answers one question: were these tokens sampled by a model. Not who wrote it. Not what it stands on. Not whether anyone read it. |
| E09 | REMOTION | And the vendors know. One of the same companies selling detection shipped a provenance-tracking product and said in its own launch copy that algorithmic AI detection is imperfect. The replacement for a detector was never a better detector. |

### CLOSING BLOCK (exempt)

**VERDICT** — `ClaudeVerdictArtifact`. Three moves: (1) the instruments are honest; similarity reports collision, watermarking reports generation, and both do it well; (2) what broke is the inference — that either number was ever a verdict about a person — and you can tell it broke because the same shop sells the check and the thing that clears it, one tab apart, to the same customer; (3) the loop produces a clean score and changes nothing about whether the work was understood, which is the only question the rules ever turned on. The instrument that reads it is a person asking you to explain your own work. We had that the whole time.

**YOUR TURN** — `ClaudeComposerAsk`, greeting `Your turn.` Prompt read aloud verbatim and discussed:

> *"Take the last substantial thing I wrote with your help. Don't judge it. List the five sources its argument is actually standing on, and tell me which of them I'd struggle to defend if someone asked me about them out loud."*

Two lines on why: it converts integrity from a detection problem into a preparation problem, and the output is a to-do list, not a verdict.

**TITLE RE-READ** — `ClaudeTitleOutro`. *The Detector Was Never the Standard* · `@NikBearBrown` · "Liam, in for Bear."

---

## EDITORIAL LAW — this film demonstrates an affordance, it does not teach a recipe

Binding on the script step. Three rules:

1. **No recipe.** Act III shows that the loop exists and closes. It does not walk through it as instructions — no settings, no ordering tips, no "this is what worked," no on-screen demonstration of a passage going from flagged to clean. The affordance is the argument; the procedure is not the content.
2. **No asserted success rate.** Whether a given rewrite defeats a given checker is an empirical claim. The film does not assert it and the build does not test it. What is documented and narratable: the two pairs are adjacent in one strip, both are free, and each product's own marketing states its purpose. C05 and C11 are written in terms of what the products are *for*, never in terms of a measured outcome.
3. **Name the line plainly.** D08 is not optional and cannot be softened or moved later in the cut. A clean score is not compliance; inserting an unreviewed section is a breach whether or not the number is green. The film's demonstration must remain self-limiting — the loop is the evidence that the detector was never the standard, never an invitation to run it.

**No real person, no real case.** No name, no photograph, no real thesis, no real institution, and no repetition of any live or unadjudicated allegation about any individual. If the script drifts toward a recognisable real case, it has failed this law.

---

## Pantry — 9 vox stills, all Tier 1

| BID | Subject | Tier |
|---|---|---|
| A02 | Bound thesis / manuscript on a desk, generic | 1 |
| A03 | Two documents side by side, generic | 1 |
| B05 | Pre-digital library index card | 1 |
| B06 | Card catalogue cabinet, wide (must match B05's stock) | 1 |
| C09 | Desk, laptop, papers, night | 1 |
| C10 | Reading room, wide (must match C09) | 1 |
| D07 | Examination room, two chairs, a table | 1 |
| E04 | Hall of desks | 1 |
| E05 | Screen at the front of a hall (must match E04) | 1 |

**Zero Tier 2, zero Tier 3.** Nothing depicts a real person, document, or institution. Tier-0 library pass (`pantry_search.py`) runs first on all nine — most should hit existing stock, which makes this reel close to fully machine-buildable.

## FACTCHECK — rows to carry into FACTCHECK.md

| # | Claim | Strength | Required before ship |
|---|---|---|---|
| 1 | The four marketing strings quoted in C04 and C08 | Verifiable | Live check character-for-character **on build day**, plus `web.archive.org` capture; log capture URLs in SOURCES.md |
| 2 | The two pairs are adjacent in the same product strip | Verifiable | Same live check. If the nav is reorganised, re-shoot against what it says then — the structural argument is unaffected |
| 3 | The university policy quotes (D03, D05, D06) | Strong | Verify against the institutions' own pages, never a news summary |
| 4 | Examiners instructed not to use detection software (D08) | Strong | Same — primary source |
| 5 | "More than fifty universities" (E02) | **Weak** — secondary roundup | Get a defensible count or soften to "dozens" |
| 6 | The 100%-on-human-text case and the thousands-of-cases case (E03) | **Weak** | Verify against each institution's own statement, or cut the specifics and keep the pattern |
| 7 | Uneven false-positive burden on non-native English writers (E06) | Medium | Trace to the primary study. **E06 currently ships with no number by design** — add one only if it comes from the study itself |
| 8 | A detection vendor shipped provenance tracking and called algorithmic detection imperfect (E09) | **Strong** — company's own launch post | Quote character-for-character; archive the post |

**Deleted in rev 3:** every claim that depended on the pseudonymous overlap analysis — the matched-sentence count, the per-million ratios, the near-control result. None of it appears in this cut, and the verdict's old self-referential caveat about unreviewed sources is no longer needed.

## Standing constraints

- Teardown voice throughout (books/CLAUDE.md rule 6); fact-check everything (rule 7); GATE T type-lock (rule 8); never publish.
- Strip the datable: no model names, no version numbers, no "as of." The watermark is a mechanism, not a product. Universities are described by what they did.
- Vendor is named only where its own published marketing is the evidence, and the beat judges the **market** — one line notes the same pairing exists across the category, so it does not read as a hit piece on one brand.

## What this cloud session cannot do

`./art`, Kokoro, Manim, Remotion and `pantry_search.py` are on the Mac. This session authors the plan, script, beat sheet, FACTCHECK and BUILD-PROMPT; GATE P, audio, Gate D2 and the Gate D1 previz run locally.

# SOURCES — claude-liam-the-lever-nobody-pulled

Fact-check performed 2026-08-03. Revised the same day against the fuller three-vendor
research document and its Part 5 verified-findings inventory.

This reel's central claim is a **negative** — that nobody has done a particular thing — and
its second claim is that only one of three vendors even ships the thing. Neither can be
sourced the way a figure can, so this file is organised around what was read, what was
carried, and what the negative is permitted to say.

## Primary sources read directly

| # | Source | Used for |
|---|---|---|
| S1 | Anthropic Help Center — *Set organization instructions* · support.claude.com/en/articles/14546867-set-organization-instructions | the plan tiers, the 3,000-character cap, the scope line, the precedence rule, the safety ceiling |
| S2 | Claude Code docs — *Settings* · code.claude.com/docs/en/settings | `managed-settings.json`, its MDM deployment path, what it governs, and the `claudeMd` field |
| S3 | Teaching@Sydney / educational-innovation.sydney.edu.au — Cogniti, and the 'Mrs S' case write-up | the teacher-authored agent model, the two verbatim instruction excerpts, the visibility claim |

## Verbatim strings that appear on screen

Every one is quoted exactly and carries an attribution line in its beat. On-screen text uses
**the source's own spelling** (American). Spoken narration anglicises freely — that is a
register choice and does not touch a quotation.

- **B02** (S1) — "All people in your organization, every conversation." · availability to
  Admins, Owners and Primary Owners on Team and Enterprise plans · the 3,000-character cap.
- **B03** (S1) — "If an individual instruction directly contradicts an organization
  instruction, Claude favors the organization-level instruction."
- **B04** (S1) — "can't disable Claude's built-in safety guidelines or content policies."
- **B11** (S3) — "isn't seen by students" · the driver's-seat framing · no programming
  knowledge required.
- **B12** (S3) — Mrs S is instructed to "roleplay as a busy kindergarten teacher" and to
  "challenge the ideas that Joanne's students presented, push back if dissatisfied." The
  narration replaces the instructor's first name with "the students" — see the naming rule.
- **B16** (S2) — `/Library/Application Support/ClaudeCode/` and the `claudeMd` field,
  "CLAUDE.md-style instructions injected as organization-managed memory. Only honored when
  set in managed or policy settings."

## B05 — the three-vendor comparison, and why it is stated at this grain

B05 is the beat that makes the title fair, and it is deliberately coarse. It says three
things and no more:

- **Anthropic** ships an organisation-wide instruction field, applying to every conversation,
  taking precedence over the user. That is S1, read directly.
- **OpenAI** Enterprise and Edu give roles, custom-role permissions, and workspace-distributed
  custom GPTs — but no workspace-level setting that restrains how answers come out. That
  restraint has to be written by hand into a single GPT's instructions.
- **Google** for Education exposes per-app and per-org-unit toggles plus age gating for
  under-18 users. The granularity is *which surfaces are on*, not *how they behave*.

The OpenAI and Google descriptions come from the research document's Part 2, which cites the
vendors' own help centres. **They were not re-read directly in this pass.** They are used
because they are negative capability claims at the coarsest possible level — "there is no
workspace-level answer-restraint setting," "there is no system-prompt equivalent" — and a
negative capability claim at that grain is the kind that a vendor help centre would
contradict loudly and visibly if it were wrong.

They still carry risk, and the risk is asymmetric in the reel's favour: if either vendor
turns out to ship a broader control than described, the film's finding gets *stronger*, not
weaker — there would be more unused lever, not less. B05's on-screen treatment is built to
survive that: three columns of different shapes, no ticks, no crosses, no scoreboard.

## Carried from the research document, NOT independently confirmed

**B13 is the whole of this category.** TritonGPT (UC San Diego), Maizey (Michigan), the
Arizona State language tutor, and Vanderbilt's Amplify come from the research document's own
Part 5 inventory. They were not re-verified against each institution's pages here.

They are used anyway: each is a publicly announced product of a named institution, the
on-screen `sub` states only what the institution itself advertises, and none carries load the
argument depends on. B13's job is to show the pattern in B11/B12 is not one university being
unusual. If one card were wrong, the claim survives on the other three plus Sydney.

**B14 (York)** sits in the same category and is the reel's most valuable carried item: an
instructor built a Gemini Gem course tutor with lecture materials and subject boundaries, and
told students they could copy the prompt and materials into another AI tool — disclosed as a
scaffold rather than an enforcement mechanism. The instructor is not named.

**B08's four institutions** — Northeastern, LSE, Champlain, Carnegie Mellon — appear only in
the *negative* column: each has a documented licence, SSO and privacy posture and **no**
publicly documented university-authored instruction. That is the safest possible use of a
carried name, because the claim being made about them is "no public evidence," which is
exactly what the inventory established.

Northeastern appears here **only** on that public-evidence footing. The private committee
correspondence that started this line of research is not referenced, quoted, characterised,
or alluded to anywhere in the film.

## B17 — the research pass that fabricated, and why it is in the film

A second research pass on this question returned considerably more than the first: named
campus tools, precise instance counts, student-population figures. It also invented a detail
about the co-authors of the paper it was helping write — a claim that happened to be
checkable, and was wrong.

Every specific from that pass is quarantined: Harvard's "AI Sandbox," a Canvas-integrated
"PingPong"/"Coaching Bot," Boston University's "TerrierGPT," "50,000 students across 13
campuses," "3,500 Maizey instances." **None of them appears in this reel, in any beat, in any
caption, or in the description.** Not disproved — unconfirmed.

B17 exists because this is the channel's own discipline demonstrated on itself: the artifact
is not the world, and a source that fabricates one checkable thing has told you what to do
with everything uncheckable. B17's production note forbids rendering any quarantined name
legibly, because drawing them would reintroduce exactly the claims the beat exists to
withhold.

## What the negative is permitted to claim — B10 and B18 as a pair

B10 states the finding hard: no documented case of a university writing an organisation-wide
instruction at campus scale. B18 then **narrows it on screen**, shrinking the card from "no
university has configured one" to "no public evidence of one exists," and draws the blind
spot — admin console configuration is not public and never will be — deliberately outside the
searched set.

**B18 may not be cut, merged, or shortened.** If the reel keeps B10 and loses B18, it makes a
claim the evidence does not support, in Bear's channel voice, on a topic universities read.
The search space is named on screen in B18 (IT policy pages · AI task force reports · faculty
governance minutes · vendor announcements) so a viewer can judge how much the absence is
worth.

## Corrections applied to the source document

1. **The Education plan is not claimed.** S1 names Team and Enterprise and does not mention
   Education or Edu anywhere. The reel says "universities on Enterprise have it." If the Edu
   tier is later confirmed to carry the field, that is a one-word edit in B00.

2. **The `managed-settings.json` correction was itself corrected.** The source first named
   that file as the campus deployment mechanism, then corrected itself. The correction was
   right about the surface and slightly overstated: it really is Claude Code, MDM-deployed to
   developer machines, governing permissions and tool use — but it *does* carry a `claudeMd`
   field that injects organisation-managed instructions, honored only in managed or policy
   settings. B16 says both halves.

3. **No individual is named.** Not the Sydney educator, not the York instructor, not anyone
   in the correspondence that prompted the research. Institutions are named; people are not.

4. **"Adoption" is separated from "configuration" and given two beats.** B07 makes the
   distinction and B08 makes it concrete with four names. The source treats these as one fact
   and it is the single largest source of bad data in this space.

5. **The authority question was promoted to a beat of its own (B09).** The source raises it in
   passing. It is the actual thesis — the committee and the console are different rooms — and
   B09/B19 are a matched pair: B09 draws a void and refuses to cross it, B19 crosses it. That
   is the only connector in the film spanning that gap.

6. **The design and enforcement material was removed to a companion reel.** Part 3's four
   bypasses, the four design axes, WashU's adversarial testing, Utah and Duke — all of it now
   lives in `claude-liam-the-smallest-lever`. Keeping it here pushed the runtime past eleven
   minutes and blurred two different films: this one is a finding, that one is a design.

## Register note

Teardown. The reel is not neutral about the finding — B15 argues the institutions did not
decline to use the operator layer, they built a parallel one by hand because the vendor's
version was never presented as something a teacher could touch. That is an interpretation and
it is marked as one, stated as a conclusion drawn from B11–B14 rather than as a quoted fact.

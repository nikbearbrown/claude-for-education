# Chapter 37 — School Effects as System Context
*"School effects" is not a thing schools do. It is the accounting category for everything they do — and the platform is selling the ledger line as a lever.*

One influence: generalized school effects, d = 0.48 — not a thing schools do, but the accounting category for everything a school is: the aggregate impact of attending one school rather than another. In Hattie's synthesis it is a context variable, sitting above the hinge with no lever attached. AI's relationship is adjacency: it can describe, compare, and forecast school-level patterns with new precision, and none of that changes a school. The chapter uses this strange entry to teach a system-level reading skill — what aggregate numbers can tell a leadership team, and what they cannot tell anyone.

**Group Profile: School Effects as System Context**

| Profile | Detail |
|---|---|
| Influences in this group | 1 of Hattie's 252 |
| Effect size | d = 0.48 |
| Hattie band | Above the d = 0.40 hinge |
| AI feasibility | AI-adjacent |
| Human irreducibility | Medium |
| Substitution risk | Low |
| Cognitive-work conflict | None |
| Influence | Generalized school effects (rank 85, d = 0.48) |

Vivian Cho is four months into her first term on the school board and has done the thing new board members are always urged to do and rarely forgiven for: the reading. Tonight's agenda includes a proposal from a consulting firm for a "School Quality Intelligence Platform" — an AI analytics layer that ingests the district's assessment, attendance, discipline, staffing, and demographic data, scores each school on a composite quality index, ranks them, and recommends "evidence-based levers" for the underperformers. The firm's deck cites the research the way decks do: school effects matter, Hattie's generalized school effects sit at d = 0.48, above the hinge — *which school a child attends shapes their achievement, and now you can manage it like a portfolio.*

Vivian's reading has left her with a question she suspects is naive and is in fact the sharpest one available: *if school effects are a thing, what exactly is the thing?* When the platform ranks Jefferson Elementary below Whitman, what has it measured — Jefferson's teaching, or Jefferson's catchment? And when it recommends "levers," is it recommending anything Jefferson can pull, or just describing Jefferson's circumstances back to it with a confidence interval?

This chapter exists for board members, superintendents, and committee chairs holding exactly this deck.

## What the Number Summarizes

Generalized school effects (d = 0.48) at rank 85 on the 2018 252-influence list summarizes a research tradition rather than an intervention: studies estimating how much of the variation in student achievement attaches to *which school a student attends*, over and above what students bring through the door.

The tradition's founding document is the 1966 Coleman Report — still arguably the most consequential piece of education research ever commissioned — whose central finding was that measured school resources explained far less of the variance in achievement than family background did. Decades of better data and better methods have refined Coleman without overturning him: across systems, something on the order of ten to twenty percent of achievement variance typically lies *between* schools, with the large majority lying *within* them — between classrooms, between teachers, between students in the same building [verify — the proportion varies substantially by country, subject, and method; OECD analyses show between-school variance far higher in heavily tracked systems]. Hattie's own gloss on his corpus has become a refrain: the greatest source of variance is within schools, not between them.

Hold both halves honestly. d = 0.48 is above the hinge: schools are not interchangeable, and which one a child attends is associated with real differences — an aggregate of everything this book has spent thirty-six chapters disaggregating: the feedback culture, the collective efficacy, the discussion quality, the goal ownership, all of it summed into one institutional residue. That is precisely why the number is not a lever. **"School effects" is not a thing schools do; it is the accounting category for everything they do.** A board cannot buy 0.48 of it, because the row has no mechanism of its own — it is the ledger line where the other 251 rows are totaled by address.

![Proportional bar showing most achievement variance lies within schools (around 85 percent) and only a small share between schools (around 15 percent)](images/37-school-effects-as-system-context-fig-01.png)
*Figure 37.1 — Where the variance lives: between vs. within schools*

One more reading discipline before the deck comes back out: school-level composites are noisy, and small schools' year-to-year swings are heavily luck. League tables built from them reliably reward enrollment size and demographic stability as if they were quality. Kraft's (2020) benchmarks apply with full force — at the school level, on real assessments, effects of 0.10 to 0.20 from genuine improvement efforts are substantial, which calibrates how seriously to take a dashboard that displays inter-school gaps to two decimal places.

## The Braid Inside the Number

Why does the influence exist at all — what makes one school's residue different from another's? The between-school signal is a braid of three strands, and untangling them is the entire interpretive task.

**Composition.** Students arrive unevenly. Prior achievement, family resources, language background, mobility — context signals from Chapter 6 — cluster by neighborhood and therefore by school. A school's average outcomes reflect its intake before they reflect anything the school did. This strand dominates raw rankings, which is why raw rankings are largely maps of housing.

**Concentration effects.** Composition is not just a confound; it is partly causal. Peer effects, the operational drag of high mobility, the difficulty of staffing high-poverty schools — disadvantage concentrated is more than disadvantage summed. This strand is real, and it is *structural*: it responds to assignment policies, staffing incentives, and resource allocation — board-level work — not to anything an analytics license touches.

**Institutional practice.** The residue that genuinely belongs to the school: the aggregate of teaching quality, leadership, coherence, and culture — the rows this book has chapters for. This is the strand a board most wants to see, and it is the *smallest and hardest to isolate* of the three, visible only after serious statistical effort to strip the first two strands out.

![Three-strand braid decomposing the school-effects number — composition the thickest confound, concentration the structural middle strand, institutional practice the thinnest and only true quality strand](images/37-school-effects-as-system-context-fig-02.png)
*Figure 37.2 — The three-strand braid inside the school-effects number*

<!-- → [DIAGRAM: Three-strand braid model of school effects — three parallel strands labeled Composition, Concentration, and Institutional practice; Composition strand labeled "dominates raw rankings; maps to housing"; Concentration strand labeled "structural, responds to board-level policy"; Institutional practice strand labeled "smallest, hardest to isolate, only strand 'quality' honestly describes"; bottom annotation: "Raw composite index = all three strands braided, presented as strand three"] -->

Now the platform's epistemics are assessable. An AI layer can describe the braid magnificently — pattern detection across noisy administrative data is exactly what the technology is for. What it cannot do, from observational district data, is reliably separate the strands. And what its interface will do by default is present the braid as if it were strand three — *quality* — because quality is what the customer wants to manage. The composite index does not lie, exactly. It answers a different question than the one on its label.

## What AI Can Safely Do

Read as an instrument panel rather than a steering wheel, this platform class is genuinely valuable — and the word "instrument" is the disciplining metaphor. An altimeter does not fly the plane.

**Aggregate and surface.** One coherent view across assessment, attendance, discipline, staffing, and mobility data — replacing the analyst-weeks that currently stand between a board and its own district's facts.

**Disaggregate relentlessly.** The platform's highest use is the opposite of its headline feature: not ranking schools but *unbundling* them — which classrooms, which student groups, which transitions carry each school's pattern. Within-school variance is where the action is. A tool that defaults to school-level composites is pointing its lens at the wrong grain.

**Run the equity audit.** Where do flags, resources, experienced teachers, and course access cluster? Do the platform's own risk labels track demographics more than performance trajectories? The Chapter 25 warning scales up intact: prediction systems scale labels fast and make them feel objective.

**Generate hypotheses for human investigation.** "Jefferson's grade 4–5 math slide is concentrated in students who joined after kindergarten" is a finding worth a site visit. The platform proposes; the visit disposes.

**Track the board's own experiments.** Whatever the district tries — a staffing incentive, a boundary adjustment, an instructional initiative — the analytics layer is the cheap, durable way to watch outcomes against a pre-registered baseline. Instrumentation for the district's interventions, never a substitute for having any.

## The Substitution Trap

With no learner in the loop, the trap mutates. What gets substituted is not cognitive work but **institutional judgment** — and the failure modes are a board-level mirror of every learner-level trap in the book.

**The ranking mistaken for a diagnosis.** The composite index becomes the district's reality. Schools are "low-performing" rather than "high-mobility with a staffing churn problem in grades 3–5." The label travels — into press coverage, into real estate sites, into the staffing market, where it makes the flagged school harder to staff — and the prediction begins purchasing its own accuracy. A dashboard can deepen the pattern it displays.

**The lever illusion.** The platform recommends "levers," and the recommendations are necessarily generic — improve attendance, strengthen Tier 1 instruction — because generic is all that observational district data can license. The board, having bought intelligence, feels it has bought capacity. It has bought a description. A model can identify risk; only a human system can allocate support, redesign instruction, or change conditions. A technically successful and educationally inert deployment is the most expensive way to learn what the district already knew.

**The dashboard as substitute for the visit.** Subtlest of all: board members stop asking superintendents hard questions because the platform appears to have asked them. Attention, the board's scarcest resource, migrates from schools to screens. The metric layer was supposed to provoke governance; it absorbs it.

| Trap | What the board believes it delivers | What it actually delivers | Observable failure signature |
|---|---|---|---|
| Ranking mistaken for diagnosis | A verdict on school quality | A composite of composition + concentration + practice, presented as practice | Labels travel into press, real estate, and the staffing market; the flagged school gets harder to staff |
| Lever illusion | Capacity to improve schools | A generic description ("improve attendance," "strengthen Tier 1") that observational data can license | Recommendations adopted, nothing changes; an expensive restatement of the known |
| Dashboard as substitute for the visit | Governance performed | The appearance that hard questions were already asked | Board attention migrates from schools to screens; site visits decline |

*Each trap involves the platform performing institutional judgment rather than informing it.*

## The Case in Full

Vivian Cho did not kill the proposal. She rewrote what it was for — in a memo that took her one evening and reframed the procurement around a single distinction: *this platform reads context; it does not pull levers; price it and govern it as an instrument panel.*

Stripped of its ranking layer — the composite index and its color-coded league table were a contract exclusion, not a setting — the platform earned its license inside a year. Its disaggregation work surfaced two findings the district's annual reports had buried. The celebrated Whitman Elementary was coasting: its strong composite masked flat growth for its lowest-prior-achievement quartile, who did no better there than at any other school in the district. And Jefferson's notorious math slide was not a teaching story at all but a mobility story, concentrated almost entirely in students arriving mid-year, landing in the district's only school with no structured onboarding for transfers. Neither finding was an intervention. Both were *better questions*, and the board funded the answers: a transfer-intake protocol at Jefferson, and a growth-equity review at Whitman that its own composite ranking would never have triggered.

The dangerous moment came from the platform's most demo-friendly feature: per-school "improvement lever" recommendations, generated automatically each quarter. The first batch recommended that Jefferson "strengthen family engagement to address attendance" — boilerplate, harmless-looking, and wrong. Jefferson's attendance figures were an artifact of its mid-year arrivals' enrollment-date accounting, which the platform read as absence. A board member quoted the recommendation in a public meeting before the error surfaced. The correction cost a news cycle and a measure of the principal's trust. The lesson entered the board's procurement vocabulary permanently: *the platform may describe; it may not prescribe.*

**The decision: five conditions written into board policy.** No composite school index, no rankings, no public-facing school scores generated by the tool. Automated recommendations disabled — every platform finding routes to the superintendent's office as a question requiring a human investigation and a written response. The equity audit runs quarterly, including an audit of the platform's own flags against demographics. Every board-funded initiative gets a pre-registered evidence plan in the platform — baseline, metric, review date — making the tool the district's memory for its own experiments. The board's standing rule, printed on the agenda template: *the dashboard generates the visit; it never replaces it.*

## What Would Change My Mind

The classification claims AI is adjacent here — that school effects are a context to read, not a mechanism to operate. Evidence that an analytics platform *causally* improved school-level outcomes through its recommendations alone — districts randomized to receive automated "levers" outperforming districts receiving only the instrument panel, on real assessments, at Kraft-credible magnitudes — would mean prescription-from-observational-data works better than this chapter believes, and the adjacency classification undersold the technology. A weaker but still chastening result: if composite school indices, for all their confounds, turned out to predict which schools respond to investment better than human-led investigations do, then the chapter's preference for visits over dashboards is sentiment, and boards should buy the ranking after all. Neither result exists. The deck on Vivian's desk implied both.

## Still Puzzling

Value-added methods are the field's serious attempt to isolate the practice strand, and after two decades the error bars are still wide enough to misclassify real schools in real years. If the best statisticians in education cannot cleanly extract strand three, what exactly is a commercial composite index claiming?

Concentration effects sit at the awkward joint of this chapter: structural, partly causal, and addressable only by the politically hardest moves a board can make — boundaries, assignment, staffing incentives. A platform that surfaced *those* trade-offs honestly — the levers that exist but hurt — would be the most valuable and least sellable product in the category.

The observer effect has no fix: any school measure a district governs by becomes a target. Whether AI-era measurement — cheaper, finer-grained, harder to game on any single metric — dampens that distortion or just distributes it is one of the next decade's open system questions.

## Further Reading

**Coleman, J. S., et al. (1966). *Equality of Educational Opportunity*. U.S. Government Printing Office.** The founding document: family background dominating measured school resources — the result every school-effects claim since has been refining, contesting, or rediscovering.

**Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49(4), 241–253.** The calibration this chapter's procurement scenes run on: what school-level improvement honestly looks like in well-measured field settings.

**Hattie, J. (2015). What doesn't work in education: The politics of distraction. Pearson.** Hattie's own argument that between-school policy fights distract from within-school variance — the source of the refrain this chapter leans on, from the author of the number on the vendor's deck.

**Raudenbush, S. W., & Willms, J. D. (1995). The estimation of school effects. *Journal of Educational and Behavioral Statistics*, 20(4), 307–335.** The technical anatomy: what "school effect" can even mean, and why the answer depends on who is asking — a parent choosing a school or a board judging one.

**O'Neil, C. (2016). *Weapons of Math Destruction*.** The label ledger's cautionary literature: what happens when opaque composite scores acquire institutional authority over schools, teachers, and neighborhoods.

---

## Exercises

**Warm-up**

1. *(Recall — What the number summarizes)* The chapter states that d = 0.48 for generalized school effects is "the ledger line where the other 251 rows are totaled by address." Explain what that means: what the number actually measures, why it is classified AI-ADJACENT rather than AI-AUGMENTED or AI-RESISTANT, and why calling it a "lever" is a category error.

2. *(Recall — Three strands)* Name the three strands of the between-school braid. For each, state whether it is a confound, a structural condition, or a school practice — and identify which one an analytics platform is most likely to present as "school quality" by default, and why.

3. *(Recall — The inertia test)* The chapter proposes an inertia test for analytics purchases: name one decision the board made differently because of the tool, and what it cost. Explain why a platform with a near-zero conversion rate on this test is "decoration, however accurate" — what the platform would have done even if no decision changed, and why that is not the same as having no value.

**Application**

4. *(Transfer — Strand audit)* A district analytics platform shows that Jefferson Elementary scores in the bottom quartile of the district's composite index, while Whitman Elementary scores in the top quartile. The gap is 0.6 composite-score units. A board member proposes directing improvement resources to Jefferson. Design a three-step strand audit: what data you would request to assess the composition strand, what data for the concentration strand, and what adjustment (if any) would be needed before the gap can be attributed to institutional practice. Identify what information the platform almost certainly cannot provide and what source you would need instead.

5. *(Transfer — Equity audit design)* The chapter argues the platform's highest use is disaggregation rather than ranking, including an audit of its own labeling. Design a quarterly equity audit for a district running a school-analytics platform: what the audit examines (which flags, labels, or risk tiers), what demographic variables it checks those against, what a failing result looks like, and what the board does when a failing result appears.

6. *(Transfer — Contract exclusion)* Vivian's memo made the composite index and color-coded league table a contract exclusion, not a setting. Draft that contract clause in procurement language specific enough that a vendor's technical team could implement it without further clarification. Then identify the most likely technical workaround — a feature the vendor might offer that achieves the same effect under a different name — and add a clause that closes it.

**Synthesis**

7. *(Combine — Instrument panel policy)* Design the complete board-level governance policy for a school-analytics platform, following the five conditions from the case study. For each condition, specify: the exact rule, how compliance is verified, who is responsible, and what the board does if the condition is violated. Your policy should be specific enough that a newly elected board member could use it to evaluate whether the district's current platform is being used correctly.

8. *(Combine — The visit protocol)* The board's standing rule is "the dashboard generates the visit; it never replaces it." Design a site-visit protocol triggered by a platform finding: what the finding must specify before a visit is authorized, who conducts the visit, what questions the visit is trying to answer that the platform cannot, what the visit produces, and how the finding-to-visit-to-decision chain is documented. Your protocol should make clear what the platform's role is and is not at each stage.

**Challenge**

9. *(Open — Prescription reversal)* The chapter claims that prescription from observational district data cannot causally improve school outcomes — that the "lever recommendations" the platform generates are necessarily generic and inert. Construct the strongest possible counterargument: conditions under which automated lever recommendations from an analytics platform could produce school-level improvements at Kraft-credible magnitudes. State the mechanism, the design features required, and the evidence that would confirm it. Then evaluate honestly: do the conditions you described correspond to any platform currently on the market, or only to a hypothetical one — and what is the board's correct posture in the gap between the hypothetical and what it is actually being sold?

## References

*Added by fact-check pass — all CONFIRMED via web verification (see factchecks/37-school-effects-as-system-context-assertions.md).*

1. Coleman, J. S., et al. (1966). *Equality of Educational Opportunity*. U.S. Government Printing Office.
2. Hattie, J. (2015). *What doesnt work in education: The politics of distraction*. Pearson.
3. Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49(4), 241–253.
4. Hattie, J. (2018 update). https://visible-learning.org/hattie-ranking-influences-effect-sizes-learning-achievement/

---

## Prompts

### Figure 37.1 — Where the variance lives: between vs. within schools
Build a single horizontal 100%-stacked proportional bar representing all achievement variance. Two segments: "Within schools" (~85%, highlighted as the dominant share) and "Between schools" (~15%). Label each segment with its approximate percentage and name. The bar should make the gross imbalance immediately legible — the within-school segment dwarfs the between-school segment. Add a short caption noting the share varies by system and method (higher between-school variance in heavily tracked systems). Use two distinct fills; emphasize the within-schools segment. The structural point: the lever the platform sells (between-school) is the small slice. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 37.2 — The three-strand braid inside the school-effects number
Build a layered-decomposition schematic showing the between-school composite index broken into three stacked horizontal strands of unequal thickness. Top to bottom by thickness: Composition (thickest) — note "confound, dominates raw rankings, maps to housing"; Concentration (medium) — note "structural, responds only to board-level policy"; Institutional practice (thinnest, highlighted) — note "smallest, hardest to isolate — the only 'quality' strand". Encode relative thickness to reflect each strand's share of the composite. Add a top annotation: "Raw composite index = all three braided, presented as strand three". Use distinct fills per strand; highlight institutional practice as the strand the board wants but the hardest to see. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

# Chapter 1 — Hattie's Visible Learning and the AI Question
*When a number on a slide is the most dangerous thing in the room.*

Slide 7 shows a single number in a font size usually reserved for stadium scoreboards: **d = 0.70**. Underneath: *"Feedback is one of the most powerful influences on student achievement — John Hattie, Visible Learning. Our platform delivers personalized AI feedback to every student, on every assignment, instantly."*

The board likes the slide. Two members have the bar-graph poster of Hattie's effect sizes hanging in their offices. The logic seems airtight — feedback has one of the largest effect sizes in education research, this product automates feedback, therefore the district should buy it. The superintendent's note to the curriculum director reads, in full: *"This checks out, right?"*

It does not check out. But the reasons it doesn't are not the ones people reach for first — not "AI bad," not "Hattie debunked," not "we can't afford it." The deck fails at a precise point: it treats an effect size as a property of a *product category* when it was a measurement of a *learning mechanism*. The 0.70 was synthesized from studies of feedback that changed what a teacher did next and what a learner understood about their own work — almost all of it predating large language models. Whether this platform touches that mechanism, replaces it, or quietly deletes it is exactly the question the slide is designed to keep anyone from asking.

Here is how to ask it.

---

## What the List Is

In 2009, John Hattie published *Visible Learning*, a synthesis of more than 800 meta-analyses covering roughly 50,000 individual studies of what influences student achievement. A meta-analysis combines many studies of one intervention into a single summary effect; Hattie's project was a meta-*meta*-analysis — combining the combinations — and it produced something education had never had before: one ranked list, from the most powerful influences on achievement down to the actively harmful ones, all expressed in a common unit.

The list has grown by accretion ever since — 138 influences in 2009, 252 by 2018, 357 across eleven domains in *Visible Learning: The Sequel* (2023). The numbers attached to individual influences drift between editions as new meta-analyses are averaged in. That drift matters and we will come back to it.

**This book works from the 2018 list of 252 influences.** Every effect size quoted here, every rank, every group chapter is anchored to that snapshot — not because the 2023 edition is wrong, but because the argument of this book does not live in the decimals. It lives in the mechanisms. Mechanisms are far more durable than meta-analytic averages, and holding one edition still gives the second layer of analysis — the AI classification — a stable object to classify.

One more thing about what the list *is*, because the misreading starts right here. The 252 entries are not 252 things you can buy. The list mixes interventions (worked examples, phonics instruction), practices (feedback, questioning), psychological conditions (self-efficacy, boredom), background factors (socioeconomic status, relative age within a class), structural variables (school size, tracking), and harms (corporal punishment, retention). "Deafness" appears on the list at d = −0.61. Nobody is proposing an intervention called deafness; the entry describes an association between a condition and measured achievement. A reader who treats the list as a menu has already made the category error that this entire book exists to prevent — and that AI vendors, as we will see, are commercially motivated to encourage.

| Influence | Effect-size band (MEASURED) | AI feasibility | Human irreducibility | Substitution risk | Mechanism conflict | Vendor activity | Hypothetical AI effect (HYPOTHESIZED) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Collective teacher efficacy (d = 1.57) | High | AI-RESISTANT | Very high | Low | Present | Low | — (cannot be purchased as software) |
| Feedback (d = 0.70) | High | AI-AUGMENTED | Moderate | Moderate | Partial | High | d ≈ 0.50 [HYPOTHESIS]: fast task-level feedback legitimate; relational/self-regulation feedback must stay human |
| Worked examples | Above hinge | AI-NATIVE | Low | High | Present | High | [HYPOTHESIS]: generation safe; must fade to avoid expertise reversal |
| Classroom management | Above hinge | AI-RESISTANT | High | Low | Present | Low | — (presence and authority not delegable) |
| Self-efficacy | Above hinge | AI-RESISTANT | High | High | Present | Moderate | [HYPOTHESIS]: track mastery evidence; never supply borrowed confidence |
| Summarization (text) | Above hinge | AI-NATIVE | Low | High | Present | High | [HYPOTHESIS]: high substitution — student never compresses |
| Spaced practice | Above hinge | AI-AUGMENTED | Low | Moderate | Absent | Moderate | [HYPOTHESIS]: AI runs logistics; learner keeps the retrieval moment |
| Socioeconomic status (d ≈ 0.52) | Above hinge | AI-ADJACENT | n/a (condition) | n/a | n/a | Low | — (signal readable, lever unpullable) |
| Relative age within class | Below hinge | AI-ADJACENT | n/a (condition) | n/a | n/a | Low | — (background factor, not intervention) |
| School size | Below hinge | AI-ADJACENT | n/a (structural) | n/a | n/a | Low | — (structural variable) |
| Retention (holding back) | Harmful (< 0) | AI-ADJACENT | n/a (policy) | n/a | n/a | Low | — (harm, not intervention) |
| Deafness (d = −0.61) | Harmful (< 0) | AI-ADJACENT | n/a (condition) | n/a | n/a | Low | — (association, not a lever) |
| … (representative selection from the 252-influence list; full classification applied row by row across all 252 entries) | | | | | | | |

---

## How to Read an Effect Size Without Being Misled

Cohen's *d* expresses a difference between groups, or growth over time, in standard-deviation units. If a class scores half a standard deviation higher after an intervention than a comparison group, that's d = 0.50. The unit's virtue is that it lets you put a reading intervention and a math intervention on the same scale. Its vice is that it tempts you to believe the scale means the same thing everywhere. It does not.

Jacob Cohen, who invented the convention, proposed rough benchmarks in the 1980s: 0.2 is small, 0.5 medium, 0.8 large. Hattie's hinge sits inside that frame. Since the average effect across his 2009 corpus was about 0.40, he argued, almost everything "works" relative to doing nothing — so the interesting question is what works *best*, and 0.40 marks the boundary between above-average and below-average impact. He loosely equated 0.40 with about a year's typical growth.

Now consider what Matthew Kraft published in 2020, in a paper practitioners should attach to every vendor deck they receive. Examining effect sizes from well-designed field experiments — randomized trials, real schools, standardized achievement outcomes — Kraft found the realistic distribution sits far lower: on that evidence, less than 0.05 is small, 0.05 to 0.20 is medium, and 0.20 or above is large. A d of 0.20 from a year-long randomized trial on a state assessment is a genuinely big deal. The same 0.20 inside Hattie's synthesis looks like a failure.

These are two different rulers, built from two different bodies of evidence. Hattie's corpus is dominated by the studies researchers actually publish: often small, brief, with researcher-designed tests administered close to the intervention — all conditions known to inflate effects. Kraft's benchmarks come from the harder world of large samples, long durations, and distal measures. Neither ruler is wrong. What's wrong is laying one against the other's measurements.

![Same d=0.40 marker on Hattie's inflated synthesis distribution versus Kraft's realistic field-experiment distribution](images/01-hatties-visible-learning-and-the-ai-question-fig-02.png)
*Figure 1.2 — Two rulers for the same effect size*

<!-- → [CHART: Two-panel comparison — left panel shows distribution of effect sizes in Hattie's synthesis with benchmarks labeled (0.2 small, 0.4 hinge, 0.8 large); right panel shows Kraft's realistic field-experiment distribution with benchmarks shifted left (0.05 small, 0.20 large). Same d = 0.40 marked on both panels to show how the same number reads as "impressive" vs. "exceptional" depending on which ruler is in hand] -->

A concrete version of the trap: two interventions both report d = 0.40 — one from ten one-week lab studies with researcher-built tests, the other from three year-long district randomized trials on state assessments. The numbers are identical; the second is worth incomparably more. An effect size does not carry its own pedigree. You have to ask.

Used properly, d = 0.40 is a triage signal. With 252 influences and finite institutional attention, you need a way to decide where to look first, and "above or below the average of everything studied" is a defensible first cut. That is the entire job this book asks the hinge to do: prioritize the reading order.

The abuses come in a matched pair.

First abuse: the hinge as verdict. "Below 0.40 means it doesn't work." By construction, something close to half of everything education does falls below the hinge. If below-the-hinge meant meaningless, then half of schooling — including, as Chapter 2 shows, worked examples, classroom management, and most educational technology as actually measured — would be meaningless by definition. That is not an empirical finding; it is an artifact of where the average happens to sit.

Second abuse: the hinge as shopping list. "Above 0.40 means buy a tool for it." But effect sizes attach to influences *as studied* — usually human-delivered, in particular conditions, on particular learners. A product claiming an influence's effect size is claiming credit for studies it was not part of. The hinge also says nothing about cost, scalability, equity, or implementation — the four things adoption decisions actually turn on.

Hold this rule for the rest of the book: **an effect size is a prioritization signal, never a verdict.** It tells you where to direct scarce attention. It cannot tell you what to buy, what to cut, or what will happen in your building.

---

## The Critiques, Carried Honestly

If this book is going to use Hattie's list for thirty-eight more chapters, it owes you the strongest case against doing so — stated before the using, not footnoted after.

Bergeron (2017) published, in the *McGill Journal of Education*, a paper whose title does not hedge: "How to Engage in Pseudoscience with Real Data." His argument: Cohen's *d* cannot serve as a universal impact ruler across studies with different populations, different measures, and different designs, and averaging such d's into rankings borrows the *form* of science without satisfying its assumptions. The charge stings because the statistical core of it is right — which is exactly why this book quarantines every effect size behind the two-rulers lesson above.

There were also computational errors. Alongside Cohen's *d*, the 2009 book reported a second statistic, the Common Language Effect size — and many of those values were mathematically impossible: negative probabilities, probabilities above 100 percent. Hattie had used z-values directly where probabilities belonged. Readers flagged it around 2011; Hattie acknowledged the error, and reprints were corrected. Two things are simultaneously true. First: the CLE errors do not contaminate the *d*-based rankings — the rankings never rested on that statistic. The speedometer was broken; the odometer was fine. Second: a synthesis offered as the foundation for evidence-based practice shipped with basic statistical errors that no reviewer caught. Not zero deference owed to the enterprise after that. Not full deference either. Adult deference.

Simpson (2017) supplied the mechanism behind Bergeron's charge: an effect size is a ratio, and researchers can enlarge it without making an intervention any better — shrink the denominator by studying restricted samples, sharpen the numerator with proximal researcher-built measures. League tables of effect sizes may really be hierarchies of *openness to research-design manipulation*. Slavin (2018) made the practitioner version of the same point bluntly: the meta-meta-analysis accepts its underlying meta-analyses uncritically, and those are dominated by small, brief, artificial studies that inflate effects.

And there is a critique internal to the averaging itself — the one this book leans on hardest. A single number per influence averages over moderators that can reverse the effect. Hattie's own feedback synthesis acknowledges that roughly one-third of feedback effects in the underlying literature are *negative*. The d = 0.70 on the vendor's slide is the mean of a distribution that includes a fat tail of feedback that made things worse. Practitioners do not live in the mean; they live in the distribution.

So why use the list at all?

Here is the book's stance, stated once and relied on everywhere: **the list is unusable as a measurement instrument and usable as a map.** It is the most comprehensive record in existence of which mechanisms educators have cared enough about to study, with a rough — design-confounded, moderator-averaged, but not random — signal of where the strong mechanisms cluster. Used as a prioritization map, it tells you where to dig. Used as a shopping list, it tells you lies.

Run the stress test on the list's own number one: collective teacher efficacy, d = 1.57. The figure is correlational, definitionally fuzzy, and almost certainly inflated — fair on all counts. Now halve it. Halve it again. The decision-relevant content — *shared professional trust among teachers is strongly associated with achievement, and it cannot be purchased as software* — survives untouched. That content lives in the mechanism, not the decimal. Every chapter in this book is built to pass that test. If a chapter's guidance would change because an effect size fell from 0.79 to 0.40, the chapter is built wrong.

---

## The Man on the Slide Co-Wrote the Caution

There is one fact that reframes the entire vendor deck, and it fits in a sentence: **the researcher being quoted co-authored a paper about minimizing AI's damage to education.**

In 2023, Arran Hamilton, Dylan Wiliam, and John Hattie released a working paper titled "The Future of AI in Education: 13 Things We Can Do to Minimize the Damage." The title is not ironic. The paper argues that without deliberate intervention, AI could diminish human agency and stifle the development of the very capabilities schooling exists to build. Whatever one's view of every recommendation, the rhetorical situation is unambiguous: vendors quote Hattie's effect sizes as a license for AI products, while Hattie's own published position on AI is co-authored caution.

His longer record points the same direction. Across decades of syntheses, technology's measured effect on achievement has hovered stubbornly around 0.3 — below his own hinge — through film strips, computers, laptops, and the internet. The technology findings he does endorse concentrate where this book keeps landing: technology helps when it amplifies feedback, supports focus, and consolidates prior learning — not when it delivers first-exposure instruction or replaces teacher judgment.

None of this makes Hattie an authority on large language models, and this book will not quote him as one. The point is narrower: the gap between the research and the sales deck is visible *within the work of the single most-quoted researcher in the genre*. If the man on the slide doesn't endorse the syllogism on the slide, the syllogism needs a better defense than his name.

---

## The Seven Dimensions: This Book's Own Layer — Read the Label

Hattie's list answers one question: what is associated with achievement? It cannot answer the question a curriculum director actually faces: *what should AI be allowed to do here?* To get from the first question to the second, this book adds a classification layer — and before describing it, an act of labeling that the entire book's credibility depends on.

**The seven-dimension framework is the author's analytical synthesis. It is not published research. It is not Hattie. It is a structured set of judgments, applied row by row to all 252 influences, and every one of those judgments is open to challenge.** When this book says "summarization is classified AI-NATIVE with conflict present," the verb is *classified* — by the author, on stated reasoning — not *found*, *shown*, or *proven*. The framework's value is that it makes the judgments explicit, consistent, and arguable, which is more than can be said for the implicit judgments embedded in every procurement decision that never names its assumptions.

The seven dimensions, for each influence:

**1. Effect-size band** — High (d ≥ 0.70), Above hinge (0.40–0.69), Below hinge (0.15–0.39), Negligible (0.01–0.14), Harmful (< 0). Hattie's number, banded; the only dimension inherited from the source.

**2. AI feasibility** — the load-bearing taxonomy. *AI-NATIVE*: current AI can perform the core task itself (generate worked examples, summarize a text, produce practice items). *AI-AUGMENTED*: AI can strengthen the influence — planning, drafting, diagnosis, feedback at scale — while humans retain the decisive cognitive or relational work. *AI-ADJACENT*: the influence is mostly context or condition (socioeconomic status, school size, prior achievement); AI can read the signal but cannot pull the lever. *AI-RESISTANT*: the active ingredient is relationship, presence, trust, or collective agency; AI can support the perimeter but must not touch the mechanism.

**3. Human irreducibility** — how much of the mechanism consists of things machines cannot reliably supply: relationship, judgment, social presence, embodiment, metacognition, accountability.

**4. Substitution risk** — the probability that AI use *replaces* the learning-producing act while improving the visible artifact.

**5. Mechanism conflict** — whether the way AI tools naturally operate contradicts the reason the influence works. AI summarizes → the student never compresses. AI answers → the student never retrieves.

**6. Vendor activity** — how aggressively the influence is currently being productized. A risk signal, not a quality signal.

**7. Hypothetical AI effect** — and here, stop.

### The [HYPOTHESIS] Column

The seventh column attaches a number to a guess: *if* AI were deployed on this influence under stated conditions, what effect might plausibly result? Every populated cell in that column carries the tag **[HYPOTHESIS]**. For the feedback row it reads: "d ≈ 0.50 [HYPOTHESIS]: AI fast task-level feedback is legitimate; relational and self-regulation feedback must be human."

Learn to read that label now, because the failure mode is predictable. Those numbers look exactly like the real effect sizes sitting six columns to their left. They are not the same kind of object. The d = 0.70 is a (flawed, averaged, but real) summary of measured studies. The d ≈ 0.50 [HYPOTHESIS] is a calibrated conjecture — a way of stating, with falsifiable precision, what the mechanism analysis predicts. It exists to be tested by your pilots, not quoted in your slide decks.

The evidence-language discipline holds throughout this book: measured results are *associated with*; classifications are *classified as*; the seventh column is *hypothesized*. Nothing in that column is ever a finding.

![One framework row carrying seven columns of three epistemic kinds — measured, classified, and quarantined hypothesized](images/01-hatties-visible-learning-and-the-ai-question-fig-04.png)
*Figure 1.4 — Anatomy of one framework row*

<!-- → [INFOGRAPHIC: Visual anatomy of one row in the seven-dimension framework — the feedback row — showing all seven columns labeled with their type (MEASURED vs. CLASSIFIED vs. HYPOTHESIZED), with the [HYPOTHESIS] column visually distinguished by color or border to make the epistemological distinction unmissable] -->

### What the Classification Reveals

Run the layer across all 252 influences and a structure appears that no tool-by-tool debate ever surfaces. AI-ADJACENT is the largest class — 97 influences, 38.5% — a plurality of Hattie's list consists of context and conditions no tool can buy you out of. AI-AUGMENTED covers 88 (34.9%), AI-RESISTANT 38 (15.1%), and AI-NATIVE — the zone where AI can actually perform the task — just 29 influences, 11.5%.

Restrict to the 122 influences at or above the hinge: 81 are AI-AUGMENTED, 18 AI-RESISTANT, 14 AI-NATIVE, 9 AI-ADJACENT. In the High band (d ≥ 0.70, 32 influences), 24 are AI-AUGMENTED and only 4 are AI-NATIVE.

![All 252 influences versus the above-hinge subset distributed across four AI-feasibility classes, the high-impact zone dominated by augmented not native](images/01-hatties-visible-learning-and-the-ai-question-fig-03.png)
*Figure 1.3 — Four AI-feasibility classes across the list*

<!-- → [CHART: Stacked bar or treemap showing the 252 influences distributed across the four AI-feasibility classes (AI-NATIVE, AI-AUGMENTED, AI-ADJACENT, AI-RESISTANT), with a second view filtered to the above-hinge subset (122 influences) — the visual should make immediately legible that the high-impact zone is dominated by AUGMENTED, not NATIVE] -->

Read that distribution slowly, because it is the structural finding of the whole book: **the high-impact end of Hattie's list is augmentation territory, not replacement territory.** The things most strongly associated with achievement are overwhelmingly things AI can *support* — and only rarely things AI can *do*. Whatever the right AI strategy for a school is, the data's shape says it cannot mainly be a substitution strategy.

---

## Substitution Risk, Mechanism Conflict, and the Phase Gate

Two of the seven dimensions do most of the protective work.

**Substitution risk** is the risk that AI improves the visible artifact while deleting the invisible learning event. The essay gets better; the writer doesn't. The summary is accurate; nobody compressed anything. The homework is correct; nothing consolidated. Substitution is dangerous precisely because every observable signal improves while the one thing that matters — change in the learner — quietly stops happening.

**Mechanism conflict** is the structural version: the way the tool works contradicts the reason the influence works. Summarization works *because* the learner selects and compresses; a tool that selects and compresses on the learner's behalf is not supporting the influence, it is impersonating it.

The empirical anchor for both concepts — the study this book will return to more than any other — is Bastani and colleagues' randomized field experiment, published in *PNAS* in 2025. Nearly a thousand high-school students practiced math under three conditions. Students with unrestricted GPT-4 access performed 48 percent better during practice — and then 17 percentage points worse on the subsequent unassisted exam than students who had practiced with no AI at all. The help helped until the help left.

But the third arm is the one that matters for policy: students using a guardrailed tutor — built on the same model, but designed to give hints and feedback without surrendering answers — practiced 127 percent better with approximately zero harm on the exam. Same technology. Opposite outcomes. The difference was nothing but design: a specification of what the AI would and would not do.

That specification has a name in this book: the **phase gate**. Three blanks, filled in before adoption, in writing:

> **AI may do X. The teacher and learner must do Y. Evidence that learning improved is Z.**

X enumerates the safe support roles. Y names the cognitive and relational work that constitutes the mechanism — the work that may never cross to the machine. And Z is the discipline most adoptions skip: evidence of *learning*, defined in advance, and defined correctly. In-tool analytics — usage minutes, completion rates, scores on assisted work — are measures of the artifact and the activity. The Bastani students' practice metrics were spectacular. Z must be delayed, unassisted, ideally transfer-bearing performance: what the learner can do later, alone, on something new.

![Identical AI technology producing opposite outcomes: practice gain versus unassisted-exam change across three experimental arms](images/01-hatties-visible-learning-and-the-ai-question-fig-01.png)
*Figure 1.1 — Bastani three-arm outcome*

<!-- → [DIAGRAM: Three-arm comparison diagram from the Bastani study — left arm (unrestricted GPT-4): practice +48%, exam −17pp; middle arm (no AI): baseline; right arm (guardrailed tutor): practice +127%, exam ≈ 0 harm — the visual should make the third arm's design lesson the focal point, not just the first arm's cautionary tale] -->

Surrounding evidence triangulates the design point. VanLehn's (2011) review found step-based intelligent tutoring systems reaching effects around 0.76 — comparable to human tutors. Wang and colleagues' Tutor CoPilot trial (2024) put AI assistance *inside* the human loop — coaching 900 live tutors in real time — and moved student mastery by 4 percentage points overall and 9 for novice tutors. AI amplifying the human mechanism rather than replacing it. The pattern across all of it: **outcomes track the division of labor, not the sophistication of the model.**

One cautionary tale to close the loop. A school piloting an AI writing-feedback tool declared the pilot a success on four measures: usage minutes, drafts produced, rubric scores of final essays, teacher satisfaction. Every one is an artifact or activity metric. When week ten brought an unassisted, on-demand writing task, performance was flat against baseline. Nobody had defined Z in advance, so the tool had spent a semester being evaluated on evidence it generated about itself. The pilot didn't fail — the *audit* failed. The phase gate exists so that "did anyone learn anything?" is locked in writing before the first license is purchased.

---

## What Would Change My Mind

This chapter rests on claims that evidence could overturn, and honesty requires naming them. If well-designed classroom trials accumulated showing that *unguardrailed* AI assistance produces durable gains on delayed, unassisted, transfer-bearing measures across contexts — the direct negation of the Bastani pattern — this book's substitution-risk architecture would be overbuilt, and its central caution wrong in the most consequential way. If the early generative-AI outcome literature matures and its effects hold up large and general under skeptical reads (current meta-analytic estimates run from strikingly large to modest once study quality is weighted — the literature is young, heterogeneous, and vendor-adjacent), the augmentation-only reading of the high band would need loosening. And if the author's classifications fail in the field — if influences tagged AI-RESISTANT keep yielding to well-designed tools without mechanism loss — then the seven dimensions are miscalibrated and should be revised row by row, in public.

## Still Puzzling

- **Where exactly does augmentation tip into substitution?** The book draws the line at "who performs the cognitive act," but real tools sit on gradients — a hint is a partial answer; a draft comment is partial composition. The Bastani guardrail result shows the line exists; no one has mapped its position across task types.
- **Can the hypothetical column be tested at scale?** The [HYPOTHESIS] estimates are falsifiable in principle. A consortium of districts running gated pilots with pre-registered Z measures could start confirming or demolishing them within a few years. Nothing like that infrastructure currently exists.
- **What does the hinge mean after AI?** Every effect size in the 252 list was synthesized in a pre-LLM world. If AI changes the cost structure of entire influence categories, the rankings' practical meaning shifts even where the numbers stand still.

## Further Reading

- **Hattie, J. (2009). *Visible Learning: A Synthesis of Over 800 Meta-Analyses Relating to Achievement*. Routledge.** The source of the list, the hinge, and the controversy. Read the first three chapters for the logic; read the critics alongside.
- **Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49(4), 241–253.** The second ruler. The single most practical statistics paper a school leader can read; it will permanently change how vendor decks look to you.
- **Bergeron, P.-J. (2017). How to engage in pseudoscience with real data: A criticism of John Hattie's arguments in Visible Learning from the perspective of a statistician. *McGill Journal of Education*, 52(1), 237–246. Translated by L. Rivard.** The strongest statistical case against the synthesis.
- **Simpson, A. (2017). The misdirection of public policy: Comparing and combining standardised effect sizes. *Journal of Education Policy*, 32(4), 450–466.** Why effect sizes are manipulable ratios, and why league tables of them may rank research designs rather than interventions.
- **Hamilton, A., Wiliam, D., & Hattie, J. (2023). The future of AI in education: 13 things we can do to minimize the damage. Working paper.** Co-authored caution from the most-quoted name in the genre.
- **Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*.** The book's central cautionary experiment: +48% with help, −17 points without it — and the guardrailed arm that shows design decides the outcome.
- **Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81–112.** What the 0.70 on the vendor slide was actually a measurement of.

---

## Exercises

### Warm-up

**1.** A vendor deck quotes d = 0.65 for its platform, citing a Hattie meta-analysis. Name two questions you must ask before treating that number as evidence for the platform's effectiveness. *(Difficulty: low. Tests: understanding of what an effect size does and does not carry.)*

**2.** Using Kraft's (2020) benchmarks rather than Hattie's, classify each of the following as small, medium, or large: d = 0.08, d = 0.19, d = 0.41. Then classify the same three values using Hattie's hinge. What does the disagreement between the two classifications reveal? *(Difficulty: low. Tests: the two-rulers concept.)*

**3.** "Deafness" appears on Hattie's list at d = −0.61. A district administrator proposes eliminating programs whose effect sizes fall below zero, citing Hattie. What category error is the administrator making, and how would you correct it in a single sentence? *(Difficulty: low. Tests: understanding what kinds of entries appear on the list.)*

### Application

**4.** A pilot program reports these four success metrics: usage minutes up 40%, assignment completion rate up 28%, rubric scores on AI-assisted work up 0.6 points, teacher satisfaction at 4.2/5. Write the phase gate this pilot should have defined before launch — specifically, what Z (evidence of learning) would have looked like, and why none of these four metrics qualifies. *(Difficulty: medium. Tests: the phase gate and the distinction between artifact metrics and learning evidence.)*

**5.** Take an influence from the 252-item list that a colleague has cited as justification for an AI purchase (choose one you know or look one up). Run it through the four protocol questions from this chapter: What is the influence and what makes it work? What may AI do here? What must humans keep? What is the evidence Z? *(Difficulty: medium. Tests: applying the full protocol to a real influence.)*

**6.** The book classifies 29 influences as AI-NATIVE and 88 as AI-AUGMENTED. Explain, in your own words, why a district whose AI strategy is primarily AI-NATIVE is structurally misaligned with the distribution of high-impact influences — and what an AI-AUGMENTED strategy would look like instead. *(Difficulty: medium. Tests: reading the classification distribution as a strategic signal.)*

### Synthesis

**7.** Bergeron's statistical critique is correct. Hattie's [HYPOTHESIS] column is the author's conjecture, not peer-reviewed findings. Yet this book uses both. Write a 200-word defense of that choice that does not dismiss either critique — and that would satisfy a methodologically trained skeptic. *(Difficulty: high. Tests: holding the epistemological distinctions together under pressure.)*

**8.** The Bastani study shows a guardrailed AI tutor producing large practice gains with no exam harm, while an unguardrailed version produced large practice gains and significant exam harm. A colleague argues: "So we just need guardrails — then AI is safe." What does this chapter add to that claim that the colleague is missing? *(Difficulty: high. Tests: mechanism conflict, substitution risk, and the specificity of what guardrails must protect.)*

### Challenge

**9.** Design a one-semester pilot for an AI writing-feedback tool that a methodologically trained evaluator would accept as credible. Specify: the influence being targeted, its mechanism, the phase gate (X, Y, Z), the evidence measure for Z, and a plan for what you would do if Z shows flat or negative results at week ten. Your design must make the same mistake the cautionary tale in this chapter makes *impossible* — explain why. *(Difficulty: challenge. Tests: integrating every concept in the chapter into a practical institutional decision.)*

---

## References

<!-- Added by fact-check pass 2026-06-08. See factchecks/01-hatties-visible-learning-and-the-ai-question-assertions.md -->

1. Hattie, J. (2009). *Visible Learning: A Synthesis of Over 800 Meta-Analyses Relating to Achievement*. Routledge. https://www.routledge.com/p/book/9780415476188
2. Hattie, J. (2023). *Visible Learning: The Sequel*. Routledge. https://www.routledge.com/p/book/9781032462035
3. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences*. Routledge.
4. Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49(4), 241–253. https://journals.sagepub.com/doi/10.3102/0013189X20912798
5. Bergeron, P.-J. (2017). How to engage in pseudoscience with real data. *McGill Journal of Education*, 52(1), 237–246. (L. Rivard, trans.) https://mje.mcgill.ca/article/view/9475
6. Hamilton, A., Wiliam, D., & Hattie, J. (2023). *The Future of AI in Education: 13 Things We Can Do to Minimize the Damage*. Working paper (EdArXiv). https://osf.io/preprints/edarxiv/372vr/
7. Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122. https://www.pnas.org/doi/10.1073/pnas.2422633122
8. VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46(4), 197–221. https://doi.org/10.1080/00461520.2011.611369
9. Wang, R. E., et al. (2024). Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise. arXiv:2410.03017. https://arxiv.org/abs/2410.03017
10. Visible Learning. Hattie Ranking: 252 Influences and Effect Sizes. https://visible-learning.org/hattie-ranking-influences-effect-sizes-learning-achievement/

---

## Prompts

### Figure 1.1 — Bastani three-arm outcome
Build a vertical bar chart of signed performance change across the three-arm Bastani math experiment. Five bars in one category axis: "Unrestricted GPT-4: practice" (+48), "Unrestricted GPT-4: exam" (−17), "No-AI control" (0), "Guardrailed tutor: practice" (+127, highlighted), "Guardrailed tutor: exam" (0). y-axis = signed performance change, zero baseline yes, with a visible reference line at 0 since bars cross it. Channels: x = arm/measure label, y = value, color = encode the guardrailed-practice highlight bar distinctly and use sign (positive vs. negative) to separate gain from harm. Do not sort; preserve the arm grouping so practice/exam pairs read together. Annotate the −17 exam bar ("the help left") and the +127 highlighted bar ("design, not model"). Title the design lesson, not the cautionary tale. Deliverable: single standalone HTML file, inline CSS, D3 v7 from the pinned CDN, Okabe-Ito-free brutalist palette via CSS variables.

### Figure 1.2 — Two rulers for the same effect size
Build a two-panel comparison. Left panel = Hattie synthesis distribution with benchmark markers at 0.20 (small), 0.40 (hinge), 0.80 (large); right panel = Kraft field-experiment distribution with markers at 0.05 (small), 0.20 (large). Each panel shows a single distribution curve/strip along a shared x-axis (Cohen's d). Place one fixed d=0.40 reference marker on BOTH panels: mid-pack on the left, far in the high tail on the right (highlight). Channels: x = effect size, panel = which ruler, color = the fixed-d marker vs. benchmark lines. Annotate that the same number reads "impressive" vs. "exceptional" depending on the ruler. zero baseline not applicable (it is a distribution, not bars). Deliverable: single standalone HTML file, inline CSS, D3 v7 from the pinned CDN, Okabe-Ito-free brutalist palette via CSS variables.

### Figure 1.3 — Four AI-feasibility classes across the list
Build a two-panel comparison of stacked counts across four AI-feasibility classes. Left panel "All 252 influences": AI-ADJACENT 97, AI-AUGMENTED 88, AI-RESISTANT 38, AI-NATIVE 29. Right panel "Above-hinge subset (122)": AI-AUGMENTED 81 (highlight), AI-RESISTANT 18, AI-NATIVE 14, AI-ADJACENT 9. Marks: stacked or grouped bars per panel; counts range 9–97. Channels: y = count, color = AI-feasibility class (consistent across panels), panel = scope. Sort each panel descending by count. zero baseline yes. Annotate that the high-impact end is dominated by AUGMENTED, not NATIVE. Deliverable: single standalone HTML file, inline CSS, D3 v7 from the pinned CDN, Okabe-Ito-free brutalist palette via CSS variables.

### Figure 1.4 — Anatomy of one framework row
Build an annotated callout figure of a single framework row (the feedback row) with seven labeled cells. Center label "One framework row"; seven callouts tagged by epistemic kind: "Effect-size band (MEASURED)", "AI feasibility (CLASSIFIED)", "Human irreducibility (CLASSIFIED)", "Substitution risk (CLASSIFIED)", "Mechanism conflict (CLASSIFIED)", "Vendor activity (CLASSIFIED)", "Hypothetical AI effect (HYPOTHESIZED, quarantined)". Channels: color = the three epistemic kinds (measured / classified / hypothesized), with the hypothesized cell visually unmistakable from the measured cell via distinct border or fill. Layout: one horizontal row of seven cells with leader lines to callout labels. No axes, no zero baseline. Annotate the quarantine boundary around the hypothesized cell. Deliverable: single standalone HTML file, inline CSS, D3 v7 from the pinned CDN, Okabe-Ito-free brutalist palette via CSS variables.

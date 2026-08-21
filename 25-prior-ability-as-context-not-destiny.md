# Chapter 25 — Prior Ability as Context, Not Destiny
*The strangest entry in the High band: a number with no lever attached, and an institution ready to mistake it for one.*

A single influence: prior ability, d = 0.94. Like the context-signals group, this is a fact about learners, not a lever — one of the strongest predictors of achievement in Hattie's synthesis, and not something any program installs. AI's relationship to it is adjacency: models can estimate it, track it, and adapt to it with unprecedented resolution. The chapter's work is keeping that resolution from hardening into destiny — prior ability as context that shapes the next instructional move, not as a classification that decides what a student is offered.

**Group Profile: Prior Ability as Context**

| Profile | Detail |
|---|---|
| Influences in this group | 1 of Hattie's 252 |
| Effect size | d = 0.94 |
| Hattie band | High |
| AI feasibility | AI-adjacent |
| Human irreducibility | Low |
| Substitution risk | Low |
| Cognitive-work conflict | None |
| Influence | Prior ability (rank 9, d = 0.94) |

Every spring, Marisol Vega's placement committee makes hundreds of consequential calls — who goes into Algebra II versus the support section, who gets recommended for AP, which incoming ninth graders land in the "foundations" English block. This year the district's new scheduling platform offers to help. It ingests middle-school records, screener results, and attendance, and produces a "readiness index" for each student, with placement recommendations attached. The sales engineer is careful to say the index "doesn't decide anything — it just informs."

An English teacher on the committee raises her hand: "When the index says a kid isn't ready, who un-says it? And when do we ever check whether the kids it routed into foundations would have been fine in the regular section?"

Marisol has until the April board meeting to recommend how the readiness index may and may not be used. The committee is staring at the strangest entry in the High band — an influence with one of the largest numbers in the dataset and no lever attached.

## What Kind of Thing This Is

Prior ability (d = 0.94) sits at rank 9 on the 2018 252-influence list. The number quantifies the association between what students arrive with and what they later achieve. It is the reason every serious education study *controls for* prior ability or achievement rather than randomizing it — nobody can assign a student a different past. In a well-run trial, prior achievement is the baseline covariate researchers subtract so the treatment effect becomes visible. In Hattie's list, it appears alongside genuine interventions as if it were one of them — a mixing of categories.

Two neighboring rows sharpen the picture. The same list carries **prior achievement at rank 61 (d = 0.55)** — overlapping construct, different number, a useful reminder that effect sizes are sensitive to how a construct is defined and which studies are pooled. And one rank below prior ability sits **"strategy to integrate with prior knowledge" (rank 10, d = 0.93)** — nearly the same number, opposite classification: AI-AUGMENTED, because it describes something teaching *does*. That adjacent pair is the sharpest contrast in the dataset: *who the student is* versus *what teaching does with what the student knows*. The closer a construct sits to what was taught, the more it is a lever. The closer it sits to who the student is, the more it is context.

![Horizontal bar chart against the 0.40 hinge: prior ability (0.94, context/destiny-risk) one rank above strategy to integrate with prior knowledge (0.93, a teachable lever), with prior achievement (0.55) showing how construct definition moves the number](images/25-prior-ability-as-context-not-destiny-fig-03.png)
*Figure 25.3 — Same number, opposite classification*

The classification for this group follows from that. AI-ADJACENT means AI works *next to* this influence, not *on* it. There is nothing here for a tool to deliver, because the influence is not a practice or a program — it is a description of what students bring through the door. Low substitution risk: there is no learning mechanism inside this influence for AI to hollow out, because there is no mechanism. Only information.

That sounds like the safest possible classification. It is not. The risk here is not that AI will replace a learning process. It is that an institution will mistake a description for a verdict and let software turn yesterday's record into next year's ceiling. This is an ethics chapter wearing a statistics costume.

## Why the Prediction Is Strong — and What That Means

Prior measures bundle together everything that has already happened to a learner: accumulated knowledge, practiced skills, home opportunity, prior schooling quality, test-taking familiarity. That bundle carries forward. New learning builds on old learning — the most secure finding in cognitive science. This is why the prediction is strong.

But notice what the bundle means for interpretation. Prior ability is partly accumulated *opportunity* wearing the costume of capacity. A student measured after six years in an under-resourced school carries that history in her score. Treat the score as a fixed trait and you convert a history of opportunity into a forecast of limitation. Treat it as a starting-point description and it becomes the most useful planning information a teacher can have. Same number, opposite institutions.

The misconception to kill on sight: "d = 0.94 means ability determines outcomes, so teaching matters little." The number is an average association, not a ceiling. The entire above-hinge list documents instruction-side variation that operates within every level of prior ability. Prior ability is the ground the class stands on. Everything else in the dataset is what teaching can build.

And here is the distinction with ethical teeth, because it matters for every adaptive platform ever sold: *diagnosing prior knowledge* ("what does this student already know about fractions?") and *measuring prior ability* ("what is this student's ability level?") can run on identical data. The first produces an instructional plan with a short shelf life. The second produces a label with a long institutional one.

![Two-column contrast fork from the same assessment data — diagnosing prior knowledge yields a short-shelf-life instructional plan (act, re-diagnose, revise) while measuring prior ability yields a long-shelf-life placement label (route, schedule, confirm)](images/25-prior-ability-as-context-not-destiny-fig-02.png)
*Figure 25.2 — Same data, two uses: diagnosis vs. measurement*

<!-- → [DIAGRAM: Two-column contrast on the same underlying data — left column: "Diagnosing prior knowledge" (shelf life: 3 weeks; output: instructional plan; institution's response: act, re-diagnose, revise); right column: "Measuring prior ability" (shelf life: indefinitely; output: placement label; institution's response: route, schedule, confirm); caption: the same assessment becomes either of these depending on what the institution does with it] -->

## What AI Can Safely Do

Because the classification finds no mechanism to protect, the safe-use list is substantial — this is the group where AI does real work without threatening what the influence is measuring.

**Build the starting-point map.** Synthesize patchy records into a per-class prerequisite picture: "most of this section lacks fraction–decimal equivalence; eight students show algebra readiness." Context-reading for human planning — the legitimate AI-ADJACENT role in its purest form.

**Flag prerequisite gaps before a unit**, so diagnosis happens by design rather than by mid-unit surprise.

**Suggest differentiated entry points** — provisional groupings, alternative on-ramps — that a teacher reviews and that expire on a schedule.

**Surface students whose trajectories contradict their averages.** A student with a weak sixth-grade score and a strong recent upward trend is a student the folder-skim misses. The platform catches her; the committee decides what to do.

**Serve as the honest moderator in evaluations.** When the school pilots any AI tool, disaggregate outcomes by prior-achievement tercile. The pattern matters: structured tutoring-style support has shown its largest documented gains where baseline capability was weakest — in the Tutor CoPilot study, +9 percentage points for students of lower-rated tutors versus +4 overall. Unstructured AI access has shown the opposite — in Bastani and colleagues' field experiment, unguardrailed GPT-4 inflated practice performance and then harmed unassisted exam performance. The same tool is a different intervention at different points of the prior-ability distribution. That is what "context" means operationally.

## The Substitution Trap

The trap here is not substitution of cognitive work. It is the conversion of context into destiny, running through two documented loops.

**The placement loop.** An adaptive platform initializes on prior performance, serves easier content to the low scorer, generates less growth, and then reads the smaller growth as confirmation of the initial estimate. A Matthew effect — to those who have, more is given — running at machine speed. A path computed from yesterday's deficits can be a slow lane with better graphics.

**The expectation loop.** Dashboard labels shape teacher expectations, and expectations shape behavior toward students — the dynamic Chapter 20 documented as the single most damaging routing error in the dataset. A readiness index that quietly tags a fourteen-year-old as "not ready" is manufacturing the conditions of its own accuracy. The label then travels with the student: September's software estimate quietly becoming the four-year track nobody chose on purpose.

Call the combined pattern the algorithmic Matthew effect — noting honestly that this framing is assembled from documented components (placement-loop dynamics, expectation effects, predictive analytics inheriting historical bias; see Holstein and Doroudi, 2021) rather than a single cited finding. The audit questions that catch it are concrete: after a student's two bad weeks — illness, a family move — how long until the system re-estimates upward? Is there a human override, and is it ever used? Who reviews placement drift by subgroup each term? If nobody in the building can answer, the platform is manufacturing destiny, whatever the sales engineer says.

![Cycle diagram of the algorithmic Matthew effect — low prior score, lower-level content served, less growth generated, estimate confirmed or lowered, looping back — with a dotted exit arrow labeled human override plus scheduled re-estimation](images/25-prior-ability-as-context-not-destiny-fig-01.png)
*Figure 25.1 — The algorithmic Matthew effect loop and its exit*

<!-- → [DIAGRAM: Algorithmic Matthew effect loop — circular flow: "Low prior score" → "Lower-level content served" → "Less growth generated" → "Estimate confirmed or lowered" → back to "Low prior score"; beside the loop, a dotted exit arrow labeled "Human override + scheduled re-estimation" with conditions listed: named reviewer, expiration date, subgroup audit — student should see that the loop is self-sealing without those structural interrupts] -->

## The Case in Full

Marisol's placement committee piloted the readiness index for one placement season under committee-written rules.

The index did something the counselors could not: it synthesized three middle schools' inconsistent records into comparable starting-point profiles, and it surfaced thirty-one students whose strong recent trajectories were buried under weak sixth-grade scores — students a folder-skim would likely have routed into foundations sections. The committee placed most of them in regular sections with a monitoring plan. That is context-reading at its best: better information, human decision.

In the second week, a counselor processing 400 placements began accepting the index's recommendation wherever it was "obvious" — which in practice meant wherever it matched the prior record, which is to say wherever it mattered most. One case forced the issue: a student with a low index (new to English, two school changes, a bad seventh-grade year) whose math teacher insisted she belonged in honors geometry. The index had no field for "her teacher has watched her reason for a year." The committee realized the recommendation column had quietly become the decision column — the gate crossed not by malice but by workload. They also noticed what the platform never offered: any report on what happened to last year's "not ready" students, or any breakdown of recommendations by subgroup.

**The decision: five conditions written into the contract renewal.** The index informs, humans decide — operationally enforced by removing the one-click "accept recommendation" button and requiring a named staff member on every placement. Any placement *below* a student's requested or teacher-recommended level requires a second human reviewer. All support-section placements expire at the semester with a mandatory re-look, so no September estimate can silently become a four-year track. The data office produces a twice-yearly drift report — placement recommendations and overrides broken down by race, language status, and IEP status — reviewed by the committee. And the school tracks "boundary students" (placed against the index's recommendation, in either direction) as the standing test of the index's actual accuracy.

The teacher's question from the first meeting got its answer built into the contract: "when the index says a kid isn't ready, who un-says it?" — a named human reviewer. And "when do we ever check?" — twice a year, by subgroup, in writing.

## What Would Change My Mind

A longitudinal study showing that adaptive-platform initial placements do *not* persist — that students starting in lower-level content streams are re-estimated upward at rates matching their actual capability, across subgroups, without the human-override machinery this chapter prescribes — would substantially soften the placement-loop warning. If well-designed platforms turn out to self-correct faster and less prejudicially than human placement committees (which have their own ugly track record), the right conclusion would be to automate *more* of placement, not less, and this chapter's gate conditions would need inverting.

No such study exists. Every district running a readiness index right now is the study.

## Still Puzzling

The honest unknown of the decade: does AI personalization narrow or widen prior-ability gaps? The early evidence runs both directions depending on design — the Bastani versus Tutor CoPilot pattern — and no settled meta-analytic answer exists yet.

Where exactly is the boundary between "ability" and "accumulated opportunity"? The dataset keeps prior ability (0.94) and prior achievement (0.55) as separate rows, which is itself an argument that the construct is unstable — but placement decisions cannot wait for the construct debate to resolve.

No one has located a longitudinal study of LLM-era placement loops on long-run student trajectories. Until one exists, every district running a readiness index is the study — which is the same sentence that ended the last section, because it is the only honest answer available.

## Further Reading

**Holstein, K., & Doroudi, S. (2021). Equity and Artificial Intelligence in Education. arXiv:2104.12920.** The clearest map of how AI systems in education can amplify or reduce existing inequities — including the placement and prediction dynamics this chapter calls the algorithmic Matthew effect.

**O'Neil, C. (2016). *Weapons of Math Destruction*.** The general theory of the feedback loop: a model trained on the past, used to allocate the future, grading itself on outcomes it shaped.

**Steele, C. M. (2010). *Whistling Vivaldi*.** What labels do to performance from the inside — the psychological loop that pairs with the algorithmic one. (Parts of the stereotype-threat literature have a contested replication record; read for mechanism, not magnitude.)

**Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49, 241–253.** Essential here for the distinction the chapter leans on: what a 0.94 means when it describes a background association rather than an intervention's payoff.

**Bastani, H., et al. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*.** The field experiment behind this chapter's equity warning: the same AI access produced gains with guardrails and harm without — design, not technology, decided whether prior differences shrank or compounded.

---

## Exercises

**Warm-up**

1. *(Recall — What the number is)* The chapter distinguishes prior ability (d = 0.94) from an intervention row. Explain the distinction in two sentences: what kind of association the d = 0.94 describes, why it appears in the High band alongside genuine interventions, and why treating it as an intervention effect would be a category error.

2. *(Recall — Two constructs, same data)* The chapter contrasts "diagnosing prior knowledge" with "measuring prior ability." Both can run on identical assessment data. Explain in one paragraph what makes them different — shelf life, institutional response, and what each does to the student's relationship to the next year of school.

3. *(Recall — Adjacent pair)* The chapter highlights the contrast between prior ability (d = 0.94, AI-ADJACENT) and "strategy to integrate with prior knowledge" (d = 0.93, AI-AUGMENTED). Explain why nearly identical numbers carry opposite classifications. What is the rule the contrast illustrates?

**Application**

4. *(Transfer — Placement loop audit)* A district has run a readiness index for two years. The data office reports that 94 percent of students placed in support sections in fall are still in support sections the following fall. The vendor calls this "consistency." Write a two-paragraph response: what consistency in placement rates actually indicates about the index's behavior, what questions the district should ask its own data office, and what a healthy re-estimation rate would look like instead.

5. *(Transfer — Contract clause)* The chapter's case study produced five contract conditions. Take condition three — all support-section placements expire at the semester with a mandatory re-look — and draft it as procurement language specific enough that a compliance auditor could verify it without asking the vendor for clarification. Then identify the most likely workaround in practice and add a clause that closes it.

6. *(Transfer — Lever/context/correlation sort)* The chapter presents a classification exercise: lever, context, or correlation between outcomes. Classify the following four statements and explain each classification in one sentence: (a) "Reciprocal teaching raises achievement (d = 0.74)"; (b) "Prior ability predicts achievement (d = 0.94)"; (c) "High-school GPA predicts college performance"; (d) "Prerequisite gap identification enables targeted reteaching." Which of these can a platform legitimately claim as evidence that its product works?

**Synthesis**

7. *(Combine — Full placement policy)* Design a complete readiness-index adoption policy for a 1,200-student comprehensive high school, covering: what the index may and may not generate in teacher-facing views, the named-reviewer requirement, the below-request placement review, the expiration and re-estimation schedule, the subgroup drift audit cadence and reviewer, and the boundary-student tracking protocol. For each condition, name the trap it prevents. Your policy should be specific enough that the committee could hand it to a new principal without further explanation.

8. *(Combine — Disaggregation as equity check)* The chapter argues that disaggregating outcome data by prior-achievement tercile is a legitimate and important AI use. Design the evaluation framework for a school piloting an adaptive math platform, using prior-achievement tercile as the primary moderator variable. Specify: what the three terciles are and how they are defined, what outcome measures are collected and when, what pattern of results would indicate the platform is reducing gaps, and what pattern would indicate it is widening them. Then explain why reporting a single average outcome — as most vendors do — is insufficient.

**Challenge**

9. *(Open — Self-correcting platform reversal)* The chapter's What Would Change My Mind section acknowledges that if adaptive platforms re-estimate students upward at rates matching actual capability, the case for human-override machinery would weaken. Construct the argument that a well-designed platform could self-correct faster and less prejudicially than a human placement committee — drawing on the documented history of human placement committees' track records. State the mechanism by which the platform would self-correct, what design features are necessary, and what evidence would confirm it. Then evaluate honestly: does your proposed platform design currently exist, or only in a hypothetical version of the technology — and what is the right institutional posture in the gap between the hypothetical and the actual?

## Prompts

### Figure 25.1 — The algorithmic Matthew effect loop and its exit
Build a closed-loop cycle diagram with four nodes connected by arrows returning to start: "Low prior score" → "Lower-level content served" → "Less growth generated" → "Estimate confirmed or lowered" → back to start. Render the loop as visibly self-sealing. Beside the loop, add a dotted exit branch leaving the cycle labeled "Human override + scheduled re-estimation," with three listed conditions: named reviewer, expiration date, subgroup audit. Contrast the solid self-sealing loop with the dotted exit so the reader sees the loop stays closed without the structural interrupts. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 25.2 — Same data, two uses: diagnosis vs. measurement
Build a two-panel comparison forking from a shared source node "Same assessment data" at the top. Left branch "Diagnosing prior knowledge": three stacked rows — "Short shelf life," "Instructional-plan output," "Act, re-diagnose, revise." Right branch "Measuring prior ability": aligned rows — "Indefinite shelf life," "Placement-label output," "Route, schedule, confirm" (highlight this last right row). Draw two diverging arrows from the shared source into each branch. Caption that the same data hardens into destiny or stays provisional depending on institutional use. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 25.3 — Same number, opposite classification
Build a horizontal bar chart, three bars, value range 0 to ~1.0 in Cohen's d. Bars sorted descending: "Prior ability (context / destiny-risk)" = 0.94 (highlighted), "Strategy to integrate with prior knowledge (lever)" = 0.93, "Prior achievement (overlapping construct)" = 0.55. Use a classification color encoding distinguishing the context/destiny-risk bar from the teachable-lever bar even though their values are nearly identical. Zero baseline at left. Vertical reference line at d = 0.40 labeled "0.40 hinge." Annotate the near-identical 0.94/0.93 pair carrying opposite classifications. Label each bar with its value. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

# Chapter 9 — AI as Expert Task Analyst
*What Experts Know They Know, What They Don't, and Why the Difference Is the Curriculum.*

Four influences with enormous effect sizes and an unusually permissive AI profile: cognitive task analysis (1.29), Piagetian programs (1.28), conceptual change programs (0.99), and help seeking (0.72). In Hattie's synthesis these run on analysis — decomposing what experts actually do, matching tasks to developmental readiness, surfacing misconceptions, lowering the cost of asking. The cognitive work they support is mostly design work, done before the learner arrives, and that is the kind of work large language models are structurally good at. This is the rare chapter where the book's answer is closer to yes than to carefully.

**Group Profile: AI as Expert Task Analyst**

| Profile | Detail |
|---|---|
| Influences in this group | 4 of Hattie's 252 |
| Effect-size range | d = 0.72 to 1.29 (weighted average 1.07) |
| Hattie band | High |
| AI feasibility | AI-augmented |
| Human irreducibility | Medium |
| Substitution risk | Low |
| Cognitive-work conflict | None |
| Members | Cognitive task analysis (rank 4, d = 1.29); Piagetian programs (rank 6, d = 1.28); Conceptual change programs (rank 8, d = 0.99); Help seeking (rank 30, d = 0.72) |

Watch Ray Delgado set up a vertical weld and he makes forty decisions. Ask him to list them and he names six.

The other thirty-four stopped being decisions decades ago. They became hands. The gap between what Ray does and what Ray knows he does is not a character flaw — it is a well-documented feature of expertise, and it is why the students who learn from him sort into two groups: the strong ones, who reconstruct the missing steps through trial and scrap metal, and the rest, who fail in ways Ray finds genuinely mysterious. The step they missed is one he no longer knows he takes.

Ray retires in eighteen months. Marcus Webb, who runs the CTE programs at Ray's technical high school, has a curriculum consultant quoting four months and a five-figure sum to extract Ray's knowledge before it walks out the door. He also has an instructional designer who spent an afternoon with a frontier LLM and produced something unsettling: a draft decomposition of vertical-position arc welding — prerequisite chains, decision points, common novice errors, practice sequence — that looks, to Marcus's half-trained eye, remarkably like what the consultant sells.

The designer's question is the chapter's: is this the consultant's deliverable at one percent of the price, or a fluent imitation of expertise with hallucinated specifications where the knowledge should be — and how would you tell?

## What Makes This Group Different

Four influences, all high-band: cognitive task analysis (d = 1.29), Piagetian programs (d = 1.28), conceptual change programs (d = 0.99), help seeking (d = 0.72). Effect sizes 0.72 to 1.29 on the 2018 252-influence list, weighted average 1.07 — the highest-band group in the book that carries neither a conflict flag nor elevated substitution risk. [verify all figures against MetaX near publication]

That combination is nearly unique in the dataset. The high-band groups ahead — feedback, discussion, collective efficacy — come wrapped in conflict flags or elevated substitution risk. This group is the rare shelf where enormous effect sizes sit next to a genuinely permissive classification, and the reason is structural. These four influences run on analysis of the learning task and the learner's existing knowledge: decomposing expertise, matching tasks to developmental readiness, surfacing and confronting misconceptions, lowering the cost of asking for help. The cognitive work being supported is mostly the teacher's design work and the system's diagnostic work — and unlike live delivery, design work benefits from exactly what large language models are: vast, fast, pattern-rich decomposition engines with no ego about being corrected.

If the book has a chapter where the answer leans *yes, use it, substantially*, this is it. The discipline is that the yes comes with one non-negotiable clause. The clause is the chapter.

## The Four Rows

Cognitive task analysis at d = 1.29 — rank 4 of 252 — is a family of interview and observation methods for extracting what experts actually do, including what they no longer know they do. Its premise is a well-replicated embarrassment in expertise research: experts' self-reports omit large fractions of the decision steps novices need. Figures around seventy percent of critical decision points appear in the CTA literature. [verify — the canonical claim traces to Clark and colleagues' reviews; confirm before quoting] Instruction built from CTA-extracted models routinely beats instruction built from expert free recall. Two honesty notes travel with the 1.29: the meta-analytic base is small and leans on military, medical, and technical training rather than K-12 classrooms [verify], and what the number rewards is better instructional input, not a classroom technique.

Piagetian programs at d = 1.28 is the group's strange passenger. The headline number derives substantially from correlating children's Piagetian developmental-stage measures with achievement — closer to a measurement finding than a program effect. [contested — treat this row as part context-variable in the grammar of Chapter 6 rather than a purchasable intervention] The durable practical content: tasks matched to a learner's demonstrated readiness outperform tasks matched to their grade label. AI can support stage-matched task design; the developmental progression itself is biologically paced.

Conceptual change programs at d = 0.99. Instruction that surfaces a learner's existing misconception, confronts it with discrepant evidence, and supports rebuilding — because misconceptions are not absences of knowledge but rival theories that fight back. The student who believes heavier objects fall faster is not ignorant; she holds a coherent theory that matches most of her life experience. The theory has to be defeated, not bypassed. AI misconception detection in student work is legitimate; the confrontation and rebuilding benefit from teacher mediation.

Help seeking at d = 0.72. Students who seek help adaptively learn more. The mechanism has a known enemy: social cost. Asking reveals ignorance to people whose regard you want. AI can lower the threshold — anonymous questions, always-available channels, no judgment. The psychological safety that makes help-seeking habitual lives in human classroom climate.

## One Mechanism, Four Rows

Learning accelerates when instruction is built from an accurate model of the task and of the learner's current head. Most instruction is built from neither. It is built from the expert's compressed memory of a path she no longer walks, delivered to a learner whose actual prior knowledge is guessed at.

Each row repairs part of that double blindness. CTA repairs the task model: it reconstructs the forty decisions, so the curriculum teaches what experts do rather than what they remember doing. Piagetian matching repairs the readiness model: tasks meet the learner where she demonstrably is. Conceptual change repairs the prior-knowledge model: it treats the learner's existing theory as the object of instruction rather than an empty space. Help seeking is the same repair run by the learner personally — the question is a self-issued diagnostic, the fastest possible alignment of instruction to need.

![Four influences repairing one double-blindness — an accurate model of the task and the learner's current knowledge — each row fixing a different component](images/09-ai-as-expert-task-analyst-fig-02.png)
*Figure 9.2 — Four rows, one repaired model*

<!-- → [DIAGRAM: Four-row mechanism map — center node: "accurate model of task and learner." Four spokes leading to: CTA (repairs task model), Piagetian matching (repairs readiness model), conceptual change (repairs prior-knowledge model), help seeking (learner-run repair). Student should see the structural unity before reading the individual rows.] -->

Why this group tolerates AI so well follows directly. The work being accelerated is model-building about tasks and minds — decomposition, pattern-matching across thousands of described performances, hypothesis generation about where novices break. That is teacher-side, design-time cognition. The learner's downstream effort — practicing the decomposed skill, fighting through the discrepant event, formulating the question — remains fully intact. No learner act is displaced. The structure-effort separability of Chapter 3 holds here at the high band.

And the mechanism dictates the non-negotiable clause. A task model is only as good as its correspondence to the real task — and an LLM's decomposition is a synthesis of how tasks like this are *described in text*, not an observation of Ray's hands. Where the textual record is rich and consistent, the draft will be strong. Where the craft knowledge is tacit, local, or safety-critical, the model will fill gaps with plausible interpolation, indistinguishable in fluency from the parts it got right. The failure mode of a human expert analyst is visible incompetence. The failure mode of an artificial one is *convincing* incompetence. Hence the dataset's phrasing — the strongest endorsement it uses anywhere — with expert validation marked as non-negotiable rather than recommended.

## What AI Can Safely Do

Draft the decomposition. Generate first-pass task hierarchies, prerequisite chains, decision-point inventories, and novice-error predictions for any teachable skill. The draft's correct role: an interview instrument, not a deliverable.

This reframing is the method's most important practical gift. Experts are dramatically better at correcting a concrete model than at free-recalling their own knowledge — the draft converts an extraction problem into an editing problem. Walk Ray through the AI's forty-step model and ask what is wrong, missing, or dangerously oversimplified. What surfaces is exactly what the consultant's structured interviews were trying to reach. The AI did not replace the expert; it gave the expert something wrong enough to argue with.

![Expert free recall yielding an incomplete curriculum versus an AI draft corrected by the expert, with the delta log as the curriculum's most valuable column](images/09-ai-as-expert-task-analyst-fig-01.png)
*Figure 9.1 — Draft-then-correct workflow and the delta log*

<!-- → [DIAGRAM: Two-path comparison — Path A: expert free recall → curriculum. Path B: AI draft → expert correction → validated curriculum. Path B shows a "delta log" branching off at the correction stage. Annotate that the delta log is the curriculum's most valuable column — the tacit knowledge that only surfaces when there is a concrete wrong thing to correct.] -->

Map misconceptions at scale. Read student work — written explanations, shop diagnostics, scenario responses — and flag the rival theory underneath the error. Assemble discrepant cases and contrasting examples for the teacher to deploy. Detection scales; confrontation and rebuilding stay mediated.

Match tasks to demonstrated readiness. Sequence practice against what the learner has actually shown, not their cohort label. This is the legitimate core of the Piagetian row — not stage diagnosis, but stage-sensitive sequencing.

Lower the asking threshold. An always-available, judgment-free channel for the questions students will not raise a hand for — anonymous queues, AI first-responders that route upward, not downward. With one design constraint the next section sharpens: the channel must coach the question, not vend the answer.

The book's classification hypothesizes the group retains most of its value under AI support — d ≈ 1.00 [HYPOTHESIS] for AI-drafted, expert-validated CTA. That is the appendix's largest hypothesized figure, still only a structured conjecture, and flagged as such.

## The Two Traps

**The unvalidated decomposition.** The trap Marcus is staring at: shipping the afternoon draft as the curriculum. In CTE the cost is concrete — a hallucinated parameter or a missing safety step in a welding progression is a burn, a failed certification, a lawsuit. But the trap's deep version is subtler than error. An LLM decomposition systematically captures the textbook-consensus version of a skill and silently omits the local, tacit, exception-handling knowledge that CTA exists to extract — the thirty-four decisions in Ray's hands that never made it into any manual. Ship the draft and you have automated the omission problem CTA was invented to solve, with better formatting. The fluency is the camouflage; validation is not a quality step, it is the method.

**The answer machine in help-seeking clothes.** Help seeking splits into two behaviors the research has always distinguished: adaptive (seeking hints, explanations, the next step — help that keeps you the solver) and executive (seeking the answer — help that replaces you). An unguardrailed AI channel is the most efficient executive-help dispenser ever built. Bastani's field experiment is the receipt: unrestricted GPT access lifted practice performance forty-eight percent and left students seventeen percent *worse* on unaided assessment, while the guardrailed tutor — hints, no answers — avoided the harm. VanLehn's review of the tutoring literature puts human tutoring at d = 0.79 and step-based intelligent tutoring at a statistically comparable 0.76 — the effect lives in coached stepping, not answer delivery. Lowering the threshold is only a gift if what is behind the threshold is adaptive.

## Marcus's Decision

Marcus Webb hired neither the consultant's full package nor the designer's afternoon draft. He bought the validation method and ran the drafting in-house — a two-day training with the consultant on structured elicitation protocols, then the LLM handling first-pass decompositions.

The hybrid workflow outran both pure options. The LLM drafted decompositions for twelve core welding competencies in a week — work the consultant had quoted a month for. Then the drafts met Ray, and the meetings became the best professional development the department had ever accidentally run. Confronted with the AI's eleven-step model for vertical-up root passes, Ray produced exactly what the method counts on: *"No. Nobody sets amperage before checking the fit-up gap; the gap tells you the amperage."* Four such corrections per competency. The tacit thirty-four surfacing because there was finally a concrete wrong thing to correct. The instructional designer logged every correction as a delta between textual consensus and Ray's mastery — the curriculum's most valuable column.

Two genuine AI catches went the other way: novice-error patterns from the wider literature that Ray had stopped noticing he compensates for. The validated progressions then powered readiness-matched practice sequences and misconception-keyed shop checklists.

The dangerous moment came from the HVAC program, not the welding one. A veteran had already retired; no domain expert remained to validate. A draft decomposition had quietly entered use, and the certifying examiner flagged a refrigerant-handling sequence as out of order against EPA procedure. No one was hurt. The lesson was priced anyway. Drafts without a validating expert are not drafts. They are liabilities with page numbers.

The AI help channel in the welding shop was discovered doing executive duty: students photographing failed welds and receiving full diagnoses, parameter corrections included. Practice welds improved; the first proctored certification mock collapsed, students unable to diagnose unaided the failures they had been photographing for weeks. The Bastani curve drawn in filler metal. The channel was rebuilt on a hint ladder — it may name the flaw's category and coach the next diagnostic step, never deliver the diagnosis — and Ray's apprenticeship norm ("bring me your weld and your theory of what went wrong") was taught as the program's help-seeking model.

![An executive-help channel lifting supervised practice performance while unaided proctored certification flattens then drops — the Bastani divergence in domain form](images/09-ai-as-expert-task-analyst-fig-03.png)
*Figure 9.3 — The Bastani curve in a help channel*

<!-- → [CHART: Two-line chart — x-axis: weeks of AI-channel use; y-axis: score. Line 1: practice-weld performance (climbing). Line 2: proctored mock-certification score (flat then dropping). Annotate the divergence point. Student should see the Bastani curve in domain-specific form — the channel lifted the supervised metric while hollowing the unaided one.] -->

Adoption conditions, written into the program's charter: no decomposition touches students until a credentialed practitioner has corrected it line by line and signed it — the signature is a professional attestation, archived with the curriculum; safety-critical sequences get second validation against the certifying body's standards; the help channel is hint-only with hard routing to humans for any question requiring diagnosis; the validation deltas are maintained as a living document, because they are the program's map of exactly what its AI cannot know; for programs without a resident expert, drafts wait — the method's bottleneck is the validator, and the bottleneck is the point.

## The Phase Gate

**AI may** draft task decompositions, prerequisite maps, and novice-error predictions; structure expert-validation interviews; detect misconceptions in student work and assemble discrepant cases; sequence practice to demonstrated readiness; and staff a guardrailed, hint-only help channel that routes hard cases to humans.

**The expert must** validate every decomposition line by line and sign it.

**The teacher must** mediate conceptual confrontation and maintain the classroom climate that makes asking cheap.

**The learner must** practice the decomposed skill, fight through the discrepant evidence, and formulate their own questions and failure theories — the downstream effort the upstream analysis exists to aim.

**Evidence that learning improved is** unaided performance on the whole task — certifications, proctored demonstrations, novel-fault diagnosis without the channel — improving against the pre-CTA baseline, plus help-seeking telemetry showing a measurable shift from answer-requests toward process-questions.

## What Evidence to Demand

Whole-task unaided performance. Certification pass rates, proctored practical exams, novel-fault diagnosis without the channel — against historical baseline. Decomposition is only as good as the recomposed skill.

The validation delta log. Demand to see what experts corrected in the AI drafts. A team that cannot produce deltas either had a perfect model — which has never happened — or never validated. Delta volume per domain is also your hallucination-risk map.

Help-channel telemetry, classified. What fraction of interactions delivered answers versus coached steps? Pair with the Bastani check: assisted practice scores against unaided assessment, divergence watched explicitly.

Readiness-match audit. Are sequencing decisions driven by demonstrated performance or cohort defaults with adaptive branding? Sample actual student paths.

What does not count: decomposition page counts, the draft's fluency, help-channel volume or satisfaction, time saved versus consultants before validation, or practice scores with the channel live.

## What Would Change My Mind

The chapter's spine is the validation clause, and it rests on an empirical claim: that LLM decompositions of skilled tasks contain expert-detectable errors and omissions at rates that matter. That claim has a shelf life. If systematic studies showed frontier-model decompositions matching validated-CTA quality across domains — expert deltas approaching zero outside the truly tacit crafts — the clause would relax from "validate everything" to "validate the tacit and the dangerous," and the group would drift toward AI-NATIVE. The permissive reading dies a different way: if guardrailed help channels in real deployments drift executive anyway — students engineering answer extraction past any hint ladder, the Bastani gap appearing despite the spec — then help seeking belongs with the danger-zone groups, and this chapter's friendliest row was a misclassification.

## Still Puzzling

The validation bottleneck has economics nobody has worked out. The method's cost collapses except for the expert hours, which means programs without resident experts — precisely the under-resourced ones — benefit least from the cost collapse. The tool is cheapest where it was already affordable.

Piagetian programs at 1.28 remains the group's unresolved row. If it is substantially a measurement correlation, its presence inflates the group average and its program framing misleads. It may belong, in spirit, with Chapter 6's context variables. The classification keeps it here; I keep my doubts on the record.

When the AI interviews the expert directly — elicitation chatbots are already being piloted — who validates the interview? The method's safeguard assumes a human asking the human. Recursive automation of the extraction step has no evidence base yet.

## Further Reading

**Clark, R. E., Feldon, D. F., van Merriënboer, J. J. G., Yates, K. A., & Early, S. (2008). Cognitive task analysis. In *Handbook of Research on Educational Communications and Technology* (3rd ed.).** The method behind the 1.29: what experts omit, why, and how structured elicitation gets it back. [verify edition and omission-percentage figures before quoting]

**VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46(4), 197–221.** Coached stepping, not answer delivery, is where tutoring's effect lives — the design law under the help channel.

**Bastani, H., et al. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*.** The adaptive/executive distinction in field data: +48 percent assisted, −17 percent unaided, and the guardrail that prevented it.

**U.S. Department of Education, Office of Educational Technology (2023). *Artificial Intelligence and the Future of Teaching and Learning*.** The expert-in-the-loop doctrine this chapter turns into a signature requirement.

**Visible Learning MetaX (visiblelearningmetax.com).** Where to re-check all four rows — and to read the Piagetian programs entry with this chapter's skepticism in hand.

---

## Exercises

**Warm-up**

1. (Low difficulty) *Tests understanding of the expert-omission problem.* Explain in two sentences why experts' self-reports systematically omit steps that novices need. What does this mean for curriculum built from expert free recall, and why does it make CTA valuable?

2. (Low difficulty) *Tests the adaptive/executive distinction.* Define adaptive help-seeking and executive help-seeking in your own words. Give one concrete example of each in a classroom context, and explain which one the research shows produces durable learning.

3. (Low difficulty) *Tests the validation clause.* A school district uses an LLM to generate skill progressions for its culinary arts program and reviews them with the department chair before use. The department chair is an administrator with a culinary background from fifteen years ago. Does this satisfy the validation requirement as described in the chapter? Explain your reasoning.

**Application**

4. (Medium difficulty) *Tests the draft-as-instrument reframe.* You are helping a veteran biology teacher prepare to retire. She is available for six hours of elicitation. Compare two approaches: (A) spending six hours in open interview asking her to describe her teaching; (B) spending one hour generating an AI draft of key skill decompositions and five hours walking her through corrections. Predict the likely output of each, with reference to the mechanism the chapter describes.

5. (Medium difficulty) *Tests conceptual change logic.* A student consistently solves current-in-a-circuit problems by assuming current is "used up" as it flows through components. Describe the misconception as a rival theory, explain why giving the student the correct theory directly is likely to fail, and outline what a conceptual-change instructional sequence would need to include.

6. (Medium difficulty) *Tests the Bastani trap in a new domain.* An online writing program offers students AI feedback on draft essays. Students who use the feedback show strong improvement in revised drafts. However, the program's end-of-semester timed writing assessment — completed without AI — shows no improvement over prior years. Apply the chapter's framework to explain what is likely happening and what the program would need to change.

**Synthesis**

7. (High difficulty) *Tests integration of CTA, validation, and evidence standard.* Design a complete expert-knowledge-capture workflow for a nursing assistant program whose veteran instructor retires in six months. Specify: what the AI produces, what the validation process requires and who performs it, what the safety-critical second-validation step covers, what evidence at what time interval would confirm the curriculum improved student outcomes, and what you would do if no credentialed validator is available before the instructor leaves.

8. (High difficulty) *Tests the bottleneck economics from "Still Puzzling."* The chapter argues the method is cheapest where it was already affordable — programs with resident experts who can validate. Propose a structural solution that would make validated AI-assisted CTA accessible to under-resourced programs without resident experts. Address the validation requirement directly: your solution cannot simply waive it.

**Challenge**

9. (Advanced) *Tests the recursive-automation problem and the validation clause's limits.* An edtech company pilots an AI system that conducts structured elicitation interviews with experts autonomously — it asks the follow-up questions, flags inconsistencies, and produces a validated-looking decomposition without a human interviewer. The company claims accuracy comparable to human-led CTA on a benchmark of ten technical skills. Design the study you would want to see before trusting this system's output in a safety-critical domain, specifying what the benchmark would need to include, who would validate the validation, and what failure mode you are most worried the benchmark cannot detect.

---

## References

<!-- Added by fact-check pass 2026-06-08. See factchecks/09-ai-as-expert-task-analyst-assertions.md -->

1. Clark, R. E., Feldon, D. F., van Merriënboer, J. J. G., Yates, K. A., & Early, S. (2008). Cognitive task analysis. In *Handbook of Research on Educational Communications and Technology* (3rd ed.).
2. Posner, G. J., Strike, K. A., Hewson, P. W., & Gertzog, W. A. (1982). Accommodation of a scientific conception: Toward a theory of conceptual change. *Science Education*, 66(2), 211–227.
3. VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46(4), 197–221. https://doi.org/10.1080/00461520.2011.611369
4. Bastani, H., et al. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122. https://www.pnas.org/doi/10.1073/pnas.2422633122
5. Visible Learning. Hattie Ranking: 252 Influences and Effect Sizes. https://visible-learning.org/hattie-ranking-influences-effect-sizes-learning-achievement/

---

## Prompts

### Figure 9.1 — Draft-then-correct workflow and the delta log
Build a left-to-right flowchart comparing two paths with a branch output. Path A (weaker route): "Expert free recall" → "Incomplete curriculum (omitted tacit steps)". Path B: "AI draft" → "expert correction" → "Validated curriculum + delta log". At the correction stage, branch off a "delta log" node labeled the most valuable output. Use arrows; mark Path A "weaker route" and the correction→delta edge "delta log branches off correction". Channels: x = stage order, vertical position = Path A vs. B, color = incomplete vs. validated outcome and the delta-log emphasis. No axes, no zero baseline. Annotate that corrections surface tacit knowledge only against a concrete wrong thing — extraction becomes editing. Deliverable: single standalone HTML file, inline CSS, D3 v7 from the pinned CDN, Okabe-Ito-free brutalist palette via CSS variables.

### Figure 9.2 — Four rows, one repaired model
Build a node-edge conceptual map with a central node and four repair spokes. Center (highlighted): "Accurate model of task and learner". Four spoke nodes each connected by an arrow into the center: "CTA: repairs task model", "Piagetian matching: repairs readiness model", "Conceptual change: repairs prior-knowledge model", "Help seeking: learner-run repair". Channels: radial position = the four influences, arrow direction = into the shared center, color = uniform spokes with the center emphasized. No axes, no zero baseline. Annotate that all four repair part of one double-blindness, each fixing a different component of the model. Deliverable: single standalone HTML file, inline CSS, D3 v7 from the pinned CDN, Okabe-Ito-free brutalist palette via CSS variables.

### Figure 9.3 — The Bastani curve in a help channel
Build a two-line divergence chart. x-axis = weeks of AI-channel use, y-axis = score. Line 1 "Practice / supervised performance": climbs steadily (misleading supervised gain). Line 2 "Unaided proctored certification": flat early, then declines toward the right (real harm). Mark the divergence point (highlight). Channels: x = weeks, y = score, color = supervised vs. unaided. zero baseline yes for the score axis. Annotate that the channel lifts the supervised metric while hollowing the unaided one — the Bastani assisted/unassisted divergence in domain-specific form. Deliverable: single standalone HTML file, inline CSS, D3 v7 from the pinned CDN, Okabe-Ito-free brutalist palette via CSS variables.

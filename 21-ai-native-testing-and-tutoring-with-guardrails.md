# Chapter 21 — AI-Native Testing and Tutoring With Guardrails
*The Fork in the Settings Menu.*

Practice testing (0.54), intelligent tutoring systems (0.48), and technology with college students (0.42): the group where AI's natural strengths and Hattie's evidence overlap most directly — and where the substitution risk is highest among the AI-native groups. Retrieval practice is one of the best-evidenced moves in cognitive psychology, and AI can generate, administer, and score it natively. The same system, optimized to be helpful, will also answer instead of asking, hint instead of waiting, and convert testing back into telling. Everything here is permitted, and everything here needs a guardrail.

**Group Profile: AI-Native Testing and Tutoring With Guardrails**

| Profile | Detail |
|---|---|
| Influences in this group | 3 of Hattie's 252 |
| Effect-size range | d = 0.42 to 0.54 (weighted average 0.48) |
| Hattie band | Above the d = 0.40 hinge |
| AI feasibility | AI-native |
| Human irreducibility | Low |
| Substitution risk | High |
| Cognitive-work conflict | Partial |
| Members | Practice testing (rank 66, d = 0.54); Intelligent tutoring systems (rank 89, d = 0.48); Technology with college students (rank 115, d = 0.42) |

Camille Foster confirmed it in about ninety seconds.

She is the director of the Learning and Testing Center at a regional public university — gateway courses, retention leak, three hundred students on the human-tutoring waitlist last term who never got a tutor. The vendor's demo was genuinely strong in places: curriculum-aligned problem sets, step-level feedback that caught *where* in a derivation a student went wrong, spaced retrieval quizzing, instructor dashboard. Then she found the chat pane. "Your 24/7 AI tutor," the interface called it. She pasted in a problem from the chemistry homework. The platform solved it.

The vendor's deck closed on Bloom's two-sigma slide: personal tutoring for every student at software prices, the problem finally solved. Camille has read enough of the tutoring literature to know that slide is doing unsupported work. But she also knows her waitlist. For most of her students the alternative to the AI tutor is not a human tutor. It is nothing. The question is not whether this platform beats a tutor. It is whether, configured honestly, it beats the nothing — without quietly manufacturing the −17 this book keeps finding behind inflated practice numbers.

The answer lives in a settings menu, and this chapter is a map to the right switches.

## A Different Kind of AI-Native

Three influences: above the hinge, AI-NATIVE, low human irreducibility, high substitution risk, partial cognitive-work conflict. Effect sizes 0.42 to 0.54 on the 2018 252-influence list, weighted average 0.48. [verify against MetaX near publication]

Compare this signature to the spelling-and-vocabulary group from two chapters ago and the difference is everything. Both are AI-NATIVE, both have low irreducibility — but the risk flag has flipped to high and a conflict flag has appeared. Spelling practice cannot be done *for* you; the absurdity protects it. Testing and tutoring can: a quiz that reveals the answer one tap early has done the retrieval for you, and a tutor that completes the step has done the thinking for you — and both feel, from inside, like being helped.

The dataset's ITS row carries the most bimodal hypothesis in the entire classification: d ≈ 0.45 curriculum-aligned [HYPOTHESIS] versus d ≈ 0.20 unconstrained chat [HYPOTHESIS]. Same product category. Same model. Forked by a configuration screen. That fork is the chapter.

## The Three Rows

Practice testing (d = 0.54) — rank 66. The most counterintuitively powerful row in the learning-strategies literature. Roediger and Karpicke's 2006 experiments fixed the canon: students who repeatedly tested themselves on material retained dramatically more at a delay than students who repeatedly restudied it — even though the restudiers felt more confident and the immediate scores favored them. The testing effect has survived hundreds of replications. The mechanism is retrieval itself: the effortful act of pulling information from memory strengthens the trace and reveals the gaps. Which is why the effect requires the pull. A practice test that shows the answer before or instantly upon error is restudy wearing a quiz costume — all the confidence, none of the consolidation. The power and the crutch are the same feature on two different timers.

Intelligent tutoring systems (d = 0.48) — rank 89. Worth reading at two altitudes. At the meta-analytic altitude: across diverse implementations, ITS effects average near 0.48 — solid, above hinge, unspectacular. At the focused altitude, VanLehn's 2011 review found step-based tutoring systems reaching d ≈ 0.76 against d ≈ 0.79 for human tutors — near-parity with the gold standard — under specific conditions: well-structured domains, step-level feedback rather than answer-level, and the system holding the student in the problem rather than solving it. The gap between 0.48 and 0.76 is not noise. It is fidelity to those conditions across the real-world distribution of products and implementations. The same review demolished the genre's marketing premise: human tutoring's d ≈ 0.79 is itself nowhere near Bloom's legendary two sigma, which came from small early studies under conditions never replicated at scale. [contested — the two-sigma figure functions as folklore; VanLehn's reanalysis is the corrective] The vendor slide is wrong twice.

Technology with college students (d = 0.42) — rank 115. The broadest and blandest row: decades of educational-technology comparisons in higher education, averaging modestly above hinge. Its job in this group is contextual — college students are the population where self-directed tool use is highest, oversight is thinnest, and the gap between a tool's guardrailed and unguardrailed selves matters most. The dataset's hypothesis: d ≈ 0.35 [HYPOTHESIS] for AI content delivery as a legitimate use case, with conflict risk concentrated exactly where Camille found it in ninety seconds — problem-solving tasks where "support" and "completion" share a text box.

![Horizontal dot plot of tutoring effect sizes against the 0.40 hinge: practice testing 0.54, ITS average 0.48, step-level high-fidelity ITS 0.76 near the human-tutor benchmark 0.79, technology with college students 0.42](images/21-ai-native-testing-and-tutoring-with-guardrails-fig-03.png)
*Figure 21.3 — Tutoring effect sizes vs. hinge and human-tutor benchmark*

## Why the Settings Matter This Much

The group's engine is effortful retrieval, immediate step-level feedback, spacing, and difficulty calibration. These are legitimate automatables in well-structured domains. What makes this group different from Chapter 19's is the addition of two things that explain both the higher ceiling and the conflict flag.

Step-level visibility is what gave VanLehn's systems near-parity with human tutors. An answer-level system knows *that* you failed; a step-level system knows *where* — which line of the derivation, which misapplied rule — and puts feedback on the step while the student is still inside the attempt. That is most of what a good human tutor does, and it is legitimately automable in algebra, chemistry stoichiometry, formal logic, code. It thins fast in ill-structured territory — essays, design, interpretation — which is where the genre's marketing goes to overreach.

Desirable difficulty, held. The testing effect and the tutoring effect share a load-bearing discomfort: both work through effort the learner would decline if offered an exit. Retrieval feels worse than rereading; being held at a step feels worse than being shown the step. The entire value of the configuration is that it removes the exit. This is the precise sense in which the group has a cognitive-work conflict: the chat pane is an exit-installation device. Every capability the LLM adds — fluent explanation on demand, full worked solutions, answers to pasted homework — is an off-ramp from the difficulty that was the product.

![Two-panel comparison of the configuration fork — guardrailed practice and exam curves converging (+127% practice, ~0 exam) versus unguardrailed diverging (+48% practice, -17% exam)](images/21-ai-native-testing-and-tutoring-with-guardrails-fig-01.png)
*Figure 21.1 — The configuration fork: guardrailed vs. unguardrailed*

<!-- → [CHART: Two-curve diagram — x-axis: weeks in platform; y-axis: performance score. Four curves: guardrailed practice, guardrailed exam, unguardrailed practice, unguardrailed exam. Guardrailed curves converge over time. Unguardrailed curves diverge — practice rising, exam falling. Annotate Bastani's specific numbers: +48% practice / −17% exam (unguardrailed); +127% practice / ≈0 exam (guardrailed). Student should see the fork visually — same model, same students, same material, split by configuration.] -->

Bastani and colleagues measured both roads. Unguardrailed GPT-4 access during practice: +48 percent on practice problems, −17 percent on the subsequent unassisted exam. The guardrailed tutor arm — prompted to coach stepwise, withhold answers — +127 percent on practice and approximately zero exam effect. Same model, same students, same material. The guardrail was the intervention.

And one result from Wang and colleagues reframes the genre's ambition: in the Tutor CoPilot trial, the AI was pointed at human tutors — live, expert-modeled suggestions mid-session — and student mastery rose four percentage points overall and nine for students of the lowest-rated tutors. For a director with three hundred students on a waitlist and a thin, variably skilled tutor corps, that is not a footnote. It is a third option the vendor's deck never mentions: AI under the adult, not instead of the adult.

## What AI Can Safely Do

Generate retrieval practice without limit. Micro-quizzes, cumulative spaced review, interleaved problem sets per course syllabus — with attempt-before-reveal enforced in the configuration, not the syllabus language. The d ≈ 0.50 [HYPOTHESIS] lives entirely on the right side of that timer.

Tutor at step level in checkable domains. Hold the student in the problem; diagnose the failed step; feed back on the step; escalate hints on a ladder that ends in a worked example only after attempts are spent. This is the VanLehn 0.76 design, and modern systems can implement it more flexibly than the pre-LLM classics did.

Model the learner for the instructor. Per-student mastery maps, error-pattern clustering across sections, early-warning flags routed to instructors — the diagnosis layer feeding human teaching loops.

Assist the human tutors. Tutor CoPilot's design: live suggestions, post-session summaries, training scenarios for the center's tutor corps. The +4/+9 result aimed at the thin end of the staffing.

Deliver content explanations outside the assessed workspace. Glossaries, examples, re-explanations — the d ≈ 0.35 [HYPOTHESIS] legitimate zone, kept structurally separate from the problem-solving environment.

## The Four Traps

**The chat pane.** The genre's flagship feature is its failure mode. An unconstrained "ask me anything" sidebar inside a tutoring platform is the Bastani control arm shipped as a product. Solve-on-request is one paste away from every assigned problem. The dataset's forked hypothesis — 0.45 aligned versus 0.20 unconstrained — is, if anything, polite. The unconstrained mode does not merely underperform; under deadline pressure it converts the platform's practice data into fiction, because the mastery map now records the chat pane's competence. The usage signature is diagnostic and Camille should demand it up front: answer-seeking spikes in the hours before deadlines, hint ladders skipped to the bottom rung, session lengths collapsing as the term progresses. Exit-seeking has a shape, and the logs show it before the exams do.

**The reveal timer.** Subtler: a quizzing module with feedback set to instant-on-error. It looks pedagogically generous — why make students stew? — and it quietly amputates the testing effect, converting retrieval practice into recognition-and-restudy. This trap hides in a settings submenu and in every well-meaning instructor who dials difficulty down when students complain. The complaint is the mechanism working.

**The two-sigma purchase.** The institutional trap: buying the platform *as* the tutoring program — defunding the human corps, the supplemental instruction, the center itself, on the strength of a folklore number. VanLehn's near-parity result is real and narrow: step-based systems, well-structured domains, students who stay in the system. It says nothing about students who disengage entirely without a human relationship attached to their effort — and at a commuter university, that is most of the leak.

**Over-reliance as a habit.** The Poulidis working paper adds the longitudinal worry: learners with structurally unrestricted AI assistance developed reliance patterns that persisted when assistance was removed — structure beat willpower. College students, the population with the least imposed structure, are the natural worst case. [verify — unreviewed working paper, single domain; treat as directional, not established]

## What Happened in Four Sections of General Chemistry

The center licensed the platform. The license negotiation was mostly about switches.

The pilot ran in four sections of general chemistry. The step-level tutor earned its place in the stoichiometry unit. Error clustering showed forty percent of students failing at the same step — mole-ratio setup, not the arithmetic the instructors had assumed. The instructors retaught that step specifically. The subsequent platform data showed the cluster dissolving. Diagnosis by machine, teaching by humans, verification by machine: the loop this book keeps endorsing, running at section scale.

The spaced quizzing module, attempt-first enforced, did what the static practice-exam library never had: cumulative retention practice that followed each student's forgetting curve rather than the syllabus calendar. And a Tutor CoPilot-style experiment — session summaries routed to the center's human tutors before appointments — let a thin tutor corps arrive already knowing where each student's derivations had broken.

![Three-panel flow loop of the chemistry pilot — platform diagnoses (error clustering, mastery map), humans teach (reteach step, pre-brief tutors), platform verifies (cluster dissolution, exam performance)](images/21-ai-native-testing-and-tutoring-with-guardrails-fig-02.png)
*Figure 21.2 — The pilot loop: diagnosis, teaching, verification*

<!-- → [INFOGRAPHIC: Three-panel pilot structure — Panel 1: platform diagnosis layer (error clustering, mastery map). Panel 2: human teaching layer (retaught step, tutor pre-briefed by session summaries). Panel 3: platform verification layer (cluster dissolution, exam performance). Arrows connecting panels show the loop. Student should see that the platform's value in the pilot came from feeding human decisions, not replacing them.] -->

Week eleven, problem set nine: the usage signature appeared. Chat-pane queries tripling in the six hours before the deadline, paste-shaped inputs. The vendor's default chat was on in two sections — a configuration error; it had been contracted off. Those sections' practice-completion numbers were the best in the pilot. Their unit-exam mean came in four points under the guardrailed sections'. One configuration error had run the Bastani experiment locally, with the predicted sign. [verify — local n was small; the center treated it as directional, consistent with the literature, not a finding]

License renewed, with configuration written into the contract as deliverables. Chat constrained to coach mode — step hints, no full solutions, no answers to pasted assessed problems — verified by red-team paste-testing each term. Attempt-before-reveal locked on all quizzing, hint ladders with spent-attempt gating. The platform deployed alongside the human tutoring corps, with session summaries feeding tutors and the corps's budget explicitly protected in the same memo as the platform license. Evidence check fixed in advance: unassisted exam performance and gateway-course completion against three prior years, plus the usage-signature audit each term. Deadline-hour spikes treated as a fire alarm.

## The Phase Gate

**AI may** generate and schedule retrieval practice with enforced attempt-before-reveal; tutor at step level in checkable domains with laddered, attempt-gated hints; cluster errors and surface mastery maps to instructors; summarize sessions for human tutors and coach the tutor corps; and deliver content explanations outside the assessed workspace.

**The learner must** perform every retrieval before any reveal, attempt every step before any hint, and sit assessments with the platform out of reach.

**The instructor and center must** read the error maps and teach to them, keep the human tutoring layer funded and informed, and audit usage signatures for exit-seeking each term.

**Evidence that learning improved is** unassisted exam performance and gateway-course completion trending against multi-year baselines — together with practice data and exam data converging rather than diverging, since divergence is the −17 announcing itself.

| Role | What it covers |
|---|---|
| AI may | Generate and schedule retrieval practice with enforced attempt-before-reveal; tutor at step level in checkable domains with laddered, attempt-gated hints; cluster errors and surface mastery maps to instructors; summarize sessions for human tutors and coach the tutor corps; deliver content explanations outside the assessed workspace. |
| The learner must | Perform every retrieval before any reveal; attempt every step before any hint; sit assessments with the platform out of reach. |
| The instructor and center must | Read the error maps and teach to them; keep the human tutoring layer funded and informed; audit usage signatures for exit-seeking each term. |
| Valid evidence | Unassisted exam performance and gateway-course completion trending against multi-year baselines; practice data and exam data converging rather than diverging. |
| Does **not** count | Practice-problem completion; in-platform mastery percentages; minutes engaged; student satisfaction with the chat pane; any figure accompanied by the phrase "two sigma." |

## What Evidence to Demand

The assisted/unassisted gap. Practice performance versus proctored, tool-free exam performance, per section, per term. A widening gap is the Bastani signature in your own data — the single most important number this group produces, and vendors will not surface it voluntarily.

Reveal-timing and hint-ladder configuration, verified. Not the policy: the settings, plus red-team evidence. Paste an assessed problem into every input box. Record what comes back.

Usage signatures. Query timing against deadlines, hint-skip rates, session-length trends across the term. Exit-seeking has a shape, and the logs show it before the exams do.

The counterfactual honestly framed. Against what alternative is the platform being judged — the human tutor most students never get, or the nothing they currently have? Both comparisons are legitimate; only one belongs in the retention memo.

What does not count: practice-problem completion, in-platform mastery percentages, minutes engaged, student satisfaction with the chat pane, or any slide containing the phrase "two sigma."

## What Would Change My Mind

The chapter's architecture rests on the fork: guardrailed delivery preserves the mechanisms, unconstrained delivery hollows them. Replicated field evidence that unconstrained AI access produces no assisted/unassisted divergence in college populations — students self-regulating effectively without imposed structure — would collapse the fork and most of this chapter's contract language with it. The Poulidis direction makes me bet against, but it is one unreviewed paper in one domain. Conversely, evidence that even well-guardrailed AI tutoring fails to move course completion — not just exam scores — for the waitlisted population would tell me the binding constraint was never practice quality but human connection, and the budget should flow to Chapter 12's mechanisms instead.

## Still Puzzling

VanLehn's parity held in well-structured domains. The current generation of LLM tutors is being deployed confidently into ill-structured ones — essay feedback, proof strategy, design critique — where step-level correctness is undefined. Nobody has established what "step-based" even means there, let alone measured it.

The guardrailed arm in Bastani showed approximately zero exam effect — no harm, after spectacular practice gains. Where is the configuration that produces positive transfer? Is the ceiling a design problem, a dosage problem, or a sign that practice-time AI help, however disciplined, mostly cannot add what unassisted retrieval alone provides?

Tutor CoPilot helped the weakest human tutors most. The unmeasured question from Chapter 12 returns: are those tutors learning the moves, or renting them? The center's tutor corps is also a learning population, and nobody is tracking their fading curve.

## Further Reading

**VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46, 197–221.** This chapter's anchor: the 0.76/0.79 near-parity, its boundary conditions, and the deflation of the two-sigma legend — the three facts every ITS procurement meeting should open with.

**Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science*, 17, 249–255.** The testing effect's canonical demonstration, including the detail this group's design rule lives on: restudy feels better and performs worse at delay.

**Bastani, H., et al. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*.** The fork measured: +48/−17 unguardrailed, +127/≈0 guardrailed — the same product split by its settings.

**Wang, R. E., et al. (2024). Tutor CoPilot: A human-AI approach for scaling real-time expertise.** The +4/+9-point third option: AI amplifying the human tutoring layer instead of replacing it.

**Poulidis, N., Bastani, H., & Bastani, O. (working paper, SSRN). Over-reliance on AI assistance — evidence from chess academies.** Unreviewed and single-domain, flagged as such: the structure-beats-willpower result that makes default configurations, not student virtue, this chapter's unit of analysis.

---

## Exercises

**Warm-up**

1. (Low difficulty) *Tests understanding of the testing effect.* Explain in two sentences why students who reread material feel more confident than students who test themselves — and why the students who feel less confident nevertheless outperform on a delayed test. What does the answer reveal about what "practice" needs to require?

2. (Low difficulty) *Tests the two-altitude reading of the ITS literature.* VanLehn's review found ITS systems averaging d = 0.48 across diverse implementations, but d = 0.76 under specific conditions. Name the specific conditions. Explain why the gap between those numbers is not noise, and what it tells a purchasing committee that the average alone cannot.

3. (Low difficulty) *Tests the configuration-as-intervention insight.* The Bastani study used the same AI model in two arms of the experiment. Describe what differed between the arms and what the outcome difference was. Then explain in one sentence why "the guardrail was the intervention" is a more accurate description than "the AI was the intervention."

**Application**

4. (Medium difficulty) *Tests the reveal-timer trap.* An instructor pilots a spaced-retrieval quizzing platform and notices students complaining that the feedback is too slow — they want to know immediately whether they got the answer right. She adjusts the settings so the correct answer appears instantly after each attempt. Explain what this change does to the platform's mechanism, why the complaints were evidence the mechanism was working, and what she should tell students instead of adjusting the timer.

5. (Medium difficulty) *Tests the ninety-second test.* You are evaluating an AI tutoring platform for your department. Describe exactly how you would conduct a ninety-second substitution test, what you would paste into each input field, and what responses would tell you the platform is in each of the following states: (a) guardrailed correctly, (b) providing hints but not solutions, (c) providing full solutions on request.

6. (Medium difficulty) *Tests the usage-signature diagnostic.* A platform's administrator dashboard shows the following pattern for a section of introductory statistics: chat-pane query volume is low and steady for weeks one through ten, then triples in the six hours before each of the last three assignments. Problem-set completion rates are near 100%. Exam scores are flat against prior semesters. Apply the chapter's framework to explain what is likely happening, what you would verify, and what single configuration change you would make first.

**Synthesis**

7. (High difficulty) *Tests integration of all three rows, the phase gate, and the evidence standard.* Design the complete procurement and configuration policy for an AI tutoring platform at a commuter university with a large gateway-course failure rate and a chronically understaffed human tutoring center. Specify: what the platform is permitted to do in each functional area, what the contract must guarantee as a verifiable deliverable (not a policy statement), how the human tutoring corps relates to the platform, and what evidence at what intervals would allow the center director to conclude the platform helped — not just that students used it.

8. (High difficulty) *Tests the two-sigma critique and the honest counterfactual.* A vendor presents data showing that students using their AI tutoring platform outperformed the prior year's cohort by 0.6 standard deviations on gateway-course exams. The vendor's memo frames this as validation of the Bloom two-sigma promise. Identify every methodological and conceptual problem with this framing, explain what comparison would be needed to make the claim credible, and describe what the center should measure in year two to distinguish "the platform helped" from "something else changed."

**Challenge**

9. (Advanced) *Tests the guardrailed-arm ceiling and the still-puzzling question.* The Bastani guardrailed arm produced large practice gains but approximately zero transfer to the unassisted exam. This chapter interprets the finding as "no harm," but an alternative interpretation is that the guardrailed design itself is the ceiling — that coached stepping during practice, however well-constrained, cannot produce the independent retrieval capacity that unassisted practice builds. Design a study that would distinguish between these two interpretations. Specify the conditions, the populations, the timing of assessments, and the result pattern that would confirm each account. Then propose a modified platform design — one specific change to the guardrailed tutor's behavior — that your study's framework would let you evaluate.

## Prompts

### Figure 21.1 — The configuration fork: guardrailed vs. unguardrailed
Build a two-panel comparison, each panel a small line chart with x-axis "weeks in platform" and y-axis "performance score." Left panel titled "Guardrailed (converge)": two lines, practice rising to +127% and exam tracking flat at ~0, ending close together (converging). Right panel titled "Unguardrailed (diverge)": two lines, practice rising to +48% and exam falling to -17%, ending far apart (diverging) — highlight the falling exam line as the Bastani signature. Annotate each line's terminal value. Use a shared y-scale across panels so the divergence is visually comparable. Caption both panels: same model, same students, same material, split by one configuration setting. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 21.2 — The pilot loop: diagnosis, teaching, verification
Build a three-panel left-to-right flow with a return loop arrow closing back to the start. Nodes: "Platform diagnoses (error clustering, mastery map)" → "Humans teach (reteach step, pre-brief tutors)" → "Platform verifies (cluster dissolution, exam performance)" → loop back. Distinguish the machine panels (1 and 3) from the human panel (2) by fill so the alternation reads instantly. Label the connecting arrows to show data feeding human decisions and results feeding back. Annotate that the platform feeds human decisions rather than replacing them. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 21.3 — Tutoring effect sizes vs. hinge and human-tutor benchmark
Build a horizontal dot/lollipop plot, value range 0 to ~0.85 in Cohen's d. Rows sorted descending by value: "Human-tutor benchmark" 0.79, "ITS, step-level high fidelity" 0.76 (highlighted), "Practice testing" 0.54, "Intelligent tutoring systems" 0.48, "Technology with college students" 0.42. Two vertical reference lines: one at d = 0.40 labeled "0.40 hinge," one at d = 0.79 labeled "human-tutor benchmark." Zero baseline at left. Annotate the near-parity gap between step-level ITS (0.76) and the human benchmark (0.79). Label each dot with its value. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

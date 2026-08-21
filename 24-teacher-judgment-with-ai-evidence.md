# Chapter 24 — Teacher Judgment With AI Evidence
*The number is real. The thing it measures is not what the vendor said.*

Teacher estimates of achievement (1.29) and teacher clarity (0.75): two high-band influences about the quality of teacher judgment and teacher communication. The first is a measurement finding — teachers' estimates of their students' achievement track reality remarkably well — not an intervention. The second is a design property of instruction that can be engineered. AI fits both as an evidence amplifier: better data for the estimates, faster drafting and checking for the clarity. The medium substitution risk is automation bias — judgment that slowly becomes ratification of the dashboard, eroding exactly the calibrated expertise the 1.29 was measuring.

**Group Profile: Teacher Judgment With AI Evidence**

| Profile | Detail |
|---|---|
| Influences in this group | 2 of Hattie's 252 |
| Effect-size range | d = 0.75 to 1.29 (weighted average 1.02) |
| Hattie band | High |
| AI feasibility | AI-augmented |
| Human irreducibility | High |
| Substitution risk | Medium |
| Cognitive-work conflict | None |
| Members | Teacher estimates of achievement (rank 3, d = 1.29); Teacher clarity (rank 24, d = 0.75) |

The vendor's onboarding webinar makes the pitch directly: "Teacher estimates of achievement is the number three influence on Hattie's list, with an effect size of 1.29. Our dashboard operationalizes it."

Dana Whitfield runs the eighth-grade data team at a middle school of about 700 students. She is watching the webinar because the district has just pushed an update to the learning management system — a new early-warning module that assigns every student a color-coded risk score, refreshed nightly from attendance, quiz results, and assignment completion. The pitch sounds rigorous. Effect size 1.29. Number three on a list of 252.

The sentence contains one true number and one large category error.

The true number: d = 1.29 is indeed what appears on the 2018 list. The category error: the vendor is treating a measurement of what teachers already know as a lever the dashboard can pull. These are not the same kind of object, and mistaking one for the other is what makes this pitch so common and so wrong. If a school could purchase 1.29 standard deviations of student improvement by buying an LMS module, that effect size would be implausible on its face in field research — larger than almost anything in the experimental literature, delivered by software overnight. Kraft (2020) notes that real intervention effects of that magnitude do not exist in controlled studies. The 1.29 does not describe a promised outcome. It describes the value of something the teacher already has.

Dana's team is split on the module. Two teachers love it — it caught a slow grade slide they had missed. A veteran teacher refuses to open it, saying she already knows her students and the colors will second-guess her. The principal wants a recommendation by December: should risk scores appear automatically in every teacher's gradebook view?

This chapter is Dana's answer.

---

## What the Group Is

High band, **AI-AUGMENTED**, high human irreducibility, medium substitution risk, no cognitive-work conflict.

In plain language: AI can genuinely help here, because the work involves gathering and weighing evidence, and machines are good at gathering. But the thing the effect size actually describes — a teacher's accurate, contextual knowledge of each student — cannot be transferred to a tool. There is no cognitive-work conflict because the cognitive work in question is not the student's; it is the teacher's. The substitution risk is medium rather than high because the danger is quiet and gradual: not a tool doing students' thinking for them, but a dashboard slowly doing teachers' judging for them.

| Influence | d (rank) | Mechanism | Provenance note | AI role | Human-irreducible component |
|---|---|---|---|---|---|
| Teacher estimates of achievement | 1.29 (rank 3) | A measurement of existing knowledge — how accurately a teacher already knows where each student stands — not an intervention | Südkamp, Kaiser & Möller (2012): 75 studies, mean r = .63, converted to d | Aggregate and surface evidence; flag slow drifts; maintain calibration records | The accurate, contextual estimate itself, strongest where data is thinnest |
| Teacher clarity | 0.75 (rank 24) | A design property of instruction — goals, explanations, examples, practice, and checks that line up — not a talent for plain talk | Fendick (1990) dissertation, r ≈ .35 [verify]; converges with the explicit-teaching literature | Draft learning intentions, success criteria, worked examples and non-examples | Live delivery and in-room checking of understanding |

---

## The Two Rows

**Teacher estimates of achievement (d = 1.29) — rank 3.** This is the cleanest case in the whole book of a number that does not mean what it appears to mean. The figure is not the payoff of an intervention anyone can buy. It derives from research on judgment *accuracy*: Südkamp, Kaiser, and Möller (2012) meta-analyzed 75 studies of how well teachers' judgments of student achievement track measured achievement, and found an average correlation of r = .63 — substantial, far from perfect, varying widely with how the judgment was elicited. The d = 1.29 comes from converting that family of correlations into a standardized-difference metric. The influence describes how much teachers already know about their students. It is a measurement of existing knowledge, not a lever a school can pull.

**Teacher clarity (d = 0.75) — rank 24.** This figure traces to a single unpublished doctoral dissertation — Fendick (1990) — which defined clarity as four components: organization, explanation, examples and guided practice, and assessment of student learning, and reported a correlation of roughly r = .35 [verify — full dissertation text not obtained; claims here are limited to what secondary analyses report]. The thin provenance is worth knowing, but the construct converges with the much larger explicit-teaching literature: clarity is a design property of instruction — goals, explanations, examples, practice, and checks that line up — not a talent for talking plainly.

One disambiguation before proceeding: teacher *estimates* (how accurately teachers know their students) is a different influence from teacher *expectations* (beliefs that can become self-fulfilling, which sit lower on the list). One is a measurement story; the other is a prophecy story. This chapter is about the first.

![Horizontal bar chart of two influences against the 0.40 hinge: teacher estimates of achievement at 1.29 near the top of the whole list and teacher clarity at 0.75, both far in the High band](images/24-teacher-judgment-with-ai-evidence-fig-03.png)
*Figure 24.3 — Two influences against the hinge*

---

## Why It Works: The Most Valuable Diagnostic Instrument in the Building

Why would teacher knowledge of students be associated with the list's third-highest effect size?

Because accurate judgment is the raw material for nearly every consequential decision in a school. Who gets which task tomorrow. Who is placed in which group. What feedback means. When to reteach. When to refer. A teacher who knows precisely where each student stands can aim instruction; a teacher working from a blurry picture aims at the average. The d = 1.29 is not a promise about what teaching can do — it is an account of how much variation in a teacher's diagnostic accuracy corresponds to variation in outcomes. The more accurately you know your students, the better you can serve them. This is not surprising. It is important to quantify.

The honest complication is that teacher judgment, while good on average, is uneven. The r = .63 hides wide variation between teachers and contexts — what Kahneman, Sibony, and Sunstein call noise. And here the empirical anchor for the AI question is unusually clean.

Eegdeman, Cornelisz, van Klaveren, and Meeter (2022) ran a head-to-head in Dutch vocational education: who predicts student dropout better, teachers or machine-learning models? At the start of the program, *teachers won* — they identified very-high-risk students who were invisible in the data, because their knowledge was relational and contextual. Once first-period grades arrived, the algorithms caught up and then outperformed the teachers on average. A combined ranking — teacher judgment plus model — showed better sensitivity than either alone, though not better precision.

One study, one context. Treat it as an existence proof of complementarity, not a law. But the shape of the result is exactly what this group's classification predicts: the teacher's contribution is strongest precisely where the data is thinnest — new students, transitions, life events, things no LMS captures — and the machine's contribution grows as structured evidence accumulates. They are not competing for the same information. They are processing different kinds.

![Multi-line trend chart across the school year: teacher judgment starts high and plateaus, the model starts low and rises steeply to overtake at the first grading period, and the combined ranking runs above both after that crossover](images/24-teacher-judgment-with-ai-evidence-fig-01.png)
*Figure 24.1 — Teacher-model complementarity over the school year*

<!-- → [DIAGRAM: Teacher-model complementarity timeline — X-axis: time into the school year; Y-axis: prediction accuracy for student risk. Two lines: teacher judgment (starts high, plateaus) and model (starts low, rises steeply). A combined-ranking line runs above both after the first grading period. The key label: "teacher wins here" marks the information-poor start; "model catches up here" marks when structured evidence accumulates. The visual makes the timing asymmetry — and the complementarity — legible.] -->

---

## What AI Can Safely Do

AI has a real role here, and it is evidence work.

**Aggregate and surface.** Pull attendance, assignment trajectories, and assessment results into one view per student, so the teacher's judgment runs on more complete information than she could assemble alone from 150 gradebook rows.

**Flag trajectories, not verdicts.** Detect slow drifts — the student whose quiz average has declined four points a week for six weeks — that no human watching 150 students will reliably catch in September. The flag arrives with the underlying evidence: the chart, the pattern, the missing-assignment list. The teacher decides what it means.

**Support clarity drafting.** On the teacher-clarity side, a language model can draft learning intentions and success criteria at several grain sizes, generate worked examples and non-examples, and standardize goal language across a course. The teacher edits against yesterday's misconceptions; the delivery and the live checking of understanding stay in the room.

**Create calibration data.** If teachers record their own estimates before seeing model output, the system can track over time where each teacher's judgment is sharp and where it drifts — making judgment improvement a measurable professional skill rather than an invisible one.

The boundary runs at the same place in this group as everywhere: AI supplies the evidence layer; the teacher supplies the judgment. The categories are cleanly separable here in a way they are not in Chapter 4's metacognitive gate or Chapter 13's self-regulation loop. That is why the substitution risk is medium, not high. The risk is behavioral, not structural — it depends on how the tool is configured and how teachers use it.

---

## The Substitution Trap: An Installment Plan

The trap in this group is teacher-side, not student-side. Nothing here lets a student outsource thinking. What can be outsourced — invisibly, comfortably, one nightly refresh at a time — is the teacher's estimate itself.

The mechanism is automation bias. A dashboard that presents *verdicts* (a red badge, a risk percentile) instead of *evidence* (the attendance record, the quiz trajectory) invites teachers to adopt the verdict as their own judgment. At first the teacher checks the score against what she knows. Then the score arrives first and anchors what she knows. Then she stops forming an independent estimate at all, because the dashboard already does that.

The capacity the d = 1.29 documents — the most valuable diagnostic instrument in the building — atrophies from disuse. And when the model mislabels a student, no one is positioned to contradict it.

Remember which direction the Eegdeman result points: the teachers beat the model exactly at the information-poor start, the moment when a new student most needs someone to see what the data cannot. If automation bias has already eroded the teacher's independent judgment by October, that advantage is unavailable precisely when it matters most.

The practical test for any tool in this group is one question: **does it require the teacher to record an independent judgment before revealing its own?** Tools that skip this step are not augmenting teacher judgment. They are replacing it on an installment plan, and the final payment is due when something goes wrong.

---

## One Semester, Two Students, One Policy

Dana's team piloted the early-warning module under rules the team wrote itself, before the principal's December deadline.

The pilot's governing question was stated explicitly: does this make our estimates better, or does it make them disappear?

In week six, the module flagged a student whose math quiz scores had drifted down so gradually that neither his math teacher nor his advisory teacher had registered it. The flag came with the underlying evidence — the trajectory chart, the missing-assignment list — and the math teacher, looking at it, said: "I'd have caught this in November. This is September." That is the augmentation case in one sentence. The machine saw a slow pattern early; the human decided what it meant and what to do.

In week nine, Dana noticed the data-meeting conversation had changed. Teachers had begun opening the meeting by reading dashboard colors aloud — "I've got four reds and a yellow" — instead of describing students. One teacher admitted she had stopped writing her own pre-meeting notes because the module "already ranks them." The team had crossed the gate without noticing. The tool's output was becoming the estimate rather than informing it.

Two students made the problem concrete. A quiet high performer was flagged red purely from an absence artifact — a recorded family emergency that the LMS had no way to interpret. A student in real trouble showed green because he submitted everything: late, minimal, and copied. The teachers knew both stories. The model knew neither. And because the pre-meeting notes had stopped, those stories had no formal channel to the table.

![Side-by-side comparison of two week-nine cases: a quiet high performer the model flags red from an absence artifact while the teacher knows the flag is wrong, and a struggling student the model shows green from completion while the teacher suspects copied work](images/24-teacher-judgment-with-ai-evidence-fig-02.png)
*Figure 24.2 — The two-student audit: where model and teacher disagree*

<!-- → [DIAGRAM: Two-student audit — Side-by-side comparison of model output versus teacher knowledge for the two week-nine cases. Left student: model flags red (absence artifact); teacher knows this is incorrect. Right student: model shows green (assignment completion); teacher suspects this is incorrect. The diagram makes concrete why teacher judgment and model output must remain distinct — and why their disagreement is the most valuable signal in the system.] -->

**The conditions, written into the recommendation.** Before each grading cycle, every teacher logs a predicted quartile per student *before* model flags are revealed — the independent-judgment rule. Flags must always display the underlying evidence, never a bare score, and teachers may annotate or contest any flag. Teacher–model disagreements are the standing first agenda item of every data meeting — a disagreement is information, not a tie the model breaks. At semester's end, the team reviews calibration: where the model beat the teachers, where the teachers beat the model, whether teacher estimates are getting sharper. The vendor's auto-display of risk badges in the default gradebook view was turned off.

---

## The Phase Gate

**AI may** aggregate evidence about each student — attendance, work patterns, assessment trajectories — flag risk patterns and slow drifts with the underlying evidence attached, draft learning intentions, success criteria, and worked examples for the teacher to edit, and maintain records of teacher estimates over time so calibration can be examined.

**The teacher must** form and record an independent estimate of each student's standing before seeing any model output, synthesize machine flags with relational and contextual knowledge the data cannot contain, treat disagreement with the model as an investigation rather than a deferral, and personally deliver and check instructional clarity in the room.

**Evidence that learning improved is** documented, revisable teacher estimates that grow more accurate over time against subsequent student performance; earlier and better-targeted interventions traceable to flags a teacher confirmed and acted on; and student outcomes on independent assessments — never the count of flags generated, dashboard logins, or the model's own accuracy statistics reported in isolation from teacher judgment.

---

## The Evidence Check

For any tool in this group, four demands.

**Calibration improvement.** Teachers' recorded estimates, compared against later measured achievement, track more closely after a year with the tool than before it. This is measurable with nothing more than a spreadsheet and the independent-judgment rule.

**Earlier accurate intervention.** Students who needed support were identified and reached sooner than the school's historical baseline — and the identifications were confirmed by outcomes, not just by flag volume.

**Preserved disagreement.** Teachers still contradict the model, and a meaningful fraction of those contradictions prove correct. If teacher–model disagreement falls to zero, that is not a sign the model is right. It is a sign no one is checking.

**Student learning on unassisted, external measures** — end-of-course assessments the tool does not touch — improving for the flagged-and-served population.

What does not count: flag volume, dashboard logins, model accuracy statistics reported in isolation, teacher satisfaction with the interface, or assignment-completion rates for students the tool flagged as risks.

---

## What Would Change My Mind

A well-designed multi-site study showing that teachers who work with verdict-style dashboards — no independent-estimate requirement, scores shown first — maintain or improve their judgment accuracy over two or more years, relative to teachers using evidence-style displays, would force a rewrite of this chapter's central warning. The atrophy argument rests on automation-bias research from other fields plus one prediction study; if classroom-scale evidence showed teacher judgment is robust to verdict-first design, the independent-judgment rule could be reframed as optional hygiene rather than a gate condition.

## Still Puzzling

- Eegdeman et al. found teacher-plus-model rankings improved sensitivity but not precision. What is the right operational recipe for combining the two — and does anyone have replicated evidence for one in K-12 settings?
- Teacher estimates and teacher expectations interact in ways the two separate Hattie influences conceal: does seeing a model's risk label change what a teacher expects, and does that expectation then change the student? No study located cleanly separates the loop.
- LLM-based "data chat" features are arriving in LMS products faster than anyone is evaluating them against teacher baselines. What would a fair benchmark for those features even look like?

## Further Reading

- **Südkamp, A., Kaiser, J., & Möller, J. (2012). Accuracy of teachers' judgments of students' academic achievement: A meta-analysis. *Journal of Educational Psychology*, 104, 743–762.** The source under the headline number: 75 studies, mean r = .63, and the moderator analysis showing judgment accuracy depends on how the judgment is asked for.
- **Eegdeman, I., Cornelisz, I., van Klaveren, C., & Meeter, M. (2022). Computer or teacher: Who predicts dropout best? *Frontiers in Education*, 7:976922.** The cleanest head-to-head of teacher versus algorithmic prediction — and the timing result (teachers win early, models win late) that should shape every early-warning deployment.
- **Kahneman, D., Sibony, O., & Sunstein, C. R. (2021). *Noise: A Flaw in Human Judgment*.** Why judgments vary between professionals looking at the same evidence, and the decision-hygiene practices this chapter's case design borrows.
- **Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49, 241–253.** The fastest vaccine against vendor effect-size citation — including this chapter's opening example.
- **Agrawal, A., Gans, J., & Goldfarb, A. (2018). *Prediction Machines*.** The economic argument that when prediction gets cheap, human judgment becomes more valuable, not less — the theoretical frame this group's classification rests on.

---

## Exercises

### Warm-up

**1.** The chapter claims the vendor's pitch contains "one true number and one large category error." Identify the true number, identify the category error, and explain in two sentences why a number describing existing teacher knowledge cannot function as a lever a dashboard pulls. *(Difficulty: low. Tests: distinguishing a measurement of existing capacity from an intervention effect.)*

**2.** The Eegdeman study found teachers beat the model at the start of the year, then the model caught up. The chapter says this is "exactly what the group's classification predicts." Explain in two sentences what the classification predicts about when teacher judgment is most valuable and when AI evidence becomes most valuable — and why the two are complementary rather than competing. *(Difficulty: low. Tests: reading the teacher-model complementarity through the timing result.)*

**3.** The chapter defines the substitution trap as "an installment plan." What is being paid in installments, what is the final payment, and why does the payment come due specifically when something goes wrong? *(Difficulty: low. Tests: understanding the automation-bias mechanism and its consequence at the moment of model error.)*

### Application

**4.** A district is deploying an early-warning system that shows teachers a nightly "student risk score" — a single number from 0–100 — in the gradebook sidebar. The vendor argues this is simpler than showing the underlying data and reduces cognitive load. Using the verdict-versus-evidence distinction and the independent-judgment rule, write the two conditions you would require before allowing the sidebar to remain in the default view — and explain why "simpler" and "safer" point in opposite directions here. *(Difficulty: medium. Tests: applying the verdict/evidence distinction to a specific UI design choice.)*

**5.** Run the calibration study the chapter recommends. Before your next significant assessment, privately record a predicted quartile (top, second, third, bottom) for each student. After results arrive, compute your accuracy and examine the misses: which students did you overestimate, which did you underestimate, and do the errors cluster by any visible pattern? Write a one-paragraph reflection on what you learned about your own judgment that a risk-score dashboard could not have shown you. *(Difficulty: medium. Tests: operationalizing the d = 1.29 construct in the reader's own practice and discovering the noise in their own judgment.)*

**6.** Dana's pilot conditions include a rule that teacher–model disagreements become the first agenda item of every data meeting. A colleague objects: "That will make meetings longer and feel adversarial." Write the two-paragraph response that explains why disagreement is the most valuable signal in the system — and proposes a specific protocol that makes disagreement-review efficient rather than adversarial, using the two week-nine students as the concrete case. *(Difficulty: medium. Tests: defending the disagreement-as-information principle and designing the protocol that operationalizes it.)*

### Synthesis

**7.** Compare the substitution risk in this group (teacher judgment eroded by automation bias) with the substitution risk in Chapter 13's group (student self-regulation eroded by outsourcing). Both involve a human capacity that atrophies through disuse when AI performs the role. What is structurally different about the two erosion processes — specifically, what makes teacher-judgment atrophy harder to detect than self-regulation atrophy — and what evidence check catches each earliest? *(Difficulty: high. Tests: cross-chapter synthesis of two capacity-atrophy risks with different subjects and different detection windows.)*

**8.** The "Still Puzzling" section raises the possibility that seeing a model's risk label changes what a teacher expects — and that expectation then changes the student. Design a study that would cleanly separate the estimation effect (accuracy improvement) from the expectation effect (self-fulfilling prophecy) in a school using an early-warning system. Specify the conditions, the measures for each effect, the timeline, and what result would cause you to require additional controls on how risk labels are displayed. *(Difficulty: high. Tests: designing an experiment that separates two theoretically entangled effects and produces a decision rule.)*

### Challenge

**9.** You are Dana, presenting to the principal in December. The vendor has attended the meeting and disputes the independent-judgment rule: "Our platform's accuracy is 87% on risk identification. Requiring teachers to form independent estimates before seeing our output introduces unnecessary cognitive friction and delays intervention for at-risk students. The research says teacher judgment is variable; our consistency is the point." Using the Südkamp meta-analysis, the Eegdeman timing result, the automation-bias mechanism, and the two week-nine students, write the three-minute presentation that responds to each of the vendor's claims — and closes with the one question the principal should ask the vendor before deciding whether to adopt the independent-judgment rule. *(Difficulty: challenge. Tests: integrating the chapter's complete empirical and mechanism framework into an adversarial institutional argument, under time pressure, for a decision-maker who is not a researcher.)*

## Prompts

### Figure 24.1 — Teacher-model complementarity over the school year
Build a horizontal timeline / multi-line trend chart with x-axis "time into the school year" and y-axis "prediction accuracy." Plot three lines: teacher judgment (starts high, plateaus), model (starts low, rises steeply, overtakes teacher at the first grading period), and a combined ranking (runs above both after the first grading period). Mark four timeline points along the bottom: "Information-poor start (teacher judgment highest)," "First grading period (model overtakes — crossover)," "Mid-year (combined runs above both)," "Year-end (model highest single signal)." Annotate the crossover point explicitly. Use distinct line styles per signal with a legend. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 24.2 — The two-student audit: where model and teacher disagree
Build a two-case side-by-side comparison panel. Left case "Quiet high performer": two rows — "Model: red flag (absence artifact)" and "Teacher: knows the flag is wrong" (highlight the teacher row). Right case "Struggling student": aligned rows — "Model: green (assignment completion)" and "Teacher: suspects copied work" (highlight the teacher row). Shared axis label spanning both: "Model output vs. teacher knowledge." Visually oppose the model row and teacher row within each case so the disagreement reads as the signal. Annotate that the disagreement is the most valuable signal in the system. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 24.3 — Two influences against the hinge
Build a horizontal bar chart, two bars, value range 0 to ~1.4 in Cohen's d. Bars: "Teacher estimates of achievement" = 1.29 (highlighted), "Teacher clarity" = 0.75. Zero baseline at left. Vertical reference line at d = 0.40 labeled "0.40 hinge"; both bars sit far above it in the High band. Sort descending. Annotate that estimates sits near the top of the entire 252-influence list. Label each bar with its value. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

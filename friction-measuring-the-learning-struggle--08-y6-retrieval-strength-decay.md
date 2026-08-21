# Chapter 8 — Y6: Retrieval Strength Decay Signature

*Genuine learning shows the spacing effect — performance holds up better after distributed practice than after massed practice. Borrowed certainty shows monotonic decay. The decay curve shape is the signal.*

---

Two students score 85% on a quiz the day after the unit ends.

Three weeks later — no announcement, no review session, no extra study — the instructor gives a short five-item quiz on the same material. Student A scores 78%. Student B scores 42%.

Same content. Same teacher. Same starting score. What the first quiz could not show is the shape of what each student walked away with. Student A walked away with storage. Student B walked away with a fluent moment. The artifact on day one lied by omission — not because it was wrong, but because it measured the wrong thing. A single quiz measures how accessible something is *right now*. The decay curve over three weeks measures how thoroughly it was encoded. Those are different quantities, and only one of them is learning.

This is also the chapter where the storage-retrieval distinction from earlier in the book stops being abstract and becomes operational.

---

## Two strengths, not one

The vocabulary matters here, so let me be precise about it. Robert and Elizabeth Bjork gave us, in 1992, what they called the New Theory of Disuse — a two-component model of memory that resolves a paradox that had been bothering researchers for decades.

The paradox: why does cramming work so well on Tuesday and fail so badly by Friday? Why does re-reading feel like studying but produce almost no durable retention? Why does a student who scores 90% on a unit exam score 40% on a cumulative final covering the same material six weeks later?

The answer requires two separate quantities. **Retrieval strength** is how accessible something is right now — how easily it comes to mind given the current context and cues. Retrieval strength is sensitive to recency. It spikes after review. It decays fast. **Storage strength** is how thoroughly something is encoded — how robust the underlying trace is. Storage strength is slow to build and slow to decay. Once something has genuinely high storage strength, it stays accessible over long delays even when retrieval strength has temporarily dropped.

The counter-intuitive prediction of the Bjork-Bjork model — and this is the result that explains almost everything in this chapter — is that high retrieval strength and high storage strength are not the same thing, and the conditions that maximize one can actively suppress the other. Cramming maximizes retrieval strength on the day of the exam and builds almost no storage strength. Spaced retrieval practice produces retrieval strength that *feels* lower during studying — the material is harder to access because it has been away for a while — and builds dramatically more storage strength in the long run.

The AI-assisted student lives entirely in the retrieval-strength world. Every time she asks the AI, the material is fluently in front of her. Her retrieval strength is high. Her storage strength is near zero, because she has never attempted to retrieve anything herself. The first quiz, taken the day after the AI delivered a clean explanation, reflects her high retrieval strength. The three-week-later quiz reflects her storage strength. That is why the second number is the honest one.

---

## What the experiments show

Hermann Ebbinghaus measured his own forgetting curve in 1885 by memorizing 2,300 nonsense syllables — strings like ZOL, DAX, BEK, deliberately stripped of prior associations — and re-testing his retention at varying delays. He worked alone, self-experimenting for years, against the prevailing view that memory was a private mental event not amenable to scientific measurement. He showed that memory could be treated as the residue of measurable behavior, and the curve he traced — fast initial drop, slow later decline, roughly exponential — has been reproduced across a century of subsequent work. Every textbook figure of the forgetting curve is his data, retraced. The spaced-repetition software that millions of students use today sits on top of his nonsense syllables.

The forgetting curve is the baseline. What matters for Y6 is the deviation from it.

Roediger and Karpicke's 2006 experiment is the cleanest single demonstration. Two groups of students studied a brief science passage. Group one restudied it four times. Group two studied it once, then attempted to retrieve it three times — recall what they had read, write it down, no looking back. On an immediate test, the restudy group scored slightly higher. On a one-week test, the retrieval group held substantially more. The crossover is the point: both groups started in the same place, and the decay curves diverged inside a week.

Karpicke and Roediger sharpened this in 2008: repeated retrieval produced 80% retention at one week; repeated restudy produced 33%. Same total study time. Same starting material. Two-and-a-half-fold difference in storage a week later. Adesope, Trevisan, and Sundararajan's 2017 meta-analysis of 118 practice-testing studies, covering more than 15,000 participants, found an effect size of approximately *g* = 0.6 — large by educational research standards, consistent across age groups, materials, and delay intervals.

The mechanism runs through the same failure dynamic that Chapter 6 described for calibration. Retrieval practice produces failures. The student tries to remember, almost remembers, sometimes fails entirely, sometimes recovers the answer through effort. Each failure is a cue that something is not yet stored, and that cue drives subsequent encoding. Restudy does not produce failures. The student reads, the words feel familiar, the cue says *stored*, and the encoding cycle is skipped. High retrieval strength on the day, almost nothing a month later.

AI-assisted study amplifies the restudy problem. The explanation is not just fluent — it is maximally fluent, organized, complete, free of the awkward half-formed language that characterizes a student's own struggling summary. The student processes it without effort. The fluency cue fires. The encoding cycle is skipped entirely. She emerges with retrieval strength and almost no storage.

The spacing effect compounds this. Cepeda and colleagues, in a 2008 study that I want to describe carefully because it makes a precise quantitative claim, showed that the optimal gap between practice sessions scales with the desired retention interval at roughly 10–20%. If you want students to remember something in six months, space practice three to six weeks apart. If you want them to remember in two weeks, space practice one to three days apart. Any non-zero spacing beats massing the same total practice time into one session. The spacing effect is one of the most replicated findings in cognitive psychology and it is not seriously contested.

What the AI-assisted student lacks is not just retrieval practice — she also lacks spacing. She asks the AI when the assignment is due. The information comes in a mass. If she asks again later, it comes in another mass. The gaps between sessions are not retrieval events. They are re-explanation events. The spacing benefit requires the student to attempt retrieval during the gap; re-reading an AI explanation during the gap provides none of it.

---

## What the two signatures look like

The genuine Y6 signature is a decay curve that bends gently. Performance at long delay is substantially better than a naive forgetting-curve prediction from immediate performance would suggest. The drop from day one to week three is modest. The drop from week three to week six is smaller still. Students tested on material from four weeks ago, with no warning, score within ten or fifteen points of what they scored when the material was current. On a cumulative final, performance on early-unit material is not catastrophically worse than performance on late-unit material. The curve flattens because storage was built, and storage is slow to decay.

When the curriculum provides distributed practice — and many do, structurally, because spiraled curricula revisit earlier concepts in later units — the spacing benefit shows up as a signature in its own right. Students who encountered the earlier material again, even briefly, in a later context retain it better at end-of-term than students who did not. The benefit is visible in aggregate across the class. It is also visible per student: the students who show the spacing benefit are the students who engaged with the re-encounter as a retrieval event, not as a re-reading event.

The borrowed-certainty signature is a cliff. Performance collapses between the immediate quiz and the first delayed probe, and is near floor by the second. The decay is steep and monotonic. What makes this diagnostic is the contrast with the student's current-unit performance, which stays fine — the AI is still available, the fluency is still high, the retrieval strength is still there. Ask a question from four weeks ago and the bottom falls out. The storage was never built.

The most diagnostic single observation in the borrowed-certainty signature is this: current-unit performance and legacy-item performance diverge, and the divergence grows over the term. In week two, the gap might be 15 points. By week ten, it might be 50. The current-unit line holds flat or rises. The legacy line drops through the floor. No single quiz shows this. The two lines together do.

<!-- → [CHART: two-panel line chart — left panel shows "genuine engagement" student: current-unit performance (solid line) and legacy-item performance (dashed line) tracking within 10–15 points of each other across 10 weeks. Right panel shows "borrowed certainty" student: current-unit performance (solid line) staying high while legacy-item performance (dashed line) drops steeply and diverges by week 10. The growing gap in the right panel is the Y6 signal.] -->

---

## How to observe this without any new infrastructure

The cleanest implementation — and the one I recommend starting with — is the embedded legacy item. On each weekly quiz, include two to four questions drawn from material covered three or more weeks earlier. Do not announce which questions are legacy and which are current. Score them in a separate column. The gap between current-unit and legacy performance, tracked per student across weeks, is the Y6 signal.

One design constraint matters: difficulty matching. If the legacy items are systematically harder than the current items, a low legacy score might reflect difficulty rather than decay. Use items from the same item bank as the original assessment, with comparable past-class success rates. When in doubt, embed more legacy items rather than fewer — the average rate stabilizes faster, and item-level difficulty noise washes out.

A second design constraint: the legacy items have to be silent. If you announce a review session before each quiz, the spacing effect kicks in for the announced items — which is pedagogically useful — but the decay-probe signal is contaminated. You will have measured prepared retention, not natural decay. The diagnostic signal requires the items to be unannounced.

The instrument-is-the-intervention property is worth noting explicitly. Embedding legacy items in quizzes both measures decay and produces spacing. The same questions do both jobs. Students who encounter a legacy item and struggle with it are generating a retrieval failure, which drives encoding. The measurement is also remediation. This is the most elegant property of the Y6 observation method.

For a more structured three-point decay measurement, test the same item bank at immediate, two-week, and six-week delays. More work than the embedded approach, but it produces a cleaner curve per concept. Useful for the specific material where you most need to know whether storage is being built.

For courses with cumulative finals that already exist, the Y6 move requires no new assessment design at all. Score the final by unit of origin — not as a single percentage, but as a per-unit retention number. Some units will hold up. Some will collapse. The unit-level data is usually already in the exam; it has just been aggregated away. Stop aggregating.

<!-- → [TABLE: implementation comparison — rows: embedded legacy items, three-time-point testing, cumulative final by unit, spaced homework restructure, student self-test prompt. Columns: setup cost, ongoing cost per quiz, diagnostic precision, also serves as intervention (yes/no), works with existing materials (yes/no). Practitioner should see at a glance that embedded legacy items score high on low cost, moderate precision, yes-intervention, and yes-existing-materials.] -->

---

## A worked example: the history instructor and the unannounced probe

A high school history instructor teaches a year-long survey course. She adds three legacy items to each weekly quiz starting in week four — questions drawn from material covered three to six weeks earlier. She does not announce this. She scores legacy items as a separate gradebook column.

By week eight she has four weeks of data on each student.

Student F's current-unit performance has hovered around 78–82% all term. Legacy-item performance: week 4 = 75%, week 5 = 73%, week 6 = 70%, week 7 = 72%, week 8 = 71%. The curve is almost flat. Current-unit and legacy scores are within five points consistently. Genuine Y6 signature. She will not worry about F.

Student G's current-unit performance has hovered around 80–85% all term — artifacts look fine, participation looks fine. Legacy-item performance: week 4 = 65%, week 5 = 52%, week 6 = 38%, week 7 = 32%, week 8 = 25%. The legacy curve is in free fall while the current-unit performance holds steady. The gap between current and legacy was 20 points in week 4. It is 60 points in week 8. G is performing well on whatever is directly in front of her. She is retaining almost nothing. The existing gradebook has actively concealed this all term. The legacy column reveals it.

Student H's current-unit performance has been variable, 60–72% — mediocre, concerning by the artifact alone. Legacy-item performance: week 4 = 50%, week 5 = 55%, week 6 = 62%, week 7 = 65%, week 8 = 68%. The legacy curve is *rising*. H is doing cumulative review on her own and is retaining the material better than her current-week quiz scores suggest. The legacy data reveals genuine Y6 in a student whose surface artifact has been weak. The conversation here is encouragement, not concern.

The instructor does not change any grades. She has different conversations. She invites G in for office hours and shows her the two-column gap — not the gap in artifact quality, which doesn't exist, but the gap between current-unit and legacy performance. The conversation does not start with "I think you've been using AI." It starts with "I notice that the material from earlier this term doesn't seem to be sticking. Let's talk about how you're studying." The data anchors the conversation. The student can see what the instructor sees.

That conversation is the instrument working as intended.

---

## What a platform adds

The platform-side version of Y6 is spaced repetition scheduling — most precisely, the FSRS algorithm (Free Spaced Repetition Scheduler), which emerged from the Anki ecosystem over the last several years as a practical improvement on the older SM-2 algorithm. FSRS maintains, per concept and per student, a three-component memory model: difficulty, stability, and retrievability. It uses these to compute the optimal review interval — the delay that keeps retrievability just above a threshold without wasting reviews on material that doesn't need them yet. The mathematics are grounded in Ebbinghaus's decay functions and Cepeda's temporal-ridgeline findings. The calibration is done on large-scale user data rather than laboratory experiments.

The practitioner payoff of a Y6-aware platform is two things beyond precision scheduling. First, it surfaces high-decay concepts at the *class* level — material that consistently fails to stick across many students. That is an instructional-design signal, not a student-level signal. It tells the instructor where the unit needs redesign. Second, it identifies students whose decay trajectory is *worsening* over the term — an early-warning flag more diagnostic than any single quiz score.

Neither of these requires the platform to start. The signal exists in pencil-and-paper legacy items, and the instructional benefit of embedded retrieval practice exists whether or not you have an algorithm scheduling it. The platform is precision-on-top-of-an-instrument-that-already-works.

---

## What would change the analysis

Evidence that AI-assisted students who use the AI specifically to *generate practice questions* — asking the AI for quiz items and then attempting them without seeing the answer — produce decay curves comparable to genuine unassisted retrieval practice would change part of the chapter's framing. The argument here is that AI-as-explanation defeats retrieval. AI-as-practice-question-generator is a different use case and may not. This is an open empirical question.

A demonstration that classroom-paced spaced retrieval does not produce the spacing benefit predicted by Cepeda — that the laboratory finding fails to generalize to year-long courses — would substantially weaken the embedded-legacy-item recommendation. The recommendation is based on a defensible but not bulletproof generalization from controlled experiments to messy classrooms.

The strongest evidence the chapter rests on for the borrowed-certainty decay prediction is Bastani 2025, which found exam-performance collapse after AI-assisted engagement. Bastani did not measure a full decay curve under controlled conditions. That study is one RCT in one country in one subject. The chapter treats it as consistent with the prediction rather than as proof of it.

---

## Still puzzling

The optimal spacing function for classroom contexts is not settled at the level of precision Cepeda's temporal ridgeline implies. The practitioner-actionable rule — any non-zero spacing beats massing — is solid. Precise optimization is a platform problem, not a classroom problem.

Whether the AI-as-explanation effect on decay curves has been measured in a controlled decay study is, to my knowledge, no. The prediction is mechanistically clean. The controlled measurement is the study the field still needs.

Item-difficulty matching for embedded decay probes is a real measurement-design problem that the chapter's working rules address but do not solve fully. The chapter's recommendation is to embed more items when in doubt. That is workable, not optimal.

The permastore question — whether some genuinely-learned material shows long-tail retention indefinitely, as Bahrick's 1984 cross-sectional Spanish-retention data suggests — is not settled for domains beyond vocabulary and mathematics. The chapter treats long-tail retention as achievable without specifying the conditions precisely.

---

## LLM Exercises

**1. Generate and examine.** Take one concept from a recent unit you taught. Ask an LLM to explain it. Then, without looking at the explanation, try to retrieve the explanation from memory one hour later and write down what you can recover. Compare your retrieval to the original. Where did the fluency cue mislead you — what felt stored that turned out not to be? Use this as calibration for the claim that AI explanations build retrieval strength without storage strength.

**2. Apply to known context.** Identify a student in your current class whose current-unit performance has been strong all term. Predict, before adding legacy items, what their legacy-item performance will look like four weeks from now if you add the embedded probe. Specify: what decay rate would you expect for a student doing genuine work? What decay rate would you expect for a student borrowing certainty? After four weeks, compare the prediction to the data.

**3. Stress-test the claim.** The chapter argues that AI-as-explanation produces steep decay because no retrieval failures occur. Construct the strongest counterargument: design an AI-assisted study workflow that would, in principle, produce a genuine-engagement decay curve. What would the student have to do differently from the typical explain-and-read pattern? Is this workflow something students actually adopt without explicit instruction?

**4. Draft a professional deliverable.** Write the three-sentence explanation you will give students when you add legacy items to your quizzes — framed as a learning-support practice, not as surveillance. Then write the two-column gradebook label system you will use to track current-unit versus legacy performance, and write the one-sentence opener for the conversation you would have with a student whose legacy column is showing steep decline while their current-unit column looks fine.

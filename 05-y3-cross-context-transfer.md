# Chapter 5 — Y3: Cross-Context Transfer

*Genuine understanding transfers to new surface features. Borrowed certainty pattern-matches the original context and fails when the surface changes. The transfer gap is the signal.*

---

A third-year medical student can tell you everything about beta blockade. She can define it, sketch the mechanism on a napkin — sympathetic outflow, beta-1 receptor antagonism, decreased contractility and heart rate, the cascade through cAMP. She can recite the indications: post-MI, heart failure with reduced ejection fraction, certain arrhythmias, migraine prophylaxis. On board-style multiple-choice questions she scores in the top quartile.

Then she meets a patient.

The man in bed 14 has chest pain, a recent myocardial infarction, a heart rate of 102, and blood pressure that can tolerate gentle slowing. Her attending asks: "What would you start him on?" The student talks through the case carefully — mentions aspirin, statins, ACE inhibitor. The attending waits. The student does not mention beta blockade. The word "beta" does not appear anywhere in the patient's presentation, the room, the chart. The trigger is missing.

She had the surface features. She did not have the schema.

This failure frustrates every clinical educator, every laboratory instructor, every English teacher who has watched a student write beautifully about *Hamlet* and then miss the same theme inside a story they haven't been told to apply it to. The student knows the thing. The student cannot recognize the thing when it shows up wearing different clothes. In the AI era, this gap is going to widen — because borrowed certainty is, almost by construction, surface-feature certainty. Y3 is the chapter where we make the gap visible.

---

## The diagnostic

Y3 measures one specific thing: the gap between a student's performance on a near-transfer item and a far-transfer item. The vocabulary is older than this book.

Near transfer means the test problem looks like the textbook problem. Same surface features, same cover story, same wording conventions. The student who has pattern-matched will do fine here, because the pattern still applies. Far transfer means the same underlying principle has been re-clothed. The cover story is different, the vocabulary is different, the domain may be different. The student who has built an actual schema will recognize the principle through the disguise. The student who has only pattern-matched will not.

The diagnostic is not "did the student get the far-transfer item right?" The diagnostic is the *gap*. A student who scores 85% on the near item and 80% on the far item has a 5-point transfer gap. That's noise. A student who scores 85% on the near item and 30% on the far item has a 55-point gap. That is the signature. The pair carries the signal in a way no single item can.

Barnett and Ceci gave the field a useful taxonomy in 2002 — nine dimensions on which a transfer task can be near or far, including knowledge domain, physical context, functional context, modality. Most practitioners don't need all nine. Two dimensions get you most of the way: change the cover story, change the domain.

---

## Where schemas come from, and why AI explanations don't build them

Why does the gap exist at all? Why doesn't every student who receives a clear explanation of the underlying principle just recognize it in new clothes?

Because schema formation is not the same event as receiving an explanation. Sweller's cognitive load theory draws a distinction that matters precisely here. There is intrinsic load — the difficulty of the material itself. There is extraneous load — difficulty added by confusing presentation. And there is *germane* load — the cognitive work that constructs the schema. Germane load is the productive part of the struggle. It is what happens when the student has to grind on an unfamiliar instance and abstract away from the surface features toward the underlying structure. When a student offloads that grinding to an AI, the answer arrives, but the germane load does not. The schema is the residue of that load. No load, no residue.

Chase and Simon's 1973 chess experiments made this concrete before anyone had the vocabulary. They showed chess masters and novices a chessboard for five seconds, then asked them to reproduce it from memory. Masters reproduced meaningful positions — positions that could arise from real games — far more accurately than novices. On *random* positions, the advantage evaporated entirely. Masters performed no better than novices on random boards. The masters did not have superior memory in general. They had a schema for what chess positions look like. The schema is what transferred. Recognizing surface features was not the same skill.

Chi, Feltovich, and Glaser ran the same logic on physics problems in 1981. They gave novices and experts a set of problems and asked them to sort into groups. Novices sorted by surface features — inclined planes together, springs together, problems with the word "pulley" together. Experts sorted by underlying principle — conservation-of-energy problems together, regardless of whether they mentioned pulleys or springs or skiers. Same problems, different schemas. What the experts noticed was the structure underneath the surface. Novices noticed the cover story.

The Gick and Holyoak radiation problem is the most famous single experiment in the transfer literature, and it deserves to be. Students were asked to solve a medical problem: how to use radiation to destroy a tumor without destroying surrounding healthy tissue? Earlier in the session, they had read an unrelated story about a general who needed to capture a fortress and chose to split his army into small groups converging from different roads simultaneously. Spontaneous transfer — students who independently recognized that the story's solution applied to the tumor — was near zero. When students were given a single hint ("the story might be relevant"), transfer jumped to about 75%. The structural mapping was *there* once prompted. It was not generated spontaneously.

This is an uncomfortable result and the chapter has to sit with it honestly. Detterman argued in 1993, reviewing the literature, that demonstrated spontaneous transfer is the exception rather than the rule. "Transfer is rare." This is useful rather than discouraging, because it tells us why far transfer is diagnostic: it is hard precisely because schema formation is hard. The asymmetry — easy on near, hard on far — is what makes Y3 a signal. If transfer were free, the gap would not be informative.

Bransford and Schwartz softened this in 1999 with what they called "preparation for future learning" — the finding that students who have genuinely learned are better positioned to pick up new material quickly, even when they can't immediately apply yesterday's lesson cold. The schema is there; it just isn't always retrievable without a cue. This rescues the practitioner from the too-harsh conclusion that genuine learning produces no transfer. It does. It just often needs a prompt. A student who sees the connection with one nudge is showing more schema than a student who needs the whole answer.

---

## Why borrowed certainty fails on far transfer specifically

There is a deeper reason the borrowed-certainty signature appears so cleanly on far-transfer items. Large language models are pattern-matchers by construction. They predict tokens conditional on context. The fluent answer an AI generates to a textbook problem is surface-feature transfer — the model has encountered many similar problems and produces something that maps onto the surface. When a student offloads the problem and absorbs the answer, the student inherits that surface-level competence. They have not built the schema. They have inherited a pattern-match.

This is also why Y3 is structurally hard to fake. To perform well on a far-transfer item, the student would need to know which features are surface and which are deep — and that knowledge *is* the schema. The fake requires the real. A student who has borrowed certainty on a concept cannot reliably fake far-transfer performance, because faking it requires exactly the abstract understanding the borrowing bypassed.

The chess masters could reproduce meaningful positions because they had spent thousands of hours building schemas for what positions mean. They could not reproduce random boards because the schema applies only where there is structure to match. Borrowed certainty is a random board dressed in meaningful clothes. It looks like structure from the outside. Under a far-transfer probe, the randomness shows.

---

## The two signatures

The genuine Y3 signature is recognizable. Both near and far transfer scores are elevated — not equal, because far transfer costs something even for genuine learners, but both above the floor. The gap is small. The student recognizes the concept across surface variations. Given three scenarios that look unrelated on the surface but instantiate the same principle, she notices the kinship. She can generate a far-transfer instance herself — ask for another example of the principle from somewhere else in the world, and she produces a new cover story, not a paraphrase of the textbook example.

Hatano and Inagaki named this adaptive expertise in 1986 — the ability to extend, modify, and invent for new situations, contrasted with routine expertise, which means getting faster and more accurate on familiar problems without the capacity to extend. Routine expertise is what borrowed certainty produces. Adaptive expertise is what Y3 measures.

The borrowed-certainty signature is the inverse. Near transfer is high, far transfer is low. The gap is large and persistent — twenty, thirty, fifty points — and it doesn't narrow over the term. The student keeps doing well on items that look like training data and keeps failing on items that don't. Given the principle in an unfamiliar cover story, the student treats it as a new and unrelated problem. The mapping is invisible because the schema is not there to do the mapping.

Asked for another example of the principle, the borrowed-certainty student reproduces the textbook one. The AI's training distribution shaped what she can produce. Outside that distribution, she has nothing.

<!-- → [CHART: scatter plot — x-axis: near-transfer score (0–100%), y-axis: far-transfer score (0–100%) — each dot is one student. Two clusters visible: a "genuine" cluster near the diagonal (high near, high far, small gap) and a "borrowed certainty" cluster in the lower-right (high near, low far, large gap). A reference diagonal drawn. Students should see the gap as a horizontal distance from the diagonal, not just the far-transfer score in isolation.] -->

---

## How to observe this without any new infrastructure

The design recipe is short. State the underlying principle in one sentence to yourself. Write a near-transfer item in the textbook's standard format. Then re-write the same principle into a scenario from a completely different domain. Hold the principle constant. Vary the cover story. Score them separately. Compute the gap per student. That is Y3.

The paired-item quiz is the cheapest implementation — paper, pencil, an existing quiz format, two items per concept instead of one. The incremental cost is the time to write the far-transfer item, which is ten minutes per concept once you have the near item in hand.

The Chi sort task borrows directly from the 1981 study. Print twelve problems on index cards. Ask students to sort them into groups and label each group. Walk the room. Students who group by cover story ("these are all about pulleys") are showing the novice signature. Students who group by principle ("these all involve conservation of energy") are showing schema. Fifteen minutes of class time, no grading, qualitative Y3 read on every student simultaneously.

The cold-call recognition probe embeds the concept in a scenario without naming it. After teaching beta blockade, present a patient with the relevant features and ask what to start. Don't say "beta blockade." Don't say "Newton's third law." Don't say "natural selection." Make the student recognize that the principle applies. The recognition is the test.

The cross-discipline retrieval prompt works as a warm-up at the start of a new unit: "Where else have you seen something like this?" Genuine schema-holders surface connections the textbook didn't make. Borrowed-certainty students name the previous chapter's example and stop.

A practitioner caution: far transfer is genuinely hard, and scoring it pass-fail is too blunt. A student who sees the connection with one nudge is showing more schema than a student who needs the whole solution. Score Y3 as a continuum. Let partial credit and hint-supported transfer count as partial evidence of schema.

<!-- → [TABLE: four implementation methods — rows: paired-item quiz, Chi sort task, cold-call recognition probe, cross-discipline retrieval prompt. Columns: setup cost, time per class period, what it directly measures, whether it also functions as instruction (interleaved practice), best class size. Practitioner should see at a glance which to start with.] -->

---

## A worked example: Newton's third law in two clothes

A high school physics teacher is teaching Newton's third law. The textbook example: a hockey puck struck by a stick on a frictionless surface. Equal and opposite forces, the stick pushes the puck, the puck pushes the stick. Standard format, standard cover story, the same diagram every textbook uses.

She writes a near-transfer item: a hockey puck struck by a stick. Mass of the puck, mass of the stick, force exerted by the stick on the puck. What is the force exerted by the puck on the stick? Standard textbook language. Students who have done the homework recognize the structure immediately.

She writes a far-transfer item: an astronaut on a spacewalk needs to return to the ISS. She is floating ten meters from the airlock with no thrusters and no tether, holding a 5 kg toolkit. Briefly describe what she should do and why it works. No mention of force. No mention of Newton. No mention of action and reaction. The diagram is a stick figure and a satellite.

She runs both items on a weekly quiz.

Class average on the near item: 82%. Class average on the far item: 51%. Class-wide transfer gap: 31 points. This is large. The unit produced surface familiarity without schema, on average.

Student A scored 90% near and 85% far — a 5-point gap. Genuine signature. Her explanation of the astronaut problem: "She should throw the toolkit in the direction away from the airlock. The toolkit pushes back on her in the opposite direction, so she moves toward the airlock. This is Newton's third law — the forces are equal and opposite." Student A saw the principle through the cover story.

Student B scored 88% near and 32% far — a 56-point gap. Borrowed-certainty signature. Student B's explanation: "The astronaut should grab onto something nearby and pull herself back. She could also try to swim through space using her arms." The hockey-puck-and-stick training distribution did not include people stranded in space. The schema is not there to do the mapping. Pattern-match failed cleanly.

Student C scored 85% near and 75% far — a 10-point gap, probably genuine. Student C wrote: "She could throw the toolkit, I think — by Newton's third law? — and that would push her the other way." The hedging is part of the genuine signature. Student C is not certain, but the structural mapping is there. The hedge is calibrated uncertainty. Y3 and Y4 tend to co-vary.

Three conversations to have, with three different students, from data two items already produced. No platform, no detector, no accusation. Just the gap.

---

## What would change the analysis

A clean empirical demonstration that AI-assisted students produce a narrow transfer gap under controlled conditions — evidence that fluent AI explanation builds schemas at rates comparable to effortful engagement — would substantially weaken Y3's diagnostic value. The mechanism would have to be specified: what is the AI exposure doing that produces schema formation without germane load? The chapter cannot rule this out, but it is structurally improbable given what we know about how schemas form.

A demonstration that transfer-friendly pedagogy — variation theory, contrast cases, interleaved practice — reliably eliminates the borrowed-certainty Y3 signature would change how to deploy the signal across contexts. In a classroom structured specifically to produce schema formation, the gap would narrow for everyone. Y3 would be less informative as a discriminator in that classroom. That is a feature, not a bug; it would mean the pedagogy is working. But it would shift what the signal means when the gap is small.

The gap-size threshold is empirically open. The chapter uses a working number — gaps under 15 points are probably genuine, 30+ points sustained are probably borrowed — but this is practitioner calibration, not a research finding. Refine it with your own data.

---

## Still puzzling

Whether teaching explicitly for transfer eliminates the diagnostic is unresolved. Interleaved practice works. Variation theory works. If the unit is structured to produce schemas in every student, the gap narrows for everyone — at which point Y3 is less informative as a discriminator. This is worth knowing but doesn't undermine the signal in conventionally-taught classrooms, which are where the problem lives.

The "preparation for future learning" version of Y3 — can a student relearn the material faster because of prior genuine engagement? — has no clean practitioner operationalization. Bransford and Schwartz's framing is theoretically useful but practically hard to score in a classroom without a controlled relearning condition. The chapter doesn't solve this; it notes it.

The stability of far-transfer item difficulty across student populations is genuinely uncertain. A far-transfer item that is well-calibrated for one class may be trivially easy or impossibly hard for another. The practical solution is Method 3 — the Chi sort task, which generates the discrimination endogenously rather than requiring the instructor to pre-calibrate item difficulty. But the gap-scoring methods depend on the near and far items being comparably difficult except for the surface-feature variation, and achieving that by design requires more care than the chapter can specify in full.

---

## LLM Exercises

**1. Generate and examine.** Take one concept from your domain and ask an LLM to generate a near-transfer item and a far-transfer item for that concept. Evaluate both items: does the far-transfer item actually change the surface features while preserving the underlying principle? Or has the LLM produced two near-transfer items with slightly different wording? Use this as calibration for writing your own paired items — the most common mistake is treating a surface variation as a deep one.

**2. Apply to known context.** Identify a recent assessment in your course. For each major concept assessed, reconstruct what the near-transfer and far-transfer items were — or note that all items were near-transfer, which is itself the finding. Estimate, based on student performance and any qualitative observations you have, what the transfer gap was per student. Which students do you think would show a small gap? Which would show a large one? Write a two-sentence description of each that a colleague who doesn't know the students could use to recognize the pattern.

**3. Stress-test the claim.** The chapter argues that far-transfer performance cannot be reliably faked without actually having the schema, because faking it requires knowing which features are surface and which are deep. Construct the strongest counterargument: design a scenario where a student could produce a convincing far-transfer response without genuine schema formation. What would the student need to know, or do, in advance? How expensive is that preparation compared to just building the schema?

**4. Draft a professional deliverable.** For one concept in an upcoming unit, write one near-transfer item and one far-transfer item following the design recipe in the chapter: state the underlying principle in one sentence to yourself first, then write the near item in textbook format, then re-clothe the same principle in a completely different domain. Then write the one-paragraph explanation you would give students for why you are including both types of items — framed as "here is what these two kinds of questions test" rather than as a detection rationale.

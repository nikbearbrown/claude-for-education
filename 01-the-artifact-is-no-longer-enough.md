# Chapter 1 — The Artifact Is No Longer Enough

*Why the essay, the exam, and the project no longer prove what they used to prove — and why detection cannot patch the gap.*

---

Here is a result that should have stopped everyone cold.

A group of researchers gave roughly a thousand Turkish high school students access to GPT-4 for four weeks of math instruction. One group used the model without guardrails — just the raw tool, however they liked. A second group used a pedagogically designed wrapper that scaffolded hints and withheld full solutions. A third group used no AI at all. At the end of the four weeks, everyone sat a closed-book exam. No AI. No notes. Just the student and the problem.

The unguarded AI group had performed forty-eight percent above the control group on the practice problems. Their dashboards looked like success. Then the exam arrived, and they scored seventeen percentage points *below* the students who had used no AI at all. [verify — Bastani et al. 2025 PNAS; figure subject to administrative correction at 10.1073/pnas.2518204122; conclusions unchanged]

The students weren't running a scam. They were using a tool that produced fluent answers. The platform was watching engagement and reporting engagement. The engagement went up. The learning did not.

<!-- → [CHART: side-by-side bar chart showing practice-problem performance vs. exam performance across the three conditions (GPT Base, GPT Tutor, No AI) — the visual inversion between practice and exam scores is the chapter's central image] -->

That gap — between what the platform measured and what the exam revealed — is what this book is about.

---

## The chain that ran one way

Before you can understand why the gap matters, you need to see the mechanism that used to make assessment work.

The system that educators inherited rested on a single causal chain. Learning is something that happens inside a student's head — it is the formation of durable schema, the encoding of skill, the internalization of a procedure until it belongs to the person rather than to the page. That internal process is invisible. You cannot see a student learn. What you can see is what learning produces: a cognitive process — drafting, reasoning, struggling through — and what that process produces: an artifact. The essay. The exam answer. The lab report.

Three links, one direction:

**Genuine Learning → Cognitive Process → Artifact**

The teacher sits at the far end of this chain. She can only see the artifact. But the chain only ran one way — if the artifact was good, you could read backwards through it with reasonable confidence. A good artifact required a good cognitive process, and a good cognitive process required that genuine learning had happened. The artifact was a valid proxy for the learning because it was the only thing that could plausibly have produced it.

Notice what that validity rested on: the artifact had exactly one upstream. One causal source. That was the whole argument.

Generative AI opens a second causal pathway to the artifact that does not pass through the student's cognition at all:

**AI Generation → Artifact**

The student now lives adjacent to a system that produces artifacts on demand. Those artifacts are increasingly indistinguishable from competent student work. From the teacher's seat, the two upstreams — the student's learning and the model's generation — are visually identical. The proxy fails not because students are cheating in any traditional sense but because the artifact now has two sources, and you cannot tell them apart by looking at the artifact.

This decoupling is not temporary. It is not a transitional problem that will resolve when students settle down or when policy clarifies or when detection gets better. It is a structural feature of the system the field is now teaching inside. The chain that ran one way runs two ways. Treating the artifact as proof of the process is treating a piece of evidence as if it had one source when it has two.

<!-- → [INFOGRAPHIC: diagram of the two causal pathways — the original single chain (Learning → Process → Artifact) and the new parallel pathway (AI Generation → Artifact) converging at the artifact node — the visual should make clear that both paths land at exactly the same place] -->

---

## Why detection is not the answer

The institution's instinct, when it first encounters this problem, is to restore the artifact's validity by answering the question: did a human type this? If the detector can answer yes or no, the proxy works again. The argument is intuitive. It is also structurally a dead end.

The first problem is temporal. Every detector is trained against the generation models that exist when the detector is built. The models then improve. Sadasivan and colleagues (2023) proved the theoretical ceiling: as generated text approaches indistinguishability from human text, any detector's performance approaches a coin flip. You are not solving a problem. You are funding maintenance on a perpetually losing arms race.

The second problem is the wrong question. "Did a human type this?" was useful as a proxy for "did a human learn this?" back when the two questions had the same answer. They no longer do. A student can type something she has not learned. A student can fail to type something she has learned. The detector, even when it works perfectly, answers a question that has stopped being load-bearing.

The third problem is the one that should end the institutional conversation about detection. Liang and colleagues (2023) ran seven commercial AI detectors against TOEFL essays from non-native English writers and against eighth-grade essays from US-born students. The detectors misclassified sixty-one percent of the TOEFL essays as AI-generated and produced near-zero false positives on the US-born eighth graders. This is not a calibration problem. The detectors were learning the statistical fingerprint of non-native English fluency, which overlaps substantially with the statistical fingerprint of AI-generated text, because both involve a certain kind of syntactic regularization. If your detector flags eight percent of submissions, you are not catching eight percent of the cheating. You are catching some opaque mixture of genuine AI-use and the writing patterns of your second-language students, and you cannot separate them at the level of the individual case.

There is a quieter fourth problem. Detection creates perverse incentives. When the detector is the system, the student's job becomes producing text the detector will accept — which is a problem the AI is exceptionally good at helping solve. The student does not learn the material. She learns to launder the AI's output through paraphrase and tone-shifting. The institution has inadvertently made the detector the curriculum.

The political capital being spent on better detection is capital that cannot be spent on a measurement framework that asks a more important, and actually answerable, question.

---

## The right question

Detection asks: did a human type this?

The right question is: did a human learn this?

These sound similar. They are not. The first is a property of the artifact. The second is a property of the student. The first can be defeated by any system that produces sufficiently human-looking text. The second cannot be defeated by any such system, because no such system can cause the student to learn. The AI can write the essay. It cannot, by writing the essay, place the schema in the student's head. The schema either formed or it didn't, and the question of whether it formed is entirely independent of the question of how the page got filled.

This sounds philosophical. It is operational.

If you can find behavioral evidence that the schema formed — evidence that does not run through the artifact — you have an evidence stream the AI cannot produce on the student's behalf. The student who had the model write her essay can hand you the artifact. She cannot hand you the trace of having struggled through the material the model was solving for her. The traces of genuine cognitive engagement are consequences of a specific cognitive process running inside a specific brain — and that brain either ran the process or it didn't.

The question is also more important. Bjork and Soderstrom (2015) wrote the canonical synthesis of the distinction that matters here: *performance versus learning*. Immediate performance — what the student can do right now, in the conditions where she practiced — is a famously unreliable predictor of durable retention. Performance is what most assessment captures. Learning is what assessment is supposed to evidence. The two have always been partially independent. Broad AI access widens the gap to a scale the assessment system was not built to handle.

There is a cultural shift that rides along with the question change. "Did you use AI?" is a question with one of two answers, and one of the two requires the student to admit something consequential. The honest student and the dishonest student have the same incentive to say no. The question collapses into a contest neither party wins. "What would tell me you learned this?" is a different conversation entirely — a conversation a teacher and a student already know how to have, and one that occasionally reveals genuine learning neither party was expecting.

---

## What Bastani and Kestin are actually saying

It is worth sitting with the Bastani result a moment longer, because it is easy to misread.

The result is not "AI hurts learning." Place the Bastani finding next to Kestin and colleagues at Harvard (2025), who ran a parallel RCT with undergraduate physics students using a well-designed AI tutor — Socratic prompting, no full solutions, calibrated scaffolding. Their students learned roughly twice as much in the same time as students in a high-quality active-learning condition, and reported higher engagement to match.

Same generation. Opposite outcome.

The model isn't the variable. The wrapper is. The Bastani students with the guardrailed wrapper — the "GPT Tutor" condition — held their ground on the unassisted exam. The model did not harm them. What harmed the unguarded students was not GPT-4. It was that GPT-4 was doing the cognitive work the students needed to do themselves, and the platform had no way to see that the work had been transferred.

<!-- → [TABLE: three-column comparison of Bastani GPT Base / GPT Tutor / No AI conditions — rows for practice-problem performance gain, exam performance relative to control, and what was being measured — surfaces why the dashboard and the exam told opposite stories] -->

Bastani is one RCT in one country in one subject. It is the strongest currently published demonstration of the engagement-learning gap, but it is not settled. Lehmann and colleagues' 2024 working paper on a Swiss higher-education sample suggests the effect is moderated by student ability — stronger students appear to gain from AI assistance while weaker students are harmed, which would complicate any single-line claim about AI effects. Stadler and colleagues (2024) report ChatGPT improving essay quality while degrading subsequent learning in the same students, consistent with the artifact-cognition decoupling. The framework in this book is designed to be useful regardless of what exact replication produces. The structural argument — that a second causal pathway to the artifact breaks the artifact-as-proxy — does not depend on any specific effect size. The Bastani finding is a demonstration. The decoupling is the diagnosis.

And the conditions of the Bastani study are not the conditions of a future scenario the field has time to prepare for. The "unguarded" condition — raw model access, used however the student prefers — is the condition most school and university AI deployments are running today, whether by policy or by default.

---

## What comes next

The good news is that genuine learning leaves traces.

Not metaphorical traces. Physical, behavioral, structural traces — the kind that are present when the cognition happened and absent when it didn't. The schema that formed inside a student's head produces consequences in how she talks about the material, how she responds when the scaffolding is removed, how she handles a problem she hasn't seen before. Those consequences are observable. They are not observable through the artifact alone, but they are observable.

This book is built around seven kinds of traces. Together they form a second evidence stream that a working teacher reads alongside artifact quality, in whatever proportion her professional judgment warrants. The framework is called the Genuine Learning Probability framework, or GLP. The seven components are labeled Y1 through Y7. The framework and the term "friction traces" are internal to Humanitarians AI [Humanitarians AI internal framework]; the underlying mechanisms are not.

This is not anti-AI. The Kestin result exists. The guardrailed wrapper in Bastani worked. The decoupling is permanent, but the wrapper can be designed to put the cognitive process back in front of the artifact rather than beside it — and that is a design problem, not a prohibition problem.

The framework is also not a new technology requirement. You do not need a platform purchase, a new credential, or institutional policy to begin. You need to know what to look for. Chapter 2 explains why the traces exist — not as metaphor, as mechanism. The chapters after that explain what each one is, what genuine looks like, what borrowed certainty looks like, and how to start observing them in your classroom this term.

---

## LLM Exercises

**1. (Analyze) The reliable-vs-unreliable inventory.** In your current practice, name one assessment where you are still confident the artifact is reliable evidence of genuine learning. Name one where you are not. What is structurally different between the two? Pay attention to whether the difference is *what you assess* or *under what conditions you assess it.* If the difference is conditions, that is information about how to expand the safe-side list without abandoning the work you care about.

**2. (Analyze) The question you actually want to ask.** A student submits an essay that is markedly more polished than her in-class writing. You suspect AI involvement but cannot prove it. Write, in one or two sentences, the question you actually want to ask her — not "did you use AI?" but a question that probes whether the schema is in her head. The test of a good question here is whether her honest answer would tell you something useful regardless of whether she used AI.

**3. (Evaluate) The eight-percent figure.** Your institution's AI detector flags eight percent of student submissions as AI-generated. Name two ways this figure is simultaneously an undercount and an overcount. Be specific about who is in each category. The Liang 2023 finding is one piece of the answer; what is the other?

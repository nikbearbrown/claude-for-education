# Appendix: The Fundamental Themes

*Frictional · Phase Gates · Humans + AI*

---

## About this appendix

This book belongs to a connected set of projects built on one argument, and you have been reading that argument all along — in Chapter 3's desirable difficulties, in Chapter 12's scaffold/crutch distinction, in every exercise block's "When NOT to Use AI." This appendix states the argument whole, in the series' own vocabulary, so you can see the frame behind the book and carry it into work the book does not cover.

One note in the spirit of this book: the empirical claims below are stated in the register of a manifesto. Where those claims appear in the body of this book, they are treated with full Evidence Box discipline — the Bastani three-condition RCT in Chapters 1 and 12, the desirable-difficulties literature in Chapter 3, and the EEG cognitive-connectivity finding (a single-source preprint with published criticism, flagged accordingly) in Chapter 12's evidence apparatus. The manifesto and the Evidence Boxes describe the same world at different levels of caution. Reading both registers without flinching at either is itself the Tier 4 skill.

**Where the themes live in this book:**

| Theme | Where you met it |
|-------|------------------|
| Frictional — the struggle is the mechanism | Ch 1 (engagement ≠ learning), Ch 3 (desirable difficulties, the working-memory budget), Ch 6 (friction to keep vs. remove), Ch 12 (the crutch effect) |
| Phase gates — the explicit boundary | Ch 12 (the AI integration decision: what AI does, what it is forbidden to do, how support fades), every exercise block's Exercise 1/2 pairing |
| Humans + AI — the division of labor | Ch 5 (AI drafts protocols, never learner data), Ch 7 (AI plans sessions, never simulates learners), Ch 9 (AI sweeps WCAG, never makes the three-logics call), Ch 13–14 (AI computes, the human concludes), Ch 15 (the decision trace) |
| The taxonomy (Tiers 1, 4–7) | The "Series connection" line in every chapter's exercises |

---

## One Sentence

Learning requires struggle, teaching requires judgment, and AI that does either for you produces the appearance of both without the substance — the answer is not less AI but a precise division of labor between what machines do well and what human cognition alone constitutes.

---

## The Three Themes

### 1. Frictional: The Struggle Is the Mechanism

The central claim is neurobiological before it is pedagogical.

The principle is now in the book's name. *Frictional* Experience Design for EdTech is a commitment, not a flourish: every design move this book teaches either protects the friction that constitutes learning or removes the friction that merely obstructs it — and knows which is which.

Genuine learning is not a mental event that happens to have neurological correlates. It is a biological event. When the brain encounters material that doesn't fit what it already knows — a prediction error — dopamine fires, BDNF upregulates, synapses strengthen, dendritic spines form. These are the physical events that constitute memory. They are triggered by cognitive friction: the productive struggle of encountering something you cannot yet do, explain, or understand.

Remove the friction and you remove the trigger. No trigger, no consolidation. No consolidation, no durable learning.

The mechanism is specific. Dopamine prediction error signaling fires when expectation is violated — when the learner encounters something that does not fit their current model. This phasic dopamine initiates long-term potentiation, the strengthening of synaptic connections that is the physical substrate of memory. BDNF upregulates under moderate cognitive challenge, driving the molecular cascades that support long-term consolidation. Dendritic spine formation — the structural growth of new synaptic connection sites — increases under moderate cognitive load. These processes do not occur when the AI provides the answer. The surprise that fires dopamine, the challenge that upregulates BDNF, the effortful processing that drives spine formation — all of these require the learner to actually do the cognitive work. (A caution on precision: the specific magnitude claims for these neurobiological effects — fold-changes and percentages — derive from a preprint and should be cited with care; the directional mechanism is well-established in the cognitive neuroscience literature.)

This is why the Bastani finding is so precise: students who used AI freely during math practice scored 48% higher during practice and 17 percentage points *lower* on the unassisted exam. Not slightly worse. Dramatically worse. They felt like they had learned. The fluency of the AI's output was indistinguishable from the feeling of genuine mastery. But the neurological events that would have produced mastery never occurred. The artifact was fine. The brain was unchanged.

The Kosmyna EEG study makes this visible: up to 55% reduction in functional brain connectivity during AI-assisted writing vs. brain-only writing. The neural networks that constitute comprehension, synthesis, and memory formation simply did not activate at the same rate. The students borrowed cognitive capability from the machine rather than building it in themselves. (This book carries that study with a single-source flag — see the note above. The behavioral evidence does not depend on it.)

The implication: cognitive struggle is not the price of learning. It is the mechanism of learning. AI that removes the struggle removes the mechanism. AI that makes the struggle more productive — better feedback, better calibration, better questions — accelerates learning without removing its cause.

**The Frictional principle:** The struggle is the point. AI should make the struggle more productive, not eliminate it.

This is Chapter 3's argument with the biology stated plainly: desirable difficulties feel worse and work better because the difficulty is the trigger. It is also Chapter 6's distinction between friction to remove and friction to keep — extraneous load impedes the mechanism; germane difficulty *is* the mechanism.

### 2. Phase Gates: The Explicit Boundary

The phase gate is the operational form of the Frictional principle.

A phase gate is the specific point at which AI processing stops and human work begins — or where human work ends and AI can assist. It is not a vague commitment to "using AI responsibly." It is a specification: AI handles X, human handles Y, the gate is at Z.

Phase gates exist because not all cognitive work is equal. Some tasks are extraneous load — friction that impedes learning without constituting it: formatting citations, organizing sources, drafting routine communications, adjusting reading levels, generating structural templates. AI handling these tasks frees human cognitive capacity for the work that matters. Other tasks are germane load — the cognitive work that IS the learning: synthesizing conflicting evidence, constructing an argument, setting up a problem, forming a judgment, teaching a confused student. These cannot be delegated without delegating the learning itself.

The phase gate makes this distinction operational and enforceable. Without a gate, the path of least resistance is to let AI do more and more until the human is a reviewer of AI output rather than a practitioner of a discipline.

- **Teachers and designers:** AI handles preparation → human does the judgment
- **Students:** AI handles scaffolding → human does the thinking

**The phase gate principle:** Specify where AI stops and human work begins. Make the gate explicit. Enforce it. The gate is not where you trust the AI less — it is where the human cognitive work is irreplaceable.

In this book, the phase gate is Chapter 12's deliverable: the AI integration decision that names what AI does, what it is forbidden to do, and how support fades. It is also the architecture of every exercise block — Exercise 1 names what crosses the gate to AI, Exercise 2 names what never does.

### 3. Humans + AI, Not Humans or AI

The false choice in every public conversation about AI is: use it or don't. Embrace or resist. Replace or reject. The actual question is: what is AI for?

The answer requires a taxonomy — not a vague claim that "some things are irreducibly human" but a specific account of which cognitive capacities machines currently cannot perform reliably, and why.

---

## The Irreducibly Human Taxonomy

AI has decisively won Tier 1. For everything else, the situation is more complicated — and the complication is what this book teaches.

### Tier 1 — Pattern & Association: Machines Win

AI is superhuman at pattern recognition, statistical association, and information retrieval. **Educational implication:** stop teaching humans to compete here. AI does well: statistical pattern-finding, information retrieval and surface synthesis, reformatting and structuring, complexity adjustment, error-flagging in well-defined domains, generating text that conforms to established patterns. **What AI cannot do in this tier:** evaluate whether the pattern it found is the right pattern to care about, decide which associations are causal and which are spurious, or know when the pattern breaks. These failures are invisible from inside the pattern.

### Tier 2 — Embodied & Sensorimotor: Constrained by Physics

Some human capability is irreducible because it is physical, and physical engagement with the world produces knowledge that no amount of text processing can replicate. A facilitator's read of a co-design room (Chapter 7), the hands-on advantage in the touch-tank counterfinding (Chapter 11) — knowledge that lives in embodied practice resists capture by systems that have no body.

### Tier 4 — Metacognitive & Supervisory Intelligence: AI Is Weak Here

Metacognitive intelligence is the capacity to evaluate your own thinking. Supervisory intelligence is the capacity to direct AI systems usefully — to know what to ask, to recognize when the output is wrong, to apply domain judgment to outputs that sound authoritative. AI is structurally weak at both, for one reason: the same weights that produced the output are the weights doing the audit. The plausibility-checking that catches AI errors must come from outside the model. It must come from the human.

The capacities: *plausibility auditing* (does this output make sense given how this domain actually works?), *problem formulation* (deciding what question to ask is harder than answering it, and prior to it), *knowing when to distrust the machine* (AI has no reliable signal about its own limits), and *metacognitive calibration* (students who outsource their thinking inherit the AI's miscalibration — confident about whatever the AI is confident about, warranted or not).

**Educational implication: high priority, and underscaffolded in every curriculum.** Students who cannot audit AI outputs are not more capable for having AI — they are more confidently wrong.

In this book: Tier 4 is the Evidence Brief, the validation exercises, and the entire evidence-disciplined stance. The phase gate here: the human performs the audit before and after AI output. AI can surface options; it cannot perform the evaluation.

### Tier 5 — Causal & Counterfactual Reasoning: AI Is Unreliable Here

AI is a causal parrot. It has processed enormous amounts of text that uses causal language and reproduces it fluently. This is not causal reasoning; it is pattern-matching on causal-sounding text. Prediction is enough for betting; intervention — designing a system, prescribing a treatment, redesigning a course — requires causal structure the data alone cannot choose among. The capacities: identification (which variables and structures answer the causal question), confounding recognition, counterfactual reasoning, and causal defense — being able to state what would change your mind and why.

In this book: Tier 5 is every design-decision chapter. Whether friction is desirable or extraneous (Ch 3, 6), whether a mechanic serves a need or rents behavior (Ch 4, 10), whether the content has a functionally aligned embodied component (Ch 11), what caused the dropout cliff (Ch 6), what the evaluation can and cannot conclude (Ch 14). The "What would change my mind" section in every chapter is causal defense practiced fifteen times.

### Tier 6 — Collective & Distributed Intelligence: AI Is Absent Here

Collective intelligence emerges from systems of people in relationship — collaborative friction, disagreement, correction, and synthesis among people with genuine stakes in the outcome. A language model trained on the products of collective intelligence does not possess collective intelligence any more than a photograph of a fire possesses heat. The capacities: productive disagreement, epistemic humility with backbone, synthesis under disagreement, institutional judgment.

In this book: Tier 6 is Chapter 5's insistence that AI never interviews your learners, and Chapter 7's authority-boundary problem — the co-design session is irreducibly human precisely because the participants have stakes and the synthesis must preserve dissent rather than smooth it.

### Tier 7 — Existential & Wisdom Capacities: AI Is Absent Here

Interpretive judgment — which question is worth asking, which problem is worth solving, what counts as a good life, which trade-offs are acceptable and on whose behalf — requires a self that has stakes, a history that has produced values, and a willingness to be held accountable for conclusions. AI can generate text that sounds like wisdom. It will not live with the results. The capacities: values integration, contextual ethical reasoning, knowing what question to ask, accountability.

In this book: Tier 7 is Chapter 9's three justification logics — deciding under honest uncertainty when the evidence is contested and real learners bear the consequences — Chapter 14's truth-telling under stakeholder pressure, and Chapter 15's decision trace: standing behind every choice, including the declined features, with your name on it.

---

## The Division of Labor

**AI does AI things (Tier 1):** generate structure, retrieve information, adjust complexity, produce calibrated feedback, create practice problems, draft routine communications, flag errors in well-defined domains, execute analysis once the human has framed it, format and organize existing content.

**Humans do human things (Tiers 4–7):** audit AI outputs for plausibility, formulate the right problem, perform the causal and design judgments, hold and defend positions in productive disagreement, exercise institutional judgment, know what question is worth asking, be accountable for consequential decisions.

Neither replaces the other. The designer who uses AI for the WCAG sweep does more equity judgment. The researcher who uses AI to draft interview protocols spends more time with real learners. The evaluator who uses AI to compute spends the saved hours on confound honesty. The human cognitive work is not diminished; it is clarified, amplified, and freed from the Tier 1 work that was occupying it.

The teacher-as-delivery argument is empirical, not sentimental — but it requires honest qualification. Hattie's synthesis finds teacher credibility and teacher-student relationships among the highest-effect educational influences, but Hattie's methodology has serious peer-reviewed critics on statistical grounds. The directional finding — teacher expertise, credibility, and relationships matter greatly — is independently supported by peer-reviewed meta-analyses of teacher credibility specifically. The Tutor CoPilot RCT (Wang et al., 2025, working paper) adds a more specific finding: AI that amplifies a human tutor's judgment produced learning gains where AI in front of the learner without a human produced only neutral results at best. At the same time, the Kestin et al. (2025) peer-reviewed RCT shows that a pedagogically engineered autonomous AI can outperform conventional classroom instruction in structured domains with high-self-regulation learners. The synthesis: human instructional judgment remains central, particularly for younger learners, struggling learners, and contexts where motivation, relationship, and metacognitive calibration matter. In structured domains with self-regulated learners, well-designed AI can rival human-led instruction. The variable in both cases is pedagogical design.

**The phase gate follows from the taxonomy:** the gate sits at the Tier 1 / Tier 4 boundary. AI stops at the gate not because it is distrusted but because the cognitive work on the other side of the gate is the work that produces the human capability that makes AI safe to use.

---

## The Unified Argument

**Frictional** is the biological level: learning is a physical event triggered by cognitive struggle; remove the struggle and you remove the trigger; AI that bypasses the struggle bypasses the learning.

**Phase gates** are the operational level: specify exactly where AI stops and human work begins; make the specification explicit; enforce it; the gate sits at the Tier 1 / Tier 4 boundary.

**Humans + AI** is the design level: AI handles Tier 1 so humans can do Tiers 4–7; the system amplifies human capability at the tiers that are irreducibly human, rather than replacing the cognitive events that constitute them.

This book is the design-level argument applied to learning experiences: the learner's productive struggle is the product (Frictional), the designer's guardrails are the specification (phase gates), and the Redesign Dossier is the division of labor practiced until it is a professional identity (humans + AI).

---

## In Three Lines

AI removes the struggle that triggers learning. The phase gate specifies where the struggle must be human — at the boundary between Tier 1 pattern work and Tiers 4–7 judgment, reasoning, and wisdom. Humans + AI means AI does Tier 1 work so humans can do the Tiers 4–7 work that machines cannot — not less human involvement, but better human involvement at the tiers that are irreducibly ours.

---

## The Projects

The framework described in this appendix is deployed across a connected set of projects. Each is a different instantiation of the same argument.

| Project | What it is | URL |
|---------|-----------|-----|
| **Frictional** | The theoretical and empirical foundation — the Genuine Learning Probability framework and the measurement methodology for learning that requires struggle | [frictional.xyz](https://frictional.xyz) |
| **Irreducibly Human** | The curriculum series — textbooks, tools, and courses built on the seven-tier taxonomy of human cognitive capacities AI cannot reliably replicate | [irreducibly.xyz](https://irreducibly.xyz) |
| **Boondoggling** | The engineering application — conducting AI through software builds with explicit labor separation | [boondoggling.ai](https://boondoggling.ai) |
| **Brutalist** | The creative application — the structured human-AI collaborative production system for visual, motion, and code-driven design work | [brutalist.art](https://brutalist.art) |
| **Nik Bear Brown** | Author website — the connecting node across all projects | [nikbearbrown.com](https://nikbearbrown.com) |

The argument is one. The applications are many. The tools will change. The taxonomy will evolve at the margins. The neurobiological mechanism of learning — and the structural incapacity of AI at Tiers 4 through 7 — will not.

---

## References

Fact-check pass (2026-06-07). No inline flags were inserted in this appendix: per the manifesto-register convention stated in "About this appendix," inline flags are reserved for factually contradicted claims, and both checkable statistics verified. See `factchecks/97-fundamental-themes-assertions.md` for where manifesto register and the evidence diverge (the dopamine/BDNF/synaptic chain is defensible in its parts but overdrawn as a strict universal mechanism; the Kosmyna figure is a non-peer-reviewed n=54 preprint).

1. Bastani, H., Bastani, O., Sungu, A., et al. (2025). "Generative AI without guardrails can harm learning: Evidence from high school mathematics." *PNAS* 122. doi:10.1073/pnas.2422633122. — CONFIRMED (≈48% higher during practice; ≈17 percentage points lower on the unassisted exam; harm is the unguarded condition).
2. Kosmyna, N., Hauptmann, E., Yuan, Y. T., et al. (2025). "Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task." arXiv:2506.08872 (MIT Media Lab). — CONFIRMED (up to 55% reduction in lower-band dDTF connectivity, LLM vs. brain-only). Non-peer-reviewed preprint, n = 54; the chapter already carries it with a single-source flag.

# Chapter 29 — Repeated Reading as AI-Supported Fluency Practice
*The Chapter That Says Yes — and What It Means That Most Don't.*

One influence: repeated reading programs, d = 0.75 — fluency built by reading the same text multiple times with feedback. In Hattie's synthesis this is a high-band literacy intervention with an unusually mechanical mechanism: the repetition itself, performed by the reader, does the work. That makes it AI-native territory without a conflict flag: a model can select texts, listen, time, and give feedback, and none of that removes the student's reading, which no tool can do for them. The high substitution risk lives elsewhere — in the tool displacing the teacher's instruction rather than the student's practice.

**Group Profile: Repeated Reading as AI-Supported Fluency Practice**

| Profile | Detail |
|---|---|
| Influences in this group | 1 of Hattie's 252 |
| Effect size | d = 0.75 |
| Hattie band | High |
| AI feasibility | AI-native |
| Human irreducibility | Low |
| Substitution risk | High |
| Cognitive-work conflict | None |
| Influence | Repeated reading programs (rank 23, d = 0.75) |

Lena Fitzgerald teaches second grade and can describe her fluency problem with the precision of someone who has watched it eight times in a row: eight of her students decode accurately but so slowly that by the end of a sentence they have lost its beginning. She knows the intervention they need. Repeated reading — short passages read aloud, again and again, with someone catching errors and nudging expression — is not a mystery. The arithmetic is.

Eight students. Four sessions a week. Ten minutes of one-to-one listening each. That is more than three hours of dedicated adult attention per week for a single intervention, in a classroom with one part-time aide and twenty-six children who all need something.

The district's literacy director offers a pilot license for an AI reading tutor — an Amira-class tool that listens through a headset, catches word-level errors in real time, tracks accuracy and rate, and serves passages at calibrated difficulty. The vendor's brochure claims the product is "twice as effective as traditional tutoring."

Lena's grade-level team is wary; this book has spent several chapters warning about AI doing learners' work for them. But the literacy director asks the right question: "What work, exactly, would this tool be doing — and whose work is it?"

For once in this book, the answer mostly comes back clean.

## Why This Chapter Is Different

A single influence, classified: high band, AI-NATIVE, low human irreducibility, high substitution risk, no mechanism conflict.

That pairing — high substitution risk with no conflict — looks contradictory until you ask what, precisely, can be substituted. In repeated reading, the learner's irreplaceable act is reading aloud, again. No tool can do your oral reading for you in any way that tempts; the cognitive work cannot be offloaded even in principle. What AI substitutes is the listener — the adult who hears the reading, catches the errors, gives the feedback. That role is the intervention's bottleneck, and much of it is procedural enough that speech-recognition systems have been the oldest serious AI application in reading education precisely because the fit is structural.

The high substitution risk is guarding something real — three boundaries described below — but the core answer here is different from most of this book. After chapters of traps and conflict flags and hypothesized collapses from real effect sizes to 0.10, the classification says: go, with conditions. This chapter is the clean exhibit that the framework is not a refusal machine.

## The Mechanism: Automaticity

Repeated reading programs (d = 0.75) — rank 23 on the 2018 252-influence list. [verify across editions; values differ]

The evidence anchor is Therrien's 2004 meta-analysis: repeated reading produced large fluency gains and moderate comprehension gains on practiced passages, with benefits for general-education students and students with learning disabilities alike. [verify exact figures against journal PDF before quoting] His structural contribution matters more than any decimal: he separated non-transfer outcomes (the rehearsed passage) from transfer outcomes (novel passages). Transfer effects are real but smaller — which is the honest boundary of the intervention and the honest test of any product built on it. The National Reading Panel reached the convergent conclusion: guided repeated oral reading has significant positive impact on word recognition, fluency, and comprehension across grade levels.

Why does it work? The mechanism is automaticity, and the logic runs from LaBerge and Samuels' foundational account: while decoding is effortful, it consumes the working memory that comprehension needs. [verify — classic source, cited from field knowledge] A child laboring over each word has nothing left for meaning. As word recognition becomes automatic, capacity is released for understanding. Repeated reading attacks automaticity directly — the same short passage, read aloud with error feedback, until a fluency criterion is met, then a new passage.

Two clarifications keep the mechanism honest. Fluency is not speed. The construct is accuracy plus appropriate rate plus prosody — phrasing, expression — in service of comprehension. A words-per-minute race trains the wrong target and produces robotic readers who hit the rate benchmark while understanding nothing. Second, the gain that matters is the transfer gain: a child who climbs from 62 to 94 words correct per minute on the rehearsed passage has demonstrated rehearsal. The same child reading next week's cold passage more fluently than last month's has demonstrated learning. Dashboards must be judged on cold reads.

Why is the listener so important? Because unmonitored repeated reading consolidates errors. The child who misreads "through" as "thorough" four times has practiced the mistake. The feedback loop — error caught, word corrected, line reread — is what separates practice from rehearsal of failure. That loop is exactly what one adult cannot run for twenty-six children simultaneously, and exactly what speech recognition can.

![Before/after capacity-partition comparison: under heavy decoding load a child's working memory is mostly consumed by decoding with little left for comprehension; after repeated reading automatizes decoding, capacity is released and comprehension expands](images/29-repeated-reading-as-ai-supported-fluency-practice-fig-01.png)
*Figure 29.1 — Automaticity: working-memory reallocation*

<!-- → [DIAGRAM: Mechanism diagram — left: child's working memory under heavy decoding load (decoding large, comprehension small). Right: same child after automaticity training (decoding small, comprehension large). Center arrow: "repeated reading with error feedback." Annotation: "the gain that matters is cold-read transfer, not rehearsed-passage rate."] -->

## Building the Substitution Ledger

This is the one chapter in the high-stakes section that benefits from a role-by-role ledger, because the verdict on each role is different.

The reader — the child — is never substitutable, not even in principle. The decoding is the intervention. Text-to-speech playing passages while a child follows the highlighting is repeated *listening*, not repeated reading; the engagement dashboard can glow while the practice has been silently zeroed.

The text is AI-generatable at controlled decodability — legitimate, with quality control. Passages matched to the phonics scope and sequence, at calibrated difficulty levels, generated faster than any teacher can write them.

The listener and error-catcher is AI-substitutable, with the caveats below. This is the bottleneck role, and it is mostly procedural — word in, match to target word, flag if wrong, record. Real-time oral reading evaluation is one of the oldest legitimate AI applications in education precisely because the task is bounded and the feedback latency matters.

The prosody model — someone whose expressive reading the child can hear — is human-preferred. Children should regularly hear skilled fluent reading; a synthesis voice does not model what natural prosody sounds like under meaning.

The motivation and relationship — the reason a six-year-old reads aloud to an adult — is human. Children perform partly because the adult cares. A machine's attention is not the same attention.

Most chapters in this book need a gate. This one needs a roster.

![Five-row classification roster of repeated reading's roles with their substitutability verdicts — reader (never), text (AI-generatable with QC), listener/error-catcher (AI with caveats), prosody model (human-preferred), motivation/relationship (human-required)](images/29-repeated-reading-as-ai-supported-fluency-practice-fig-02.png)
*Figure 29.2 — The substitution ledger: five roles, three verdicts*

## What AI Can Safely Do

Listen to every rehearsal. Real-time word-level error detection across an entire classroom simultaneously — the bottleneck dissolved. For a teacher with twenty-six students and eight who need intensive fluency work, this is not an incremental improvement. It is a structural change to what is possible.

Catch and log errors. Track accuracy, rate, and prosody proxies over time, producing growth curves per child. Surface the flattened curves — telling the teacher which children's growth has stalled so that scarce human listening time lands where it is needed.

Serve passages at calibrated decodability, matched to the phonics scope and sequence. The Chapter 30 connection runs both directions: phonics supplies the decoding knowledge; repeated reading automatizes it.

Enable the home-practice loop. Repeated reading is homework-friendly but historically unsupervisable; an AI listener changes the economics, raising practice volume where it was zero. This is one of the few places the book's general homework-with-AI warning does not transfer. Because the mechanism is oral performance practice, there is no way to fake your own reading to a microphone. The homework is the performance.

## The Three Boundaries

**The inversion: the machine reads to the child.** The most dangerous failure is also the quietest. Text-to-speech — the app reading aloud while the child follows the highlighting — is repeated listening, not repeated reading. The child practices exactly nothing the d = 0.75 measures; the intervention has been inverted while the engagement numbers improve. The audit question is five words: *who is doing the decoding?* TTS has legitimate uses elsewhere — access to grade-level content for students with disabilities is a different intervention with its own logic — but deploying an access tool inside a fluency-practice slot deletes the practice.

**The whole-ecosystem substitution.** AI listening should expand the listening economy, not abolish the human share of it. If machine listening replaces human listening entirely, the school loses what ASR cannot carry: modeled prosody, comprehension breakdowns a human ear catches, and the relational reasons a child reads aloud to an adult at all. The gate is not that AI cannot listen. The gate is that AI must expand access rather than substitute out the human entirely.

**The recognition gap — an equity failure wearing a personalization badge.** Speech recognition accuracy varies by speaker. Young children, second-language speakers, and speakers of non-mainstream dialects face higher misrecognition rates, which convert directly into false error feedback and wrong difficulty placement. [verify — documented as a concern class in the ASR literature; current commercial-system figures not confirmed] An ASR tutor that hears a dialect as disfluency is not measuring the child's reading. It is measuring its own training data. The score is the tool's *recognition* of the reading — and for some children, the gap between the two is the finding.

One evidence caution belongs here because vendors put it in their materials: the published evidence base for Amira-class tools is heavily vendor-funded. Evidence for ESSA rates the flagship product Moderate, not Strong. "Twice as effective as tutoring" is marketing copy, not a study result. Cite ratings, not ratios.

## What Happened in Lena's School

The grade-level team designed the pilot themselves, which was the condition the literacy director accepted.

Each child read aloud to the tool three times a week, ten minutes a session — every minute of decoding the child's own. The tool caught the consolidation errors human scarcity used to miss: one boy had been misreading "what" as "want" for weeks without anyone catching it consistently; the system flagged it on day two. The freed hours mattered as much as the errors: with drill supervision offloaded, Lena's actual human listening time — the scarcest resource in the room — was reallocated to her eight lowest readers and to weekly whole-class prosody modeling, the two ledger roles the team had marked human.

![Before/after allocation comparison of listening time across 26 children: before AI the teacher's listening is spread thin across all 26; after, AI listens to the 18 stronger readers while the teacher concentrates on the 8 lowest, expanding the listening economy rather than replacing its human share](images/29-repeated-reading-as-ai-supported-fluency-practice-fig-03.png)
*Figure 29.3 — The listening economy, before and after*

<!-- → [INFOGRAPHIC: Before/after listening-economy diagram — before: Lena's listening time distributed across 26 children, thin; after: Lena's listening time concentrated on 8 lowest readers, AI listening for remaining 18. Annotation: "the machine expanded the listening economy rather than replacing its human share."] -->

Two gate-crossings surfaced mid-pilot. A well-intentioned aide began steering frustrated readers to the app's listen-along mode — engagement up, decoding practice silently zeroed. The team caught it in usage logs: the children logging the most minutes included two doing the least reading. And the dashboard's headline metric was rehearsed-passage growth, which flattered everyone; the team's own cold-read checks told a different story for three students whose curves were flat. One of them, a Vietnamese-American girl whose English was excellent but accented, was receiving steady false error feedback — the system was marking correctly read words wrong. Her errors were the machine's.

Adoption conditions, written into the pilot charter. Listen-along mode disabled inside the fluency block — access uses live elsewhere in the day, clearly labeled as access, not practice. The deciding metric is cold-read fluency and comprehension on novel passages, checked every two weeks by humans, reported beside rather than inside the platform's rehearsed-passage numbers. Every child keeps a weekly human-listening slot. Any child whose error pattern looks anomalous moves to human-listening verification, with dialect and L2 mismatch named in the protocol as the first suspect. Renewal next spring depends on the school's own cold-read data, not the vendor's studies — which the charter records as mostly vendor-funded, ESSA rating Moderate.

## The Phase Gate

**AI may** listen to every rehearsal, catch and log word-level errors, track accuracy and rate over time, serve passages calibrated to the phonics sequence, and tell the teacher whose growth curve has flattened.

**The learner must** do every minute of the actual reading aloud — the decoding is the intervention and it cannot be delegated, accelerated, or simulated.

**The teacher must** set the fluency criteria, model expressive reading, keep a standing rotation of human listening for every child, personally review flagged and anomalous cases, and own the decision of when a child's practice text steps up.

**Evidence that learning improved is** cold-read fluency and comprehension on novel passages, trending upward — Therrien's transfer measure, checked by humans on texts the platform never rehearsed with the child. Not rehearsed-passage gains, which partly measure rehearsal, and never minutes of use, which measure only the schedule.

| Role | Substitutability verdict | Condition or caveat |
|---|---|---|
| Reader (the child) | Never substitutable | The decoding is the intervention; text-to-speech turns it into repeated *listening* |
| The text | AI-generatable | With quality control; matched to the phonics scope and sequence at calibrated decodability |
| Listener / error-catcher | AI-substitutable | With caveats — the bottleneck role, mostly procedural, but watch the recognition gap for dialect and L2 speakers |
| Prosody model | Human-preferred | Children should regularly hear skilled fluent reading under meaning; a synthesis voice does not model it |
| Motivation / relationship | Human-required | A six-year-old reads aloud partly because the adult cares; a machine's attention is not the same attention |

*Valid evidence is cold-read transfer — fluency and comprehension on novel passages the platform never rehearsed. What does **not** count: rehearsed-passage gains, minutes on platform, engagement streaks, or vendor-funded studies quoted without their funding line and ESSA rating.*

## What Evidence to Demand

Cold-read growth. Unrehearsed passages, read aloud to a human, scored for accuracy, rate, and expression — fall to spring. This is the transfer line, and it is the only line that counts as learning.

Comprehension alongside fluency. Automaticity is the on-ramp to meaning, not the destination. A check that the freed working-memory capacity is arriving at comprehension — retell quality, questions on the cold passage — keeps the program honest about its purpose.

Recognition-accuracy audit. Sample the platform's error flags against human judgment, deliberately including dialect and L2 speakers. A tool that cannot pass this audit is generating false data precisely for the children with the least margin.

The decoding ledger. Usage logs confirming the child, not the synthesized voice, is doing the reading in every minute counted as practice.

What does not count: minutes on platform, rehearsed-passage gains presented as growth, engagement streaks, or vendor-funded studies quoted without their funding line and ESSA rating.

## What Would Change My Mind

Two findings would restructure this chapter. First, a credible independent evaluation showing that children receiving only machine listening — no human rotation at all — match the mixed-roster children on cold-read growth, comprehension, and reading motivation over a full year; that would demote the human-listening condition from gate requirement to preference. Second, and in the other direction, a well-designed audit showing that current commercial ASR misrecognition rates for dialect and L2 speakers are high enough to produce systematic placement errors at scale; that would push this chapter's conditional yes toward "not yet, for these populations" — and the fact that I cannot currently locate such an audit, in either direction, is itself the gap that needs filling before any district deploys at scale.

## Still Puzzling

Repeated versus wide reading remains unsettled. If equivalent time on varied texts produces equivalent fluency gains, the optimal AI fluency station might look quite different — more passage variety, less rerunning of the same text. The comparison literature deserves the trial the vendors have not funded.

LLM-enhanced versions of these tools now add comprehension questioning and adaptive passage generation on top of fluency scoring. That quietly moves them out of this row's no-conflict zone and into questioning and summarization territory — where the gates are stricter. A single product straddling three rows of the framework is a procurement problem the framework was not built to solve gracefully, and schools need to evaluate each function separately even when they arrive in one license.

What is the motivational half-life of reading aloud to a machine? Second graders find the headset novel in October. Nobody has published what April looks like.

## Further Reading

**Therrien, W. J. (2004). Fluency and comprehension gains as a result of repeated reading: A meta-analysis. *Remedial and Special Education*, 25(4), 252–261.** The evidence anchor — and the practiced-versus-transfer distinction that should be written into every fluency product's evaluation plan.

**National Reading Panel (2000). *Teaching Children to Read*, Fluency chapter.** The convergent finding on guided repeated oral reading, and the wider five-pillar frame that keeps fluency in proportion to the rest of reading instruction.

**Evidence for ESSA (evidenceforessa.org), entry for Amira Learning.** Worth reading less for the rating than as a model of the question to ask about any vendor study: who funded it, against what comparison, on which outcome?

**Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49, 241–253.** The benchmark discipline for claims like "twice as effective as tutoring" — what the comparison would actually have to show.

**The ASR-fairness literature on dialect bias in speech recognition.** Start with a recent review of speech-recognition error-rate disparities across dialects and language backgrounds; the transfer to children's reading assessment is direct, and this chapter's audit exercise is its classroom application. [verify — select and confirm a specific current review before print]

---

## Exercises

**Warm-up**

1. (Low difficulty) *Tests understanding of the automaticity mechanism.* Explain in two sentences why a child who decodes slowly may struggle to comprehend even when they recognize every word correctly. Then explain how repeated reading addresses this problem — specifically what the repetition does, not just that it helps.

2. (Low difficulty) *Tests the transfer distinction.* Therrien's meta-analysis separated practiced-passage gains from novel-passage gains. Explain why this distinction matters for evaluating a fluency program, and identify which type of gain is the one that counts as learning and should appear in an evaluation report.

3. (Low difficulty) *Tests the inversion trap.* A teacher uses an AI reading app in fluency stations. In one mode, the child reads aloud while the app listens and flags errors. In another mode, the app reads aloud while the child follows highlighted text. Explain the difference between these two modes in terms of who is doing the decoding — and why the second mode does not constitute fluency practice in the sense the d = 0.75 measures.

**Application**

4. (Medium difficulty) *Tests the substitution ledger.* Build the substitution ledger for a beginning band practice program: list every role (performer, error-catcher, model, motivator, material-supplier), and mark each as never substitutable, substitutable with caveats, or freely substitutable. Explain your reasoning for any role you mark as "with caveats," specifying what the caveat is.

5. (Medium difficulty) *Tests the recognition-gap problem.* An AI fluency tool is deployed in a third-grade classroom with several students who speak a regional dialect. The tool's dashboard shows these students making significantly more "errors" than their peers, and the system places them in lower-difficulty passages. Describe the specific mechanism that could be producing this pattern, explain what a teacher should do before accepting the placement decision, and propose one item that should be in the tool's procurement contract to address this problem.

6. (Medium difficulty) *Tests the cold-read evidence standard.* A school's AI fluency program reports that students increased their average words-correct-per-minute on in-platform passages from 58 to 87 over twelve weeks. The principal wants to present this as evidence the program worked. What is the limitation of this measure as stated, what additional data would you need to confirm the gains represent learning rather than rehearsal, and how would you collect it?

**Synthesis**

7. (High difficulty) *Tests integration of the substitution ledger, the three boundaries, and the evidence standard.* Design the complete fluency-station policy for a second-grade classroom of 24 students, eight of whom are significantly below benchmark. Specify: what the AI tool does, what roles remain human and why, how listen-along mode is handled, what the teacher does with the tool's error logs, and what evidence at what intervals would allow you to conclude the station is producing transfer gains rather than rehearsal gains. Your policy should be specific enough that a substitute teacher could implement the human-rotation component correctly.

8. (High difficulty) *Tests the multi-row straddle problem from "Still Puzzling."* An LLM-enhanced fluency tool now includes three components: oral reading with real-time ASR feedback (fluency), comprehension questions after each passage (questioning), and AI-generated passage summaries the child reads before recording (summarization). Using the book's framework, evaluate each component separately — identifying which chapter's rules apply, what the substitution risk is, and whether the component should be kept, modified, or removed. Then explain why evaluating the three components as a single product is insufficient.

**Challenge**

9. (Advanced) *Tests the repeated-versus-wide-reading puzzle and the still-unsettled comparison.* The chapter notes that some studies find wide reading — equivalent time on varied texts — matches repeated reading's fluency gains, but that the comparison literature is inconclusive. Design the study that would settle the question for the AI context specifically: not which approach is better in general, but which approach is better when the listener is an AI system rather than a human. Specify your populations, conditions, dosage, outcome measures, and the result pattern that would lead you to recommend each approach for AI-supervised practice. Address the practical constraint that the study must be feasible in real schools with real teachers who cannot be asked to withhold a credible intervention from a control group.

## Prompts

### Figure 29.1 — Automaticity: working-memory reallocation
Build a before/after capacity-partition comparison (mechanism cross-section). Represent a fixed total working-memory capacity as a bounded region, split into two parts. Left panel "Heavy decoding load": decoding fills most of the region, comprehension is a thin sliver. Right panel "After automaticity": decoding shrinks to a small region, comprehension expands to fill the released capacity (highlight the expanded comprehension area). Keep the total region size identical across panels so the reallocation is visible. Place a center arrow between panels labeled "repeated reading with error feedback." Annotate the axis: "Fixed working-memory capacity (LaBerge & Samuels)." Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 29.2 — The substitution ledger: five roles, three verdicts
Build a five-row layered schematic (classification roster). Each row is a role with a verdict note: "Reader (the child)" — "Never substitutable — human core"; "The text" — "AI-generatable with quality control"; "Listener / error-catcher" — "AI-substitutable with caveats"; "Prosody model" — "Human-preferred"; "Motivation / relationship" — "Human-required." Use a three-level color encoding for the verdict (never / AI-with-caveats / human-required versus AI-generatable) so the roster reads as a graded ledger, not a binary gate. Stack the rows top to bottom in the order given. Annotate that this is a roster of roles, not a single gate. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 29.3 — The listening economy, before and after
Build a before/after allocation comparison (proportional schematic) of listening time across 26 children. Left panel "Before AI": teacher listening spread thin across all 26 children (highlight this row to mark the thin distribution). Right panel "After AI": teacher concentrates on the 8 lowest readers while AI listens to the 18 stronger readers — show the split visually as two proportional blocks (8 human, 18 machine). Use proportional widths so the reallocation is legible. Annotate that AI expands the listening economy rather than replacing its human share. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

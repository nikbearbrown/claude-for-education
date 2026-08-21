# Chapter 30 — Phonics Support Without Replacing Instruction
*Two numbers, one committee, and the question of what "AI-delivered" actually means.*

One influence: phonics instruction, d = 0.70 — systematic teaching of sound-letter correspondence, one of the most evidence-settled interventions on Hattie's list. AI can support it well: decodable texts on demand, practice calibrated to the exact correspondence a child is learning, patient repetition. The high substitution risk is institutional rather than mechanical: phonics apps are cheap, teachers are not, and the temptation is to let the app do the first teaching rather than the practice that follows it. The chapter draws that line — support after instruction, never instead of it.

**Group Profile: Phonics Support**

| Profile | Detail |
|---|---|
| Influences in this group | 1 of Hattie's 252 |
| Effect size | d = 0.70 |
| Hattie band | High |
| AI feasibility | AI-augmented |
| Human irreducibility | Medium |
| Substitution risk | High |
| Cognitive-work conflict | None |
| Influence | Phonics instruction (rank 31, d = 0.70) |

The vendor's pitch has four words that are doing unearned work: *AI-delivered phonics lessons.*

Renee Castile is assistant superintendent for elementary instruction in a district of nine elementary schools. The state's new early-literacy law requires systematic, evidence-based phonics instruction in every K-2 classroom. The district is short three literacy coaches. Two of the four finalist curriculum packages arrive with AI built in — and one vendor's brochure carries the sentence she will spend the next five weeks unpacking: "AI-delivered phonics lessons that guarantee every child receives the science of reading, d = 0.70."

The adoption committee is split along a line Renee recognizes. Half the committee hears "guaranteed delivery" and thinks of the second-year teachers improvising phonics from Pinterest. The other half hears "AI-delivered lessons" and asks who, exactly, will be teaching the children to read.

Before the vote, Renee needs two numbers on the table: the 0.70 in the vendor's pitch, and a 0.41 the vendor never mentions. The difference between them is not a rounding error. It is a grade band, a comparison condition, and a lesson about what effect sizes inherit from the studies that built them.

---

## What the Group Is

A single influence: High band, **AI-AUGMENTED**, medium human irreducibility, **high substitution risk**, **no mechanism conflict**.

The pairing repeats the puzzle from the last two chapters, one layer up. No mechanism conflict: an app cannot decode for a child — every word a student sounds out is the student's own cognitive work, so the learner's side of the gate is safe by construction. The high substitution risk names a different casualty: **the instruction itself.** Phonics is a *taught* intervention, and what gets displaced when a district buys its way out of a staffing problem is not the child's practice but the teacher's explicit teaching. The failure here is institutional: a school adopts the app, counts app minutes as the phonics block, and the first teaching of letter-sound relationships quietly evaporates — at highest cost to exactly the children who need instruction, not just exposure.

Across three chapters the substitution-risk concept has now meant three different casualties: the learner's cognitive act (Chapter 28), the listener's processing (Chapter 29), and here, the teacher's first teaching. Same dimension, three different things being replaced. Which is why the phase gate must always name *what* is being substituted before ruling on it.

---

## The Two Numbers

**Phonics instruction (d = 0.70) — rank 31 on the 2018 list.** Hattie's figure pools multiple phonics meta-analyses with broad inclusion criteria. That breadth is what produces the higher number.

The anchor is Ehri, Nunes, Stahl, and Willows (2001) — the National Reading Panel's phonics meta-analysis: 66 treatment-control comparisons from 38 experiments, overall **d = 0.41** for systematic phonics versus unsystematic or no phonics. Same intervention. Smaller number. Tighter studies.

The moderator every adoption committee should memorize sits inside the NRP work: **d = 0.55 when instruction began in kindergarten or first grade, dropping to 0.27 after first grade.** The same intervention earns roughly half the effect as a third-grade remediation. No vendor pitch includes this table. It belongs on the committee's wall.

By field-experiment standards — Kraft's (2020) realistic benchmarks — 0.41 from rigorous experiments is a strong result. The direction is not in dispute. But "what works" has a *when* attached, and the 0.70 versus 0.41 discrepancy is not a contradiction to be resolved by picking the higher number. It is a lesson about how pooling choices inflate effect sizes, and why both figures belong in the room.

| Source / condition | Effect size (d) | Study design | What it means by Kraft's benchmarks |
|---|---|---|---|
| Hattie 2018 list value | 0.70 | Broad pooling of multiple phonics meta-analyses, wide inclusion criteria | A large effect — but inflated by breadth of pooling, not a single rigorous estimate |
| NRP / Ehri et al. (overall) | 0.41 | 66 treatment-control comparisons, 38 tight experiments | A strong result from rigorous experiments — the defensible anchor |
| NRP — instruction begun in K-1 | 0.55 | Subset, early grades | The intervention working where the evidence concentrates it |
| NRP — instruction begun after Grade 1 | 0.27 | Subset, later grades | Roughly half the effect — remediation-by-exposure is the weak version |

*The grade-band moderator (0.55 in K-1 falling to 0.27 after Grade 1) is the line no vendor brochure prints. It belongs on the committee's wall, not in a footnote.*

![Phonics effect sizes plotted against the 0.40 hinge: Hattie 0.70, NRP 0.41, K-1 0.55, after Grade 1 0.27](images/30-phonics-support-without-replacing-instruction-fig-01.png)
*Figure 30.1 — Two phonics numbers and the grade-band moderator*

Honesty also requires the live dispute. Bowers (2020) reviewed twelve meta-analyses and concluded the evidence that systematic phonics is *superior to alternative methods* is weak to nonexistent. The replies — Fletcher, Savage, and Vaughn (2021), among others — charge him with miscast comparisons and the wrong question, since no serious party proposes zero phonics [contested]. The defensible convergence point, which is all this chapter needs: explicit phonics instruction reliably helps beginning readers; claims of superiority over every alternative mixture, and of phonics-first exclusivity, are where genuine dispute lives. A committee that can state that distinction will read every vendor brochure in the stack more accurately, because "the science of reading is settled" is precisely the kind of flattened claim that AI products inherit and amplify.

---

## Why It Works: The Mechanism Stack

English writing is a code: letters and letter combinations map to sounds. Some children crack the code from exposure; many do not, and for them the mapping must be taught — explicitly, in a planned sequence, with immediate corrective feedback. The mechanism runs in layers: phonemic awareness (hearing the sounds inside words) → grapheme-phoneme mapping (which letters spell which sounds) → blending (assembling sounds into words) → orthographic mapping (words becoming sight words *through* successful decoding) → automaticity. Phonics is the on-ramp, not the destination. Decoding feeds fluency feeds comprehension, and the effect size measures the on-ramp's value, concentrated in the early grades.

The load-bearing distinction of the whole chapter: **instruction versus practice.** Systematic phonics is a taught intervention — explicit modeling of new correspondences, guided blending with the teacher's immediate correction, and responsive error analysis: when a child misreads, is it a letter-sound gap, a blending failure, or a phonemic-awareness gap underneath? Each diagnosis calls for different teaching. Apps deliver practice and assessment well. Most apps do not deliver instruction — they exercise what someone has taught. The question is always: who taught the correspondence the app is practicing?

![Five-layer phonics mechanism stack with parallel AI-support and teacher-only role columns at each layer](images/30-phonics-support-without-replacing-instruction-fig-02.png)
*Figure 30.2 — Phonics mechanism stack and the AI/teacher split*

<!-- → [DIAGRAM: The phonics mechanism stack — vertical layers from phonemic awareness at the base through grapheme-phoneme mapping, blending, orthographic mapping, to automaticity at the top. Two parallel columns alongside: what AI can support at each layer (assessment, practice generation, progress tracking) and what requires a human teacher at each layer (first modeling of new correspondences, diagnosis of error type, responsive reteaching). The diagram should make unmistakable that AI supports the stack; it does not build it.] -->

---

## What AI Can Safely Do

Around an intact, teacher-led phonics block, the support roles are substantial.

**Screening and progress mapping.** Speech-recognition assessment of phonemic awareness and letter-sound knowledge, generating a weekly gap map per class — which teachers validate against their own observation. The same dialect-and-accent cautions from Chapter 29 apply wholesale: false flags from accent transfer are not edge cases, and the validation step is not optional.

**Distributed practice.** Short daily app drill on taught correspondences — practice, clearly labeled as practice, supplementing rather than replacing first teaching. The deliberate-practice logic from Chapter 27: design beats dosage, and targeted practice on taught patterns beats undirected exposure.

**Decodable-text generation — the genuinely new affordance.** Language models can draft decodable passages on demand, constrained to taught correspondences: only short vowels and the digraphs ch and sh; no r-controlled vowels. This eases a real scarcity — engaging texts matched to each week of a scope and sequence, on demand rather than after a librarian's year of searching.

Two cautions ride along. LLMs do not natively respect phonics constraints; they drift into untaught patterns because the model has no concept of "what this class has been taught this week." So outputs need rule-checking — scriptable: a program can verify every word against the constraint list — plus teacher review. And no peer-reviewed evaluation of LLM decodable-text generation exists yet. <!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/30-phonics-support-without-replacing-instruction-assertions.md --> This is a promising, verifiable-by-construction affordance, not an evidenced one.

**Progress curves and flag lists** telling the teacher which children's decoding growth has stalled and on which correspondences — directing scarce small-group time to the right targets.

---

## The Three Substitution Traps

**"The app teaches phonics."** Most apps *exercise* phonics. The first teaching of a new correspondence — the explicit modeling, the guided blending, the corrective feedback tuned to the child's articulation error in this moment — is instruction, and almost no app delivers it in any meaningful sense. The verb in the brochure is doing unearned work. The app drills what someone has taught; it is not that someone.

**Coverage metrics replace instructional ones.** "100% of K-2 students receiving systematic phonics" can mean every student has an app license. That metric measures procurement, not teaching. The audit that catches it is arithmetic: count the minutes. Before and after adoption, how many weekly minutes of explicit teacher modeling of new correspondences does each class receive, versus minutes of app drill? If adoption moved minutes from the first column to the second, substitution happened — regardless of intent, regardless of how good the app is.

**Remediation loops without reteaching.** When a child fails app items, well-designed software serves easier items. What it cannot do is what a teacher does: notice that the child's letter-sound errors are actually a phonemic-awareness gap and reteach upstream. Strugglers cycling through remedial app loops without a human ever re-teaching the correspondence get exposure where the evidence prescribes instruction — and the post-Grade-1 d = 0.27 says remediation-by-exposure was already the weak version of this intervention before the app made it cheaper.

---

## One Adoption, One Principal's Proposal, One Minute-Audit

Renee's committee adopted a curriculum — and wrote the AI's job description into the adoption itself.

Both numbers went on the committee's table in week one, with the timing moderator. The presentation changed the conversation: the question stopped being "does phonics work?" and became "which parts of this package are instruction, and which are practice?" That distinction, once named, let the committee evaluate the finalist packages on the right dimension.

In the pilot classrooms, the support stack earned its place. ASR screening produced weekly gap maps that one kindergarten teacher described as "three assessment afternoons given back to me a month" — and her validation caught two false flags, both accent artifacts, exactly as the protocol anticipated. The LLM decodable-text feature, run through the district's rule-check script and a teacher skim, supplied fresh mini-books matched to each week's correspondences. Ten minutes of daily app practice consolidated what teachers had taught. The teachers kept teaching: every new correspondence introduced by a human, every error pattern interpreted by one.

The dangerous moment arrived dressed as the solution to the staffing problem. One principal, down a literacy coach and two veteran teachers, proposed running the "AI-delivered lessons" mode as the core phonics block in her three least-experienced classrooms: "the app's lessons are more systematic than what my second-year teachers improvise." It was the strongest version of the substitution argument, and the committee took it seriously rather than dismissing it. Inconsistent human instruction is a real cost.

The minute-audit reframed it. The proposal did not add the app's systematicity to those classrooms' instruction; it removed the teachers from first teaching at the precise career stage where they would have learned to deliver it — manufacturing, within three years, a faculty that had never taught decoding. And the children in those rooms — disproportionately the district's highest-need — would receive exposure where the evidence prescribes instruction.

![Before/after minute-audit of a weekly literacy block — teacher-led-plus-app keeps a large explicit-instruction segment, app-as-core leaves first-teaching near zero while total minutes hold constant](images/30-phonics-support-without-replacing-instruction-fig-03.png)
*Figure 30.3 — Minute-audit: two configurations of the literacy block*

<!-- → [INFOGRAPHIC: The minute-audit comparison — shows a week of a K-2 literacy block in two configurations: (A) teacher-led + app supplement (explicit instruction minutes vs. practice minutes labeled separately); (B) app-as-core-instruction (practice minutes up, explicit instruction minutes near zero). The visual point: adoption of the app as core instruction does not add systematicity — it removes the first-teaching column entirely.] -->

**The conditions, written into the contract.** The teacher-led phonics block is non-negotiable and scheduled; AI-delivered lesson mode is disabled as core instruction, permitted only as catch-up supplementation for absences, with a coach's sign-off. The district's implementation metric is the minute-audit, reported termly per school: explicit instruction minutes must hold steady or rise post-adoption. Struggling readers get more human instruction, not more app minutes — the flag lists route children to small-group reteaching, never to remediation loops. For the underprepared teachers, the gap is met with the package's scripted materials plus coaching — the Tutor CoPilot pattern: AI's strongest documented contribution to struggling-learner instruction is making the human instructor better, not replacing her. The spring evidence check is nonword decoding and oral reading of untaught decodable text, alongside — never inside — the app's own levels.

---

## The Phase Gate

**AI may** screen and map phonemic awareness and letter-sound knowledge (with human validation of flags and a dialect-aware protocol), generate decodable texts under rule-checked constraints, deliver short distributed practice on taught correspondences, and surface which children have stalled on which patterns.

**The teacher must** do all first teaching of new correspondences — the explicit modeling, guided blending, and immediate corrective feedback that constitute the instruction — interpret every error pattern (letter-sound gap, blending failure, or phonemic-awareness gap underneath), and lead all reteaching for children the screening flags. The institution must guarantee, by schedule and by audit, that app minutes supplement and never replace instruction minutes.

**Evidence that learning improved is** nonword decoding accuracy and oral reading of untaught decodable text, trending upward on human-administered checks — measures the app cannot rehearse and the child cannot fake — never app levels completed, license coverage, or minutes logged.

---

## The Evidence Check

Four demands, no substitutes.

**Nonword decoding growth.** The cleanest probe of the alphabetic principle: progress on pseudowords proves letter-sound mastery, not memorization. No app's internal levels substitute for it.

**Transfer to untaught text.** Children reading decodable passages built from taught patterns but never seen in the app or the classroom. Transfer is the point; in-program performance is not.

**The minute-audit, held over time.** Explicit instruction minutes per week, by classroom, before and after adoption. This is evidence about the institution rather than the child — and in this group, the institution is where the mechanism fails.

**Strugglers' trajectories specifically.** Disaggregate: are the lowest-baseline children receiving more human teaching post-adoption, and is their nonword-decoding gap narrowing? A bimodal distribution — fast finishers fine, strugglers cycling — is the failure signature.

What does not count: app completion levels, coverage percentages, engagement minutes, or vendor effect-size citations that omit grade band, outcome type, and comparison condition.

---

## What Would Change My Mind

A well-designed independent trial showing app-delivered phonics instruction matching teacher-led explicit instruction for beginning readers — same nonword-decoding and untaught-text growth, including for the lowest-baseline children, sustained across a year — would collapse this chapter's central distinction. The instruction-versus-practice wall rests on the claim that responsive first teaching cannot yet be automated; if a product demonstrates it can, the high substitution risk becomes an implementation note rather than a gate, and the staffing-shortage argument the case study's principal made would deserve a different answer.

## Still Puzzling

- The Bowers exchange will not resolve soon: how much of phonics' measured advantage is the system (scope and sequence) versus the explicitness versus simply the guarantee that decoding gets taught at all? The answer matters for what an app would have to replicate to count as instruction.
- LLM decodable-text generation is verifiable by construction — a script can check every word — which makes it nearly unique among AI affordances in this book. Should "verifiability by construction" earn a formal place in the framework's feasibility dimension?
- The science-of-reading legislative wave is driving procurement at a pace the evidence cannot match, and AI vendors are riding it. What does responsible adoption look like when the law's clock runs faster than the evaluation cycle?

## Further Reading

- **Ehri, L. C., Nunes, S. R., Stahl, S. A., & Willows, D. M. (2001). Systematic phonics instruction helps students learn to read: Evidence from the National Reading Panel's meta-analysis. *Review of Educational Research*, 71, 393–447.** The anchor: d = 0.41 overall, 0.55 in K-1, 0.27 after — the moderator table every adoption committee should tape to the wall.
- **Bowers, J. S. (2020). Reconsidering the evidence that systematic phonics is more effective than alternative methods of reading instruction. *Educational Psychology Review*, 32, 681–705.** The strongest version of the dissent — read alongside the next entry, never alone.
- **Fletcher, J. M., Savage, R., & Vaughn, S. (2021). A commentary on Bowers (2020). *Educational Psychology Review*, 33, 1249–1274.** The reply. The pair models how to read a heated literature without joining a side prematurely.
- **National Reading Panel (2000). *Teaching Children to Read*.** The five-pillar structure (phonemic awareness, phonics, fluency, vocabulary, comprehension) that keeps phonics in proportion — necessary, not sufficient.
- **Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49, 241–253.** Why 0.41 from rigorous experiments is a strong result, and the calibration that turns the two-numbers problem from embarrassment into instruction.

---

## Exercises

### Warm-up

**1.** The chapter presents two effect sizes for phonics instruction: d = 0.70 (Hattie) and d = 0.41 (NRP). A committee member says "they can't both be right — which one should we use?" Explain in two sentences why both numbers can be accurate, what accounts for the difference, and what a committee should do with both rather than selecting one. *(Difficulty: low. Tests: understanding how pooling choices and inclusion criteria produce different but valid effect sizes.)*

**2.** The NRP meta-analysis found phonics instruction earns d = 0.55 in kindergarten and first grade, dropping to d = 0.27 after first grade. In terms of Kraft's field-experiment benchmarks, what does each figure mean — and what practical implication does the moderator carry for a district deciding whether to invest in phonics remediation in Grade 3 versus kindergarten screening? *(Difficulty: low. Tests: applying the timing moderator and Kraft's benchmarks to a practical resource-allocation question.)*

**3.** The chapter states: "The app drills what someone has taught; it is not that someone." Explain the instruction-versus-practice distinction in two sentences using the mechanism stack — specifically, what a human teacher does when a child misreads that an app cannot do. *(Difficulty: low. Tests: operationalizing the instruction/practice distinction at the mechanism level.)*

### Application

**4.** A first-grade team wants to use an LLM to generate decodable passages for the week's correspondences (short *a* and short *i*, the digraphs *sh* and *th*, and twelve sight words). Describe the complete workflow: what the teacher prompts, what the rule-check script verifies, what the teacher reviews before handing the text to students, and what the teacher does if the script flags three constraint violations in the draft. *(Difficulty: medium. Tests: operationalizing the LLM decodable-text affordance with its full verification protocol.)*

**5.** A principal reports: "Our phonics adoption is a success — 97% of K-2 students are logging into the app daily, and in-app phonics levels advanced by an average of 2.3 bands this semester." Using the evidence check, write the four questions you would ask before accepting this as evidence of phonics learning — and explain why none of the reported metrics answers any of them. *(Difficulty: medium. Tests: applying the evidence framework to a specific set of vendor/principal metrics and identifying what each metric measures versus what the influence requires.)*

**6.** The case study's principal proposed running the AI-delivered lesson mode as the core phonics block for her three least-experienced classrooms, arguing the app is more systematic than what her second-year teachers improvise. The committee rejected this — but acknowledged that inconsistent human instruction is a real cost. What should the district do instead to address the genuine problem (underprepared teachers delivering inconsistent phonics instruction) without crossing the gate? Be specific about the support structures and what evidence would show they're working. *(Difficulty: medium. Tests: accepting the legitimate problem the substitution argument points to while generating a gate-compliant solution.)*

### Synthesis

**7.** Compare the substitution risk in this group (teacher's first teaching displaced by app instruction) with the substitution risk in Chapter 27's group (scaffolding without fading). Both have high-to-medium substitution risk. What is structurally different about *what* is being substituted in each — and why does the minute-audit catch this chapter's failure while the two-line graph catches Chapter 27's? *(Difficulty: high. Tests: cross-chapter synthesis that identifies the different substitution casualty in each group and the evidence instrument designed to catch it.)*

**8.** The "Still Puzzling" section raises whether "verifiability by construction" — the property that LLM decodable text generation can be rule-checked by script — should earn a formal place in the framework's AI-feasibility dimension. Design the argument for including it: what would the new feasibility subcategory be called, which other AI uses in this book would qualify, and how would the classification change for any influence where AI output can be verified against a formal constraint list before reaching a learner? *(Difficulty: high. Tests: extending the seven-dimension framework through principled analysis of a new structural property, with cross-chapter application.)*

### Challenge

**9.** You are Renee, presenting the district's phonics adoption plan to the state education department, which has funded the adoption under the new early-literacy law. The state's program officer wants to see "AI utilization metrics" in the quarterly report — specifically, app login rates, time-on-task, and in-app phonics level advancement. The state's rationale: these metrics demonstrate the science-of-reading mandate is being implemented with fidelity. Write the memo you send to the program officer: acknowledge the state's legitimate interest in implementation fidelity, explain why the requested metrics do not measure phonics learning or instructional fidelity as the research defines them, propose a replacement metric set that the state could collect and that would actually demonstrate the mandate is being implemented correctly, and close with the one question the state should add to its next site-visit protocol to verify that instruction — not just app coverage — is happening. *(Difficulty: challenge. Tests: translating the chapter's complete evidence framework into state-level policy advocacy, for a regulatory audience operating under a legislative mandate, with the goal of changing what the state measures without dismissing the state's legitimate interest.)*

## References

*Added by fact-check pass — all CONFIRMED via web verification (see factchecks/30-phonics-support-without-replacing-instruction-assertions.md).*

1. Ehri, L. C., Nunes, S. R., Stahl, S. A., & Willows, D. M. (2001). Systematic phonics instruction helps students learn to read. *Review of Educational Research*, 71(3), 393–447. https://journals.sagepub.com/doi/10.3102/00346543071003393
2. Bowers, J. S. (2020). Reconsidering the evidence that systematic phonics is more effective than alternative methods. *Educational Psychology Review*, 32(3), 681–705. https://link.springer.com/article/10.1007/s10648-019-09515-y
3. Fletcher, J. M., Savage, R., & Vaughn, S. (2021). A commentary on Bowers (2020). *Educational Psychology Review*, 33. https://eric.ed.gov/?id=EJ1310133
4. Hattie, J. (2018 update). Ranking of influences. https://visible-learning.org/hattie-ranking-influences-effect-sizes-learning-achievement/

---

## Prompts

### Figure 30.1 — Two phonics numbers and the grade-band moderator
Build a horizontal dot/lollipop plot comparing four phonics effect sizes on a shared x-axis in Cohen's d, range 0 to 0.8, zero baseline shown. Four rows, sorted descending by value: Hattie 2018 broad pooling (0.70), NRP/Ehri overall (0.41, highlighted), NRP K-1 subset (0.55), NRP after Grade 1 (0.27). Each row is a labeled lead line from zero to a terminal dot; encode value by dot x-position. Draw a vertical reference line at d = 0.40 labeled "0.40 hinge". Highlight the 0.41 row (the defensible anchor) with the accent color. Annotate the K-1 vs after-Grade-1 pair to make the timing moderator visible (e.g. a bracket noting "same intervention, half the effect"). Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 30.2 — Phonics mechanism stack and the AI/teacher split
Build a layered schematic: a vertical stack of five horizontal layer-bands from base to top — Phonemic awareness (base), Grapheme-phoneme mapping, Blending, Orthographic mapping, Automaticity (top). Bottom-to-top reading order indicates dependency. Alongside each band run two parallel role columns: left column = what AI supports at that layer (support, progress tracking, error/practice generation, assessment, practice/tracking), right column = what only a human teacher does (first teaching, first modeling, error diagnosis, reteaching, builds it). Use two distinct fills for the two role columns; layer bands share a neutral fill. The structural point: AI columns flank the stack but the teacher column builds it. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

### Figure 30.3 — Minute-audit: two configurations of the literacy block
Build a two-panel before/after stacked-bar comparison. Each panel is a single full-height stacked bar representing one weekly literacy block of constant total minutes (identical bar heights across panels — the constant is the point). Left panel "Teacher-led + app supplement": large explicit-instruction segment plus a small app-practice segment. Right panel "App-as-core": explicit-instruction segment near zero plus app-practice filling the bar. Use two segment fills (instruction vs. app practice); highlight the collapse of the explicit-instruction segment between panels. Shared y-axis labeled "One weekly literacy block (minutes)", zero baseline. Annotate that total minutes are unchanged while first-teaching vanishes. Deliverable: single standalone HTML file, inline CSS, D3 v7 pinned CDN, brutalist palette via CSS variables.

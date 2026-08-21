# Appendix 93: Hattie x AI Analysis Summary

This appendix summarizes the files in `data/` for the Visible Learning x AI project. The dataset starts from 252 Hattie influences, preserves their effect sizes, and adds an AI classification layer: AI feasibility, human irreducibility, substitution risk, mechanism conflict, vendor activity, categorical profile, and hypothetical AI-mediated effect notes.

The central finding is simple: the strongest Visible Learning influences are not the places where AI can replace human teaching. They are mostly the places where AI can make human judgment, feedback, practice, diagnosis, planning, and reflection more precise. The danger zone is substitution: using AI to remove the cognitive or relational work that made the influence powerful in the first place.

---

## File Inventory

| File | Role |
|---|---|
| `README.md` | Short map of current, appendix, and legacy data files. |
| `2018-updated-hattie-ranking-hatties-list-of-influences-effect-sizes-achievement-rangliste.png` | Source/reference image of the 2018 Hattie ranking list; 826 x 5604 PNG. |
| `hattie-ai-7dimensions-normalized.csv` | Current full coding dataset, 252 rows x 11 columns. Includes hypothetical effect notes. `substitution_risk=Moderate` has been normalized to `Medium`. |
| `hattie-ai-7dimensions.csv` | Original full coding dataset, retained for traceability. Same structure as the normalized file, but with both `Moderate` and `Medium` substitution-risk labels. |
| `hattie-ai-main-analysis.csv` | Main paper dataset, 252 rows x 10 columns. Same as the normalized dataset but without the hypothetical AI effect column. |
| `hattie-ai-hypothetical-effects-appendix.csv` | Appendix-only hypotheses about possible AI-mediated effect changes, 252 rows x 4 columns. These are analyst hypotheses, not observed effect sizes. |
| `hattie-ai-analysis-summary.md` | Existing headline summary of counts, bands, categorical profiles, vendor activity, and high-activity influences. |
| `hattie-ai-categorical-profiles-normalized.csv` | Row-level normalized dataset with `profile_id`, 252 rows x 12 columns. |
| `hattie-ai-categorical-profile-summary-normalized.csv` | Profile-level normalized summary, 78 profiles x 10 columns. Preferred current profile file. |
| `hattie-ai-band-by-feasibility.csv` | Crosstab for effect-size band by AI feasibility. |
| `hattie-ai-band-by-mechanism-conflict.csv` | Crosstab for effect-size band by mechanism conflict. |
| `hattie-ai-priority-review-cases.csv` | 62 high-priority cases for closer paper review. These are high or above-hinge influences with substitution, mechanism, or vendor concerns. |
| `hattie_ai_classification_first_pass.csv` | Legacy first-pass classification, 252 rows x 8 columns. Does not include substitution risk or mechanism conflict. |
| `hattie_ai_classification_first_pass.xlsx` | Excel copy of the same legacy first-pass classification. |
| `hattie-ai-clustered.csv` | Legacy row-level clustered dataset, 252 rows x 14 columns. |
| `hattie-ai-cluster-summary.csv` | Legacy cluster summary, 78 clusters x 8 columns. |
| `hattie-ai-cluster-groups.md` | Legacy narrative cluster-group summary. Prefer the normalized categorical-profile files for current analysis. |

---

## Dataset Structure

The current normalized full dataset contains 252 influences and these main fields:

| Field | Meaning |
|---|---|
| `rank` | Hattie rank order. |
| `influence` | Name of the educational influence. |
| `effect_size` | Hattie's reported effect size. |
| `band` | Effect-size band: High, Above hinge, Below hinge, Negligible, Harmful. |
| `ai_feasibility` | Whether the influence is AI-RESISTANT, AI-AUGMENTED, AI-ADJACENT, or AI-NATIVE. |
| `human_irreducibility` | How much the mechanism depends on human judgment, relationship, embodiment, or social presence. |
| `substitution_risk` | Risk that AI use will replace the mechanism rather than support it. |
| `mechanism_conflict` | Whether AI use conflicts with the causal mechanism of the influence. |
| `vendor_activity` | Whether current AI vendor activity is low, moderate, or high around the influence. |
| `hypothetical_ai_effect` | Analyst hypothesis about possible AI-mediated effect size, included only in appendix files. |
| `notes` | Rationale for classification. |

The normalization step affects only substitution-risk vocabulary. The original file had 22 rows coded `Moderate` and 7 rows coded `Medium`; the normalized file recodes the 22 `Moderate` rows to `Medium`, yielding 29 total `Medium` substitution-risk cases.

---

## Headline Counts

### AI Feasibility

| Category | n | Share |
|---|---:|---:|
| AI-ADJACENT | 97 | 38.5% |
| AI-AUGMENTED | 88 | 34.9% |
| AI-RESISTANT | 38 | 15.1% |
| AI-NATIVE | 29 | 11.5% |

Most influences are not AI-native. Nearly three quarters are either AI-adjacent or AI-augmented. This matters for book framing: AI is usually a support layer around teaching and learning mechanisms, not the mechanism itself.

### Human Irreducibility

| Category | n | Share |
|---|---:|---:|
| Low | 117 | 46.4% |
| Medium | 78 | 31.0% |
| High | 57 | 22.6% |

Almost one quarter of the list is highly human-irreducible. These are the cases where AI may help with preparation, monitoring, documentation, or pattern detection, but the decisive work remains relational, embodied, ethical, or pedagogical.

### Substitution Risk

| Category | n | Share |
|---|---:|---:|
| Low | 170 | 67.5% |
| Medium | 29 | 11.5% |
| High | 53 | 21.0% |

The majority of cases have low substitution risk, but the 53 high-risk cases are strategically important because many sit near influential practices that vendors are likely to automate.

### Mechanism Conflict

| Category | n | Share |
|---|---:|---:|
| No conflict | 169 | 67.1% |
| Partial conflict | 48 | 19.0% |
| Conflict present | 35 | 13.9% |

Two thirds of influences have no direct mechanism conflict with AI use. The problem is not "AI in education" as a category. The problem is AI crossing the phase gate and doing the cognitive or social work that produces the learning effect.

### Vendor Activity

| Category | n | Share |
|---|---:|---:|
| Low | 229 | 90.9% |
| Moderate | 11 | 4.4% |
| High | 12 | 4.8% |

Vendor activity is concentrated. Most Hattie influences are not yet direct product battlegrounds, but the ones that are active include high-impact areas such as feedback, scaffolding, response to intervention, writing, intelligent tutoring systems, and mastery learning.

### Effect-Size Bands

| Band | n | Share |
|---|---:|---:|
| High | 32 | 12.7% |
| Above hinge | 90 | 35.7% |
| Below hinge | 81 | 32.1% |
| Negligible | 32 | 12.7% |
| Harmful | 17 | 6.7% |

There are 122 influences at or above the hinge point of d >= 0.40. The average effect size across all 252 influences is approximately d = 0.379, with a median of d = 0.375, a minimum of d = -0.90, and a maximum of d = 1.57.

---

## What Happens Above the Hinge Point

Among the 122 influences at or above d = 0.40:

| Dimension | Pattern |
|---|---|
| AI feasibility | 81 AI-AUGMENTED, 18 AI-RESISTANT, 14 AI-NATIVE, 9 AI-ADJACENT |
| Mechanism conflict | 63 no conflict, 38 partial conflict, 21 conflict present |
| Human irreducibility | 72 medium, 27 high, 23 low |
| Substitution risk | 68 low, 36 high, 18 medium |
| Vendor activity | 100 low, 11 high, 11 moderate |

The above-hinge set is dominated by AI-augmented practices. This is the main design implication: the best AI strategy is usually not replacement, but amplification of feedback, metacognition, practice, task analysis, planning, prediction, formative evaluation, and instructional clarity.

Among the 32 high-band influences, the same pattern intensifies:

| Dimension | Pattern |
|---|---|
| AI feasibility | 24 AI-AUGMENTED, 4 AI-NATIVE, 3 AI-RESISTANT, 1 AI-ADJACENT |
| Mechanism conflict | 17 no conflict, 11 partial conflict, 4 conflict present |
| Human irreducibility | 19 medium, 8 high, 5 low |
| Substitution risk | 17 low, 8 high, 7 medium |
| Vendor activity | 23 low, 6 high, 3 moderate |

The highest-impact end of the list is therefore not a simple technology story. It is a phase-gate story. AI can help, but it must not be allowed to replace the learner's metacognitive act, the teacher's situated judgment, or the peer/social mechanism where that mechanism is the source of the effect.

---

## Cross-Tab: Effect Band by AI Feasibility

| Band | AI-ADJACENT | AI-AUGMENTED | AI-NATIVE | AI-RESISTANT |
|---|---:|---:|---:|---:|
| High | 1 | 24 | 4 | 3 |
| Above hinge | 8 | 57 | 10 | 15 |
| Below hinge | 51 | 2 | 13 | 15 |
| Negligible | 27 | 1 | 2 | 2 |
| Harmful | 10 | 4 | 0 | 3 |

Interpretation: AI-native influences exist, but they are not the bulk of high-impact learning. The high and above-hinge zones are concentrated in AI-augmented practices.

---

## Cross-Tab: Effect Band by Mechanism Conflict

| Band | No conflict | Partial conflict | Conflict present |
|---|---:|---:|---:|
| High | 17 | 11 | 4 |
| Above hinge | 46 | 27 | 17 |
| Below hinge | 64 | 6 | 11 |
| Negligible | 29 | 2 | 1 |
| Harmful | 13 | 2 | 2 |

Interpretation: many strong influences can be supported by AI without direct mechanism conflict, but the partial-conflict cases are where the book's phase-gate language matters most. AI can prepare, prompt, monitor, or scaffold; the human still must perform the learning-producing act.

---

## Largest Categorical Profiles

The normalized profile summary groups rows by band, AI feasibility, human irreducibility, substitution risk, mechanism conflict, and vendor activity. There are 78 normalized categorical profiles.

| Profile | n | Mean d | Signature |
|---|---:|---:|---|
| P01 | 38 | 0.27 | Below hinge / AI-ADJACENT / Low irreducibility / Low substitution risk / No conflict / Low vendor activity |
| P02 | 22 | 0.08 | Negligible / AI-ADJACENT / Low irreducibility / Low substitution risk / No conflict / Low vendor activity |
| P03 | 21 | 0.50 | Above hinge / AI-AUGMENTED / Medium irreducibility / Low substitution risk / No conflict / Low vendor activity |
| P04 | 11 | 0.50 | Above hinge / AI-AUGMENTED / Medium irreducibility / Low substitution risk / Partial conflict / Low vendor activity |
| P05 | 9 | 0.25 | Below hinge / AI-NATIVE / Low irreducibility / High substitution risk / No conflict / Low vendor activity |
| P06 | 6 | 0.89 | High / AI-AUGMENTED / Medium irreducibility / Low substitution risk / Partial conflict / Low vendor activity |
| P07 | 6 | 0.52 | Above hinge / AI-ADJACENT / Low irreducibility / Low substitution risk / No conflict / Low vendor activity |
| P08 | 6 | -0.21 | Harmful / AI-ADJACENT / Low irreducibility / Low substitution risk / No conflict / Low vendor activity |
| P09 | 5 | 0.54 | Above hinge / AI-RESISTANT / High irreducibility / High substitution risk / Conflict present / Low vendor activity |
| P10 | 5 | 0.48 | Above hinge / AI-AUGMENTED / Medium irreducibility / Medium substitution risk / No conflict / Low vendor activity |

The largest single profile is below-hinge, AI-adjacent, low-conflict work. The most important profile for the book's positive argument is P03/P04: above-hinge, AI-augmented practices where AI can help if it does not take over the cognitive work.

---

## Priority Review Cases

The `hattie-ai-priority-review-cases.csv` file identifies 62 cases needing closer paper review. These are not necessarily "bad" AI cases. They are the cases where the effect is large enough, or the substitution/mechanism/vendor risk is high enough, that the book should treat the classification carefully.

Priority review cases by band:

| Band | n |
|---|---:|
| High | 18 |
| Above hinge | 44 |

Priority review cases by AI feasibility:

| AI feasibility | n |
|---|---:|
| AI-AUGMENTED | 39 |
| AI-RESISTANT | 18 |
| AI-NATIVE | 5 |

Priority review cases by mechanism conflict:

| Mechanism conflict | n |
|---|---:|
| Partial conflict | 38 |
| Conflict present | 21 |
| No conflict | 3 |

The top priority cases include:

| Rank | Influence | d | AI feasibility | Human irreducibility | Substitution risk | Mechanism conflict | Vendor activity |
|---:|---|---:|---|---|---|---|---|
| 1 | Collective teacher efficacy | 1.57 | AI-RESISTANT | High | High | No conflict | Low |
| 2 | Self-reported grades | 1.33 | AI-AUGMENTED | Medium | Low | Partial conflict | Low |
| 5 | Response to intervention | 1.29 | AI-AUGMENTED | Medium | Medium | No conflict | High |
| 7 | Jigsaw method | 1.20 | AI-RESISTANT | High | High | Conflict present | Low |
| 10 | Strategy to integrate with prior knowledge | 0.93 | AI-AUGMENTED | Medium | Low | Partial conflict | High |
| 11 | Self-efficacy | 0.92 | AI-AUGMENTED | Medium | Low | Partial conflict | Low |
| 12 | Teacher credibility | 0.90 | AI-RESISTANT | High | High | Conflict present | Low |
| 13 | Micro-teaching/video review of lessons | 0.88 | AI-AUGMENTED | Medium | Medium | No conflict | High |
| 14 | Transfer strategies | 0.86 | AI-AUGMENTED | Medium | Low | Partial conflict | Low |
| 15 | Classroom discussion | 0.82 | AI-AUGMENTED | High | High | Conflict present | Moderate |
| 16 | Scaffolding | 0.82 | AI-AUGMENTED | Medium | Medium | Partial conflict | High |
| 17 | Deliberate practice | 0.79 | AI-AUGMENTED | Medium | Medium | Partial conflict | Low |
| 18 | Summarization | 0.79 | AI-NATIVE | Low | High | Conflict present | Low |
| 22 | Planning and prediction | 0.76 | AI-AUGMENTED | Medium | Low | Partial conflict | High |
| 32 | Feedback | 0.70 | AI-AUGMENTED | Medium | High | Partial conflict | High |

These are the cases most likely to carry the book's argument. They show that AI can produce leverage in precisely the places where it can also hollow out learning if used as a substitute.

---

## High and Moderate Vendor Activity

Only 23 influences have moderate or high vendor activity. They are strategically important because they show where the market is most likely to push schools toward AI adoption.

High vendor-activity influences include:

| Rank | Influence | d | Band | AI feasibility | Substitution risk | Mechanism conflict |
|---:|---|---:|---|---|---|---|
| 5 | Response to intervention | 1.29 | High | AI-AUGMENTED | Medium | No conflict |
| 10 | Strategy to integrate with prior knowledge | 0.93 | High | AI-AUGMENTED | Low | Partial conflict |
| 13 | Micro-teaching/video review of lessons | 0.88 | High | AI-AUGMENTED | Medium | No conflict |
| 16 | Scaffolding | 0.82 | High | AI-AUGMENTED | Medium | Partial conflict |
| 22 | Planning and prediction | 0.76 | High | AI-AUGMENTED | Low | Partial conflict |
| 32 | Feedback | 0.70 | High | AI-AUGMENTED | High | Partial conflict |
| 46 | Meta-cognitive strategies | 0.60 | Above hinge | AI-AUGMENTED | Low | Partial conflict |
| 57 | Mastery learning | 0.57 | Above hinge | AI-AUGMENTED | High | Partial conflict |
| 89 | Intelligent tutoring systems | 0.48 | Above hinge | AI-NATIVE | High | Partial conflict |
| 97 | Writing programs | 0.45 | Above hinge | AI-AUGMENTED | High | Partial conflict |
| 114 | Technology in writing | 0.42 | Above hinge | AI-NATIVE | High | Conflict present |
| 159 | Homework | 0.29 | Below hinge | AI-RESISTANT | High | Conflict present |

This list is useful for chapter planning because it marks where readers are most likely to encounter products, sales claims, and institutional pressure.

---

## AI-Native Influences

There are 29 AI-native influences. The highest-ranked include summarization, mnemonics, repeated reading programs, rehearsal and memorization, vocabulary programs, spelling programs, technology with learning-needs students, practice testing, interactive video methods, intelligent tutoring systems, and technology in writing.

The AI-native category should not be interpreted as "safe to automate." Some AI-native cases have high substitution risk or mechanism conflict. For example, summarization is high impact but high risk when students let AI perform the summarizing instead of doing the condensation and selection work themselves. Practice testing can be highly useful when it preserves retrieval effort; it becomes weaker when the system supplies answers too quickly.

---

## AI-Resistant Above-Hinge Influences

There are 18 AI-resistant influences at or above the hinge point. They include:

| Rank | Influence | d | Why it matters |
|---:|---|---:|---|
| 1 | Collective teacher efficacy | 1.57 | Collective professional trust and responsibility cannot be automated. |
| 7 | Jigsaw method | 1.20 | The peer teaching exchange is the mechanism. |
| 12 | Teacher credibility | 0.90 | Credibility is relational and situated. |
| 42 | Behavioral intervention programs | 0.62 | Intervention depends on human context, trust, and delivery. |
| 64 | Cooperative vs. individualistic learning | 0.55 | The cooperative structure is social, not merely informational. |
| 70 | Positive peer influences | 0.53 | Peer influence depends on real group dynamics. |
| 75 | Teacher-student relationships | 0.52 | The relationship itself is the active ingredient. |
| 101 | Strong classroom cohesion | 0.44 | Cohesion is an emergent property of a group. |
| 120 | Cooperative learning | 0.40 | AI can structure, but it cannot be the cooperation. |

These cases are the book's strongest evidence against replacement logic. AI may document, prompt, recommend grouping, or surface evidence, but the effect comes from social and human mechanisms.

---

## Hypothetical AI Effects Appendix

The hypothetical-effects file contains 252 analyst hypotheses about possible AI-mediated effects. These should be treated as interpretive notes, not empirical estimates.

Examples from the top of the list:

| Rank | Influence | Original d | Hypothetical note |
|---:|---|---:|---|
| 1 | Collective teacher efficacy | 1.57 | AI dashboard only; collective trust cannot be automated. |
| 2 | Self-reported grades | 1.33 | AI prompts reflection, but the student must retain metacognitive ownership. |
| 3 | Teacher estimates of achievement | 1.29 | AI risk-flagging supports but cannot replace localized teacher judgment. |
| 4 | Cognitive task analysis | 1.29 | AI can map task hierarchies; human experts must validate domain accuracy. |
| 5 | Response to intervention | 1.29 | AI tier-tracking is legitimate; physical intervention delivery remains human. |
| 7 | Jigsaw method | 1.20 | AI group-composition optimization only; peer teaching exchange must be human. |
| 10 | Strategy to integrate with prior knowledge | 0.93 | AI schema-mapping is promising, but analogies must connect to the student's actual prior knowledge. |

Use this file as a hypothesis generator for the book's argument, not as a results table.

---

## Legacy Files and Traceability

The first-pass classification files (`hattie_ai_classification_first_pass.csv` and `.xlsx`) include 252 rows and 8 columns: rank, influence, effect size, band, AI feasibility, human irreducibility, vendor activity, and notes. They do not include substitution risk or mechanism conflict.

The legacy cluster files (`hattie-ai-clustered.csv`, `hattie-ai-cluster-summary.csv`, and `hattie-ai-cluster-groups.md`) group the same 252 influences into 78 clusters using older terminology. The current analysis should prefer the normalized categorical-profile files, but the cluster files remain useful for auditing how the profile logic developed.

---

## Interpretation for the Book

The data supports four claims that should shape *Visible Learning x AI*.

First, AI is most powerful as augmentation, not replacement. The high and above-hinge bands are dominated by AI-augmented influences. That means the design question is not whether AI can "teach," but where it can improve diagnosis, feedback, practice, planning, reflection, and formative evaluation while preserving the learner's and teacher's active work.

Second, the phase gate is the decisive design principle. Partial-conflict influences are not off limits; they require explicit boundaries. AI can prepare a prompt, generate practice items, surface misconceptions, or organize evidence. The learner must still retrieve, explain, summarize, reflect, discuss, and revise. The teacher must still judge, relate, intervene, and orchestrate.

Third, vendor activity is concentrated in attractive but risky zones. Feedback, scaffolding, writing, intelligent tutoring, and mastery learning are plausible AI product categories because they are high leverage. They are also places where bad implementation can confuse output quality with learning quality.

Fourth, the human-irreducible cases are not marginal. Collective teacher efficacy, teacher credibility, jigsaw, teacher-student relationships, cooperative learning, classroom cohesion, peer influence, and family/home dynamics show that many powerful effects are social systems. AI can support those systems, but it cannot become them.

The practical conclusion is not "less AI." It is better division of labor: AI for pattern work, retrieval, scaffolding, monitoring, and generation; humans for judgment, relationship, metacognition, causal interpretation, and accountability.


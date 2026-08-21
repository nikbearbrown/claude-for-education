# TYPECHECK.md — GATE T

Reel: `claude-liam-two-numbers-one-report-short`  |  Checked: 2026-08-20T09:03  |  Overall: PASS  |  Beats checked: 16  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | — | no video | SKIP | — |
| B01 | ? | — | no-wordy-card §8.5: ChipGrid: per-element check passed (max 12 words in 'sparkLine') | PASS | — |
| B02 | ? | — | no video | SKIP | — |
| B03 | ? | — | no video | SKIP | — |
| B04 | ? | — | no-wordy-card §8.5: 2 element(s), 16 words — within budget. Detail: 'left.note' (7 words);… | PASS | — |
| B05 | ? | — | no video | SKIP | — |
| B06 | ? | — | no-wordy-card §8.5: pull-quote (12 words ≤ 12) | PASS | — |
| B07 | ? | — | no video | SKIP | — |
| BRA | ? | — | no video | SKIP | — |
| B08 | ? | — | no video | SKIP | — |
| B09 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | ? | — | no-wordy-card §8.5: 2 element(s), 17 words — within budget. Detail: 'left.note' (9 words);… | PASS | — |
| B12 | ? | — | no video | SKIP | — |
| B15 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| BOUT | ? | — | no video | SKIP | — |
| END | ? | — | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 6 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| contrast-local §8.3b | 0 | 0 |
| bbox-overlap §8.6b | 0 | 0 |
| card-clip §8.13 | 0 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*

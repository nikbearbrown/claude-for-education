# TYPECHECK.md — GATE T

Reel: `claude-liam-two-numbers-one-report`  |  Checked: 2026-08-20T08:42  |  Overall: PASS  |  Beats checked: 24  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [BVDT] narration recites the card (0.97) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 12 words in 'sparkLine') | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B03 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B04 | ? | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'note') | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 38px >= floor 35px | PASS | — |
| B06 | ? | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 12 words in 'note') | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 48px >= floor 35px | PASS | — |
| BRA | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| BRM | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B09 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 43px >= floor 35px | PASS | — |
| B11 | ? | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 12 words in 'right.note') | PASS | — |
| B12 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B13 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | ? | light | min-size §8.1: min text-run height 37px >= floor 35px | PASS | — |
| B15 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B17 | ? | light | min-size §8.1: min text-run height 38px >= floor 35px | PASS | — |
| BDTL | ? | light | min-size §8.1: min text-run height 54px >= floor 35px | PASS | — |
| BVDT | ? | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| BHTF | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | ? | light | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 7 | 0 |
| min-size §8.1 | 24 | 0 |
| overflow §8.2 | 24 | 0 |
| contrast §8.3 | 24 | 0 |
| contrast-local §8.3b | 24 | 0 |
| bbox-overlap §8.6b | 24 | 0 |
| card-clip §8.13 | 24 | 0 |
| kerning §8.4 | 9 | 0 |
| redundancy §8.10 (advisory) | 1 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*

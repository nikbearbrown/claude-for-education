# TYPECHECK.md — GATE T

Reel: `claude-liam-the-lever-nobody-pulled`  |  Checked: 2026-08-04T23:56  |  Overall: PASS  |  Beats checked: 23  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B01 | ? | min-size §8.1: min text-run height 49px >= floor 35px | PASS | — |
| B02 | ? | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B03 | ? | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B04 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B05 | ? | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B06 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B07 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B08 | ? | min-size §8.1: min text-run height 193px >= floor 35px | PASS | — |
| B09 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B10 | ? | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B11 | ? | min-size §8.1: min text-run height 42px >= floor 35px | PASS | — |
| B12 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B13 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B15 | ? | min-size §8.1: min text-run height 247px >= floor 35px | PASS | — |
| B16 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B17 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B18 | ? | min-size §8.1: min text-run height 38px >= floor 35px | PASS | — |
| B19 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| BVDT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |
| BHTF | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 23 | 0 |
| overflow §8.2 | 23 | 0 |
| contrast §8.3 | 23 | 0 |
| contrast-local §8.3b | 23 | 0 |
| bbox-overlap §8.6b | 23 | 0 |
| kerning §8.4 | 16 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*

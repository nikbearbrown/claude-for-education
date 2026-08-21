# SHARPNESS GATE — short

Compiled master: `claude-liam-the-lever-nobody-pulled-short.mp4`
Median Laplacian variance: **24.8**
Failure threshold: 12.4 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 95.1 | 383% | PASS — 383% |
| B01 | 28.3 | 114% | PASS — 114% |
| B02 | 67.0 | 270% | PASS — 270% |
| B03 | 24.2 | 98% | PASS — 98% |
| B06 | 100.7 | 405% | PASS — 405% |
| B09 | 12.5 | 50% | PASS — 50% |
| B11 | 12.0 | 48% | SKIP (exempt — no pixel-art rotation possible) |
| B14 | 17.1 | 69% | PASS — 69% |
| BVDT | 111.8 | 450% | PASS — 450% |
| BOUT | 24.8 | 100% | PASS — 100% |
| END | 6.2 | 25% | SKIP (exempt — no pixel-art rotation possible) |

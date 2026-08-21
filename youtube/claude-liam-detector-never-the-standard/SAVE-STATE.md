# SAVE-STATE — content-prop sentinel fix (Part B of detector session)
**Saved:** 2026-08-17

---

1. **Primary Request and Intent:**

   Complete the four-part repo-wide content-prop sentinel fix (REMOTION-STANDARDS §6). Triggered by finding `segment: 'Photoelectric Effect'` in Root.tsx defaultProps, which caused a plagiarism reel to render "Photoelectric Effect" as its subtitle when the beat sheet omitted the prop.

   **Hard constraints (carried over):**
   - Detector reel constraints from prior SAVE-STATE remain in effect
   - STANDING ORDER: slate cut only, no art final/post/publish autonomously

2. **Key Technical Concepts:**
   - REMOTION-STANDARDS §6: every content-prop schema `.default()` must be `'⚠ SET IN BEAT SHEET'` (or `['⚠ SET IN BEAT SHEET']` for arrays). Never plausible copy.
   - Demo twins (`*Demo.tsx`, `Demo*`) are exempt — their filled props are the job.
   - `content_default_check.py` — the tier-0 gate: fast, file-local, exit 2 on violation.
   - Regex fix: `[^;{]*?` → `[^\n;{]*?` to prevent cross-line false positives (CCPlanCard `items.default([])` was spuriously matching against `title`).

3. **Files and Code Sections:**

   - **`brutalist-art/runtime/qc/content_default_check.py`** — NEW. Tier-0 check; `--all` scans all 573 scene files. Exit 2 on violation, exit 0 clean.
   - **`brutalist-art/art`** — added `check` subcommand: dispatches to `content_default_check.py`.
   - **`books/.claude/hooks/postedit-check.sh`** — `.tsx` section upgraded from advisory-only to blocking (exit 2). Now calls `content_default_check.py` on every write to a Remotion scene file.
   - **`runtime/remotion/src/scenes/*.tsx`** — ~492 content-prop defaults changed across ~471 files in two passes:
     - Pass 1 (prior session agent): ~98 props in ~90 files
     - Pass 2 (bulk fix this session): 393 props in 380 files
     - ClaudeWindow.tsx `artifactLines`: `default([])` → `default(['⚠ SET IN BEAT SHEET'])`
   - **Root.tsx** (prior session): ClaudeComposerAsk + ClaudeComposerAsk916 defaultProps fixed — `segment`/`command`/`greeting`/`runningText` → sentinel.

4. **Current State:**
   - `content_default_check.py --all` → **PASS — 573 file(s) clean**
   - `art check --all` subcommand wired and working
   - `postedit-check.sh` blocking on content-prop violations in `.tsx` scene files
   - Detector reel B00/BHTF: all six required ClaudeComposerAsk props set; reel unaffected by sentinel change

5. **Re-render Bug List (bugs FOUND, not introduced):**

   | Component | Missing prop | Beats affected | Was silently showing |
   |---|---|---|---|
   | `ClaudeWindow` | `artifactTitle` | 240 | `'Verdict'` |
   | `ClaudeWindow` | `artifactHeading` | 241 | `'The verdict'` |
   | `ClaudeWindow` | `artifactLines` | 217 | empty (nothing) |
   | `ClaudeComposerAsk` | `greeting` | 1,695 | Root.tsx plausible default |
   | `NikBearBrownTerminalAsk` | `runningText` | 10 | plausible default |
   | `MedhavyConceptCard/PredictCard/ShellSession` | — | 0 | CLEAN |

   Already-compiled mp4s are unaffected. Sentinel shows only on re-render of affected beats.

6. **Pending:**
   - No pending build tasks for the sentinel fix or detector reel.
   - The 1,695 ClaudeComposerAsk greeting gaps and 240/241/217 ClaudeWindow gaps are known bugs requiring beat-sheet fixes per reel before re-render.

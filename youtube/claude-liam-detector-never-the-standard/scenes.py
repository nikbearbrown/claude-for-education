from manim import *
import numpy as np

BG   = ManimColor("#FAF9F5")
INK  = ManimColor("#3D3929")
ACC  = ManimColor("#D97757")  # terracotta
SOFT = ManimColor("#73705F")
GHOST= ManimColor("#A9A491")
GREEN= ManimColor("#4A7C59")

def src(label="Pseudonymous analysis, 2023 — not independently verified"):
    return Text(label, font_size=10, color=GHOST).to_corner(DR, buff=0.85)


# ── CARD beats ────────────────────────────────────────────────────────────────

class B01_ActTrace(Scene):
    def construct(self):
        self.camera.background_color = BG
        rule_top = Line(LEFT*4, RIGHT*4, color=ACC, stroke_width=2).shift(UP*0.3)
        act   = Text("ACT I", font_size=22, color=ACC, font="EB Garamond").next_to(rule_top, UP, buff=0.25)
        title = Text("The Trace", font_size=52, color=INK, font="EB Garamond").next_to(rule_top, DOWN, buff=0.3)
        sub   = Text("Where the evidence came from, and where it ended.",
                     font_size=18, color=SOFT, font="EB Garamond").next_to(title, DOWN, buff=0.35)
        rule_bot = Line(LEFT*3, RIGHT*3, color=GHOST, stroke_width=1).shift(DOWN*2.2)
        self.play(FadeIn(rule_top), FadeIn(act), run_time=0.4)   # state 1: {top_rule}
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.4)
        self.play(FadeIn(rule_bot), run_time=0.3)                 # state 2: {top_rule, bot_rule}
        self.wait(1.5)


class B16_ActRules(Scene):
    def construct(self):
        self.camera.background_color = BG
        rule = Line(LEFT*4, RIGHT*4, color=ACC, stroke_width=2).shift(UP*0.3)
        act  = Text("ACT III", font_size=22, color=ACC, font="EB Garamond").next_to(rule, UP, buff=0.25)
        title= Text("The Rules of 2026", font_size=48, color=INK, font="EB Garamond").next_to(rule, DOWN, buff=0.3)
        rule_bot = Line(LEFT*3, RIGHT*3, color=GHOST, stroke_width=1).shift(DOWN*2.2)
        self.play(FadeIn(rule), FadeIn(act), run_time=0.4)   # state 1: {rule}
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(rule_bot), run_time=0.3)             # state 2: {rule, rule_bot}
        self.wait(2.0)


class B24_ActCounterfactual(Scene):
    def construct(self):
        self.camera.background_color = BG
        rule = Line(LEFT*4, RIGHT*4, color=ACC, stroke_width=2).shift(UP*0.3)
        act  = Text("ACT IV", font_size=22, color=ACC, font="EB Garamond").next_to(rule, UP, buff=0.25)
        title= Text("The Counterfactual", font_size=46, color=INK, font="EB Garamond").next_to(rule, DOWN, buff=0.3)
        rule_bot = Line(LEFT*3, RIGHT*3, color=GHOST, stroke_width=1).shift(DOWN*2.2)
        self.play(FadeIn(rule), FadeIn(act), run_time=0.4)   # state 1: {rule}
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(rule_bot), run_time=0.3)             # state 2: {rule, rule_bot}
        self.wait(1.0)


# ── MANIM beats ───────────────────────────────────────────────────────────────

class B05_MatchCount(Scene):
    """322 matched sentences / 179 twelve-word pairs — from one unverified analysis."""
    def construct(self):
        self.camera.background_color = BG
        self.add(src())

        title = Text("What the analysis found", font_size=24, color=SOFT).to_edge(UP, buff=0.65)
        self.play(FadeIn(title))

        n322  = Text("322", font_size=120, color=INK, font="EB Garamond")
        lbl322= Text("matched sentences", font_size=22, color=SOFT).next_to(n322, DOWN, buff=0.15)
        left  = VGroup(n322, lbl322).shift(LEFT*2.8)

        div   = Line(UP*2, DOWN*2, color=GHOST, stroke_width=1.5)

        n179  = Text("179", font_size=120, color=ACC, font="EB Garamond")
        lbl179= Text("pairs: 12+ identical words", font_size=20, color=SOFT).next_to(n179, DOWN, buff=0.15)
        right = VGroup(n179, lbl179).shift(RIGHT*2.8)

        caveat= Text("One pseudonymous analysis — not independently replicated.",
                     font_size=13, color=GHOST, slant=ITALIC
                     ).to_edge(DOWN, buff=1.1)
        accent = Line(LEFT*1.2, RIGHT*1.2, color=ACC, stroke_width=1.5).shift(DOWN*2.6)

        self.play(FadeIn(left), run_time=0.6)
        self.play(Create(div), run_time=0.3)          # state 1: {div}
        self.play(FadeIn(right), run_time=0.6)
        self.play(FadeIn(caveat))
        self.play(FadeIn(accent), run_time=0.2)       # state 2: {div, accent}
        self.wait(12)


class B06_Concentration(Scene):
    """20.8% intro/lit-rev vs 1.1% methods/findings."""
    def construct(self):
        self.camera.background_color = BG
        self.add(src())

        title = Text("Where the overlap concentrated", font_size=24, color=SOFT).to_edge(UP, buff=0.65)
        self.play(FadeIn(title))

        sections  = ["Introduction &\nLit Review", "Methods &\nFindings"]
        percents  = [20.8, 1.1]
        colours   = [ACC, GHOST]
        max_h     = 4.0

        base_y = -1.8
        bar_w  = 1.6
        positions= [-2.2, 2.2]

        bars = []
        for i, (sec, pct, col, px) in enumerate(zip(sections, percents, colours, positions)):
            h = max(pct / 25 * max_h, 0.06)
            bar = Rectangle(width=bar_w, height=h,
                            fill_color=col, fill_opacity=0.85,
                            stroke_color=col, stroke_width=0)
            bar.move_to([px, base_y + h/2, 0])

            pct_lbl = Text(f"{pct}%", font_size=38, color=col, font="EB Garamond")
            pct_lbl.next_to(bar, UP, buff=0.2)

            sec_lbl = Text(sec, font_size=16, color=SOFT, line_spacing=1.1)
            sec_lbl.move_to([px, base_y - 0.55, 0])

            bars.append(VGroup(bar, pct_lbl, sec_lbl))

        baseline = Line(LEFT*4.5, RIGHT*4.5, color=INK, stroke_width=1.5).move_to([0, base_y, 0])
        self.play(Create(baseline))

        for g in bars:
            self.play(GrowFromEdge(g[0], DOWN), FadeIn(g[1]), FadeIn(g[2]), run_time=0.7)

        note = Text("His own fieldwork lives in the low bar.", font_size=16, color=INK
                    ).to_edge(DOWN, buff=1.1)
        self.play(FadeIn(note))
        self.wait(9)


class B09_SimilarityScore(Scene):
    """What a similarity score actually measures."""
    def construct(self):
        self.camera.background_color = BG

        header = Text("What the instrument measures", font_size=22, color=SOFT).to_edge(UP, buff=0.6)
        self.play(FadeIn(header))

        box = RoundedRectangle(width=8.5, height=2.5, corner_radius=0.15,
                               fill_color=ManimColor("#F0EDE4"), fill_opacity=1,
                               stroke_color=GHOST, stroke_width=1.5)
        measure = Text(
            "How much of this document\nalready exists somewhere else.",
            font_size=34, color=INK, font="EB Garamond", line_spacing=1.3
        )
        group = VGroup(box, measure).arrange(ORIGIN).shift(UP*0.3)
        self.play(FadeIn(box), run_time=0.4)
        self.play(FadeIn(measure), run_time=0.6)

        not_measure = Text("Not: did this author steal from that one.",
                           font_size=20, color=ACC).to_edge(DOWN, buff=1.4)
        divider = Line(LEFT*3.5, RIGHT*3.5, color=GHOST, stroke_width=1).shift(DOWN*1.0)
        self.play(FadeIn(not_measure))
        self.play(FadeIn(divider), run_time=0.2)      # state 2: {box, divider}
        self.wait(7)


class B11_NearControl(Scene):
    """Control thesis: zero matches at high threshold vs matched pair."""
    def construct(self):
        self.camera.background_color = BG
        self.add(src())

        title = Text("What background noise looks like", font_size=22, color=SOFT).to_edge(UP, buff=0.65)
        self.play(FadeIn(title))

        labels = ["Another reflective-\npractice thesis\n(control)", "The matched\npair"]
        values = [0, 16.1]
        colours= [GHOST, ACC]
        base_y = -1.6
        bar_w  = 1.8
        positions = [-2.5, 2.5]
        max_h  = 3.8

        baseline = Line(LEFT*5, RIGHT*5, color=INK, stroke_width=1.5).move_to([0, base_y, 0])
        self.play(Create(baseline))

        for i, (lbl, val, col, px) in enumerate(zip(labels, values, colours, positions)):
            h = max(val / 20 * max_h, 0.06)
            bar = Rectangle(width=bar_w, height=h,
                            fill_color=col, fill_opacity=0.85,
                            stroke_color=col, stroke_width=0)
            bar.move_to([px, base_y + h/2, 0])

            v_lbl = Text(f"{val}", font_size=36, color=col, font="EB Garamond")
            v_lbl.next_to(bar, UP, buff=0.2)

            sec_lbl = Text(lbl, font_size=15, color=SOFT, line_spacing=1.1)
            sec_lbl.move_to([px, base_y - 0.7, 0])

            self.play(GrowFromEdge(bar, DOWN), FadeIn(v_lbl), FadeIn(sec_lbl), run_time=0.8)

        unit = Text("matches per million pairs at 12-word threshold", font_size=14, color=GHOST
                    ).to_edge(DOWN, buff=1.1)
        silence = Text("The control returns silence.", font_size=18, color=INK
                       ).next_to(unit, UP, buff=0.3)
        self.play(FadeIn(silence), FadeIn(unit))
        self.wait(9)


class B12_Ratio(Scene):
    """16.1 vs 0.009 per million — ~1800×."""
    def construct(self):
        self.camera.background_color = BG
        self.add(src())

        title = Text("Twelve-identical-words metric", font_size=22, color=SOFT).to_edge(UP, buff=0.65)
        self.play(FadeIn(title))

        # Log-scale visual: show as proportional heights with actual labels
        labels = ["Controls\n(0.009/M)", "Matched pair\n(16.1/M)"]
        values = [0.009, 16.1]
        log_v  = [np.log10(v + 0.001) + 3.5 for v in values]  # shift to positive
        colours= [GHOST, ACC]
        base_y = -1.6
        bar_w  = 1.8
        positions = [-2.5, 2.5]

        scale = 0.8
        baseline = Line(LEFT*5, RIGHT*5, color=INK, stroke_width=1.5).move_to([0, base_y, 0])
        self.play(Create(baseline))

        for lbl, lv, col, px in zip(labels, log_v, colours, positions):
            h = max(lv * scale, 0.06)
            bar = Rectangle(width=bar_w, height=h,
                            fill_color=col, fill_opacity=0.85,
                            stroke_color=col, stroke_width=0)
            bar.move_to([px, base_y + h/2, 0])
            sec_lbl = Text(lbl, font_size=16, color=SOFT, line_spacing=1.1)
            sec_lbl.move_to([px, base_y - 0.7, 0])
            self.play(GrowFromEdge(bar, DOWN), FadeIn(sec_lbl), run_time=0.7)

        ratio = Text("~1,800×", font_size=64, color=ACC, font="EB Garamond").shift(UP*0.5)
        self.play(FadeIn(ratio))

        scale_note = Text("(log scale — bars proportional to log₁₀ of value)",
                          font_size=12, color=GHOST).to_edge(DOWN, buff=1.2)
        caveat = Text("From the same single, unverified analysis.",
                      font_size=13, color=GHOST, slant=ITALIC).next_to(scale_note, UP, buff=0.15)
        self.play(FadeIn(scale_note), FadeIn(caveat))
        self.wait(7)


class B18_PolicyDeclaration(Scene):
    """Institution permits generative tools with declaration."""
    def construct(self):
        self.camera.background_color = BG

        header = Text("Policy (paraphrased)", font_size=18, color=GHOST).to_edge(UP, buff=0.65)
        self.play(FadeIn(header))

        lines = [
            ("Generative tools:", INK),
            ("PERMITTED", ACC),
            ("with mandatory declaration", SOFT),
            ("on the thesis form.", SOFT),
        ]
        group = VGroup(*[
            Text(txt, font_size=36 if i==1 else 28, color=col, font="EB Garamond")
            for i, (txt, col) in enumerate(lines)
        ]).arrange(DOWN, buff=0.2).shift(UP*0.2)

        for item in group:
            self.play(FadeIn(item), run_time=0.4)

        note = Text("Source: primary guidance — confirm before ship (SOURCES.md §5)",
                    font_size=11, color=GHOST).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(note))
        self.wait(6)


class B20_PolicyExpression(Scene):
    """AI assistance in expressing your own ideas."""
    def construct(self):
        self.camera.background_color = BG

        header = Text("Policy (paraphrased)", font_size=18, color=GHOST).to_edge(UP, buff=0.65)
        self.play(FadeIn(header))

        box = RoundedRectangle(width=9, height=2.2, corner_radius=0.15,
                               fill_color=ManimColor("#F0EDE4"), fill_opacity=1,
                               stroke_color=GHOST, stroke_width=1.5)
        text = Text(
            "AI assistance in expressing\nyour own ideas is permitted.",
            font_size=32, color=INK, font="EB Garamond", line_spacing=1.3
        )
        VGroup(box, text).arrange(ORIGIN)
        self.play(FadeIn(box))
        self.play(FadeIn(text))

        sub = Text("Not generation of substance. Expression of existing ideas.",
                   font_size=17, color=SOFT).to_edge(DOWN, buff=1.2)
        rule_bot = Line(LEFT*3.5, RIGHT*3.5, color=GHOST, stroke_width=1).shift(DOWN*1.85)
        self.play(FadeIn(sub))
        self.play(FadeIn(rule_bot), run_time=0.2)     # state 2: {box, rule_bot}
        self.wait(4)


class B21_PolicyLine(Scene):
    """The line: inserting unreviewed AI sections."""
    def construct(self):
        self.camera.background_color = BG

        header = Text("The prohibition (paraphrased)", font_size=18, color=GHOST).to_edge(UP, buff=0.65)
        self.play(FadeIn(header))

        permit = Text("Where the words came from:", font_size=22, color=SOFT).shift(UP*1.8 + LEFT*0.5)
        permit_val = Text("NOT the line.", font_size=30, color=GHOST, font="EB Garamond"
                          ).next_to(permit, RIGHT, buff=0.3)

        rule_lbl = Text("The line:", font_size=22, color=INK).shift(UP*0.4 + LEFT*3.2)
        rule = Text("Did you read them?", font_size=44, color=ACC, font="EB Garamond"
                    ).next_to(rule_lbl, RIGHT, buff=0.3)

        detail = Text(
            "Inserting AI-generated sections you have not reviewed\nis prohibited — regardless of provenance.",
            font_size=18, color=SOFT, line_spacing=1.2
        ).shift(DOWN*1.2)

        self.play(FadeIn(permit), FadeIn(permit_val))
        self.play(FadeIn(rule_lbl), FadeIn(rule))
        self.play(FadeIn(detail))
        self.wait(6)


class B27_NovelText(Scene):
    """Model output is novel text — statistical aggregate of corpus."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("What the model returns", font_size=22, color=SOFT).to_edge(UP, buff=0.65)
        self.play(FadeIn(title))

        # Animated text: fragments coalescing
        fragments = [
            "Dewey (1933) argued…",
            "Schön's reflective…",
            "Carr & Kemmis…",
            "Kolb's experiential…",
            "…the practitioner…",
        ]
        f_objs = VGroup(*[
            Text(t, font_size=16, color=GHOST)
            for t in fragments
        ])
        positions = [UP*1.8+LEFT*2.5, UP*1.1+RIGHT*2.2, UP*0.2+LEFT*1.8,
                     DOWN*0.7+RIGHT*1.5, DOWN*1.4+LEFT*0.8]
        for fo, pos in zip(f_objs, positions):
            fo.move_to(pos)
            self.play(FadeIn(fo), run_time=0.25)

        result = RoundedRectangle(width=8, height=1.6, corner_radius=0.12,
                                  fill_color=ManimColor("#EDE8DE"), fill_opacity=1,
                                  stroke_color=ACC, stroke_width=1.5).shift(DOWN*0.2)
        result_text = Text("Novel text — resembles no single source.",
                           font_size=26, color=INK, font="EB Garamond")
        result_text.move_to(result.get_center())

        self.play(*[f.animate.set_opacity(0.25) for f in f_objs], run_time=0.6)
        self.play(FadeIn(result), FadeIn(result_text), run_time=0.6)

        sub = Text("A blend of all of them — a statistical aggregate of the corpus.",
                   font_size=16, color=SOFT).to_edge(DOWN, buff=1.0)
        rule_bot = Line(LEFT*3, RIGHT*3, color=GHOST, stroke_width=1).shift(DOWN*2.5)
        self.play(FadeIn(sub))
        self.play(FadeIn(rule_bot), run_time=0.2)     # state 2: {result, rule_bot}
        self.wait(5)


class B28_ScoreGauge(Scene):
    """Similarity score falls near zero for generated text."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Run it through the instrument.", font_size=26, color=SOFT
                     ).to_edge(UP, buff=0.65)
        self.play(FadeIn(title))

        # Simple gauge arc
        arc = Arc(radius=2.5, start_angle=PI*0.1, angle=PI*0.8,
                  color=GHOST, stroke_width=8).shift(DOWN*0.3)

        # Needle (points near start = low similarity)
        needle_angle = PI*0.1 + PI*0.05  # near zero end
        needle = Arrow(ORIGIN, 2.2*np.array([np.cos(needle_angle), np.sin(needle_angle), 0]),
                       color=ACC, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.12)
        needle.shift(DOWN*0.3)

        label_low  = Text("0%", font_size=20, color=GHOST).move_to(
            arc.get_start() + LEFT*0.5 + DOWN*0.3)
        label_high = Text("100%", font_size=20, color=GHOST).move_to(
            arc.get_end() + RIGHT*0.5 + DOWN*0.3)

        self.play(Create(arc), FadeIn(label_low), FadeIn(label_high), run_time=0.5)
        self.play(FadeIn(needle), run_time=0.4)

        score = Text("~0%", font_size=72, color=INK, font="EB Garamond").shift(DOWN*0.5)
        self.play(FadeIn(score))

        note = Text("The 322 sentences never exist. Nothing to lay side by side.",
                    font_size=16, color=SOFT).to_edge(DOWN, buff=1.0)
        self.play(FadeIn(note))
        self.wait(5)


class B34_SwitchedOff(Scene):
    """Many institutions withdrew AI detection tools."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("The sector's experiment with detection", font_size=22, color=SOFT
                     ).to_edge(UP, buff=0.65)
        self.play(FadeIn(title))

        # 5×6 grid of institution dots: most grey (switched off), a few green (still on)
        rows, cols = 5, 8
        dot_r = 0.18
        spacing = 0.65
        start = np.array([-(cols-1)*spacing/2, (rows-1)*spacing/2, 0]) + DOWN*0.2

        still_on = {(0,0),(0,7),(2,3)}  # minority kept
        dots = VGroup()
        for r in range(rows):
            for c in range(cols):
                col = GHOST if (r,c) not in still_on else GREEN
                d = Dot(radius=dot_r, color=col, fill_opacity=0.9)
                d.move_to(start + np.array([c*spacing, -r*spacing, 0]))
                dots.add(d)

        self.play(FadeIn(dots), run_time=1.0)

        crossed = VGroup(*[
            Cross(dot, color=SOFT, stroke_width=1.5)
            for i, dot in enumerate(dots)
            if i % (rows*cols // 37) == 0  # roughly 37 of 40
        ])
        self.play(FadeIn(crossed), run_time=0.8)

        note = Text("Many institutions: adopted → then withdrew.\nThe instrument built for the old problem does not transfer.",
                    font_size=16, color=SOFT, line_spacing=1.2).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note))
        self.wait(6)


class B35_TwoCases(Scene):
    """Two documented failure modes of AI detection."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Two failure patterns", font_size=22, color=SOFT).to_edge(UP, buff=0.65)
        self.play(FadeIn(title))

        card_bg = ManimColor("#F0EDE4")

        c1 = RoundedRectangle(width=5.5, height=3.2, corner_radius=0.15,
                              fill_color=card_bg, fill_opacity=1,
                              stroke_color=GHOST, stroke_width=1.5).shift(LEFT*3)
        c1t = Text("Institution A", font_size=15, color=GHOST).move_to(c1.get_top()+DOWN*0.35)
        c1b = Text(
            "Detection tool flags\nhuman writing as\nmachine-generated\nwith high confidence.",
            font_size=17, color=INK, font="EB Garamond", line_spacing=1.25
        ).move_to(c1.get_center()+DOWN*0.2)

        c2 = RoundedRectangle(width=5.5, height=3.2, corner_radius=0.15,
                              fill_color=card_bg, fill_opacity=1,
                              stroke_color=GHOST, stroke_width=1.5).shift(RIGHT*3)
        c2t = Text("Institution B", font_size=15, color=GHOST).move_to(c2.get_top()+DOWN*0.35)
        c2b = Text(
            "Hundreds of misconduct\ncases opened in one year.\nMost dismissed\non investigation.",
            font_size=17, color=INK, font="EB Garamond", line_spacing=1.25
        ).move_to(c2.get_center()+DOWN*0.2)

        self.play(FadeIn(c1), FadeIn(c1t), FadeIn(c1b), run_time=0.7)
        self.play(FadeIn(c2), FadeIn(c2t), FadeIn(c2b), run_time=0.7)
        self.wait(8)


class B37_DisparityBars(Scene):
    """False-positive rates higher for non-native English writers."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("AI detector false-positive rates by writer background",
                     font_size=21, color=SOFT).to_edge(UP, buff=0.65)
        self.play(FadeIn(title))

        groups  = ["Native\nEnglish writers", "Non-native\nEnglish writers"]
        values  = [12, 55]   # illustrative; directional claim only
        colours = [GHOST, ACC]
        base_y  = -1.5
        bar_w   = 2.2
        positions = [-2.5, 2.5]
        max_h   = 3.6

        baseline = Line(LEFT*5, RIGHT*5, color=INK, stroke_width=1.5).move_to([0, base_y, 0])
        self.play(Create(baseline))

        for grp, val, col, px in zip(groups, values, colours, positions):
            h = val / 60 * max_h
            bar = Rectangle(width=bar_w, height=h,
                            fill_color=col, fill_opacity=0.85,
                            stroke_color=col, stroke_width=0)
            bar.move_to([px, base_y + h/2, 0])
            pct_lbl = Text(f"~{val}%", font_size=32, color=col, font="EB Garamond")
            pct_lbl.next_to(bar, UP, buff=0.2)
            grp_lbl = Text(grp, font_size=16, color=SOFT, line_spacing=1.1)
            grp_lbl.move_to([px, base_y - 0.65, 0])
            self.play(GrowFromEdge(bar, DOWN), FadeIn(pct_lbl), FadeIn(grp_lbl), run_time=0.7)

        caveat = Text(
            "Illustrative — directional finding confirmed across published studies;\nspecific figures require named source (FACTCHECK.md row 18).",
            font_size=11, color=GHOST, line_spacing=1.2
        ).to_edge(DOWN, buff=0.75)
        note = Text("The instrument did not read the same writing the same way.",
                    font_size=16, color=INK).next_to(caveat, UP, buff=0.25)
        self.play(FadeIn(note), FadeIn(caveat))
        self.wait(8)


class BearsDoodlesVideo(Scene):
    """Aggregator required by static_scene_check.py — runs every beat in sequence."""
    def construct(self):
        self.camera.background_color = BG
        for Cls in [
            B01_ActTrace, B05_MatchCount, B06_Concentration,
            B09_SimilarityScore, B11_NearControl, B12_Ratio,
            B16_ActRules, B18_PolicyDeclaration, B20_PolicyExpression,
            B21_PolicyLine, B24_ActCounterfactual, B27_NovelText,
            B28_ScoreGauge, B34_SwitchedOff, B35_TwoCases,
            B37_DisparityBars, B38_Watermarking,
        ]:
            Cls().construct()


class B38_Watermarking(Scene):
    """Mechanism: statistical bias at word-selection time, z-score detection."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("How watermarking works", font_size=22, color=SOFT).to_edge(UP, buff=0.65)
        self.play(FadeIn(title))

        # Token selection diagram
        tokens = ["the", "instrument", "found", "it", "—", "clearly"]
        marked = [False, True, False, True, False, True]  # alternating bias
        cols   = [ACC if m else GHOST for m in marked]
        boxes  = VGroup(*[
            VGroup(
                RoundedRectangle(width=1.25, height=0.7, corner_radius=0.1,
                                 fill_color=col, fill_opacity=0.8 if m else 0.3,
                                 stroke_color=col, stroke_width=1.5),
                Text(tok, font_size=14, color=INK)
            ).arrange(ORIGIN)
            for tok, col, m in zip(tokens, cols, marked)
        ]).arrange(RIGHT, buff=0.15).shift(UP*1.0)
        self.play(FadeIn(boxes), run_time=0.8)

        thumb = Text("← thumb on the scale", font_size=16, color=ACC).next_to(boxes, RIGHT, buff=0.3)
        self.play(FadeIn(thumb))

        formula = MathTex(r"z = \frac{\#\text{marked tokens} - \mathbb{E}[\text{marked}]}{\sqrt{n \cdot p \cdot (1-p)}}",
                          color=INK, font_size=32).shift(DOWN*0.5)
        self.play(FadeIn(formula))

        conclusion = Text(
            "Count the biased-side tokens. Compute z-score. Threshold detects watermark.",
            font_size=15, color=SOFT
        ).to_edge(DOWN, buff=1.0)
        divider = Line(LEFT*4, RIGHT*4, color=GHOST, stroke_width=1).shift(DOWN*0.1)
        self.play(FadeIn(conclusion))
        self.play(FadeIn(divider), run_time=0.2)      # state 2: {boxes…, divider}
        self.wait(6)

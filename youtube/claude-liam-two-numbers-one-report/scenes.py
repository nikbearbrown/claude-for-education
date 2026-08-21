from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")   # terracotta
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")
GREEN = ManimColor("#4A7C59")
CREAM = ManimColor("#F2F0E9")

SERIF = "EB Garamond"


def cite(label):
    # buff=1.2 keeps text inside title-safe right boundary (≤5.9 units from center)
    return Text(label, font_size=10, color=GHOST).to_corner(DR, buff=1.2)


# ── B03 -- Accuracy Table ──────────────────────────────────────────────────────

class B03_AccuracyTable(Scene):
    """Rebuilt Table 4 -- four tools, fully AI-generated condition (n=40)."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Fully AI-Generated Papers (n=40)", font_size=21, color=SOFT)
        title.to_edge(UP, buff=0.55)
        self.play(FadeIn(title), run_time=0.4)

        # Column x positions
        cx = [-3.1, 0.55, 2.95]   # tool label | STRICT | INCLUSIVE
        # Row y positions: header at ry[0], data rows ry[1..4]
        ry = [0.85, 0.1, -0.6, -1.3, -2.0]

        # Headers
        hdr_t = Text("TOOL",               font_size=16, color=INK)
        hdr_s = Text("STRICT\nACCURACY",   font_size=15, color=INK)
        hdr_i = Text("INCLUSIVE\nACCURACY",font_size=15, color=INK)
        for obj, x in zip([hdr_t, hdr_s, hdr_i], cx):
            obj.move_to([x, ry[0], 0])
        div = Line([-4.8, 0.50, 0], [4.8, 0.50, 0], color=INK, stroke_width=1.4)

        self.play(FadeIn(VGroup(hdr_t, hdr_s, hdr_i)), Create(div), run_time=0.5)

        # Rows 1-3: 0% strict, animate one at a time
        for i in range(3):
            lbl = Text(f"TOOL {i+1}", font_size=16, color=SOFT)
            pct = Text("0%", font_size=22, color=GHOST, font=SERIF)
            lbl.move_to([cx[0], ry[i+1], 0])
            pct.move_to([cx[1], ry[i+1], 0])
            self.play(FadeIn(lbl), FadeIn(pct), run_time=0.38)

        # Row 4 -- highlight box then both figures
        hi = Rectangle(width=9.3, height=0.60,
                        fill_color=CREAM, fill_opacity=0.88,
                        stroke_color=ACC, stroke_width=1.8)
        hi.move_to([0, ry[4], 0])
        self.play(FadeIn(hi), run_time=0.22)

        t4   = Text("TOOL 4",  font_size=14, color=ACC)
        s4   = Text("65%",     font_size=26, color=ACC, font=SERIF)
        i4   = Text("97.5%",   font_size=26, color=ACC, font=SERIF)
        t4.move_to([cx[0], ry[4], 0])
        s4.move_to([cx[1], ry[4], 0])
        i4.move_to([cx[2], ry[4], 0])

        self.play(FadeIn(t4), FadeIn(s4), FadeIn(i4), run_time=0.50)

        # Pulse -- both cells flash together on "two numbers"
        self.play(
            Flash(s4, color=ACC, line_length=0.18, flash_radius=0.48, num_lines=8),
            Flash(i4, color=ACC, line_length=0.18, flash_radius=0.52, num_lines=8),
            run_time=0.55,
        )

        note = cite("Table 4 -- fully AI-generated condition (n=40) · Van Vlasselaer et al. 2026")
        self.play(FadeIn(note), run_time=0.25)
        self.wait(5.8)


# ── B05 -- Human Corpus ───────────────────────────────────────────────────────

class B05_HumanCorpus(Scene):
    """40 human theses -- non-native, pre-2019, zero false positives."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("The Human Corpus", font_size=22, color=SOFT).to_edge(UP, buff=0.55)
        self.play(FadeIn(title), run_time=0.3)

        # 40 isotype circles -- 5 rows × 8 cols
        rows, cols = 5, 8
        sx, sy = 0.58, 0.58
        origin = np.array([-(cols - 1) * sx / 2, 0.9, 0])
        dots = VGroup()
        for r in range(rows):
            for c in range(cols):
                d = Dot(radius=0.20, color=SOFT, fill_opacity=0.80)
                d.move_to(origin + np.array([c * sx, -r * sy, 0]))
                dots.add(d)

        self.play(FadeIn(dots, lag_ratio=0.04), run_time=1.0)

        # 0 FP label
        zero  = Text("0", font_size=44, color=GREEN, font=SERIF)
        label = Text("FALSE POSITIVES", font_size=16, color=GREEN)
        check = Text("✓", font_size=30, color=GREEN)
        fp = VGroup(check, zero, label).arrange(RIGHT, buff=0.18)
        fp.next_to(dots, DOWN, buff=0.30)
        self.play(FadeIn(fp), run_time=0.40)

        # Non-native label
        nn = Text("NON-NATIVE ENGLISH SPEAKERS", font_size=14, color=SOFT)
        nn.next_to(fp, DOWN, buff=0.25)
        self.play(FadeIn(nn), run_time=0.30)

        # Timeline -- PRE-2019 zone
        ty = -2.55
        full  = Line([-3.8, ty, 0], [3.8, ty, 0], color=GHOST, stroke_width=3.5)
        pre   = Line([-3.8, ty, 0], [-0.6, ty, 0], color=ACC,   stroke_width=5.5)
        tick  = Line([-0.6, ty - 0.18, 0], [-0.6, ty + 0.18, 0], color=INK, stroke_width=2)
        y19   = Text("2019", font_size=13, color=INK).move_to([-0.6, ty - 0.44, 0])
        lbl_p = Text("PRE-2019", font_size=13, color=ACC).move_to([-2.3, ty + 0.42, 0])
        lbl_n = Text("AFTER 2019", font_size=12, color=GHOST).move_to([2.2, ty + 0.42, 0])
        note2 = Text("nothing could have generated this text", font_size=12, color=SOFT
                     ).move_to([-2.3, ty - 0.64, 0])

        self.play(Create(full), run_time=0.28)
        self.play(Create(pre), FadeIn(tick), FadeIn(y19), FadeIn(lbl_p), run_time=0.42)
        self.play(FadeIn(lbl_n), FadeIn(note2), run_time=0.30)

        self.wait(5.2)


# ── B07 -- Sole-Evidence Quote ─────────────────────────────────────────────────

class B07_SoleEvidenceQuote(Scene):
    """Verbatim abstract quote -- 'sole evidence' and 'broader evaluation strategy'."""
    def construct(self):
        self.camera.background_color = BG

        hdr = Text("FROM THE ABSTRACT", font_size=20, color=SOFT).to_edge(UP, buff=0.65)
        self.play(FadeIn(hdr), run_time=0.38)

        open_q = Text("“", font_size=88, color=GHOST, font=SERIF).next_to(hdr, DOWN, buff=0.18)
        self.play(FadeIn(open_q), run_time=0.22)

        card = RoundedRectangle(
            width=11.5, height=5.8, corner_radius=0.20,
            fill_color=CREAM, fill_opacity=0.80,
            stroke_color=GHOST, stroke_width=0.8,
        ).shift(DOWN * 0.15)
        self.play(FadeIn(card), run_time=0.22)

        FS = 38

        line1a = Text("should not be used as",           font_size=FS, color=INK, font=SERIF)
        line1b = Text("sole evidence",                    font_size=FS, color=ACC, font=SERIF)
        row1   = VGroup(line1a, line1b).arrange(RIGHT, buff=0.22)

        line2  = Text("in high-stakes decision-making",  font_size=FS, color=INK, font=SERIF)
        line3  = Text("but should be implemented in a",  font_size=FS, color=INK, font=SERIF)
        line4  = Text("broader evaluation strategy",      font_size=FS, color=ACC, font=SERIF)

        quote_block = VGroup(row1, line2, line3, line4).arrange(DOWN, buff=0.36, aligned_edge=LEFT)
        quote_block.shift(DOWN * 0.08)

        close_q = Text('”', font_size=88, color=GHOST, font=SERIF)
        close_q.next_to(quote_block, DOWN, buff=0.10).align_to(quote_block, RIGHT)

        attrib = Text(
            "Van Vlasselaer, Van Droogenbroeck & Spruyt · IJEI 22:16 · 2026",
            font_size=14, color=GHOST,
        ).to_edge(DOWN, buff=0.55)

        verdict = Text("That sentence is the verdict.", font_size=28, color=INK, font=SERIF)
        verdict.to_edge(DOWN, buff=1.40)

        self.play(FadeIn(line1a), run_time=0.36)
        self.play(FadeIn(line1b), run_time=0.30)
        self.play(FadeIn(line2),  run_time=0.34)
        self.play(FadeIn(line3),  run_time=0.34)
        self.play(FadeIn(line4),  run_time=0.30)
        self.play(FadeIn(close_q), FadeIn(attrib), run_time=0.34)
        self.play(FadeIn(verdict), run_time=0.36)

        self.wait(8.2)


# ── BRM -- Report's Menu ──────────────────────────────────────────────────────

class BRM_ReportMenu(Scene):
    """Pangram social-media report -- four figures; 40% highlights as the one that travelled."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("The Report's Menu", font_size=22, color=SOFT).to_edge(UP, buff=0.55)
        self.play(FadeIn(title), run_time=0.35)

        subtitle = Text("Same scan · all true", font_size=15, color=GHOST).next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(subtitle), run_time=0.22)

        # Four rows: number (large) + label (small)
        # Row y positions — expanded vertical spread so early rows fill frame
        ry = [1.95, 0.70, -0.55, -1.80]

        rows_data = [
            ("13.8%",  "global average — all platforms",                 INK,  False),
            ("21.9%",  "Substack combined rate",                          INK,  False),
            ("25.72%", "longform >250 words — all platforms — fully AI",  SOFT, False),
            ("40%",    "LinkedIn longform — fully AI",                    ACC,  True),
        ]

        # Ghosted slot lines — all 4 visible from start to fill frame
        slot_lines = VGroup(*[
            Line([-5.5, y - 0.62, 0], [5.5, y - 0.62, 0], color=GHOST, stroke_width=0.7, stroke_opacity=0.5)
            for y in ry
        ])
        self.play(FadeIn(slot_lines), run_time=0.22)

        row_groups = []
        for (num, lbl, col, _), y in zip(rows_data, ry):
            fs = 46 if col == ACC else 38
            n  = Text(num, font_size=fs, color=col, font=SERIF)
            l  = Text(lbl, font_size=15, color=SOFT)
            grp = VGroup(n, l).arrange(RIGHT, buff=0.38)
            grp.move_to([0, y, 0])
            row_groups.append(grp)

        # Appear row by row on narration cues
        # Row 1: 13.8%
        self.play(FadeIn(row_groups[0]), run_time=0.40)
        self.wait(1.0)

        # Row 2: 21.9%
        self.play(FadeIn(row_groups[1]), run_time=0.40)

        # Exception sentence below Row 2
        exc = Text(
            '"Substack was an exception."',
            font_size=14, color=GHOST, font=SERIF,
        ).next_to(row_groups[1], DOWN, buff=0.14)
        self.play(FadeIn(exc), run_time=0.30)
        self.wait(0.8)

        # Row 3: 25.72%
        self.play(FadeIn(row_groups[2]), run_time=0.40)
        self.wait(0.8)

        # Row 4: 40% — large, terracotta, flash
        self.play(FadeIn(row_groups[3]), run_time=0.50)
        self.play(
            Flash(row_groups[3][0], color=ACC, line_length=0.22, flash_radius=0.65, num_lines=10),
            run_time=0.45,
        )
        self.wait(0.5)

        # Dim rows 1–3; draw arrow from 40% to "USED IN ANNOUNCEMENT"
        self.play(
            row_groups[0].animate.set_opacity(0.44),
            row_groups[1].animate.set_opacity(0.44),
            exc.animate.set_opacity(0.44),
            row_groups[2].animate.set_opacity(0.44),
            run_time=0.40,
        )

        used_lbl = Text("USED IN ANNOUNCEMENT", font_size=16, color=INK)
        used_lbl.next_to(row_groups[3], RIGHT, buff=0.55)
        arr = Arrow(
            row_groups[3].get_right() + RIGHT * 0.10,
            used_lbl.get_left() + LEFT * 0.08,
            color=ACC, stroke_width=2.8, buff=0,
            max_tip_length_to_length_ratio=0.20,
        )
        self.play(Create(arr), FadeIn(used_lbl), run_time=0.45)

        note = cite("Pangram social-media AI-writing-rate report · build-day live verification required")
        self.play(FadeIn(note), run_time=0.22)
        self.wait(5.0)


# ── B10 -- Vendor Figures (rev 4: Second Pick — Same Move) ───────────────────

class B10_VendorFigures(Scene):
    """Study table (left) vs what the Pangram page quotes (right). Rev 4: 'Same move as the report'."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Second Pick — Same Move", font_size=21, color=SOFT).to_edge(UP, buff=0.55)
        self.play(FadeIn(title), run_time=0.35)

        # Vertical divider
        vdiv = Line([0, 2.8, 0], [0, -3.1, 0], color=GHOST, stroke_width=1.2)
        self.play(Create(vdiv), run_time=0.22)

        # Column headers
        lhdr = Text("STUDY TABLE (Table 4)", font_size=13, color=SOFT).move_to([-2.9, 2.5, 0])
        rhdr = Text("PANGRAM PAGE",           font_size=13, color=SOFT).move_to([ 2.9, 2.5, 0])
        self.play(FadeIn(lhdr), FadeIn(rhdr), run_time=0.28)

        # Study-side rows
        rows = [
            ("65% STRICT",      [-2.9, 1.55]),
            ("97.5% INCLUSIVE", [-2.9, 0.75]),
            ("0 FALSE POS.",    [-2.9, -0.05]),
            ("PRE-2019 CORPUS", [-2.9, -0.85]),
        ]
        row_objs = {}
        for label, pos in rows:
            c = GHOST if label.startswith("65%") or label.startswith("PRE") else INK
            t = Text(label, font_size=18, color=c, font=SERIF)
            t.move_to(pos + [0])
            row_objs[label] = t
        self.play(*[FadeIn(v) for v in row_objs.values()], run_time=0.52)

        # 97.5% animates across to vendor side — INK for WCAG contrast compliance
        r975_copy = Text("97.5%", font_size=30, color=INK, font=SERIF).move_to([2.9, 0.75, 0])
        self.play(FadeIn(r975_copy), run_time=0.40)

        # 0 FP animates across
        rfp_copy = Text("0 FALSE POSITIVES", font_size=20, color=INK, font=SERIF).move_to([2.9, -0.05, 0])
        rfp_note = Text("on second-language academic writing", font_size=12, color=SOFT
                        ).move_to([2.9, -0.42, 0])
        self.play(FadeIn(rfp_copy), FadeIn(rfp_note), run_time=0.40)

        # 65% -- circled on study side, absent (strike) on vendor side
        circle = Circle(radius=0.38, color=ACC, stroke_width=2.2).move_to([-2.9, 1.55, 0])
        self.play(Create(circle), run_time=0.35)

        r65_absent = Text("65%", font_size=26, color=GHOST, font=SERIF).move_to([2.9, 1.55, 0])
        strike = Line([2.9 - 0.55, 1.55, 0], [2.9 + 0.55, 1.55, 0], color=ACC, stroke_width=2.5)
        self.play(FadeIn(r65_absent), Create(strike), run_time=0.38)

        # PRE-2019 -- crossed out on vendor side
        pre_absent = Text("PRE-2019", font_size=20, color=GHOST, font=SERIF).move_to([2.9, -0.85, 0])
        strike2 = Line([2.9 - 0.82, -0.85, 0], [2.9 + 0.82, -0.85, 0], color=ACC, stroke_width=2.5)
        self.play(FadeIn(pre_absent), Create(strike2), run_time=0.38)

        # "SAME MOVE AS THE REPORT" label at bottom — INK for WCAG contrast compliance
        same_move = Text("SAME MOVE AS THE REPORT", font_size=18, color=INK)
        same_move.move_to([0, -2.60, 0])
        self.play(FadeIn(same_move), run_time=0.40)

        note = cite("Figures from Table 4 · Van Vlasselaer et al. 2026 · Pangram page: build-day verify")
        self.play(FadeIn(note), run_time=0.22)
        self.wait(5.5)


# ── B14 -- Link Graph (rev 4: named nodes + self-citation loop) ──────────────

class B14_LinkGraph(Scene):
    """Three named nodes: Substack post → Pangram page (not paper); self-citation loop."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Where Does the Link Go?", font_size=21, color=SOFT).to_edge(UP, buff=0.55)
        self.play(FadeIn(title), run_time=0.35)

        def node_box(label, color=INK, fill=CREAM):
            box = RoundedRectangle(width=3.4, height=1.20, corner_radius=0.16,
                                   fill_color=fill, fill_opacity=0.92,
                                   stroke_color=GHOST, stroke_width=1.0)
            txt = Text(label, font_size=15, color=color, line_spacing=0.85)
            return VGroup(box, txt)

        n_paper    = node_box("PAPER",                  color=INK)
        n_vendor   = node_box("PANGRAM\nEVALUATIONS PAGE", color=INK)
        n_announce = node_box("SUBSTACK POST",          color=INK)

        n_paper.move_to([-4.5, 0.8, 0])
        n_vendor.move_to([0,   0.8, 0])
        n_announce.move_to([4.5, 0.8, 0])

        self.play(FadeIn(n_paper), FadeIn(n_vendor), FadeIn(n_announce), run_time=0.55)

        # Dashed arrow SUBSTACK POST → PAPER -- crossed out
        arr_blocked = DashedLine(
            [3.0, 0.92, 0], [-3.0, 0.92, 0],
            color=GHOST, stroke_width=2.0, dash_length=0.18,
        )
        cross_h = Line([-1.1, 1.22, 0], [-0.1, 0.62, 0], color=GHOST, stroke_width=3.5)
        cross_v = Line([-0.1, 1.22, 0], [-1.1, 0.62, 0], color=GHOST, stroke_width=3.5)
        self.play(Create(arr_blocked), run_time=0.42)
        self.play(Create(cross_h), Create(cross_v), run_time=0.32)

        lbl_no = Text("does not go to the research", font_size=14, color=GHOST
                      ).move_to([-1.5, 1.55, 0])
        self.play(FadeIn(lbl_no), run_time=0.22)

        # Solid terracotta arrow SUBSTACK POST → PANGRAM PAGE
        arr_vendor = Arrow(
            [3.0, 0.64, 0], [1.72, 0.64, 0],
            color=INK, stroke_width=3.5, buff=0,
            max_tip_length_to_length_ratio=0.18,
        )
        self.play(Create(arr_vendor), run_time=0.42)

        lbl_vendor = Text("CITED THROUGH THE VENDOR", font_size=15, color=INK)
        lbl_vendor.move_to([2.3, 0.12, 0])
        self.play(FadeIn(lbl_vendor), run_time=0.28)

        # Self-citation loop on PANGRAM PAGE node
        self_loop_lbl = Text("SELF-CITED ON ACCURACY + FP RATE", font_size=13, color=ACC)
        self_loop_lbl.move_to([0, -1.20, 0])
        self_arc = Arc(
            radius=0.72, start_angle=PI / 6, angle=4 * PI / 3,
            color=ACC, stroke_width=2.5,
        ).move_to(n_vendor.get_center() + DOWN * 0.68)
        tip_dot = Dot(radius=0.09, color=ACC).move_to(
            n_vendor.get_center() + DOWN * 0.68 + RIGHT * 0.68
        )
        self.play(Create(self_arc), FadeIn(tip_dot), FadeIn(self_loop_lbl), run_time=0.42)

        self.wait(5.5)


# ── B16 -- Four-Address Chain ──────────────────────────────────────────────────

class B16_FourAddressChain(Scene):
    """Four nodes animate sequentially; green checkmarks on every arrow."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("Four Addresses", font_size=22, color=SOFT).to_edge(UP, buff=0.55)
        self.play(FadeIn(title), run_time=0.35)

        labels = ["PAPER", "VENDOR\nPAGE", "ANNOUNCE-\nMENT", "BUTTON"]
        xs = [-4.8, -1.6, 1.6, 4.8]

        node_objs = []
        for lbl, x in zip(labels, xs):
            box = RoundedRectangle(width=2.2, height=1.10, corner_radius=0.14,
                                   fill_color=CREAM, fill_opacity=0,
                                   stroke_width=0)
            txt = Text(lbl, font_size=16, color=INK, line_spacing=0.88)
            g = VGroup(box, txt).move_to([x, 0, 0])
            node_objs.append(g)

        self.play(*[FadeIn(n) for n in node_objs], run_time=0.55)

        arrow_tips = []
        for i in range(3):
            x0 = xs[i] + 1.22
            x1 = xs[i+1] - 1.22
            arr = Arrow([x0, 0, 0], [x1, 0, 0], color=INK,
                        stroke_width=2.5, buff=0,
                        max_tip_length_to_length_ratio=0.22)
            self.play(Create(arr), run_time=0.42)
            arrow_tips.append([(x0 + x1) / 2, 0, 0])

        checks = VGroup(*[
            Text("✓", font_size=20, color=GREEN).move_to([mx, 0.48, 0])
            for mx, _, __ in arrow_tips
        ])
        self.play(FadeIn(checks, lag_ratio=0.15), run_time=0.45)

        note = Text("Every hop cites something real. Nothing at any link is false.",
                    font_size=16, color=SOFT).to_edge(DOWN, buff=0.85)
        self.play(FadeIn(note), run_time=0.30)

        self.wait(5.8)


# ── B17 -- What Fell Off (rev 4: symmetric, both picks) ──────────────────────

class B17_WhatFellOff(Scene):
    """Two-column layout: FROM THE REPORT (left) and FROM THE STUDY (right).
    Qualifiers peel off from each column on cue. Final: 40% · 97.5% — BOTH CHOSEN."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("What Did Not Travel", font_size=22, color=SOFT).to_edge(UP, buff=0.42)
        self.play(FadeIn(title), run_time=0.30)

        # Column headers
        lhdr = Text("FROM THE REPORT", font_size=16, color=SOFT).move_to([-3.2, 2.55, 0])
        rhdr = Text("FROM THE STUDY",  font_size=16, color=SOFT).move_to([ 3.2, 2.55, 0])
        vdiv = Line([0, 2.85, 0], [0, -3.25, 0], color=GHOST, stroke_width=1.0)
        self.play(FadeIn(lhdr), FadeIn(rhdr), Create(vdiv), run_time=0.40)

        # LEFT column qualifiers (report side)
        left_quals = [
            ("13.8% GLOBAL AVG",          20, SOFT),
            ("21.9% SUBSTACK RATE",       20, SOFT),
            ("\"SUBSTACK WAS AN EXCEPTION\"", 17, GHOST),
        ]
        left_ys = [1.70, 0.85, 0.00]
        left_objs = []
        for (lbl, fs, col), y in zip(left_quals, left_ys):
            t = Text(lbl, font_size=fs, color=col, font=SERIF)
            t.move_to([-3.2, y, 0])
            left_objs.append(t)

        # RIGHT column qualifiers (study side)
        right_quals = [
            ("65% STRICT ACCURACY",        20, SOFT),
            ("PRE-2019 CORPUS",            20, SOFT),
            ("ONE FACULTY",                20, SOFT),
            ("GENERATOR CONFOUND",         20, SOFT),
            ("SHOULD NOT BE SOLE EVIDENCE",22, INK),
        ]
        right_ys = [1.70, 0.85, 0.00, -0.85, -1.75]
        right_objs = []
        for (lbl, fs, col), y in zip(right_quals, right_ys):
            t = Text(lbl, font_size=fs, color=col, font=SERIF)
            t.move_to([3.2, y, 0])
            right_objs.append(t)

        # Reveal all qualifiers at once
        self.play(
            *[FadeIn(q) for q in left_objs],
            *[FadeIn(q) for q in right_objs],
            run_time=0.50,
        )
        self.wait(0.6)

        # Peel LEFT column on cue
        for q in left_objs:
            self.play(FadeOut(q, shift=LEFT * 1.8), run_time=0.42)

        self.wait(0.4)

        # Peel RIGHT column on cue
        for i, q in enumerate(right_objs):
            ft = 0.50 if i == len(right_objs) - 1 else 0.38
            col = ACC if i == len(right_objs) - 1 else None
            if col:
                q.set_color(col)
            self.play(FadeOut(q, shift=RIGHT * 1.8), run_time=ft)

        # Final reveal: BOTH CHOSEN
        divider = Line([-5.5, 0.40, 0], [5.5, 0.40, 0], color=GHOST, stroke_width=1.0)

        chosen_lbl = Text("BOTH CHOSEN", font_size=24, color=SOFT)
        chosen_lbl.move_to([0, 0.90, 0])

        num_l = Text("40%",  font_size=68, color=INK, font=SERIF)
        num_r = Text("97.5%",font_size=68, color=INK, font=SERIF)
        dot   = Text("·",    font_size=68, color=GHOST, font=SERIF)
        num_row = VGroup(num_l, dot, num_r).arrange(RIGHT, buff=0.45)
        num_row.move_to([0, -0.65, 0])

        self.play(
            Create(divider),
            FadeIn(chosen_lbl),
            FadeIn(num_row),
            run_time=0.55,
        )
        self.wait(4.5)


# ── BDTL -- Decimal Tell ──────────────────────────────────────────────────────

class BDTL_DecimalTell(Scene):
    """Six decimal-point numbers land one by one; decimal pulses terracotta on each.
    Final line: PRECISION WAS NOT THE QUESTION · SELECTION WAS."""
    def construct(self):
        self.camera.background_color = BG

        title = Text("The Decimal Point", font_size=22, color=SOFT).to_edge(UP, buff=0.55)
        self.play(FadeIn(title), run_time=0.35)

        # Six numbers in a 2×3 grid
        numbers = ["13.8", "21.9", "25.72", "65.0", "97.5", "0.01"]
        positions = [
            [-3.6, 0.80, 0], [0, 0.80, 0], [3.6, 0.80, 0],
            [-3.6, -0.55, 0], [0, -0.55, 0], [3.6, -0.55, 0],
        ]
        objs = []
        for num, pos in zip(numbers, positions):
            # Split on decimal so we can flash the dot
            parts = num.split(".")
            whole = Text(parts[0] + ".", font_size=48, color=INK, font=SERIF)
            frac  = Text(parts[1],      font_size=48, color=INK, font=SERIF)
            row   = VGroup(whole, frac).arrange(RIGHT, buff=0.02)
            row.move_to(pos)
            objs.append((whole, frac, row))

        # Appear one by one; decimal pulses on each
        for whole, frac, row in objs:
            self.play(FadeIn(row), run_time=0.30)
            self.play(
                whole[-1].animate.set_color(ACC),
                run_time=0.22,
            )
            self.play(
                whole[-1].animate.set_color(INK),
                run_time=0.18,
            )

        self.wait(0.5)

        # Bottom lines
        line1 = Text("Precision was not the question.", font_size=22, color=SOFT)
        line2 = Text("Selection was.",                  font_size=28, color=ACC, font=SERIF)
        bottom = VGroup(line1, line2).arrange(DOWN, buff=0.22)
        bottom.to_edge(DOWN, buff=0.80)

        self.play(FadeIn(line1), run_time=0.35)
        self.play(FadeIn(line2), run_time=0.35)

        note = cite("Figures: Pangram report + Van Vlasselaer et al. 2026 · build-day verify for report figures")
        self.play(FadeIn(note), run_time=0.22)
        self.wait(5.5)


# ── Aggregator -- required by static_scene_check.py ───────────────────────────

class BearsDoodlesVideo(Scene):
    """Aggregator: runs all rev-4 scenes for QC checks."""
    def construct(self):
        self.camera.background_color = BG
        for Cls in [
            B03_AccuracyTable,
            B05_HumanCorpus,
            B07_SoleEvidenceQuote,
            BRM_ReportMenu,
            B10_VendorFigures,
            B14_LinkGraph,
            B16_FourAddressChain,
            B17_WhatFellOff,
            BDTL_DecimalTell,
        ]:
            Cls().construct()

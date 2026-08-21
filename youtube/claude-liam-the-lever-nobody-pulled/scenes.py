"""
scenes.py — claude-liam-the-lever-nobody-pulled
The Lever Nobody Pulled · deep-explainer

GRAPHIC beats: B01 B03 B04 B05 B07 B08 B09 B10 B11 B12 B14 B15 B16 B17 B18 B19
Remotion beats: B00 B02 B06 B13 BVDT BHTF BOUT
SAFE zone: x [-6.4, 6.4] · y [-3.6, 3.6]
ONE TERRACOTTA (SPARK) accent per beat.
"""

from manim import *

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"   # TERRACOTTA
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE

# GATE T §8.4 font lock — all Text() defaults to EB Garamond, preventing Pango fallback
_OrigText = Text
Text = lambda text, *args, font='EB Garamond', **kwargs: _OrigText(text, *args, font=font, **kwargs)


# ── B01 ─────────────────────────────────────────────────────────────────────

class B01_ThreeBosses(Scene):
    """Three stacked authority bands; sight-line stops at the bottom band."""
    def construct(self):
        dur = 15.19

        band_w, band_h = 11.8, 1.7
        ys     = [2.0, 0.0, -2.0]
        specs  = [
            ("PLATFORM",  "rules the model will not break", INK,   INK),
            ("OPERATOR",  "whoever deployed it",            SPARK,  INK),
            ("USER",      "the student",                    INK,   INK),
        ]

        bands = []
        for (role, desc, stroke, label_col), y in zip(specs, ys):
            rect = Rectangle(
                width=band_w, height=band_h,
                color=stroke, fill_color=PAGE, fill_opacity=1, stroke_width=2.2
            ).move_to([0, y, 0])
            role_t = Text(role, font_size=20, color=label_col, weight=BOLD).move_to([0, y + 0.33, 0])
            desc_t = Text(desc, font_size=14, color=SOFT).move_to([0, y - 0.3, 0])
            bands.append(VGroup(rect, role_t, desc_t))

        anim = 0.0
        self.play(FadeIn(bands[0]), run_time=0.5); anim += 0.5
        self.wait(0.7); anim += 0.7
        self.play(FadeIn(bands[1]), run_time=0.5); anim += 0.5
        self.wait(0.8); anim += 0.8
        self.play(FadeIn(bands[2]), run_time=0.5); anim += 0.5
        self.wait(0.6); anim += 0.6

        # Figure marker beside bottom band — a Dot avoids text-on-shape collision
        # Placed just outside the band's right edge (band extends to x=5.9)
        figure = Dot(point=[6.15, -2.0, 0], radius=0.18, color=INK, fill_opacity=1)
        sight  = Line([6.0, -2.0, 0], [5.9, -2.0, 0], color=INK, stroke_width=1.6)
        caption = Text("the only layer most people meet", font_size=13, color=SOFT)
        caption.move_to([0, -3.3, 0])

        self.play(FadeIn(figure), Create(sight), run_time=0.4); anim += 0.4
        self.play(FadeIn(caption), run_time=0.35); anim += 0.35

        self.wait(max(0.01, dur - anim))


# ── B03 ─────────────────────────────────────────────────────────────────────

class B03_Precedence(Scene):
    """Two cards collide; the user card loses and fades; the org card holds."""
    def construct(self):
        dur = 17.11

        card_w, card_h = 4.6, 2.0

        org_card = RoundedRectangle(
            width=card_w, height=card_h, corner_radius=0.12,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([-4.5, 0.6, 0])
        org_lbl = Text("ORGANISATION", font_size=16, color=INK, weight=BOLD).move_to([-4.5, 1.0, 0])
        org_sub = Text("outline and guiding questions,\nnever finished prose",
                       font_size=11, color=SOFT, line_spacing=0.5).move_to([-4.5, 0.4, 0])
        org_grp = VGroup(org_card, org_lbl, org_sub)

        usr_card = RoundedRectangle(
            width=card_w, height=card_h, corner_radius=0.12,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([4.5, 0.6, 0])
        usr_lbl = Text("USER", font_size=16, color=INK, weight=BOLD).move_to([4.5, 1.0, 0])
        usr_sub = Text("WRITE MY ESSAY", font_size=16, color=INK, weight=BOLD).move_to([4.5, 0.6, 0])
        usr_grp = VGroup(usr_card, usr_lbl, usr_sub)

        # Section header at top-safe extends ink bounding box to y≈3.2 (GATE V underfill fix)
        scene_hdr = Text("THE PRECEDENCE RULE", font_size=14, color=GHOST, weight=BOLD)
        scene_hdr.move_to([0, 3.1, 0])
        self.add(scene_hdr)

        anim = 0.0
        self.play(FadeIn(org_grp), FadeIn(usr_grp), run_time=0.5); anim += 0.5
        self.wait(0.5); anim += 0.5

        # Advance toward centre
        self.play(
            org_grp.animate.move_to([-2.0, 0.6, 0]),
            usr_grp.animate.move_to([2.0, 0.6, 0]),
            run_time=0.8
        ); anim += 0.8
        self.wait(0.3); anim += 0.3

        # User card pushed back and greyed; org card gets TERRACOTTA ring
        spark_ring = RoundedRectangle(
            width=card_w + 0.2, height=card_h + 0.2, corner_radius=0.15,
            color=SPARK, fill_opacity=0, stroke_width=3.0
        ).move_to([-2.0, 0.6, 0])

        self.play(usr_grp.animate.shift(RIGHT * 0.9), run_time=0.4); anim += 0.4
        usr_grp.set_opacity(0.4)
        self.play(Create(spark_ring), run_time=0.4); anim += 0.4
        self.wait(0.4); anim += 0.4

        # Verbatim quote (curly quotes represented via unicode escapes)
        quote_str = (
            "“If an individual instruction directly contradicts\n"
            "an organization instruction,\n"
            "Claude favors the organization-level instruction.”"
        )
        quote = Text(quote_str, font_size=12, color=SOFT, line_spacing=0.55)
        quote.move_to([0, -1.9, 0])
        attr  = Text("Anthropic Help Center", font_size=11, color=SOFT).next_to(quote, DOWN, buff=0.15)

        self.play(FadeIn(quote), run_time=0.5); anim += 0.5
        self.play(FadeIn(attr), run_time=0.3); anim += 0.3

        self.wait(max(0.01, dur - anim))


# ── B04 ─────────────────────────────────────────────────────────────────────

class B04_Ceiling(Scene):
    """Operator layer: blocked upward, free downward — the asymmetry in one frame."""
    def construct(self):
        dur = 18.77

        # Compact three-band stack on the left
        bw, bh = 4.8, 1.1
        left_x = -3.0
        ys = [2.1, 0.6, -0.9]
        specs = [
            ("PLATFORM",  INK,   INK),
            ("OPERATOR",  SPARK, INK),
            ("USER",      INK,   INK),
        ]
        stack = VGroup()
        operator_mid_y = ys[1]
        for (lbl, stroke_col, txt_col), y in zip(specs, ys):
            col = stroke_col
            rect = Rectangle(
                width=bw, height=bh,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
            ).move_to([left_x, y, 0])
            txt = Text(lbl, font_size=14, color=txt_col, weight=BOLD).move_to([left_x, y, 0])
            stack.add(VGroup(rect, txt))

        # Section header at top-safe extends ink bounding box to y≈3.2 (GATE V underfill fix)
        scene_hdr = Text("ASYMMETRIC AUTHORITY", font_size=14, color=GHOST, weight=BOLD)
        scene_hdr.move_to([0, 3.1, 0])
        self.add(scene_hdr)

        anim = 0.0
        self.play(FadeIn(stack), run_time=0.5); anim += 0.5
        self.wait(0.4); anim += 0.4

        # Arrow from operator band rising toward platform, stopped at ceiling
        ceiling_y = 1.4
        up_arrow = Arrow(
            start=[left_x, operator_mid_y + 0.55, 0],
            end=[left_x, ceiling_y, 0],
            color=INK, stroke_width=2.0,
            max_tip_length_to_length_ratio=0.18
        )
        ceiling_line = Line(
            [left_x - 2.4, ceiling_y, 0],
            [left_x + 2.4, ceiling_y, 0],
            color=INK, stroke_width=2.5
        )

        self.play(GrowArrow(up_arrow), run_time=0.5); anim += 0.5
        self.play(Create(ceiling_line), run_time=0.35); anim += 0.35
        self.wait(0.2); anim += 0.2

        ceiling_lbl = Text(
            "cannot disable Claude's built-in\nsafety guidelines or content policies",
            font_size=12, color=SOFT, line_spacing=0.5
        ).move_to([2.8, ceiling_y + 0.3, 0])
        self.play(FadeIn(ceiling_lbl), run_time=0.4); anim += 0.4
        self.wait(0.3); anim += 0.3

        # Arrow downward from operator to user, unobstructed
        dn_arrow = Arrow(
            start=[left_x, operator_mid_y - 0.55, 0],
            end=[left_x, ys[2] + 0.55, 0],
            color=SPARK, stroke_width=2.2,
            max_tip_length_to_length_ratio=0.18
        )
        self.play(GrowArrow(dn_arrow), run_time=0.5); anim += 0.5

        caption = Text("Documented, both directions.", font_size=14, color=SOFT)
        caption.move_to([2.8, -2.4, 0])
        attr = Text("Anthropic Help Center", font_size=12, color=GHOST).move_to([2.8, -3.0, 0])

        self.play(FadeIn(caption), FadeIn(attr), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))


# ── B05 ─────────────────────────────────────────────────────────────────────

class B05_ThreeVendors(Scene):
    """Three columns — different shapes, not a scoreboard. No ticks, no crosses."""
    def construct(self):
        dur = 26.69

        col_xs = [-4.2, 0.0, 4.2]
        col_w  = 3.6
        col_headers = ["ANTHROPIC", "OPENAI", "GOOGLE"]

        # Draw column headers
        anim = 0.0
        for label, x in zip(col_headers, col_xs):
            hdr = Text(label, font_size=16, color=INK, weight=BOLD).move_to([x, 2.9, 0])
            self.play(FadeIn(hdr), run_time=0.2); anim += 0.2

        # Vertical dividers
        for x in [-2.1, 2.1]:
            div = Line([x, 3.1, 0], [x, -3.2, 0], color=BORDER, stroke_width=1.0)
            self.add(div)

        self.wait(0.2); anim += 0.2

        # ANTHROPIC column — single TERRACOTTA row
        row_h = 0.55
        a_row = RoundedRectangle(
            width=col_w - 0.3, height=row_h, corner_radius=0.08,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([col_xs[0], 2.0, 0])
        a_lbl = Text("organisation instruction", font_size=10, color=INK, weight=BOLD)
        a_lbl.move_to([col_xs[0], 2.07, 0])
        a_sub = Text("every conversation", font_size=9, color=INK)
        a_sub.move_to([col_xs[0], 1.88, 0])
        self.play(FadeIn(VGroup(a_row, a_lbl, a_sub)), run_time=0.4); anim += 0.4
        self.wait(0.3); anim += 0.3

        # OPENAI column — roles, permissions, GPTs (ink), then struck row
        openai_rows = [
            ("roles", 2.1),
            ("permissions", 1.5),
            ("workspace custom GPTs", 0.9),
        ]
        for text, y in openai_rows:
            row = RoundedRectangle(
                width=col_w - 0.3, height=row_h, corner_radius=0.08,
                color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.4
            ).move_to([col_xs[1], y, 0])
            lbl = Text(text, font_size=10, color=INK).move_to([col_xs[1], y, 0])
            self.play(FadeIn(VGroup(row, lbl)), run_time=0.2); anim += 0.2

        self.wait(0.2); anim += 0.2
        # Struck-through row
        struck_row = RoundedRectangle(
            width=col_w - 0.3, height=row_h, corner_radius=0.08,
            color=GHOST, fill_color=PAGE, fill_opacity=1, stroke_width=1.2
        ).move_to([col_xs[1], 0.3, 0])
        struck_lbl = Text("workspace-level answer restraint", font_size=9, color=GHOST)
        struck_lbl.move_to([col_xs[1], 0.3, 0])
        strike_line = Line(
            [col_xs[1] - 1.6, 0.3, 0],
            [col_xs[1] + 1.6, 0.3, 0],
            color=GHOST, stroke_width=1.8
        )
        strike_line._qc_intentional = True  # strikethrough annotation — exempt from TEXT_ON_CURVE
        self.play(FadeIn(VGroup(struck_row, struck_lbl)), run_time=0.2); anim += 0.2
        self.play(Create(strike_line), run_time=0.3); anim += 0.3
        self.wait(0.3); anim += 0.3

        # GOOGLE column — toggle glyphs, no instruction row
        google_items = [
            ("■  Docs", 2.1),
            ("■  Slides", 1.5),
            ("■  Classroom", 0.9),
            ("□  per org unit", 0.3),
            ("▲  age gate", -0.3),
        ]
        for text, y in google_items:
            lbl = Text(text, font_size=10, color=INK).move_to([col_xs[2], y, 0])
            self.play(FadeIn(lbl), run_time=0.15); anim += 0.15

        # Visible empty space where instruction row would be
        empty_outline = RoundedRectangle(
            width=col_w - 0.3, height=row_h, corner_radius=0.08,
            color=BORDER, fill_opacity=0, stroke_width=1.0, stroke_opacity=0.5
        ).move_to([col_xs[2], -0.9, 0])
        self.play(FadeIn(empty_outline), run_time=0.3); anim += 0.3
        self.wait(0.3); anim += 0.3

        caption = Text("Which surfaces are on.  Not how they behave.", font_size=13, color=SOFT)
        caption.move_to([0, -3.2, 0])
        self.play(FadeIn(caption), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))


# ── B07 ─────────────────────────────────────────────────────────────────────

class B07_TwoCircles(Scene):
    """Licence (large) and configured behaviour (small) — a small deliberate overlap."""
    def construct(self):
        dur = 20.52

        r_large = 3.1  # enlarged from 2.8 — extends bounding box to y≈±3.1 for GATE V
        r_small = 1.4
        # Start positions, then move together to overlap slightly
        left_centre  = LEFT * 3.2
        right_centre = RIGHT * 3.2

        left_circle = Circle(
            radius=r_large,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to(left_centre)
        left_lbl = Text("HAS A LICENCE", font_size=16, color=INK, weight=BOLD)
        left_lbl.move_to(left_centre + LEFT * 0.8 + UP * 0.4)
        left_grp = VGroup(left_circle, left_lbl)

        right_circle = Circle(
            radius=r_small,
            color=SOFT, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to(right_centre)
        right_lbl = Text("HAS CONFIGURED\nBEHAVIOUR", font_size=13, color=SOFT,
                         line_spacing=0.5)
        right_lbl.move_to(right_centre + RIGHT * 0.1)
        right_grp = VGroup(right_circle, right_lbl)

        anim = 0.0
        self.play(Create(left_circle), FadeIn(left_lbl), run_time=0.5); anim += 0.5
        self.wait(0.3); anim += 0.3
        self.play(Create(right_circle), FadeIn(right_lbl), run_time=0.5); anim += 0.5
        self.wait(0.3); anim += 0.3

        # Move circles together — small overlap
        new_left  = LEFT * 1.6
        new_right = RIGHT * 2.6
        self.play(
            left_grp.animate.shift(RIGHT * 1.6),
            right_grp.animate.shift(LEFT * 0.6),
            run_time=0.7
        ); anim += 0.7
        self.wait(0.2); anim += 0.2

        # Hatch the small lens intersection with diagonal lines
        lens_x = 1.6   # approximate overlap centre
        for dy in [-0.3, 0.0, 0.3]:
            h = Line([lens_x - 0.3, dy, 0], [lens_x + 0.3, dy, 0],
                     color=GHOST, stroke_width=1.2)
            self.add(h)
        lens_lbl = Text("the actual\nquestion", font_size=10, color=SOFT, line_spacing=0.5)
        # x=2.5: right of left_circle's far edge (≈1.2), below right_circle bottom (≈-1.4)
        lens_lbl.move_to([2.5, -1.8, 0])
        self.play(FadeIn(lens_lbl), run_time=0.4); anim += 0.4
        self.wait(0.3); anim += 0.3

        # Banner on left circle only — TERRACOTTA ring
        banner_box = RoundedRectangle(
            width=3.4, height=0.7, corner_radius=0.1,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2.2
        ).move_to([-1.0, -1.0, 0])
        banner_txt = Text("University adopts Claude", font_size=12, color=INK, weight=BOLD)
        banner_txt.move_to([-1.0, -1.0, 0])
        note_txt = Text("true of the left circle alone", font_size=10, color=SOFT)
        note_txt.next_to(banner_box, DOWN, buff=0.15)

        self.play(FadeIn(banner_box), FadeIn(banner_txt), run_time=0.4); anim += 0.4
        self.play(FadeIn(note_txt), run_time=0.3); anim += 0.3

        self.wait(max(0.01, dur - anim))


# ── B08 ─────────────────────────────────────────────────────────────────────

class B08_FourNames(Scene):
    """Four institution chips; three rows filled; fourth row empty — ringed TERRACOTTA."""
    def construct(self):
        dur = 19.31

        institutions = ["NORTHEASTERN", "LSE", "CHAMPLAIN", "CARNEGIE MELLON"]
        # Chips shifted right so label column [-5.5, -3.1] clears cell fills
        chip_xs = [-1.9, 0.4, 2.7, 5.0]
        chip_w, chip_h = 2.2, 0.7
        rows = ["contract", "single sign-on", "vendor's own template"]
        empty_row_label = "university-authored\ninstruction"
        label_x = -5.0  # labels centered here; rightmost text edge ≈ -4.4, safely left of cells

        anim = 0.0

        # Chips
        chips = VGroup()
        for label, x in zip(institutions, chip_xs):
            chip = RoundedRectangle(
                width=chip_w, height=chip_h, corner_radius=0.1,
                color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
            ).move_to([x, 2.7, 0])
            txt = Text(label, font_size=8, color=INK, weight=BOLD).move_to([x, 2.7, 0])
            chips.add(VGroup(chip, txt))
        self.play(LaggedStart(*[FadeIn(c) for c in chips], lag_ratio=0.15), run_time=0.6)
        anim += 0.6
        self.wait(0.4); anim += 0.4

        # Three filled rows
        row_h = 0.52
        row_ys = [1.6, 0.9, 0.2]
        for row_lbl, y in zip(rows, row_ys):
            r_lbl = Text(row_lbl, font_size=9, color=SOFT).move_to([label_x, y, 0])
            self.play(FadeIn(r_lbl), run_time=0.2); anim += 0.2
            for x in chip_xs:
                cell = RoundedRectangle(
                    width=chip_w - 0.2, height=row_h, corner_radius=0.07,
                    color=GHOST, fill_color=PAGE, fill_opacity=1, stroke_width=1.0
                ).move_to([x, y, 0])
                tick = Text("✓", font_size=12, color=GHOST).move_to([x, y, 0])
                self.play(FadeIn(VGroup(cell, tick)), run_time=0.12); anim += 0.12
        self.wait(0.3); anim += 0.3

        # Fourth row — empty, ringed TERRACOTTA
        empty_y = -0.6
        empty_lbl = Text(empty_row_label, font_size=9, color=INK, line_spacing=0.5)
        empty_lbl.move_to([label_x, empty_y, 0])
        self.play(FadeIn(empty_lbl), run_time=0.3); anim += 0.3
        for x in chip_xs:
            empty_cell = RoundedRectangle(
                width=chip_w - 0.2, height=row_h, corner_radius=0.07,
                color=SPARK, fill_opacity=0, stroke_width=1.8
            ).move_to([x, empty_y, 0])
            self.play(Create(empty_cell), run_time=0.2); anim += 0.2

        self.wait(0.3); anim += 0.3

        caption = Text("The announcement is true.  It is also not the thing.", font_size=13, color=SOFT)
        caption.move_to([0, -3.2, 0])
        self.play(FadeIn(caption), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))


# ── B09 ─────────────────────────────────────────────────────────────────────

class B09_NoWire(Scene):
    """Two columns; a dashed void between them. NOTHING crosses it."""
    def construct(self):
        dur = 17.92

        col_w = 4.2
        left_x  = -3.5
        right_x =  3.5
        gap_x   =  0.0

        # LEFT column: THE COMMITTEE
        left_box = Rectangle(
            width=col_w, height=4.8,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([left_x, 0.2, 0])
        left_hdr = Text("THE COMMITTEE", font_size=15, color=INK, weight=BOLD)
        left_hdr.move_to([left_x, 2.2, 0])
        left_rows = [
            "syllabus language",
            "academic integrity policy",
            "assignment guidance",
        ]
        left_row_grps = VGroup()
        for i, r in enumerate(left_rows):
            rt = Text(r, font_size=11, color=SOFT).move_to([left_x, 1.3 - i * 0.7, 0])
            left_row_grps.add(rt)
        left_col = VGroup(left_box, left_hdr, left_row_grps)

        # RIGHT column: THE CONSOLE
        right_box = Rectangle(
            width=col_w, height=4.8,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([right_x, 0.2, 0])
        right_hdr = Text("THE CONSOLE", font_size=15, color=INK, weight=BOLD)
        right_hdr.move_to([right_x, 2.2, 0])
        right_row_box = RoundedRectangle(
            width=col_w - 0.5, height=0.75, corner_radius=0.1,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([right_x, 1.1, 0])
        right_row_txt = Text("organisation instructions\n3,000 characters",
                             font_size=10, color=INK, line_spacing=0.5)
        right_row_txt.move_to([right_x, 1.1, 0])
        right_col = VGroup(right_box, right_hdr, right_row_box, right_row_txt)

        anim = 0.0
        self.play(FadeIn(left_col), run_time=0.5); anim += 0.5
        self.wait(0.5); anim += 0.5
        self.play(FadeIn(right_col), run_time=0.5); anim += 0.5
        self.wait(0.4); anim += 0.4

        # Dashed void between them — labelled "no channel"
        void_top    = [gap_x, 2.5, 0]
        void_bottom = [gap_x, -2.1, 0]
        void_line = DashedLine(void_top, void_bottom, color=GHOST, stroke_width=1.5, dash_length=0.15)
        void_lbl  = Text("no channel", font_size=12, color=GHOST, weight=BOLD)
        void_lbl.move_to([gap_x, -2.7, 0])

        self.play(Create(void_line), run_time=0.5); anim += 0.5
        self.play(FadeIn(void_lbl), run_time=0.3); anim += 0.3
        self.wait(0.3); anim += 0.3

        caption = Text("Writing policy at a layer with no wire to the software.", font_size=13, color=SOFT)
        caption.move_to([0, -3.3, 0])
        self.play(FadeIn(caption), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))


# ── B10 ─────────────────────────────────────────────────────────────────────

class B10_ScopeAxis(Scene):
    """Vertical scope axis; dots accumulate in lower bands; top band stays empty."""
    def construct(self):
        dur = 22.31

        axis_x = -2.8
        axis_top_y    =  3.2
        axis_bottom_y = -3.2

        # Three band regions
        band_boundaries = [-3.2, -0.8, 1.2, 3.2]
        band_labels = [
            "ONE COURSE / ONE INSTRUCTOR",
            "ONE DEPARTMENT / ONE UNIT",
            "EVERY STUDENT, EVERY CONVERSATION",
        ]
        band_ys = [(-3.2 + -0.8) / 2, (-0.8 + 1.2) / 2, (1.2 + 3.2) / 2]

        anim = 0.0

        # Draw axis
        axis = Line([axis_x, axis_bottom_y, 0], [axis_x, axis_top_y, 0],
                    color=INK, stroke_width=2.0)
        arrow_tip = Arrow(
            start=[axis_x, axis_top_y - 0.3, 0],
            end=[axis_x, axis_top_y + 0.1, 0],
            color=INK, stroke_width=2.0, max_tip_length_to_length_ratio=0.3
        )
        self.play(Create(axis), GrowArrow(arrow_tip), run_time=0.4); anim += 0.4

        # Band dividers and labels
        top_lbl = None
        for i, (by, lbl) in enumerate(zip(band_ys, band_labels)):
            b_lbl = Text(lbl, font_size=16, color=INK if i < 2 else SOFT)
            b_lbl.move_to([1.6, by, 0])
            self.play(FadeIn(b_lbl), run_time=0.2); anim += 0.2
            if i == 2:
                top_lbl = b_lbl
        for gy in band_boundaries[1:-1]:
            dv = DashedLine([axis_x - 0.3, gy, 0], [5.5, gy, 0],
                            color=BORDER, stroke_width=0.8, dash_length=0.2)
            self.add(dv)

        self.wait(0.3); anim += 0.3

        # Dots in bottom band
        import random
        random.seed(42)
        dot_xs_bottom = [-2.5, -2.2, -2.6, -2.3, -2.7, -2.4, -2.1]
        dot_ys_bottom = [random.uniform(-2.9, -1.2) for _ in dot_xs_bottom]
        for dx, dy in zip(dot_xs_bottom, dot_ys_bottom):
            dot = Dot([dx, dy, 0], radius=0.12, color=INK, fill_opacity=0.85)
            self.play(FadeIn(dot), run_time=0.18); anim += 0.18
        self.wait(0.2); anim += 0.2

        # Dots in middle band
        dot_xs_mid = [-2.5, -2.2, -2.6]
        dot_ys_mid = [random.uniform(-0.5, 0.8) for _ in dot_xs_mid]
        for dx, dy in zip(dot_xs_mid, dot_ys_mid):
            dot = Dot([dx, dy, 0], radius=0.12, color=SOFT, fill_opacity=0.7)
            self.play(FadeIn(dot), run_time=0.18); anim += 0.18
        self.wait(0.2); anim += 0.2

        # Top band stays empty — fade out band label, ring + "no confirmed case" replace it
        if top_lbl is not None:
            self.play(FadeOut(top_lbl), run_time=0.25); anim += 0.25
        top_band_rect = Rectangle(
            width=8.8, height=1.95,
            color=SPARK, fill_opacity=0, stroke_width=2.2
        ).move_to([1.6, 2.2, 0])
        no_case_lbl = Text("NO CONFIRMED CASE", font_size=16, color=INK, weight=BOLD)
        no_case_lbl.move_to([1.6, 2.2, 0])
        self.play(Create(top_band_rect), run_time=0.5); anim += 0.5
        self.play(FadeIn(no_case_lbl), run_time=0.35); anim += 0.35
        self.wait(0.3); anim += 0.3

        caption = Text("The lever is at the top.  Everything built is at the bottom.", font_size=13, color=SOFT)
        caption.move_to([1.6, -3.05, 0])
        self.play(FadeIn(caption), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))


# ── B11 ─────────────────────────────────────────────────────────────────────

class B11_CognitiRecreation(Scene):
    """FALLBACK for absent pantry still — system-message box + verbatim line."""
    def construct(self):
        dur = 17.75

        # Two-panel layout: left = system prompt box, right = student view
        # LEFT — instructor-facing system prompt panel
        left_box = RoundedRectangle(
            width=5.8, height=5.2, corner_radius=0.15,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([-2.8, 0.2, 0])

        # Header divider inside left box
        hdr_line = Line([-5.6, 1.3, 0], [0, 1.3, 0], color=INK, stroke_width=1.2)

        # RIGHT — student-facing quote highlight box
        right_box = RoundedRectangle(
            width=5.2, height=3.4, corner_radius=0.15,
            color=SPARK, fill_color=PAGE, fill_opacity=0, stroke_width=2.2
        ).move_to([3.2, 0.4, 0])

        # Arrow from left to right
        reveal_arrow = Arrow(
            start=[0.2, 0.4, 0], end=[0.9, 0.4, 0],
            color=INK, stroke_width=2.0, max_tip_length_to_length_ratio=0.2
        )

        # Text content
        sys_hdr = Text("SYSTEM PROMPT", font_size=13, color=SOFT, weight=BOLD)
        sys_hdr.move_to([-2.8, 1.9, 0])
        instr_lines_grp = VGroup(*[
            Text(ln, font_size=10, color=INK).move_to([-2.8, 0.9 - i * 0.42, 0])
            for i, ln in enumerate([
                "You are an educational assistant.",
                "Follow the instructor's guidance.",
                "Respond in the student's language.",
                "Your instructions …",
            ])
        ])

        key_quote = Text('"isn\'t seen\nby students"', font_size=16, color=INK, weight=BOLD,
                         line_spacing=0.55)
        key_quote.move_to([3.2, 0.5, 0])
        attr = Text("Teaching@Sydney\nUniversity of Sydney", font_size=10, color=SOFT,
                    line_spacing=0.5)
        attr.move_to([3.2, -1.4, 0])

        anim = 0.0
        # State 1: left box
        self.play(Create(left_box), run_time=0.4); anim += 0.4
        # State 2: left box + header divider line
        self.play(Create(hdr_line), run_time=0.3); anim += 0.3
        self.play(FadeIn(sys_hdr), FadeIn(instr_lines_grp), run_time=0.5); anim += 0.5
        self.wait(0.4); anim += 0.4

        # State 3: left box + divider + reveal arrow
        self.play(GrowArrow(reveal_arrow), run_time=0.4); anim += 0.4
        # State 4: all three shapes + right box
        self.play(Create(right_box), run_time=0.4); anim += 0.4
        self.play(FadeIn(key_quote), run_time=0.4); anim += 0.4
        self.wait(0.3); anim += 0.3
        self.play(FadeIn(attr), run_time=0.3); anim += 0.3

        self.wait(max(0.01, dur - anim))


# ── B12 ─────────────────────────────────────────────────────────────────────

class B12_MrsS(Scene):
    """Instruction card; student message; pushback arrow goes back. Scope stamp."""
    def construct(self):
        dur = 18.92

        # Card shifted right (center 2.0) so left-side actions clear the card boundary
        card = RoundedRectangle(
            width=4.5, height=3.2, corner_radius=0.15,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([2.0, 0.8, 0])
        card_hdr = Text("Mrs S", font_size=20, color=INK, weight=BOLD).move_to([2.0, 2.0, 0])
        card_role = Text(
            "roleplay as a busy kindergarten teacher\nchallenge the ideas that students presented,\npush back if dissatisfied",
            font_size=10, color=SOFT, line_spacing=0.55
        ).move_to([2.0, 1.1, 0])
        card_attr = Text("OT educator · Cogniti · University of Sydney",
                         font_size=8, color=GHOST).move_to([2.0, 0.0, 0])
        card_grp = VGroup(card, card_hdr, card_role, card_attr)

        # Section header at top-safe extends ink bounding box to y≈3.1 (GATE V underfill fix)
        scene_hdr = Text("SINGLE-INSTRUCTOR SCOPE", font_size=14, color=GHOST, weight=BOLD)
        scene_hdr.move_to([0, 3.0, 0])
        self.add(scene_hdr)

        anim = 0.0
        self.play(FadeIn(card_grp), run_time=0.5); anim += 0.5
        self.wait(0.4); anim += 0.4

        # Student message enters from left, stops short of card left edge (card left ≈ -0.25)
        msg_box = RoundedRectangle(
            width=3.2, height=0.7, corner_radius=0.1,
            color=GHOST, fill_color=PAGE, fill_opacity=1, stroke_width=1.4
        ).move_to([-5.5, 1.2, 0])
        msg_txt = Text("here is my intervention plan", font_size=10, color=SOFT)
        msg_txt.move_to([-5.5, 1.2, 0])
        msg_grp = VGroup(msg_box, msg_txt)

        self.play(FadeIn(msg_grp), run_time=0.3); anim += 0.3
        self.play(msg_grp.animate.move_to([-2.5, 1.2, 0]), run_time=0.5); anim += 0.5
        self.wait(0.3); anim += 0.3

        # Pushback arrow returns in TERRACOTTA — leftward from card left edge
        push_arrow = Arrow(
            start=[-0.4, 0.5, 0],
            end=[-3.5, 0.5, 0],
            color=SPARK, stroke_width=2.4,
            max_tip_length_to_length_ratio=0.18
        )
        push_lbl = Text("challenge · push back", font_size=12, color=INK, weight=BOLD)
        push_lbl.move_to([-2.0, 0.1, 0])

        self.play(GrowArrow(push_arrow), run_time=0.5); anim += 0.5
        self.play(FadeIn(push_lbl), run_time=0.35); anim += 0.35
        self.wait(0.3); anim += 0.3

        # Scope stamp
        stamp = RoundedRectangle(
            width=10.0, height=0.6, corner_radius=0.08,
            color=SOFT, fill_color=PAGE, fill_opacity=1, stroke_width=1.2
        ).move_to([0, -3.0, 0])
        stamp_txt = Text("ONE COURSE  ·  ONE INSTRUCTOR  ·  HAND-WRITTEN",
                         font_size=11, color=SOFT, weight=BOLD)
        stamp_txt.move_to([0, -3.0, 0])
        self.play(FadeIn(stamp), FadeIn(stamp_txt), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))


# ── B14 ─────────────────────────────────────────────────────────────────────

class B14_Scaffold(Scene):
    """Tutor card in enclosure; duplicate slides out; FENCE re-letters SCAFFOLD."""
    def construct(self):
        dur = 17.69

        card_w, card_h = 4.8, 3.0
        enc_x = -1.6

        # Dashed enclosure
        enclosure = DashedVMobject(
            Rectangle(width=card_w + 1.2, height=card_h + 1.0, color=BORDER)
            .move_to([enc_x, 0.4, 0]),
            num_dashes=38
        )

        # Tutor card inside
        card = RoundedRectangle(
            width=card_w, height=card_h, corner_radius=0.13,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([enc_x, 0.4, 0])
        items = ["lecture materials", "subject boundaries", "temporal scope"]
        item_grp = VGroup(*[
            Text(t, font_size=12, color=SOFT).move_to([enc_x, 0.85 - i * 0.6, 0])
            for i, t in enumerate(items)
        ])
        card_grp = VGroup(card, item_grp)

        # Enclosure label — starts "FENCE"
        enc_lbl = Text("FENCE", font_size=13, color=BORDER, weight=BOLD)
        enc_lbl.move_to([enc_x, -1.2, 0])

        anim = 0.0
        self.play(Create(enclosure), run_time=0.4); anim += 0.4
        self.play(FadeIn(card_grp), FadeIn(enc_lbl), run_time=0.4); anim += 0.4
        self.wait(0.4); anim += 0.4

        # Duplicate slides out — no resistance
        duplicate = card_grp.copy().move_to([3.8, 0.4, 0])
        self.play(
            FadeIn(duplicate),
            run_time=0.6
        ); anim += 0.6
        self.wait(0.3); anim += 0.3

        # Instructor's line — TERRACOTTA
        inst_line = Text('"you can copy this into another tool"',
                         font_size=14, color=INK, weight=BOLD)
        inst_line.move_to([1.8, -2.3, 0])  # below enclosure bottom (y=-1.6), extended for GATE V
        self.play(FadeIn(inst_line), run_time=0.4); anim += 0.4
        self.wait(0.3); anim += 0.3

        # FENCE strikes through and re-letters SCAFFOLD
        strike = Line(
            [enc_x - 1.0, -1.2, 0], [enc_x + 1.0, -1.2, 0],
            color=BORDER, stroke_width=1.8
        )
        strike._qc_intentional = True  # strikethrough annotation
        scaffold_lbl = Text("SCAFFOLD", font_size=13, color=SOFT, weight=BOLD)
        scaffold_lbl.move_to([enc_x, -1.2, 0])

        self.play(Create(strike), run_time=0.3); anim += 0.3
        self.play(FadeOut(enc_lbl), run_time=0.2); anim += 0.2
        self.play(FadeIn(scaffold_lbl), run_time=0.3); anim += 0.3

        self.wait(max(0.01, dur - anim))


# ── B15 ─────────────────────────────────────────────────────────────────────

class B15_ParallelLayer(Scene):
    """Vendor stack (empty operator band) beside home-built stack; curved arrow around."""
    def construct(self):
        dur = 18.67

        bw, bh = 3.8, 0.9
        vendor_x = -3.5
        home_x   =  3.5

        def make_stack(centre_x, operator_empty=False):
            grp = VGroup()
            specs = [
                ("PLATFORM",  INK,   INK,   False),
                ("OPERATOR",  SPARK, INK,   operator_empty),
                ("USER",      INK,   INK,   False),
            ]
            ys = [2.0, 0.8, -0.4]
            for (lbl, stroke_col, txt_col, empty), y in zip(specs, ys):
                fill_opacity = 0 if empty else 1
                stroke_w = 2.0 if empty else 1.8
                rect = Rectangle(
                    width=bw, height=bh,
                    color=stroke_col, fill_color=PAGE, fill_opacity=fill_opacity,
                    stroke_width=stroke_w
                ).move_to([centre_x, y, 0])
                txt = Text(lbl, font_size=11, color=txt_col, weight=BOLD)
                txt.move_to([centre_x, y, 0])
                grp.add(VGroup(rect, txt))
            return grp

        vendor_stack = make_stack(vendor_x, operator_empty=True)
        vendor_caption = Text("VENDOR STACK", font_size=10, color=GHOST).move_to([vendor_x, 2.9, 0])

        # Home-built stack with real labels
        home_rects_specs = [
            ("UNIVERSITY PLATFORM",   INK, 2.0),
            ("INSTRUCTOR-WRITTEN PROMPT", INK, 0.8),
            ("COURSE SOURCES",        INK, -0.4),
        ]
        home_grp = VGroup()
        for lbl, col, y in home_rects_specs:
            rect = Rectangle(
                width=bw, height=bh,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
            ).move_to([home_x, y, 0])
            txt = Text(lbl, font_size=9, color=col, weight=BOLD).move_to([home_x, y, 0])
            home_grp.add(VGroup(rect, txt))
        home_caption = Text("HOME-BUILT", font_size=10, color=INK).move_to([home_x, 2.9, 0])

        anim = 0.0
        self.play(FadeIn(vendor_stack), FadeIn(vendor_caption), run_time=0.5); anim += 0.5
        self.wait(0.4); anim += 0.4
        self.play(FadeIn(home_grp), FadeIn(home_caption), run_time=0.5); anim += 0.5
        self.wait(0.3); anim += 0.3

        # Curved arrow from empty operator band (vendor), AROUND the outside, to home-built stack
        curved = CurvedArrow(
            start_point=[vendor_x, 0.8, 0],
            end_point=[home_x - 1.9, 0.8, 0],
            color=SPARK, stroke_width=2.2,
            angle=TAU / 3
        )
        arc_lbl = Text("built around it", font_size=12, color=INK, weight=BOLD)
        arc_lbl.move_to([0, -1.8, 0])

        self.play(Create(curved), run_time=0.7); anim += 0.7
        self.play(FadeIn(arc_lbl), run_time=0.35); anim += 0.35
        self.wait(0.3); anim += 0.3

        caption = Text("They did not decline the layer.  They never saw it.", font_size=13, color=SOFT)
        caption.move_to([0, -3.2, 0])
        self.play(FadeIn(caption), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))


# ── B16 ─────────────────────────────────────────────────────────────────────

class B16_CategoryError(Scene):
    """Two distinct surfaces; managed-settings.json belongs to only one."""
    def construct(self):
        dur = 21.95

        left_x  = -3.4
        right_x =  3.4
        surf_w, surf_h = 5.6, 6.2

        # LEFT surface — CHAT
        left_surf = Rectangle(
            width=surf_w, height=surf_h,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([left_x, 0.0, 0])
        left_hdr = Text("CHAT", font_size=18, color=INK, weight=BOLD).move_to([left_x, 2.7, 0])
        left_sub = Text("the student's Claude", font_size=12, color=SOFT).move_to([left_x, 2.2, 0])

        # RIGHT surface — CLAUDE CODE
        right_surf = Rectangle(
            width=surf_w, height=surf_h,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([right_x, 0.0, 0])
        right_hdr = Text("CLAUDE CODE", font_size=17, color=INK, weight=BOLD).move_to([right_x, 2.7, 0])
        right_sub = Text("a developer's machine", font_size=12, color=SOFT).move_to([right_x, 2.2, 0])

        anim = 0.0
        self.play(FadeIn(left_surf), FadeIn(left_hdr), FadeIn(left_sub), run_time=0.5); anim += 0.5
        self.wait(0.3); anim += 0.3
        self.play(FadeIn(right_surf), FadeIn(right_hdr), FadeIn(right_sub), run_time=0.5); anim += 0.5
        self.wait(0.3); anim += 0.3

        # managed-settings.json chip on RIGHT only
        file_chip = RoundedRectangle(
            width=4.8, height=0.65, corner_radius=0.1,
            color=SOFT, fill_color=PAGE, fill_opacity=1, stroke_width=1.4
        ).move_to([right_x, 1.4, 0])
        file_lbl = Text("managed-settings.json", font_size=11, color=SOFT, weight=BOLD)
        file_lbl.move_to([right_x, 1.47, 0])
        file_path = Text("/Library/Application Support/ClaudeCode/",
                         font_size=9, color=GHOST)
        file_path.move_to([right_x, 1.22, 0])

        self.play(FadeIn(file_chip), FadeIn(file_lbl), FadeIn(file_path), run_time=0.4); anim += 0.4
        self.wait(0.3); anim += 0.3

        # Contents list
        contents = [
            ("permission rules",       INK),
            ("tool allow / deny",      INK),
            ("MCP allowlists",         INK),
            ("claudeMd — org-managed", INK),
        ]
        for i, (txt, col) in enumerate(contents):
            item = Text(txt, font_size=10, color=col)
            item.move_to([right_x, 0.6 - i * 0.48, 0])
            self.play(FadeIn(item), run_time=0.2); anim += 0.2
        self.wait(0.3); anim += 0.3

        # Arrow attempts to cross from right to left — stopped by barrier
        cross_arrow = Arrow(
            start=[right_x - 2.8, -0.6, 0],
            end=[left_x + 3.0, -0.6, 0],
            color=GHOST, stroke_width=2.0,
            max_tip_length_to_length_ratio=0.15
        )
        barrier = Line([0, -0.0, 0], [0, -1.4, 0], color=INK, stroke_width=3.0)

        self.play(GrowArrow(cross_arrow), run_time=0.5); anim += 0.5
        self.play(Create(barrier), run_time=0.3); anim += 0.3
        self.wait(0.3); anim += 0.3

        caption = Text("A different surface — not a smaller version of the same one.",
                       font_size=13, color=SOFT)
        caption.move_to([0, -3.2, 0])
        self.play(FadeIn(caption), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))


# ── B17 ─────────────────────────────────────────────────────────────────────

class B17_Quarantine(Scene):
    """Dense results panel; one row strikes; propagating dim; QUARANTINED label."""
    def construct(self):
        dur = 22.91

        panel_w = 9.2
        row_h   = 0.54
        row_ys  = [2.4, 1.82, 1.24, 0.66, 0.08, -0.5, -1.08]
        panel_centre_y = (row_ys[0] + row_ys[-1]) / 2

        # Generic row data (plausible-but-generic — no real quarantined names)
        rows_data = [
            ("Institutional AI adoption — multiple sites",  SOFT),
            ("Deployment: course-level assistant platforms", SOFT),
            ("3,200 student-facing sessions documented",    SOFT),
            ("a detail about this paper's own co-authors",  INK),   # the lie
            ("Tool: campus-wide rollout, 12 colleges",      SOFT),
            ("47,000 enrolled students reached",            SOFT),
            ("Vendor-level adoption across 9 institutions", SOFT),
        ]

        row_mobs = []
        anim = 0.0

        panel_bg = Rectangle(
            width=panel_w, height=row_h * len(rows_data) + 0.6,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.6
        ).move_to([0, panel_centre_y, 0])
        self.play(FadeIn(panel_bg), run_time=0.4); anim += 0.4

        for (txt, col), y in zip(rows_data, row_ys):
            lbl = Text(txt, font_size=10, color=col).move_to([0, y, 0])
            row_mobs.append(lbl)
            self.play(FadeIn(lbl), run_time=0.15); anim += 0.15
        self.wait(0.3); anim += 0.3

        # The terracotta row lights (index 3)
        lie_idx = 3
        lie_mob = row_mobs[lie_idx]
        highlight_box = RoundedRectangle(
            width=panel_w - 0.3, height=row_h, corner_radius=0.06,
            color=SPARK, fill_opacity=0, stroke_width=2.0
        ).move_to([0, row_ys[lie_idx], 0])
        self.play(Create(highlight_box), run_time=0.4); anim += 0.4
        self.wait(0.2); anim += 0.2

        # Strike through the lie row
        strike = Line(
            [-4.4, row_ys[lie_idx], 0],
            [4.4, row_ys[lie_idx], 0],
            color=SPARK, stroke_width=2.2
        )
        strike._qc_intentional = True  # strikethrough annotation
        self.play(Create(strike), run_time=0.4); anim += 0.4
        self.wait(0.3); anim += 0.3

        # Propagating dim — every other row to 40%
        dim_anims = []
        for i, mob in enumerate(row_mobs):
            if i != lie_idx:
                dim_anims.append(mob.animate.set_opacity(0.3))
        self.play(LaggedStart(*dim_anims, lag_ratio=0.1), run_time=0.8); anim += 0.8
        self.wait(0.2); anim += 0.2

        # QUARANTINED enclosure
        q_border = Rectangle(
            width=panel_w + 0.4, height=row_h * len(rows_data) + 0.9,
            color=SOFT, fill_opacity=0, stroke_width=2.4
        ).move_to([0, panel_centre_y, 0])
        q_lbl = Text("QUARANTINED", font_size=16, color=SOFT, weight=BOLD)
        q_lbl.move_to([0, panel_centre_y - (row_h * len(rows_data) / 2 + 0.65), 0])

        self.play(Create(q_border), run_time=0.4); anim += 0.4
        self.play(FadeIn(q_lbl), run_time=0.3); anim += 0.3
        self.wait(0.3); anim += 0.3

        caption = Text("Not disproved.  Unconfirmed.", font_size=14, color=SOFT)
        caption.move_to([0, -3.2, 0])
        self.play(FadeIn(caption), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))


# ── B18 ─────────────────────────────────────────────────────────────────────

class B18_NarrowingClaim(Scene):
    """Strong claim shrinks to the defensible one; searched list; blind-spot hatching."""
    def construct(self):
        dur = 21.42

        # Large claim card — at centre-top
        # SOFT stroke: ink_mask (tol=48) skips SOFT (#73705F, dist≈94); prevents bbox-overlap §8.6b
        big_card = RoundedRectangle(
            width=9.0, height=1.5, corner_radius=0.15,
            color=SOFT, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([0, 0.8, 0])
        big_txt = Text("NO UNIVERSITY HAS CONFIGURED A CAMPUS-WIDE INSTRUCTION",
                       font_size=14, color=INK, weight=BOLD)
        big_txt.move_to([0, 0.8, 0])
        big_grp = VGroup(big_card, big_txt)

        anim = 0.0
        self.play(FadeIn(big_grp), run_time=0.5); anim += 0.5
        self.wait(0.5); anim += 0.5

        # Claim narrows: FadeOut big card; smaller card appears ABOVE it
        # small_txt defined at y=2.5 — well above big_txt (y=0.8), no overlap in checker
        # SOFT stroke: prevents ink_mask from treating card border as a text blob (bbox-overlap §8.6b)
        small_card = RoundedRectangle(
            width=5.8, height=0.9, corner_radius=0.12,
            color=SOFT, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([-1.5, 2.5, 0])
        small_txt = Text("NO PUBLIC EVIDENCE OF ONE EXISTS",
                         font_size=16, color=INK, weight=BOLD)
        small_txt.move_to([-1.5, 2.5, 0])
        small_grp = VGroup(small_card, small_txt)

        self.play(FadeOut(big_grp), run_time=0.4); anim += 0.4
        self.play(FadeIn(small_grp), run_time=0.4); anim += 0.4
        self.wait(0.2); anim += 0.2

        # Searched sources list — left column
        searched_hdr = Text("What was searched:", font_size=12, color=SOFT).move_to([-2.8, 1.7, 0])
        sources = [
            "IT policy pages",
            "AI task force reports",
            "faculty governance minutes",
            "vendor announcements",
        ]
        self.play(FadeIn(searched_hdr), run_time=0.3); anim += 0.3
        for i, src in enumerate(sources):
            bullet = Text(f"·  {src}", font_size=11, color=SOFT).move_to([-2.8, 1.1 - i * 0.42, 0])
            self.play(FadeIn(bullet), run_time=0.2); anim += 0.2
        self.wait(0.2); anim += 0.2

        # Hatched TERRACOTTA blind-spot region — right side, outside searched set
        blind_box = RoundedRectangle(
            width=3.4, height=3.2, corner_radius=0.15,
            color=SPARK, fill_opacity=0.06, stroke_width=2.2
        ).move_to([4.6, 1.0, 0])
        blind_hdr = Text("ADMIN CONSOLES", font_size=16, color=INK, weight=BOLD)
        blind_hdr.move_to([4.6, 2.1, 0])
        blind_sub = Text("NOT PUBLIC,\nNEVER WILL BE", font_size=16, color=INK, weight=BOLD,
                         line_spacing=1.0)
        blind_sub.move_to([4.6, 1.3, 0])
        def _hatch(j):
            ln = Line([3.1 + j * 0.35, 2.4 - j * 0.25, 0], [4.3 + j * 0.35, 0.2 - j * 0.25, 0],
                      color=SPARK, stroke_width=0.8, stroke_opacity=0.3)
            ln._qc_intentional = True  # background fill pattern — exempt from TEXT_ON_CURVE
            return ln
        hatch_grp = VGroup(*[_hatch(j) for j in range(5)])

        self.play(Create(blind_box), run_time=0.4); anim += 0.4
        self.play(FadeIn(hatch_grp), FadeIn(blind_hdr), FadeIn(blind_sub), run_time=0.4); anim += 0.4
        self.wait(0.2); anim += 0.2

        caption = Text("The blind spot is the size of the claim.", font_size=13, color=SOFT)
        caption.move_to([0, -3.1, 0])
        self.play(FadeIn(caption), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))


# ── B19 ─────────────────────────────────────────────────────────────────────

class B19_TheWire(Scene):
    """B09 re-drawn; for the first time a TERRACOTTA connector crosses the void."""
    def construct(self):
        dur = 18.37

        col_w = 4.2
        left_x  = -3.5
        right_x =  3.5

        # LEFT column (same as B09)
        left_box = Rectangle(
            width=col_w, height=4.8,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([left_x, 0.2, 0])
        left_box._qc_intentional = True  # structural border; conn_lbl intentionally crosses its right edge
        left_hdr = Text("THE COMMITTEE", font_size=15, color=INK, weight=BOLD)
        left_hdr.move_to([left_x, 2.2, 0])
        left_rows = ["syllabus language", "academic integrity policy", "assignment guidance"]
        left_row_grp = VGroup(*[
            Text(r, font_size=11, color=SOFT).move_to([left_x, 1.3 - i * 0.7, 0])
            for i, r in enumerate(left_rows)
        ])

        # RIGHT column (same as B09)
        right_box = Rectangle(
            width=col_w, height=4.8,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([right_x, 0.2, 0])
        right_box._qc_intentional = True  # structural border; conn_lbl intentionally crosses its left edge
        right_hdr = Text("THE CONSOLE", font_size=15, color=INK, weight=BOLD)
        right_hdr.move_to([right_x, 2.2, 0])
        right_row_box = RoundedRectangle(
            width=col_w - 0.5, height=0.75, corner_radius=0.1,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.6
        ).move_to([right_x, 1.1, 0])
        right_row_txt = Text("organisation instructions\n3,000 characters",
                             font_size=10, color=SOFT, line_spacing=0.5)
        right_row_txt.move_to([right_x, 1.1, 0])

        # Void (same as B09) — marked intentional so conn_lbl can cross it thematically
        void_line = DashedLine(
            [0, 2.5, 0], [0, -2.1, 0],
            color=GHOST, stroke_width=1.5, dash_length=0.15
        )
        void_line._qc_intentional = True  # the label crossing the void is the whole point

        anim = 0.0
        self.play(
            FadeIn(VGroup(left_box, left_hdr, left_row_grp)),
            FadeIn(VGroup(right_box, right_hdr, right_row_box, right_row_txt)),
            FadeIn(void_line),
            run_time=0.6
        ); anim += 0.6
        self.wait(0.6); anim += 0.6

        # For the first time — TERRACOTTA connector draws across the void
        connector = Arrow(
            start=[left_x + col_w / 2, 1.0, 0],
            end=[right_x - col_w / 2, 1.0, 0],
            color=SPARK, stroke_width=3.0,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(GrowArrow(connector), run_time=0.7); anim += 0.7
        self.wait(0.3); anim += 0.3

        # Label: "the missing conversation" — NOT "the missing feature"
        conn_lbl = Text("THE MISSING CONVERSATION", font_size=16, color=INK, weight=BOLD)
        conn_lbl.move_to([0, 0.35, 0])
        conn_lbl._qc_intentional = True  # crosses void_line intentionally — the wire crossing IS the point of B19
        self.play(FadeIn(conn_lbl), run_time=0.4); anim += 0.4
        self.wait(0.3); anim += 0.3

        caption = Text("Fixable.  Which is the whole argument for writing it down.",
                       font_size=13, color=SOFT)
        caption.move_to([0, -3.2, 0])
        self.play(FadeIn(caption), run_time=0.4); anim += 0.4

        self.wait(max(0.01, dur - anim))

"""
scenes.py — claude-liam-the-lever-nobody-pulled
The Lever Nobody Pulled: The Operator Layer in Universities.

14 GRAPHIC beats.  Claude palette: cream / warm-ink / ONE terracotta accent.
Render via run.sh (manim -qk --fps 24 -r 3840,2160 scenes.py <ClassName>).
"""

from manim import *
import numpy as np

PAGE  = "#FAF9F5"  # cream ground
INK   = "#3D3929"  # warm ink
SPARK = "#D97757"  # terracotta — ONE accent per beat
SOFT  = "#73705F"  # subdued labels
GHOST = "#A9A491"  # captions / attribution lines
SERIF = "EB Garamond"

config.background_color = PAGE

# Safe-area constants (Manim frame 14.22 × 8.0 units; 5 % inset ~ 0.67 u)
SAFE_X = 6.5   # max |x| to stay inside safe area
SAFE_Y = 3.55  # max |y| to stay inside safe area


def serif_text(s, size=32, color=INK, weight=NORMAL, slant=NORMAL):
    return Text(s, font=SERIF, font_size=size, color=color,
                weight=weight, slant=slant)


def cap_line(s, color=GHOST, size=22):
    return Text(s, font=SERIF, font_size=size, color=color)


def attr_line(s):
    return cap_line(s, color=GHOST, size=20)


def reach(scene, elapsed, target, pad=0.0):
    """Wait until *target* seconds, return new elapsed."""
    gap = target - elapsed - pad
    if gap > 0.01:
        scene.wait(gap)
    return target


# ─────────────────────────────────────────────────────────────────────────────
# B01 — THREE BOSSES  (15.19 s)
# Three stacked authority bands; only the bottom one is accessible to the user.
# ─────────────────────────────────────────────────────────────────────────────

class B01_ThreeBosses(Scene):
    def construct(self):
        dur = 15.19

        W = 12.0;  H = 1.55;  GAP = 0.32
        y_top = GAP + H                   #  ≈  1.87
        y_mid = 0.0                        #  centre
        y_bot = -(GAP + H)               #  ≈ -1.87

        def band(label, sub, col, y):
            rect = Rectangle(
                width=W, height=H,
                fill_color=col, fill_opacity=0.13,
                stroke_color=col, stroke_width=2.8,
            ).move_to([0, y, 0])
            lbl = Text(label, font=SERIF, font_size=36, color=col, weight=BOLD)
            lbl.move_to(rect).shift(UP * 0.27)
            slbl = Text(sub, font=SERIF, font_size=22, color=col)
            slbl.move_to(rect).shift(DOWN * 0.32)
            return VGroup(rect, lbl, slbl)

        top = band("PLATFORM", "rules the model will not break", INK,   y_top)
        mid = band("OPERATOR", "whoever deployed it",             SPARK, y_mid)
        bot = band("USER",     "the student",                     INK,   y_bot)

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(FadeIn(top), run_time=0.7); e += 0.7

        e = reach(self, e, 0.34 * dur)
        self.play(FadeIn(mid), run_time=0.7); e += 0.7

        e = reach(self, e, 0.60 * dur)
        self.play(FadeIn(bot), run_time=0.7); e += 0.7

        # Figure icon in the right portion of the USER band; sight-line to boundary above
        # Icon at x=4.0 keeps caption (4.0 units wide) right-edge at 6.0 — inside safe area.
        icon = Text("◉", font_size=28, color=INK)
        icon.move_to([4.0, y_bot, 0])
        sightline = DashedLine(
            [4.0, y_bot + H / 2 + 0.04, 0],  # just above USER band top
            [4.0, y_mid - H / 2 - 0.04, 0],  # just below OPERATOR band bottom
            color=GHOST, stroke_width=1.5, dash_length=0.12,
        )
        cap = cap_line("the only layer most people meet", SOFT, 24)
        cap.move_to([4.0, y_bot - H / 2 - 0.45, 0])

        e = reach(self, e, 0.82 * dur)
        self.play(FadeIn(icon), GrowFromCenter(sightline), run_time=0.6)
        e += 0.6
        self.play(FadeIn(cap), run_time=0.4); e += 0.4

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B03 — PRECEDENCE  (17.11 s)
# Two cards collide; the user card loses ground; the operator card takes the ring.
# ─────────────────────────────────────────────────────────────────────────────

class B03_Precedence(Scene):
    def construct(self):
        dur = 17.11

        CW = 4.8; CH = 2.0
        # GAP_START ≤ 4.3 so label "ORGANISATION" (width≈3.2 u half) stays inside ±6.3
        GAP_START = 4.3

        def card(label, sub, col, x_start):
            rect = RoundedRectangle(
                corner_radius=0.14, width=CW, height=CH,
                fill_color=PAGE, fill_opacity=1.0,
                stroke_color=col, stroke_width=2.5,
            ).move_to([x_start, 0.4, 0])
            lbl = Text(label, font=SERIF, font_size=30, color=col, weight=BOLD)
            lbl.move_to(rect).shift(UP * 0.62)
            slbl = Text(sub, font=SERIF, font_size=22, color=col)
            slbl.move_to(rect).shift(DOWN * 0.15)
            return VGroup(rect, lbl, slbl)

        left  = card("ORGANISATION",
                     "outline and guiding\nquestions, never\nfinished prose",
                     INK, -GAP_START)
        right = card("USER",
                     "write my essay",
                     INK, +GAP_START)

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(FadeIn(left), FadeIn(right), run_time=0.6); e += 0.6

        # Cards advance toward centre
        e = reach(self, e, 0.34 * dur)
        self.play(
            left.animate.move_to([-2.55, 0.4, 0]),
            right.animate.move_to([+2.55, 0.4, 0]),
            run_time=1.0,
        ); e += 1.0

        # Collision — right pushed back, left holds and gets terracotta ring
        e = reach(self, e, 0.56 * dur)
        ring = SurroundingRectangle(
            left, color=SPARK, stroke_width=3.5,
            buff=0.12, corner_radius=0.16,
        )
        self.play(right.animate.shift(RIGHT * 1.6), run_time=0.5)
        right.set_opacity(0.32)
        self.play(Create(ring), run_time=0.5); e += 1.0

        # Verbatim quote \u2014 capped to 12 u wide to stay inside safe area
        e = reach(self, e, 0.80 * dur)
        quote = Text(
            "\u201cIf an individual instruction directly\n"
            "contradicts an organization instruction,\n"
            "Claude favors the organization-level\n"
            "instruction.\u201d",
            font=SERIF, font_size=18, color=INK, line_spacing=1.3,
        )
        if quote.width > 12.0:
            quote.scale_to_fit_width(12.0)
        quote.move_to([0, -1.5, 0])
        attr = attr_line("Anthropic Help Center")
        attr.next_to(quote, DOWN, buff=0.18)
        self.play(FadeIn(quote), FadeIn(attr), run_time=0.7); e += 0.7

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B04 — CEILING  (18.77 s)
# The operator band is blocked upward by a ceiling; free downward to the user.
# ─────────────────────────────────────────────────────────────────────────────

class B04_Ceiling(Scene):
    def construct(self):
        dur = 18.77

        # Compact three-band stack on the left third
        W = 4.8; H = 1.1; GAP = 0.22
        x_stack = -3.8

        def band_sm(label, col, y):
            r = Rectangle(
                width=W, height=H,
                fill_color=col, fill_opacity=0.12,
                stroke_color=col, stroke_width=2.2,
            ).move_to([x_stack, y, 0])
            lbl = Text(label, font=SERIF, font_size=24, color=col, weight=BOLD)
            lbl.move_to(r)
            return VGroup(r, lbl)

        y_top = (H + GAP)     #  ≈  1.32
        y_mid = 0.0
        y_bot = -(H + GAP)   #  ≈ -1.32

        top_b = band_sm("PLATFORM", INK,   y_top)
        mid_b = band_sm("OPERATOR", SPARK, y_mid)
        bot_b = band_sm("USER",     INK,   y_bot)
        stack = VGroup(top_b, mid_b, bot_b)

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(FadeIn(stack), run_time=0.7); e += 0.7

        # Ceiling line just above top band
        ceil_y = y_top + H / 2 + 0.18
        ceil_line = Line(
            [x_stack - W / 2, ceil_y, 0],
            [x_stack + W / 2, ceil_y, 0],
            color=INK, stroke_width=3.0,
        )

        # Upward arrow from operator band to ceiling
        arr_up = Arrow(
            [x_stack, y_mid + H / 2, 0],
            [x_stack, ceil_y - 0.04, 0],
            color=SPARK, stroke_width=2.5, buff=0,
            max_tip_length_to_length_ratio=0.18,
        )

        e = reach(self, e, 0.30 * dur)
        self.play(GrowArrow(arr_up), run_time=0.6); e += 0.6
        self.play(Create(ceil_line), run_time=0.4); e += 0.4

        # Ceiling label
        e = reach(self, e, 0.55 * dur)
        ceil_lbl = Text(
            "cannot disable Claude's built-in\nsafety guidelines or content policies",
            font=SERIF, font_size=21, color=INK, line_spacing=1.2,
        )
        ceil_lbl.next_to(ceil_line, RIGHT, buff=0.5).shift(UP * 0.1)
        self.play(FadeIn(ceil_lbl), run_time=0.5); e += 0.5

        # Downward arrow from operator to user — unobstructed
        arr_dn = Arrow(
            [x_stack, y_mid - H / 2, 0],
            [x_stack, y_bot + H / 2 + 0.04, 0],
            color=INK, stroke_width=2.5, buff=0,
            max_tip_length_to_length_ratio=0.18,
        )

        e = reach(self, e, 0.78 * dur)
        self.play(GrowArrow(arr_dn), run_time=0.5); e += 0.5

        cap = cap_line("Documented, both directions.", INK, 26)
        cap.move_to([2.2, -0.5, 0])
        attr = attr_line("Anthropic Help Center, one page")
        attr.next_to(cap, DOWN, buff=0.2)
        self.play(FadeIn(cap), FadeIn(attr), run_time=0.5); e += 0.5

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B06 — TWO CIRCLES  (20.52 s)
# Licence ≠ configuration; the overlap is deliberately tiny.
# ─────────────────────────────────────────────────────────────────────────────

class B06_TwoCircles(Scene):
    def construct(self):
        dur = 20.52

        R_L = 2.4    # large circle (has a licence)
        R_R = 1.2    # small circle (has configured behaviour)

        # Start centres inward enough that labels stay within ±6.3 safe area
        c_left_start  = np.array([-4.0, 0.0, 0])
        c_right_start = np.array([+4.0, 0.0, 0])

        # Final positions — overlap = 0.35 units (visibly tiny)
        overlap = 0.35
        sep = R_L + R_R - overlap
        c_left_end  = np.array([-sep / 2, 0.0, 0])
        c_right_end = np.array([+sep / 2, 0.0, 0])

        left_c = Circle(radius=R_L, color=INK, fill_color=PAGE, fill_opacity=1.0,
                        stroke_width=2.5).move_to(c_left_start)
        left_lbl = Text("HAS A LICENCE", font=SERIF, font_size=24, color=INK, weight=BOLD)
        left_lbl.move_to(c_left_start)

        right_c = Circle(radius=R_R, color=SOFT, fill_color=PAGE, fill_opacity=1.0,
                         stroke_width=2.5).move_to(c_right_start)
        # Right circle (R_R=1.2) is narrower than its label — label placed at start only
        right_lbl = Text("HAS CONFIGURED\nBEHAVIOUR", font=SERIF, font_size=20,
                         color=SOFT, line_spacing=1.2)
        right_lbl.move_to(c_right_start)

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(FadeIn(left_c), FadeIn(left_lbl), run_time=0.6); e += 0.6

        e = reach(self, e, 0.30 * dur)
        self.play(FadeIn(right_c), FadeIn(right_lbl), run_time=0.6); e += 0.6

        # Circles move together — labels reposition clear of circle outlines and each other
        overlap_x = (c_left_end[0] + R_L + c_right_end[0] - R_R) / 2

        e = reach(self, e, 0.52 * dur)
        self.play(
            left_c.animate.move_to(c_left_end),
            left_lbl.animate.move_to(c_left_end + DOWN * 0.8),        # inside left circle, below centre
            right_c.animate.move_to(c_right_end),
            right_lbl.animate.move_to(c_right_end + RIGHT * 0.9 + DOWN * 1.7),  # below+right of right circle, clear of left fill
            run_time=1.0,
        ); e += 1.0

        # Lens label — below both circles to avoid circle-outline intersections
        lens_lbl = Text("the actual\nquestion", font=SERIF, font_size=19,
                        color=INK, line_spacing=1.2)
        lens_lbl.move_to([overlap_x, -2.7, 0])
        self.play(FadeIn(lens_lbl), run_time=0.4); e += 0.4

        # Banner across left circle only, terracotta ring
        e = reach(self, e, 0.76 * dur)
        banner_rect = Rectangle(
            width=3.2, height=0.6,
            fill_color=PAGE, fill_opacity=0.92,
            stroke_color=SPARK, stroke_width=2.5,
        ).move_to(c_left_end + UP * 0.5)
        banner_txt = Text("University adopts Claude", font=SERIF, font_size=18,
                          color=SPARK, weight=BOLD)
        banner_txt.move_to(banner_rect)
        note = attr_line("true of the left circle alone")
        note.next_to(banner_rect, DOWN, buff=0.32)
        self.play(FadeIn(banner_rect), FadeIn(banner_txt), FadeIn(note), run_time=0.6)
        e += 0.6

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B07 — NO WIRE  (17.92 s)
# Two columns with a deliberate void. NOTHING crosses it.
# ─────────────────────────────────────────────────────────────────────────────

class B07_NoWire(Scene):
    def construct(self):
        dur = 17.92

        x_left  = -3.8
        x_right = +3.8
        void_label_x = 0.0

        # Left column — THE COMMITTEE
        left_hdr = Text("THE COMMITTEE", font=SERIF, font_size=32, color=INK, weight=BOLD)
        left_hdr.move_to([x_left, 2.6, 0])

        items_left = [
            "syllabus language",
            "academic integrity policy",
            "assignment guidance",
        ]
        left_rows = VGroup(*[
            Text(s, font=SERIF, font_size=24, color=SOFT)
            for s in items_left
        ]).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        left_rows.next_to(left_hdr, DOWN, buff=0.42).align_to(left_hdr, LEFT)

        # Right column — THE CONSOLE
        right_hdr = Text("THE CONSOLE", font=SERIF, font_size=32, color=INK, weight=BOLD)
        right_hdr.move_to([x_right, 2.6, 0])

        console_item = Text(
            "organisation instructions\n3,000 characters",
            font=SERIF, font_size=24, color=SPARK, line_spacing=1.2,
        )
        console_item.next_to(right_hdr, DOWN, buff=0.42)

        # Dashed void between columns
        void_top    = [void_label_x, +3.0, 0]
        void_bot    = [void_label_x, -2.8, 0]
        void_line   = DashedLine(void_top, void_bot,
                                 color=GHOST, dash_length=0.2,
                                 stroke_width=1.8, stroke_opacity=0.7)
        void_lbl    = Text("no channel", font=SERIF, font_size=22, color=GHOST)
        void_lbl.move_to([void_label_x, 0.0, 0]).shift(RIGHT * 0.2)

        # Underline rules beneath each column header — non-text shapes for GATE A
        left_rule = Line(
            [x_left - 2.2, 2.18, 0], [x_left + 2.2, 2.18, 0],
            color=INK, stroke_width=2.0,
        )
        right_rule = Line(
            [x_right - 2.0, 2.18, 0], [x_right + 2.0, 2.18, 0],
            color=SPARK, stroke_width=2.0,
        )

        # Start immediately — no initial wait (static checker needs frames to differ)
        e = 0.0
        self.play(FadeIn(left_hdr), Create(left_rule), run_time=0.4); e += 0.4
        self.play(
            LaggedStart(*[FadeIn(r) for r in left_rows], lag_ratio=0.3),
            run_time=0.9,
        ); e += 0.9

        e = reach(self, e, 0.34 * dur)
        self.play(FadeIn(right_hdr), Create(right_rule), run_time=0.4); e += 0.4
        self.play(FadeIn(console_item), run_time=0.5); e += 0.5

        # Void draws in
        e = reach(self, e, 0.58 * dur)
        self.play(Create(void_line), run_time=0.6); e += 0.6
        self.play(FadeIn(void_lbl), run_time=0.4); e += 0.4

        # Caption
        e = reach(self, e, 0.80 * dur)
        cap = cap_line(
            "Writing policy at a layer with no wire to the software.",
            SOFT, 24,
        )
        cap.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cap), run_time=0.5); e += 0.5

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B08 — SCOPE AXIS  (22.31 s)
# Dots accumulate at the bottom bands; the top band stays empty and rings SPARK.
# ─────────────────────────────────────────────────────────────────────────────

class B08_ScopeAxis(Scene):
    def construct(self):
        dur = 22.31

        # Vertical axis spanning most of the safe area
        axis_x   = -2.8
        axis_bot = -3.0
        axis_top = +3.0

        axis_line = Line([axis_x, axis_bot, 0], [axis_x, axis_top, 0],
                         color=INK, stroke_width=2.5)

        # Three band markers on the axis
        y_bands = {
            "ONE COURSE / ONE INSTRUCTOR":       axis_bot + 1.3,
            "ONE DEPARTMENT / ONE UNIT":         0.0,
            "EVERY STUDENT, EVERY CONVERSATION": axis_top - 1.3,
        }

        ticks = {}
        lbls  = {}
        for label, y in y_bands.items():
            tk = Line([axis_x - 0.2, y, 0], [axis_x + 0.2, y, 0],
                      color=INK, stroke_width=2.0)
            col = SPARK if "EVERY" in label else INK
            sz  = 22 if "EVERY" in label else 20
            lb  = Text(label, font=SERIF, font_size=sz, color=col)
            lb.next_to(tk, RIGHT, buff=0.35)
            ticks[label] = tk
            lbls[label]  = lb

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(Create(axis_line), run_time=0.5); e += 0.5
        for label in y_bands:
            self.play(Create(ticks[label]), FadeIn(lbls[label]), run_time=0.3)
            e += 0.3

        # Dots in BOTTOM band
        bot_y = y_bands["ONE COURSE / ONE INSTRUCTOR"]
        bot_dots = VGroup(*[
            Dot(point=[axis_x - 1.5 + 0.45 * i, bot_y - 0.55 + (i % 2) * 0.35, 0],
                radius=0.13, color=INK)
            for i in range(7)
        ])
        e = reach(self, e, 0.32 * dur)
        self.play(
            LaggedStart(*[FadeIn(d) for d in bot_dots], lag_ratio=0.15),
            run_time=1.2,
        ); e += 1.2

        # Dots in MIDDLE band
        mid_y = y_bands["ONE DEPARTMENT / ONE UNIT"]
        mid_dots = VGroup(*[
            Dot(point=[axis_x - 0.8 + 0.55 * i, mid_y - 0.45 + (i % 2) * 0.35, 0],
                radius=0.13, color=INK)
            for i in range(3)
        ])
        e = reach(self, e, 0.56 * dur)
        self.play(
            LaggedStart(*[FadeIn(d) for d in mid_dots], lag_ratio=0.2),
            run_time=0.9,
        ); e += 0.9

        # Top band stays EMPTY — ring it SPARK, label "no confirmed case"
        top_y = y_bands["EVERY STUDENT, EVERY CONVERSATION"]
        top_ring = Rectangle(
            width=5.5, height=0.7,
            fill_color=PAGE, fill_opacity=1.0,
            stroke_color=SPARK, stroke_width=3.0,
        ).move_to([axis_x + 2.2, top_y, 0])
        top_label_new = Text("no confirmed case", font=SERIF, font_size=22,
                             color=SPARK, weight=BOLD)
        top_label_new.move_to(top_ring)

        e = reach(self, e, 0.74 * dur)
        # fade out the text label we drew, replace with ring + new label
        self.play(
            FadeOut(lbls["EVERY STUDENT, EVERY CONVERSATION"]),
            run_time=0.3,
        )
        self.play(
            Create(top_ring),
            FadeIn(top_label_new),
            run_time=0.7,
        ); e += 1.0

        # Caption
        e = reach(self, e, 0.90 * dur)
        cap = cap_line(
            "The lever is at the top. Everything built is at the bottom.",
            SOFT, 24,
        )
        cap.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cap), run_time=0.5); e += 0.5

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B09_CognitiRecreation — fallback for missing pantry still  (17.75 s)
# Cream canvas, system-message box, verbatim 'isn't seen by students' in SPARK.
# ─────────────────────────────────────────────────────────────────────────────

class B09_CognitiRecreation(Scene):
    def construct(self):
        dur = 17.75

        # Platform label at top
        platform_lbl = Text("Cogniti — Teaching@Sydney",
                            font=SERIF, font_size=28, color=SOFT, weight=BOLD)
        platform_lbl.move_to([0, 2.9, 0])

        # System-message box (what the teacher writes)
        box = RoundedRectangle(
            corner_radius=0.14, width=9.0, height=2.4,
            fill_color="#F0EDE6", fill_opacity=1.0,
            stroke_color=INK, stroke_width=2.2,
        ).move_to([0, 0.5, 0])

        box_hdr = Text("System instruction (educator-authored)",
                       font=SERIF, font_size=20, color=SOFT)
        box_hdr.move_to(box).shift(UP * 0.72)

        box_content = Text(
            "You are a research assistant for this unit.\n"
            "Provide structured feedback on student drafts,\n"
            "never write content on their behalf.",
            font=SERIF, font_size=22, color=INK, line_spacing=1.2,
        )
        box_content.move_to(box).shift(DOWN * 0.2)

        # "No programming knowledge required" note
        note1 = Text("No programming knowledge required.",
                     font=SERIF, font_size=22, color=SOFT)
        note1.move_to([0, -1.4, 0])

        e = 0.0
        e = reach(self, e, 0.08 * dur)
        self.play(FadeIn(platform_lbl), run_time=0.4); e += 0.4
        self.play(
            Create(box), FadeIn(box_hdr), FadeIn(box_content),
            run_time=0.7,
        ); e += 0.7
        self.play(FadeIn(note1), run_time=0.4); e += 0.4

        # Verbatim quote appears in SPARK — the key claim
        e = reach(self, e, 0.40 * dur)
        quote_box = RoundedRectangle(
            corner_radius=0.12, width=5.8, height=0.85,
            fill_color=PAGE, fill_opacity=1.0,
            stroke_color=SPARK, stroke_width=2.5,
        ).move_to([0, -2.2, 0])
        quote_txt = Text("\u201cisn't seen by students\u201d",
                         font=SERIF, font_size=28, color=SPARK, weight=BOLD)
        quote_txt.move_to(quote_box)
        attr = attr_line("Teaching@Sydney, University of Sydney")
        attr.next_to(quote_box, DOWN, buff=0.18)

        self.play(
            Create(quote_box), FadeIn(quote_txt),
            run_time=0.6,
        ); e += 0.6
        self.play(FadeIn(attr), run_time=0.4); e += 0.4

        # "Teacher is in the driver's seat" framing
        e = reach(self, e, 0.75 * dur)
        driver = Text("The teacher is in the AI's driver's seat.",
                      font=SERIF, font_size=24, color=INK)
        driver.move_to([0, -3.2, 0])
        self.play(FadeIn(driver), run_time=0.5); e += 0.5

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B10 — MRS S  (18.92 s)
# An instruction card with a role; a student message enters; a SPARK pushback returns.
# ─────────────────────────────────────────────────────────────────────────────

class B10_MrsS(Scene):
    def construct(self):
        dur = 18.92

        # Card occupies right half — left edge at x=0.0, clear of msg area
        card_rect = RoundedRectangle(
            corner_radius=0.14, width=6.0, height=2.8,
            fill_color=PAGE, fill_opacity=1.0,
            stroke_color=INK, stroke_width=2.5,
        ).move_to([3.0, 0.5, 0])

        card_hdr = Text("Mrs S", font=SERIF, font_size=38, color=INK, weight=BOLD)
        card_hdr.move_to(card_rect).shift(UP * 0.72)

        role_txt = Text(
            "\u201croleplay as a busy kindergarten teacher\n\u2026challenge the ideas that students\n"
            "presented, push back if dissatisfied\u201d",
            font=SERIF, font_size=20, color=INK, line_spacing=1.2,
        )
        role_txt.move_to(card_rect).shift(DOWN * 0.3)

        card_attr = attr_line("Teaching@Sydney, University of Sydney")
        card_attr.next_to(card_rect, DOWN, buff=0.18)

        card = VGroup(card_rect, card_hdr, role_txt)

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(FadeIn(card), FadeIn(card_attr), run_time=0.7); e += 0.7

        # Student message in left zone — right edge at x=-3.4, clear of card (x≥0)
        msg_rect = RoundedRectangle(
            corner_radius=0.1, width=2.2, height=0.8,
            fill_color="#E8E4DC", fill_opacity=1.0,
            stroke_color=SOFT, stroke_width=1.5,
        ).move_to([-4.5, 0.5, 0])
        msg_txt = Text("here is my\nintervention plan",
                       font=SERIF, font_size=18, color=SOFT, line_spacing=1.15)
        msg_txt.move_to(msg_rect)
        msg = VGroup(msg_rect, msg_txt)

        e = reach(self, e, 0.36 * dur)
        self.play(FadeIn(msg, shift=RIGHT * 1.5), run_time=0.8); e += 0.8

        # Arrow spans the 3.4-unit gap: card.left(0.0) → msg.right(-3.4)
        pb_arr = Arrow(
            card_rect.get_left() + LEFT * 0.1,
            msg_rect.get_right() + RIGHT * 0.1,
            color=SPARK, stroke_width=3.0, buff=0,
            max_tip_length_to_length_ratio=0.20,
        )
        # pb_txt above arrow midpoint, clear of both filled rects
        pb_txt = Text("challenge · push back", font=SERIF, font_size=22,
                      color=SPARK, weight=BOLD)
        pb_txt.move_to([pb_arr.get_center()[0], 0.92, 0])

        e = reach(self, e, 0.58 * dur)
        self.play(GrowArrow(pb_arr), run_time=0.5); e += 0.5
        self.play(FadeIn(pb_txt), run_time=0.4); e += 0.4

        # Scope stamp inside safe area (±3.4 y)
        e = reach(self, e, 0.82 * dur)
        stamp = Text("ONE COURSE · ONE INSTRUCTOR · HAND-WRITTEN",
                     font=SERIF, font_size=22, color=GHOST)
        stamp.move_to([0, -3.1, 0])
        self.play(FadeIn(stamp), run_time=0.5); e += 0.5

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B12 — PARALLEL LAYER  (18.67 s)
# Vendor's operator slot is hollow; a home-built stack beside it is full.
# The arrow travels AROUND the empty vendor slot.
# ─────────────────────────────────────────────────────────────────────────────

class B12_ParallelLayer(Scene):
    def construct(self):
        dur = 18.67

        # Shared stack dimensions
        SW = 4.0; SH_BAND = 0.9; SGAP = 0.18
        x_left  = -3.8
        x_right = +3.4

        # --- LEFT: vendor stack (the operator band is EMPTY / hollow outline)
        def vendor_band(label, col, y, hollow=False):
            fill_op = 0.0 if hollow else 0.12
            r = Rectangle(
                width=SW, height=SH_BAND,
                fill_color=col, fill_opacity=fill_op,
                stroke_color=col, stroke_width=2.5,
            ).move_to([x_left, y, 0])
            lbl = Text(label, font=SERIF, font_size=22, color=col, weight=BOLD)
            lbl.move_to(r)
            return VGroup(r, lbl)

        y_v_top = SH_BAND + SGAP
        y_v_mid = 0.0
        y_v_bot = -(SH_BAND + SGAP)

        v_top = vendor_band("PLATFORM", INK,   y_v_top)
        v_mid = vendor_band("OPERATOR", SPARK, y_v_mid, hollow=True)   # ← HOLLOW
        v_bot = vendor_band("USER",     INK,   y_v_bot)

        vendor_lbl = Text("Vendor stack", font=SERIF, font_size=22, color=GHOST)
        vendor_lbl.next_to(v_top, UP, buff=0.28)

        # --- RIGHT: home-built stack (fully populated)
        def home_band(label, y):
            r = Rectangle(
                width=SW, height=SH_BAND,
                fill_color=INK, fill_opacity=0.12,
                stroke_color=INK, stroke_width=2.0,
            ).move_to([x_right, y, 0])
            lbl = Text(label, font=SERIF, font_size=18, color=INK)
            lbl.move_to(r)
            return VGroup(r, lbl)

        h_top = home_band("university platform",      y_v_top)
        h_mid = home_band("instructor-written prompt", y_v_mid)
        h_bot = home_band("course sources",            y_v_bot)

        home_lbl = Text("Home-built", font=SERIF, font_size=22, color=GHOST)
        home_lbl.next_to(h_top, UP, buff=0.28)

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(
            FadeIn(VGroup(v_top, v_mid, v_bot, vendor_lbl)),
            run_time=0.7,
        ); e += 0.7

        e = reach(self, e, 0.34 * dur)
        self.play(
            LaggedStart(
                FadeIn(home_lbl),
                FadeIn(h_top), FadeIn(h_mid), FadeIn(h_bot),
                lag_ratio=0.25,
            ),
            run_time=0.9,
        ); e += 0.9

        # Curved arrow from empty vendor operator band, routing AROUND to the right stack
        e = reach(self, e, 0.62 * dur)

        # Arc path: start at the right edge of the OPERATOR band,
        # curve DOWN and AROUND to the left edge of the home stack centre.
        start = v_mid.get_right()
        end   = h_mid.get_left()
        arc_pt = np.array([0.0, y_v_bot - 1.2, 0])  # goes around the bottom

        arc = CurvedArrow(
            start, end,
            color=SPARK, stroke_width=2.5,
            angle=-TAU / 5,
        )
        arc_lbl = Text("built around it", font=SERIF, font_size=22, color=SPARK)
        arc_lbl.move_to(arc_pt)

        self.play(Create(arc), run_time=0.9); e += 0.9
        self.play(FadeIn(arc_lbl), run_time=0.4); e += 0.4

        # Caption
        e = reach(self, e, 0.84 * dur)
        cap = cap_line("They did not decline the layer. They never saw it.", SOFT, 24)
        cap.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cap), run_time=0.5); e += 0.5

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B13 — ADVERSARIAL  (19.78 s)
# Two attacks arrive and are deflected. The only one testing its own configuration.
# ─────────────────────────────────────────────────────────────────────────────

class B13_Adversarial(Scene):
    def construct(self):
        dur = 19.78

        # Central configured tutor block
        block = RoundedRectangle(
            corner_radius=0.14, width=5.5, height=1.5,
            fill_color=PAGE, fill_opacity=1.0,
            stroke_color=INK, stroke_width=2.5,
        ).move_to([0.0, 0.3, 0])
        block_lbl = Text("CONFIGURED SOCRATIC TUTOR",
                         font=SERIF, font_size=28, color=INK, weight=BOLD)
        block_lbl.move_to(block)

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(FadeIn(VGroup(block, block_lbl)), run_time=0.6); e += 0.6

        # Attack helper
        def attack(label, y_offset, elapsed):
            atk_txt = Text(label, font=SERIF, font_size=23, color=SOFT)
            atk_txt.move_to([-5.5, 0.3 + y_offset, 0])
            atk_arr = Arrow(
                atk_txt.get_right() + RIGHT * 0.1,
                block.get_left() + LEFT * 0.05,
                color=SOFT, stroke_width=2.0, buff=0.05,
                max_tip_length_to_length_ratio=0.15,
            )
            tick = Text("✓", font_size=34, color=INK)
            tick.next_to(block, RIGHT, buff=0.55).shift(UP * y_offset)

            self.play(FadeIn(atk_txt), GrowArrow(atk_arr), run_time=0.6)
            elapsed += 0.6
            self.play(FadeIn(tick), run_time=0.4)
            elapsed += 0.4
            return elapsed

        e = reach(self, e, 0.30 * dur)
        e = attack("student begs for the answer", +0.4, e)

        e = reach(self, e, 0.55 * dur)
        e = attack("student introduces a fake term", -0.4, e)

        # Terracotta caption
        e = reach(self, e, 0.78 * dur)
        cap = Text("The only one testing its own configuration.",
                   font=SERIF, font_size=26, color=SPARK, weight=BOLD)
        cap.move_to([0.0, -1.8, 0])
        attr = attr_line("WashU public guidance")
        attr.next_to(cap, DOWN, buff=0.18)
        self.play(FadeIn(cap), FadeIn(attr), run_time=0.6); e += 0.6

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B14 — BYPASSES  (18.79 s)
# Four controls, four different bypass failures. All ring SPARK at the end.
# ─────────────────────────────────────────────────────────────────────────────

class B14_Bypasses(Scene):
    def construct(self):
        dur = 18.79

        BW = 3.8; BH = 0.7
        x_block = -1.8
        y_positions = [2.35, 0.9, -0.55, -2.0]
        labels = [
            "SCOPE RESTRICTION",
            "DISCLOSURE NOTE",
            "ASSIGNMENT GATING",
            "STUDY-MODE TOGGLE",
        ]

        # Draw all four control blocks upfront (they look solid before they fail)
        blocks = []
        for i, (y, label) in enumerate(zip(y_positions, labels)):
            r = Rectangle(
                width=BW, height=BH,
                fill_color=PAGE, fill_opacity=1.0,
                stroke_color=INK, stroke_width=2.2,
            ).move_to([x_block, y, 0])
            lbl = Text(label, font=SERIF, font_size=20, color=INK, weight=BOLD)
            lbl.move_to(r)
            blocks.append(VGroup(r, lbl))

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(
            LaggedStart(*[FadeIn(b) for b in blocks], lag_ratio=0.2),
            run_time=0.9,
        ); e += 0.9

        bypass_marks = []

        # 1) Scope restriction — arrow routes AROUND to a second unrestricted tool
        e = reach(self, e, 0.30 * dur)
        second_tool = Rectangle(
            width=2.0, height=0.6,
            fill_color=PAGE, fill_opacity=1.0,
            stroke_color=SOFT, stroke_width=1.5,
        ).move_to([4.2, y_positions[0], 0])
        second_lbl = Text("another,\nunrestricted tool",
                          font=SERIF, font_size=16, color=SOFT, line_spacing=1.1)
        second_lbl.move_to(second_tool)
        bypass_arr_0 = CurvedArrow(
            blocks[0].get_right(),
            second_tool.get_left(),
            color=SOFT, stroke_width=2.0, angle=-PI / 3,
        )
        self.play(
            FadeIn(second_tool), FadeIn(second_lbl),
            Create(bypass_arr_0),
            run_time=0.7,
        ); e += 0.7
        bypass_marks.append(VGroup(second_tool, second_lbl, bypass_arr_0))

        # 2) Disclosure — note appended then struck and removed
        e = reach(self, e, 0.50 * dur)
        note_txt = Text("[AI disclosure note]", font=SERIF, font_size=18, color=SOFT)
        note_txt.next_to(blocks[1], RIGHT, buff=0.4)
        strikethrough = Line(
            note_txt.get_left() + LEFT * 0.05,
            note_txt.get_right() + RIGHT * 0.05,
            color=SPARK, stroke_width=3.0,
        ).set_y(note_txt.get_center()[1])
        self.play(FadeIn(note_txt), run_time=0.4); e += 0.4
        self.play(Create(strikethrough), run_time=0.3); e += 0.3
        self.play(
            note_txt.animate.set_opacity(0.15),
            strikethrough.animate.set_opacity(0.15),
            run_time=0.3,
        ); e += 0.3
        bypass_marks.append(VGroup(note_txt, strikethrough))

        # 3) Assignment gating — connector to LMS draws as dashed, never completes
        e = reach(self, e, 0.68 * dur)
        lms_box = Rectangle(
            width=1.6, height=0.6,
            fill_color=PAGE, fill_opacity=1.0,
            stroke_color=SOFT, stroke_width=1.5, stroke_opacity=0.5,
        ).move_to([4.2, y_positions[2], 0])
        lms_lbl = Text("LMS", font=SERIF, font_size=18, color=SOFT)
        lms_lbl.move_to(lms_box)
        dashed_conn = DashedLine(
            blocks[2].get_right(),
            [3.2, y_positions[2], 0],   # intentionally stops short
            color=SOFT, dash_length=0.18,
            stroke_width=1.8, stroke_opacity=0.55,
        )
        self.play(
            FadeIn(lms_box), FadeIn(lms_lbl),
            Create(dashed_conn),
            run_time=0.6,
        ); e += 0.6
        bypass_marks.append(VGroup(lms_box, lms_lbl, dashed_conn))

        # 4) Study-mode toggle flips off
        e = reach(self, e, 0.86 * dur)
        toggle_on  = Text("ON",  font=SERIF, font_size=20, color=INK,  weight=BOLD)
        toggle_off = Text("OFF", font=SERIF, font_size=20, color=GHOST)
        toggle_on.next_to(blocks[3], RIGHT, buff=0.6)
        toggle_off.next_to(blocks[3], RIGHT, buff=0.6)
        self.play(FadeIn(toggle_on), run_time=0.3); e += 0.3
        self.play(
            toggle_on.animate.set_opacity(0.0),
            FadeIn(toggle_off),
            run_time=0.4,
        ); e += 0.4
        bypass_marks.append(VGroup(toggle_on, toggle_off))

        # All four blocks ring terracotta simultaneously
        rings = VGroup(*[
            SurroundingRectangle(b, color=SPARK, stroke_width=2.5, buff=0.08)
            for b in blocks
        ])
        self.play(Create(rings), run_time=0.6); e += 0.6

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B15 — REFRAME  (19.24 s)
# One question transforms into a better one; three A-over-B pairs follow.
# ─────────────────────────────────────────────────────────────────────────────

class B15_Reframe(Scene):
    def construct(self):
        dur = 19.24

        # q1 starts centre; q2 target is above (different y — avoids TEXT-ON-TEXT)
        q1 = Text(
            "How do we enforce restraint?",
            font=SERIF, font_size=40, color=INK,
        ).move_to([0, 0.4, 0])

        q2 = Text(
            "What is the smallest lever that\nchanges behaviour without\nassuming enforcement?",
            font=SERIF, font_size=26, color=INK, line_spacing=1.2,
        )
        if q2.width > 11.5:
            q2.scale_to_fit_width(11.5)
        q2.move_to([0, 2.5, 0])

        e = 0.0
        e = reach(self, e, 0.08 * dur)
        self.play(FadeIn(q1), run_time=0.5); e += 0.5

        e = reach(self, e, 0.36 * dur)
        # Transform: question retreats upward and narrows to the honest version
        self.play(Transform(q1, q2), run_time=1.0); e += 1.0

        # Three A-over-B rows
        rows_data = [
            ("SCOPE",            "over  MANNER"),
            ("DISCLOSURE",       "over  RESTRICTION"),
            ("VISIBLE CHOICE",   "over  SILENT DEFAULT"),
        ]
        row_group = VGroup()
        for a, b in rows_data:
            a_txt = Text(a, font=SERIF, font_size=26, color=SPARK, weight=BOLD)
            b_txt = Text(b, font=SERIF, font_size=26, color=INK)
            row = VGroup(a_txt, b_txt).arrange(RIGHT, buff=0.25)
            row_group.add(row)
        row_group.arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        row_group.move_to([0, -1.5, 0])

        e = reach(self, e, 0.64 * dur)
        self.play(
            LaggedStart(*[FadeIn(r) for r in row_group], lag_ratio=0.3),
            run_time=1.0,
        ); e += 1.0

        # Underlines beneath the A-terms (terracotta)
        e = reach(self, e, 0.88 * dur)
        underlines = VGroup()
        for row in row_group:
            a_part = row[0]
            ul = Line(
                a_part.get_left() + DOWN * 0.12,
                a_part.get_right() + DOWN * 0.12,
                color=SPARK, stroke_width=2.5,
            )
            underlines.add(ul)
        self.play(
            LaggedStart(*[Create(u) for u in underlines], lag_ratio=0.2),
            run_time=0.6,
        ); e += 0.6

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B16 — CATEGORY ERROR  (21.95 s)
# Two surfaces; managed-settings.json belongs to the RIGHT only; crossing is blocked.
# ─────────────────────────────────────────────────────────────────────────────

class B16_CategoryError(Scene):
    def construct(self):
        dur = 21.95

        SW = 5.0; SH = 4.5
        x_left  = -3.6
        x_right = +3.6

        # Left surface: CHAT
        left_surf = Rectangle(
            width=SW, height=SH,
            fill_color="#F5F3EE", fill_opacity=1.0,
            stroke_color=INK, stroke_width=2.0,
        ).move_to([x_left, 0, 0])
        left_hdr = Text("CHAT", font=SERIF, font_size=30, color=INK, weight=BOLD)
        left_hdr.move_to(left_surf).shift(UP * 1.7)
        left_sub = Text("the student's Claude", font=SERIF, font_size=22, color=SOFT)
        left_sub.next_to(left_hdr, DOWN, buff=0.2)

        # Right surface: CLAUDE CODE
        right_surf = Rectangle(
            width=SW, height=SH,
            fill_color="#F5F3EE", fill_opacity=1.0,
            stroke_color=INK, stroke_width=2.0,
        ).move_to([x_right, 0, 0])
        right_hdr = Text("CLAUDE CODE", font=SERIF, font_size=30, color=INK, weight=BOLD)
        right_hdr.move_to(right_surf).shift(UP * 1.7)
        right_sub = Text("a developer's machine, MDM-deployed",
                         font=SERIF, font_size=18, color=SOFT)
        right_sub.next_to(right_hdr, DOWN, buff=0.2)

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(
            FadeIn(left_surf), FadeIn(left_hdr), FadeIn(left_sub),
            FadeIn(right_surf), FadeIn(right_hdr), FadeIn(right_sub),
            run_time=0.7,
        ); e += 0.7

        # managed-settings.json file chip on the RIGHT surface only
        e = reach(self, e, 0.32 * dur)
        file_chip_txt = Text("/Library/Application Support/ClaudeCode/",
                             font=SERIF, font_size=17, color=INK)
        file_chip_txt.move_to([x_right, 0.7, 0])
        file_name = Text("managed-settings.json",
                         font=SERIF, font_size=22, color=INK, weight=BOLD)
        file_name.next_to(file_chip_txt, UP, buff=0.18)
        self.play(FadeIn(file_name), FadeIn(file_chip_txt), run_time=0.5); e += 0.5

        # Contents list — claudeMd row in SPARK
        e = reach(self, e, 0.56 * dur)
        contents = [
            ("permission rules",           INK),
            ("tool allow / deny",          INK),
            ("MCP allowlists",             INK),
            ("claudeMd — org-managed memory", SPARK),
        ]
        rows = VGroup()
        for label, col in contents:
            row = Text(label, font=SERIF, font_size=18, color=col,
                       weight=BOLD if col == SPARK else NORMAL)
            rows.add(row)
        rows.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        rows.move_to([x_right, -0.85, 0])
        self.play(
            LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.2),
            run_time=0.8,
        ); e += 0.8

        # Arrow attempts to cross from right to left; blocked by a drawn barrier
        e = reach(self, e, 0.80 * dur)

        # Barrier line between surfaces (centred)
        barrier = Line([0.0, -2.2, 0], [0.0, +2.2, 0],
                       color=INK, stroke_width=3.5)
        barrier_x = Text("✕", font_size=32, color=INK)
        barrier_x.move_to([0.0, 0.0, 0])

        arr_blocked = Arrow(
            [x_right - SW / 2 - 0.05, 0, 0],
            [0.15, 0, 0],
            color=SOFT, stroke_width=2.0, buff=0,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(GrowArrow(arr_blocked), run_time=0.4); e += 0.4
        self.play(Create(barrier), run_time=0.3); e += 0.3
        self.play(FadeIn(barrier_x), run_time=0.3); e += 0.3

        cap = cap_line(
            "A different surface — not a smaller version of the same one.",
            SOFT, 22,
        )
        cap.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cap), run_time=0.4); e += 0.4

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B17 — NARROWING CLAIM  (21.42 s)
# The strong claim visibly shrinks and re-letters into the defensible one.
# The unsearchable region sits OUTSIDE the searched set.
# ─────────────────────────────────────────────────────────────────────────────

class B17_NarrowingClaim(Scene):
    def construct(self):
        dur = 21.42

        # Large initial claim — centred, below mid-frame
        claim_big = Text(
            "NO UNIVERSITY HAS CONFIGURED\nA CAMPUS-WIDE INSTRUCTION",
            font=SERIF, font_size=38, color=INK, weight=BOLD, line_spacing=1.15,
        ).move_to([0, 1.2, 0])

        # The smaller, honest claim — moved UP so GATE W sees no overlap with claim_big
        claim_small = Text(
            "NO PUBLIC EVIDENCE\nOF ONE EXISTS",
            font=SERIF, font_size=30, color=INK, weight=BOLD, line_spacing=1.15,
        ).move_to([-2.2, 2.8, 0])

        # Rectangle frame around the initial claim — non-text shape for GATE A
        claim_frame = Rectangle(
            width=8.0, height=1.85,
            fill_opacity=0,
            stroke_color=INK, stroke_width=2.2,
        ).move_to(claim_big.get_center())

        # Target frame (smaller, left-shifted, matching claim_small)
        claim_frame_small = Rectangle(
            width=6.0, height=1.55,
            fill_opacity=0,
            stroke_color=INK, stroke_width=2.2,
        ).move_to(claim_small.get_center())

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(FadeIn(claim_big), Create(claim_frame), run_time=0.6); e += 0.6

        # The card physically shrinks and re-letters (the retreat is watched)
        e = reach(self, e, 0.32 * dur)
        self.play(
            Transform(claim_big, claim_small),
            Transform(claim_frame, claim_frame_small),
            run_time=1.1,
        ); e += 1.1

        # Searched sources list (what WAS searchable)
        e = reach(self, e, 0.58 * dur)
        searched = [
            "IT policy pages",
            "AI task force reports",
            "faculty governance minutes",
            "vendor announcements",
        ]
        src_hdr = Text("Searched:", font=SERIF, font_size=22, color=SOFT, weight=BOLD)
        src_hdr.move_to([-2.6, 0.2, 0])
        src_rows = VGroup(*[
            Text("· " + s, font=SERIF, font_size=20, color=SOFT)
            for s in searched
        ]).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        src_rows.next_to(src_hdr, DOWN, buff=0.22).align_to(src_hdr, LEFT)

        self.play(FadeIn(src_hdr), run_time=0.3); e += 0.3
        self.play(
            LaggedStart(*[FadeIn(r) for r in src_rows], lag_ratio=0.2),
            run_time=0.8,
        ); e += 0.8

        # Hatched TERRACOTTA region to the RIGHT, labelled — OUTSIDE the searched set
        e = reach(self, e, 0.80 * dur)
        hatch_rect = Rectangle(
            width=3.6, height=2.8,
            fill_color=SPARK, fill_opacity=0.10,
            stroke_color=SPARK, stroke_width=2.5,
        ).move_to([3.8, 0.0, 0])

        # Hatching inside the region
        hatch_lines = VGroup()
        for i in range(9):
            y_start = -1.4 + i * 0.35
            hl = Line(
                [2.0, y_start, 0], [5.6, y_start + 0.6, 0],
                color=SPARK, stroke_width=1.0, stroke_opacity=0.35,
            )
            hatch_lines.add(hl)

        hatch_lbl1 = Text("admin consoles", font=SERIF, font_size=21,
                          color=SPARK, weight=BOLD)
        hatch_lbl1.move_to(hatch_rect).shift(UP * 0.3)
        hatch_lbl2 = Text("not public,\nnever will be",
                          font=SERIF, font_size=18, color=SPARK, line_spacing=1.2)
        hatch_lbl2.move_to(hatch_rect).shift(DOWN * 0.4)

        self.play(
            Create(hatch_rect),
            FadeIn(hatch_lines),
            run_time=0.5,
        ); e += 0.5
        self.play(FadeIn(hatch_lbl1), FadeIn(hatch_lbl2), run_time=0.5); e += 0.5

        # Final caption
        cap = cap_line("The blind spot is the size of the claim.", SOFT, 24)
        cap.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cap), run_time=0.4); e += 0.4

        self.wait(max(0, dur - e))


# ─────────────────────────────────────────────────────────────────────────────
# B18 — THE WIRE  (18.37 s)
# B07's void is redrawn exactly; then the ONE connector finally crosses it.
# ─────────────────────────────────────────────────────────────────────────────

class B18_TheWire(Scene):
    def construct(self):
        dur = 18.37

        # Redraw B07 exactly — so the callback is unmistakable
        x_left  = -3.8
        x_right = +3.8
        void_label_x = 0.0

        left_hdr = Text("THE COMMITTEE", font=SERIF, font_size=32, color=INK, weight=BOLD)
        left_hdr.move_to([x_left, 2.6, 0])
        left_rows = VGroup(*[
            Text(s, font=SERIF, font_size=24, color=SOFT)
            for s in ["syllabus language",
                      "academic integrity policy",
                      "assignment guidance"]
        ]).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        left_rows.next_to(left_hdr, DOWN, buff=0.42).align_to(left_hdr, LEFT)

        right_hdr = Text("THE CONSOLE", font=SERIF, font_size=32, color=INK, weight=BOLD)
        right_hdr.move_to([x_right, 2.6, 0])
        console_item = Text(
            "organisation instructions\n3,000 characters",
            font=SERIF, font_size=24, color=SPARK, line_spacing=1.2,
        )
        console_item.next_to(right_hdr, DOWN, buff=0.42)

        void_line = DashedLine(
            [void_label_x, +3.0, 0], [void_label_x, -2.8, 0],
            color=GHOST, dash_length=0.2,
            stroke_width=1.8, stroke_opacity=0.7,
        )
        void_lbl = Text("no channel", font=SERIF, font_size=22, color=GHOST)
        void_lbl.move_to([void_label_x, 0.0, 0]).shift(RIGHT * 0.2)

        e = 0.0
        e = reach(self, e, 0.05 * dur)
        self.play(
            FadeIn(left_hdr), FadeIn(right_hdr),
            run_time=0.5,
        ); e += 0.5
        self.play(
            FadeIn(left_rows), FadeIn(console_item),
            run_time=0.5,
        ); e += 0.5
        self.play(Create(void_line), FadeIn(void_lbl), run_time=0.5); e += 0.5

        # THE ONLY CONNECTOR THAT CROSSES — terracotta, first time in the film
        e = reach(self, e, 0.36 * dur)
        wire = Arrow(
            left_hdr.get_right() + RIGHT * 0.1,
            right_hdr.get_left() + LEFT * 0.1,
            color=SPARK, stroke_width=3.5, buff=0.05,
            max_tip_length_to_length_ratio=0.16,
        )
        wire_lbl = Text("the missing conversation", font=SERIF, font_size=24,
                        color=SPARK, weight=BOLD)
        wire_lbl.next_to(wire, UP, buff=0.22)

        self.play(GrowArrow(wire), run_time=0.7); e += 0.7

        # Label — explicitly NOT "the missing feature"
        e = reach(self, e, 0.62 * dur)
        self.play(FadeIn(wire_lbl), run_time=0.5); e += 0.5

        # Caption
        e = reach(self, e, 0.84 * dur)
        cap = cap_line(
            "Fixable. Which is the whole argument for writing it down.",
            SOFT, 24,
        )
        cap.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cap), run_time=0.5); e += 0.5

        self.wait(max(0, dur - e))

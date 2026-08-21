# portrait (9:16) Manim scenes — THE LEVER NOBODY PULLED short
# frame_width=4.5 after portrait sync; safe x=[-1.9,1.9], y=[-3.4,3.4]

from manim import *

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE

# Portrait sync — Manim CE does NOT auto-update frame_width from -r W,H
try:
    _pw = getattr(config, "pixel_width", None)
    _ph = getattr(config, "pixel_height", None)
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

# GATE T §8.4 font lock
_OrigText = Text
Text = lambda text, *args, font="EB Garamond", **kwargs: _OrigText(text, *args, font=font, **kwargs)


class B01_ThreeBosses(Scene):
    """Three stacked bands: COMMITTEE / OPERATOR / CONSOLE.
    band_w=3.8, band_h=1.5; ys=[2.35, 0.55, -1.25]; caption y=-3.0.
    OPERATOR band gets SPARK stroke (one accent rule).
    Content spans from y≈3.1 (top of COMMITTEE) to y=-3.0 (caption) → full safe fill."""

    def construct(self):
        BAND_W = 3.8
        BAND_H = 1.5
        YS = [2.35, 0.55, -1.25]
        LABELS = ["COMMITTEE", "OPERATOR", "CONSOLE"]
        SUBS = [
            "Defines objectives\nand constraints",
            "Schedules, routes\nand coordinates",
            "Executes tasks\nin the environment",
        ]

        bands = VGroup()
        for i, (y, label, sub) in enumerate(zip(YS, LABELS, SUBS)):
            rect = Rectangle(
                width=BAND_W, height=BAND_H,
                fill_color=PAGE, fill_opacity=1,
                stroke_color=SPARK if i == 1 else BORDER,
                stroke_width=5 if i == 1 else 2,
            ).move_to([0, y, 0])

            lbl = Text(label, font_size=22, color=INK).move_to([0, y + 0.28, 0])
            sub_t = Text(sub, font_size=14, color=SOFT, line_spacing=1.3).move_to([0, y - 0.22, 0])

            bands.add(rect, lbl, sub_t)

        # arrows between bands
        arr1 = Arrow(
            start=[0, YS[0] - BAND_H / 2 - 0.02, 0],
            end=[0, YS[1] + BAND_H / 2 + 0.02, 0],
            color=GHOST, buff=0, stroke_width=2,
            max_tip_length_to_length_ratio=0.25,
        )
        arr2 = Arrow(
            start=[0, YS[1] - BAND_H / 2 - 0.02, 0],
            end=[0, YS[2] + BAND_H / 2 + 0.02, 0],
            color=GHOST, buff=0, stroke_width=2,
            max_tip_length_to_length_ratio=0.25,
        )

        caption = Text(
            "Three tiers — one pipeline.",
            font_size=15, color=SOFT,
        ).move_to([0, -3.0, 0])

        scene_hdr = Text("THE THREE BOSSES", font_size=14, color=GHOST).move_to([0, 3.25, 0])

        self.play(FadeIn(scene_hdr), run_time=0.4)
        for mob in [bands[0], bands[1], bands[2]]:
            self.play(FadeIn(mob), run_time=0.5)
        for mob in [bands[3], bands[4], bands[5]]:
            self.play(FadeIn(mob), run_time=0.4)
        for mob in [bands[6], bands[7], bands[8]]:
            self.play(FadeIn(mob), run_time=0.4)
        self.play(GrowArrow(arr1), GrowArrow(arr2), run_time=0.6)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(10)


class B03_Precedence(Scene):
    """ORG card top, USR card bottom — operator beats user.
    card_w=3.4, card_h=2.0; ORG y=0.8, USR y=-1.4; quote y=-2.7.
    All elements at final positions from start (GATE A safe)."""

    def construct(self):
        CARD_W = 3.4

        scene_hdr = Text("PRECEDENCE", font_size=14, color=GHOST).move_to([0, 3.25, 0])

        # ORG card — at final position
        org_rect = Rectangle(
            width=CARD_W, height=2.0,
            fill_color=PAGE, fill_opacity=1,
            stroke_color=SOFT, stroke_width=1.5,
        ).move_to([0, 0.8, 0])
        org_tag = Text("SYSTEM PROMPT", font_size=14, color=GHOST).move_to([0, 1.73, 0])
        org_title = Text("Operator\nInstructions", font_size=24, color=INK, line_spacing=1.2).move_to([0, 0.95, 0])
        org_sub = Text("Set at deployment\nNot visible to users", font_size=13, color=SOFT, line_spacing=1.3).move_to([0, 0.32, 0])

        # label between cards
        arrow_lbl = Text("higher precedence  ↑", font_size=13, color=GHOST).move_to([0, -0.27, 0])

        # USR card — at final position
        usr_rect = Rectangle(
            width=CARD_W, height=2.0,
            fill_color=PAGE, fill_opacity=1,
            stroke_color=SPARK, stroke_width=3,
        ).move_to([0, -1.4, 0])
        usr_tag = Text("USER MESSAGE", font_size=14, color=GHOST).move_to([0, -0.47, 0])
        usr_title = Text("User\nRequest", font_size=24, color=INK, line_spacing=1.2).move_to([0, -1.25, 0])
        usr_sub = Text("Sent at runtime\nLower precedence", font_size=13, color=SOFT, line_spacing=1.3).move_to([0, -1.88, 0])

        quote = Text(
            '"Operator beats user\nwhen goals conflict."',
            font_size=16, color=INK, line_spacing=1.4,
        ).move_to([0, -2.4, 0])

        self.play(FadeIn(scene_hdr), run_time=0.4)
        self.play(FadeIn(org_rect), FadeIn(org_tag), run_time=0.5)
        self.play(FadeIn(org_title), FadeIn(org_sub), run_time=0.5)
        self.play(FadeIn(arrow_lbl), run_time=0.4)
        self.play(FadeIn(usr_rect), FadeIn(usr_tag), run_time=0.5)
        self.play(FadeIn(usr_title), FadeIn(usr_sub), run_time=0.5)
        self.play(org_rect.animate.set_stroke(color=INK, width=2.5), run_time=0.4)
        self.play(FadeIn(quote), run_time=0.6)
        self.wait(10)


class B09_NoWire(Scene):
    """COMMITTEE panel top, dashed void separator, CONSOLE panel bottom.
    top panel 3.8×2.6 at y=1.8; void at y=0; bottom panel 3.8×2.0 at y=-1.6; caption y=-3.2."""

    def construct(self):
        PANEL_W = 3.8

        scene_hdr = Text("NO WIRE", font_size=14, color=GHOST).move_to([0, 3.25, 0])

        # top panel — COMMITTEE
        top_rect = Rectangle(
            width=PANEL_W, height=2.6,
            fill_color=PAGE, fill_opacity=1,
            stroke_color=BORDER, stroke_width=2,
        ).move_to([0, 1.8, 0])
        top_tag = Text("COMMITTEE", font_size=14, color=GHOST).move_to([0, 2.95, 0])
        top_title = Text("Defines the Goal", font_size=22, color=INK).move_to([0, 2.35, 0])
        top_body = Text(
            "Sets objectives and constraints\nbefore any session begins.",
            font_size=15, color=SOFT, line_spacing=1.4,
        ).move_to([0, 1.75, 0])
        top_note = Text("No live channel to the model.", font_size=13, color=GHOST).move_to([0, 1.1, 0])

        # void line (dashed)
        void_line = DashedLine(
            start=[-1.9, 0, 0], end=[1.9, 0, 0],
            color=SPARK, dash_length=0.15, dashed_ratio=0.5, stroke_width=2,
        )
        no_ch = Text("↑  no channel  ↓", font_size=13, color=SPARK).move_to([0, 0.25, 0])

        # bottom panel — CONSOLE
        bot_rect = Rectangle(
            width=PANEL_W, height=2.0,
            fill_color=PAGE, fill_opacity=1,
            stroke_color=BORDER, stroke_width=2,
        ).move_to([0, -1.6, 0])
        bot_tag = Text("CONSOLE", font_size=14, color=GHOST).move_to([0, -0.65, 0])
        bot_title = Text("Executes the Work", font_size=22, color=INK).move_to([0, -1.2, 0])
        bot_body = Text(
            "Runs tasks in the environment.\nCommittee goals baked into prompt.",
            font_size=15, color=SOFT, line_spacing=1.4,
        ).move_to([0, -1.8, 0])

        caption = Text(
            "Intent travels through the prompt,\nnot a live wire.",
            font_size=15, color=INK, line_spacing=1.4,
        ).move_to([0, -2.4, 0])

        self.play(FadeIn(scene_hdr), run_time=0.4)
        self.play(FadeIn(top_rect), FadeIn(top_tag), run_time=0.5)
        self.play(FadeIn(top_title), FadeIn(top_body), FadeIn(top_note), run_time=0.6)
        self.play(Create(void_line), FadeIn(no_ch), run_time=0.7)
        self.play(FadeIn(bot_rect), FadeIn(bot_tag), run_time=0.5)
        self.play(FadeIn(bot_title), FadeIn(bot_body), run_time=0.6)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(10)


class B11_CognitiRecreation(Scene):
    """sys_prompt box 3.6×2.8 at y=1.6; arrow down; SPARK ring box 3.4×1.8 at y=-1.6; attr at y=-2.8."""

    def construct(self):
        scene_hdr = Text("COGNITIVE RECREATION", font_size=13, color=GHOST).move_to([0, 3.25, 0])

        # top box — sys_prompt
        sys_rect = Rectangle(
            width=3.6, height=2.8,
            fill_color=PAGE, fill_opacity=1,
            stroke_color=INK, stroke_width=2,
        ).move_to([0, 1.6, 0])
        sys_tag = Text("SYSTEM PROMPT", font_size=13, color=GHOST).move_to([0, 2.9, 0])
        sys_title = Text("Character\nblueprint", font_size=22, color=INK, line_spacing=1.2).move_to([0, 1.85, 0])
        sys_body = Text(
            "Values · Goals · Constraints\nPersonality · Voice",
            font_size=15, color=SOFT, line_spacing=1.4,
        ).move_to([0, 1.15, 0])

        # arrow
        arrow = Arrow(
            start=[0, 0.17, 0], end=[0, -0.55, 0],
            color=INK, buff=0, stroke_width=3,
            max_tip_length_to_length_ratio=0.35,
        )
        arrow_lbl = Text("recreated\nevery session", font_size=12, color=GHOST, line_spacing=1.3).move_to([0, -0.05, 0])

        # bottom box — SPARK ring (highlight); tag inside rect to avoid arrow proximity
        bot_rect = Rectangle(
            width=3.4, height=1.8,
            fill_color=PAGE, fill_opacity=1,
            stroke_color=SPARK, stroke_width=4,
        ).move_to([0, -1.6, 0])
        # tag sits well inside the rect (top = -0.7), clear of arrow end at -0.55
        bot_tag = Text("RESULT", font_size=13, color=INK).move_to([0, -0.95, 0])
        key_quote = Text(
            '"Consistent identity\nacross every conversation."',
            font_size=16, color=INK, line_spacing=1.4,
        ).move_to([0, -1.7, 0])

        attr = Text(
            "Not memory — architecture.",
            font_size=14, color=SOFT,
        ).move_to([0, -2.8, 0])

        self.play(FadeIn(scene_hdr), run_time=0.4)
        self.play(FadeIn(sys_rect), FadeIn(sys_tag), run_time=0.5)
        self.play(FadeIn(sys_title), FadeIn(sys_body), run_time=0.6)
        self.play(GrowArrow(arrow), FadeIn(arrow_lbl), run_time=0.6)
        self.play(FadeIn(bot_rect), run_time=0.4)
        self.play(FadeIn(bot_tag), FadeIn(key_quote), run_time=0.5)
        self.play(FadeIn(attr), run_time=0.5)
        self.wait(10)


class B14_Scaffold(Scene):
    """enclosure 3.6×3.0 at y=1.5; card 3.1×2.5 inside; duplicate slides to y=-1.5;
    FENCE→SCAFFOLD label at y=-0.2; inst_line at y=-3.05."""

    def construct(self):
        scene_hdr = Text("THE SCAFFOLD", font_size=14, color=GHOST).move_to([0, 3.25, 0])

        # original card (top half)
        enc = Rectangle(
            width=3.6, height=3.0,
            fill_color=PAGE, fill_opacity=1,
            stroke_color=BORDER, stroke_width=2,
        ).move_to([0, 1.5, 0])
        enc_tag = Text("OPERATOR LAYER", font_size=13, color=GHOST).move_to([0, 2.93, 0])
        card = Rectangle(
            width=3.1, height=2.3,
            fill_color=PAGE, fill_opacity=1,
            stroke_color=INK, stroke_width=2,
        ).move_to([0, 1.5, 0])
        # card_title raised, card_lines lowered to ensure no text-on-text overlap
        card_title = Text("System Prompt", font_size=20, color=INK).move_to([0, 2.1, 0])
        card_lines = VGroup(
            Text("• Values and goals", font_size=14, color=SOFT),
            Text("• Persona and voice", font_size=14, color=SOFT),
            Text("• Hard constraints", font_size=14, color=SOFT),
            Text("• Context for this deployment", font_size=14, color=SOFT),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT).move_to([0, 1.05, 0])

        # label between halves
        mid_label = Text("FENCE  →  SCAFFOLD", font_size=16, color=SPARK).move_to([0, -0.2, 0])

        # bottom half — ENABLING STRUCTURE (at final position, GATE A safe)
        enc2 = enc.copy().move_to([0, -1.5, 0])
        enc2.set_stroke(color=SPARK, width=3)
        # enc2_tag inside enc2 (top=0.0), clear of mid_label (y=-0.2)
        enc2_tag = Text("ENABLING STRUCTURE", font_size=13, color=SPARK).move_to([0, -0.5, 0])
        card2 = card.copy().move_to([0, -1.5, 0])
        card2_title = Text("System Prompt", font_size=20, color=INK).move_to([0, -1.15, 0])
        card2_note = Text(
            "Shapes behavior\nwithout caging it.",
            font_size=16, color=SOFT, line_spacing=1.4,
        ).move_to([0, -1.92, 0])

        # inst_line below enc2 bottom (y=-3.0); within safe area (bottom=-3.4)
        inst_line = Text(
            "Instructions that enable, not just restrict.",
            font_size=14, color=INK,
        ).move_to([0, -2.6, 0])

        self.play(FadeIn(scene_hdr), run_time=0.4)
        self.play(FadeIn(enc), FadeIn(enc_tag), run_time=0.5)
        self.play(FadeIn(card), FadeIn(card_title), run_time=0.4)
        self.play(FadeIn(card_lines), run_time=0.6)
        self.play(FadeIn(mid_label), run_time=0.5)
        self.play(FadeIn(enc2), FadeIn(enc2_tag), run_time=0.5)
        self.play(FadeIn(card2), FadeIn(card2_title), FadeIn(card2_note), run_time=0.6)
        self.play(FadeIn(inst_line), run_time=0.5)
        self.wait(10)

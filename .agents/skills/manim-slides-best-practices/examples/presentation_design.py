"""
Presentation Design Patterns for manim-slides

This file demonstrates best practices for slide design: minimal information per slide,
visual hierarchy through font size and weight, progressive reveal for gaze control,
and monochrome design with a single accent color.

Render: manim-slides render presentation_design.py SceneName
Present: manim-slides present SceneName
"""

from manim import *
from manim_slides import Slide

# Design constants: monochrome palette + 1 accent color
ACCENT = "#3B82F6"
TEXT_PRIMARY = WHITE
TEXT_SECONDARY = GREY_B
TEXT_TERTIARY = GREY_C
BG_COLOR = "#111111"


class MinimalInfoSlide(Slide):
    """Demonstrates the principle of minimal information per slide.

    Each slide contains only one idea, making it immediately graspable.
    Complex content is split across multiple slides.
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # Slide 1: One idea, one line
        claim = Text(
            "One idea per slide",
            font_size=56,
            color=TEXT_PRIMARY,
        )
        self.play(FadeIn(claim))

        self.next_slide()

        # Slide 2: Replace with next idea
        self.play(FadeOut(claim))
        why = Text(
            "So the audience never feels lost",
            font_size=48,
            color=TEXT_PRIMARY,
        )
        self.play(FadeIn(why))

        self.next_slide()

        # Slide 3: A diagram, not a wall of text
        self.play(FadeOut(why))
        box1 = RoundedRectangle(
            corner_radius=0.15, width=3, height=1.2,
            color=TEXT_PRIMARY, fill_opacity=0.1,
        )
        label1 = Text("Problem", font_size=28, color=TEXT_PRIMARY).move_to(box1)
        arrow = Arrow(
            box1.get_right(), box1.get_right() + RIGHT * 2,
            color=TEXT_SECONDARY,
        )
        box2 = RoundedRectangle(
            corner_radius=0.15, width=3, height=1.2,
            color=ACCENT, fill_opacity=0.15,
        )
        box2.next_to(arrow, RIGHT, buff=0.3)
        label2 = Text("Solution", font_size=28, color=ACCENT).move_to(box2)

        diagram = VGroup(box1, label1, arrow, box2, label2).move_to(ORIGIN)
        self.play(
            FadeIn(box1), Write(label1),
        )
        self.play(GrowArrow(arrow))
        self.play(
            FadeIn(box2), Write(label2),
        )

        self.next_slide()

        # Slide 4: Conclusion
        self.play(FadeOut(diagram))
        conclusion = Text(
            "If they can't read it instantly, remove it",
            font_size=44,
            color=ACCENT,
        )
        self.play(FadeIn(conclusion))


class VisualHierarchySlide(Slide):
    """Demonstrates information hierarchy using font size and weight.

    Large + bold = most important (eyes land here first).
    Large + thin = important but skippable initially.
    Small = supplementary detail.
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # Build a slide with clear visual hierarchy
        heading = Text(
            "VISUAL HIERARCHY",
            font_size=20,
            color=TEXT_TERTIARY,
            weight=BOLD,
        ).to_edge(UP, buff=0.8)

        main_point = Text(
            "Size and weight guide the eye",
            font_size=52,
            color=TEXT_PRIMARY,
            weight=BOLD,
        )

        supporting = Text(
            "Larger text draws attention first",
            font_size=32,
            color=TEXT_SECONDARY,
        )

        detail = Text(
            "Small text serves as supplementary information",
            font_size=20,
            color=TEXT_TERTIARY,
        )

        content = VGroup(main_point, supporting, detail).arrange(
            DOWN, buff=0.6, aligned_edge=LEFT,
        ).move_to(ORIGIN + DOWN * 0.3)

        # Reveal hierarchy levels one at a time
        self.play(FadeIn(heading))

        self.next_slide()
        self.play(FadeIn(main_point))

        self.next_slide()
        self.play(FadeIn(supporting))

        self.next_slide()
        self.play(FadeIn(detail))

        self.next_slide()

        # Highlight the main point with accent color
        self.play(main_point.animate.set_color(ACCENT))


class ProgressiveRevealSlide(Slide):
    """Demonstrates progressive reveal for gaze control.

    Information appears step by step so the audience processes each point
    before the next one is shown. This prevents the audience from reading
    ahead and losing sync with the speaker.
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text(
            "THREE REASONS",
            font_size=20,
            color=TEXT_TERTIARY,
            weight=BOLD,
        ).to_edge(UP, buff=0.8)
        self.play(FadeIn(title))

        heading = Text(
            "Why progressive reveal works",
            font_size=44,
            color=TEXT_PRIMARY,
            weight=BOLD,
        ).next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(heading))

        self.next_slide()

        # Build bullet points progressively
        bullets_data = [
            ("1.", "Controls where the audience looks", ACCENT),
            ("2.", "Prevents reading ahead", TEXT_PRIMARY),
            ("3.", "Synchronizes audience with speaker", TEXT_PRIMARY),
        ]

        bullets = VGroup()
        for num_str, text_str, color in bullets_data:
            num = Text(num_str, font_size=28, color=ACCENT)
            txt = Text(text_str, font_size=28, color=color)
            line = VGroup(num, txt).arrange(RIGHT, buff=0.3)
            bullets.add(line)

        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        bullets.next_to(heading, DOWN, buff=0.8)

        # Reveal each bullet point one at a time
        for bullet in bullets:
            self.next_slide()
            self.play(FadeIn(bullet, shift=RIGHT * 0.3))

        self.next_slide()

        # Emphasize all at once
        self.play(
            *[bullet[1].animate.set_color(ACCENT) for bullet in bullets],
        )


class MonochromeDesignSlide(Slide):
    """Demonstrates monochrome base + single accent color design.

    The entire presentation uses only shades of grey. A single accent color
    is reserved exclusively for emphasis, keeping it consistent throughout.
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # Section label in tertiary color
        section = Text(
            "COLOR STRATEGY",
            font_size=20,
            color=TEXT_TERTIARY,
            weight=BOLD,
        ).to_edge(UP, buff=0.8)
        self.play(FadeIn(section))

        self.next_slide()

        # Show the palette
        palette_title = Text(
            "Monochrome + one accent",
            font_size=44,
            color=TEXT_PRIMARY,
            weight=BOLD,
        ).next_to(section, DOWN, buff=0.6)
        self.play(FadeIn(palette_title))

        # Color swatches
        swatch_colors = [TEXT_PRIMARY, TEXT_SECONDARY, TEXT_TERTIARY, ACCENT]
        swatch_labels = ["Primary", "Secondary", "Tertiary", "Accent"]
        swatches = VGroup()
        for color, label_text in zip(swatch_colors, swatch_labels):
            rect = RoundedRectangle(
                corner_radius=0.1, width=1.5, height=1.5,
                color=color, fill_color=color, fill_opacity=1.0,
                stroke_width=0,
            )
            label = Text(label_text, font_size=16, color=TEXT_SECONDARY)
            label.next_to(rect, DOWN, buff=0.2)
            swatches.add(VGroup(rect, label))

        swatches.arrange(RIGHT, buff=0.6).next_to(palette_title, DOWN, buff=0.8)

        self.next_slide()
        self.play(
            LaggedStart(*[FadeIn(s) for s in swatches], lag_ratio=0.2),
        )

        self.next_slide()

        # Show accent usage rule
        rule = Text(
            "Reserve accent for the single most important element",
            font_size=24,
            color=TEXT_SECONDARY,
        ).next_to(swatches, DOWN, buff=0.8)
        self.play(FadeIn(rule))

        self.next_slide()

        # Demonstrate: highlight the accent swatch
        accent_rect = swatches[3][0]
        highlight = SurroundingRectangle(
            accent_rect, color=ACCENT, buff=0.15, stroke_width=3,
        )
        self.play(Create(highlight))
        self.play(rule.animate.set_color(ACCENT))

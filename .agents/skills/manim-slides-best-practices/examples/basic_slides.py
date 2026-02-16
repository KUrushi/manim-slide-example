"""
Basic Slide Patterns for manim-slides

This file demonstrates fundamental slide creation techniques using manim-slides.
Each scene shows a core feature: basic slides, loops, auto-next, and speaker notes.

Render: manim-slides render basic_slides.py SceneName
Present: manim-slides present SceneName
"""

from manim import *
from manim_slides import Slide


class BasicSlide(Slide):
    """Demonstrates the simplest possible slide with next_slide() transitions."""

    def construct(self):
        # Slide 1: Title
        title = Text("Basic Slide Demo", font_size=56)
        self.play(Write(title))

        self.next_slide()

        # Slide 2: Transform title and show content
        subtitle = Text("Using next_slide() to create transitions", font_size=32)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(title.animate.to_edge(UP))
        self.play(FadeIn(subtitle))

        self.next_slide()

        # Slide 3: Show a shape
        circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.3)
        self.play(FadeOut(subtitle))
        self.play(Create(circle))

        self.next_slide()

        # Slide 4: Transform shape
        square = Square(side_length=3, color=RED, fill_opacity=0.3)
        self.play(Transform(circle, square))


class LoopSlide(Slide):
    """Demonstrates the loop feature that repeats animations until user advances."""

    def construct(self):
        title = Text("Loop Demo", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Create a dot and a circular path
        circle_path = Circle(radius=2, color=GREY_B)
        dot = Dot(color=BLUE, radius=0.15)
        dot.move_to(circle_path.point_from_proportion(0))

        self.play(Create(circle_path), FadeIn(dot))

        # This slide will loop: the dot orbits until the user presses next
        self.next_slide(loop=True)
        self.play(
            MoveAlongPath(dot, circle_path),
            run_time=3,
            rate_func=linear,
        )

        # After user advances, stop looping and continue
        self.next_slide()
        self.play(FadeOut(circle_path), dot.animate.move_to(ORIGIN).scale(3))

        self.next_slide()
        label = Text("Loop ended", font_size=36).next_to(dot, DOWN)
        self.play(Write(label))


class AutoNextSlide(Slide):
    """Demonstrates auto_next for slides that advance automatically."""

    def construct(self):
        title = Text("Auto-Next Demo", font_size=48)
        self.play(Write(title))

        self.next_slide()

        # This slide auto-advances when its animations finish (HTML export only)
        self.next_slide(auto_next=True)
        self.play(title.animate.to_edge(UP))
        countdown = VGroup(*[
            Text(str(i), font_size=72, color=YELLOW) for i in [3, 2, 1]
        ])
        for num in countdown:
            self.play(FadeIn(num, scale=1.5))
            self.play(FadeOut(num, scale=0.5))

        # This slide requires manual advance
        self.next_slide()
        go_text = Text("GO!", font_size=96, color=GREEN)
        self.play(FadeIn(go_text, scale=2))


class SpeakerNotesSlide(Slide):
    """Demonstrates speaker notes attached to slides."""

    def construct(self):
        self.next_slide(notes="Welcome the audience. Introduce the topic.")
        title = Text("Speaker Notes Demo", font_size=48)
        self.play(Write(title))

        self.next_slide(notes="""\
            Explain that speaker notes appear in the presenter view.
            - Visible in `manim-slides present` info window
            - Also available in HTML export via RevealJS speaker view
        """)
        self.play(title.animate.to_edge(UP))
        bullet1 = Text("Notes are visible in presenter view", font_size=28)
        bullet2 = Text("Supports Markdown formatting", font_size=28)
        bullets = VGroup(bullet1, bullet2).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(bullets))

        self.next_slide(notes="Wrap up and transition to the next topic.")
        conclusion = Text("Use notes to guide your delivery", font_size=32, color=BLUE)
        conclusion.next_to(bullets, DOWN, buff=0.8)
        self.play(Write(conclusion))


class PlaybackRateSlide(Slide):
    """Demonstrates playback_rate to control animation speed during presentation."""

    def construct(self):
        title = Text("Playback Rate Demo", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Normal speed slide
        self.next_slide()
        normal_label = Text("Normal speed (1.0x)", font_size=32)
        square = Square(color=BLUE, fill_opacity=0.5)
        VGroup(normal_label, square).arrange(DOWN, buff=0.5)
        self.play(FadeIn(normal_label), Create(square))
        self.play(Rotate(square, PI))

        # Slow playback slide
        self.next_slide(playback_rate=0.5)
        self.play(FadeOut(normal_label), FadeOut(square))
        slow_label = Text("Slow playback (0.5x)", font_size=32)
        circle = Circle(color=RED, fill_opacity=0.5)
        VGroup(slow_label, circle).arrange(DOWN, buff=0.5)
        self.play(FadeIn(slow_label), Create(circle))
        self.play(Rotate(circle, PI))

        # Fast playback slide
        self.next_slide(playback_rate=2.0)
        self.play(FadeOut(slow_label), FadeOut(circle))
        fast_label = Text("Fast playback (2.0x)", font_size=32)
        triangle = Triangle(color=GREEN, fill_opacity=0.5)
        VGroup(fast_label, triangle).arrange(DOWN, buff=0.5)
        self.play(FadeIn(fast_label), Create(triangle))
        self.play(Rotate(triangle, PI))

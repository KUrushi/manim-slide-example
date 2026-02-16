"""
Basic Slide Template for manim-slides

Use this template for a simple single-topic slide.
Copy this file and replace the placeholder code with your content.

Render: manim-slides render your_file.py YourSlide
Present: manim-slides present YourSlide
"""

from manim import *
from manim_slides import Slide


class YourSlide(Slide):
    """Basic slide template. Replace with your slide description."""

    def construct(self):
        # ============================================================
        # SETUP: Configure scene, create initial objects
        # ============================================================

        # Optional: Set background color
        # self.camera.background_color = "#111111"

        # Create your mobjects
        title = Text("Your Title", font_size=48)

        # ============================================================
        # CONTENT: Build your slide content with next_slide() transitions
        # ============================================================

        # Slide 1: Show title
        self.play(Write(title))

        self.next_slide()

        # Slide 2: Add more content
        self.play(title.animate.to_edge(UP))
        content = Text("Your content here", font_size=32)
        self.play(FadeIn(content))

        self.next_slide()

        # Slide 3: Continue building
        # self.play(...)

        # ============================================================
        # CLEANUP: Final animations, fade out
        # ============================================================

        self.play(FadeOut(title), FadeOut(content))


# Render: manim-slides render basic_slide.py YourSlide
# Present: manim-slides present YourSlide

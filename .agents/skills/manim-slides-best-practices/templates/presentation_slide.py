"""
Full Presentation Template for manim-slides

Use this template for a multi-slide presentation with persistent title and
slide number managed through Canvas. Suitable for talks with 5+ slides.

Render: manim-slides render your_file.py YourPresentation
Present: manim-slides present YourPresentation
"""

from manim import *
from manim_slides import Slide


class YourPresentation(Slide):
    """Full presentation template with Canvas-managed persistent elements."""

    def update_slide_number(self):
        """Increment and update the slide number in the canvas."""
        self.slide_count += 1
        old_number = self.canvas["slide_number"]
        new_number = Text(
            str(self.slide_count), font_size=20, color=GREY_B
        ).move_to(old_number)
        self.play(Transform(old_number, new_number))

    def construct(self):
        # ============================================================
        # SETUP: Configure scene and canvas
        # ============================================================

        # Optional: Set background color
        # self.camera.background_color = "#111111"

        # Initialize canvas elements (persist across all slides)
        presentation_title = Text(
            "Your Presentation Title", font_size=24
        ).to_corner(UL)
        self.slide_count = 1
        slide_number = Text("1", font_size=20, color=GREY_B).to_corner(DR)

        self.add_to_canvas(title=presentation_title, slide_number=slide_number)
        self.play(FadeIn(presentation_title), FadeIn(slide_number))

        # ============================================================
        # TITLE SLIDE: Opening slide
        # ============================================================

        main_title = Text("Your Presentation Title", font_size=56)
        subtitle = Text("Your Name / Date", font_size=28, color=GREY_B)
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.5)
        self.play(FadeIn(title_group))

        self.next_slide()

        # ============================================================
        # CONTENT SLIDES: Main presentation body
        # ============================================================

        # --- Slide 2 ---
        self.update_slide_number()
        slide2_content = Text("First content slide", font_size=36)
        self.wipe(self.mobjects_without_canvas, slide2_content)

        self.next_slide()

        # --- Slide 3 ---
        self.update_slide_number()
        slide3_content = Text("Second content slide", font_size=36)
        self.wipe(self.mobjects_without_canvas, slide3_content)

        self.next_slide()

        # Add more slides following the same pattern:
        # self.update_slide_number()
        # new_content = ...
        # self.wipe(self.mobjects_without_canvas, new_content)
        # self.next_slide()

        # ============================================================
        # CONCLUSION: Closing slide
        # ============================================================

        self.update_slide_number()
        thanks = Text("Thank you", font_size=56)
        self.wipe(self.mobjects_without_canvas, thanks)

        self.next_slide()

        # ============================================================
        # CLEANUP: Remove canvas and clear scene
        # ============================================================

        self.remove_from_canvas("title", "slide_number")
        self.wipe(self.mobjects_without_canvas, [])


# Render: manim-slides render presentation_slide.py YourPresentation
# Present: manim-slides present YourPresentation

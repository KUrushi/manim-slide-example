"""
3D Slide Template for manim-slides

Use this template for presentations involving 3D visualizations.
ThreeDSlide inherits from both Slide and ThreeDScene, providing
camera orientation controls and 3D rendering.

Render: manim-slides render your_file.py Your3DSlide
Present: manim-slides present Your3DSlide
"""

from manim import *
from manim_slides import ThreeDSlide


class Your3DSlide(ThreeDSlide):
    """3D slide template. Replace with your 3D visualization description."""

    def construct(self):
        # ============================================================
        # SETUP: Configure 3D scene and camera
        # ============================================================

        # Set initial camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create 3D axes
        axes = ThreeDAxes()
        self.add(axes)

        # For 2D text overlays in 3D scenes, use add_fixed_in_frame_mobjects
        title = Text("Your 3D Slide", font_size=36)
        self.add_fixed_in_frame_mobjects(title)
        title.to_corner(UL)
        self.play(FadeIn(title))

        # ============================================================
        # CONTENT: Build 3D content with slide transitions
        # ============================================================

        # Slide 1: Add your 3D objects
        # surface = Surface(
        #     lambda u, v: axes.c2p(u, v, np.sin(u) * np.cos(v)),
        #     u_range=[-PI, PI],
        #     v_range=[-PI, PI],
        #     resolution=(30, 30),
        # )
        # self.play(Create(surface))

        self.next_slide()

        # Slide 2: Animate camera
        # self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=2)

        self.next_slide()

        # Optional: Ambient camera rotation (loops well)
        # self.begin_ambient_camera_rotation(rate=60 * DEGREES / 4)
        # self.next_slide(loop=True)
        # self.wait(4)
        # self.next_slide()
        # self.stop_ambient_camera_rotation()

        # ============================================================
        # CLEANUP: Reset camera, fade out
        # ============================================================

        # self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, run_time=2)
        self.play(FadeOut(title))


# Render: manim-slides render threed_slide.py Your3DSlide
# Present: manim-slides present Your3DSlide

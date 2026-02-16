"""
Advanced Slide Patterns for manim-slides

This file demonstrates advanced features: Canvas management for persistent elements,
Wipe/Zoom transitions, 3D slides, and custom scene subclassing.

Render: manim-slides render advanced_slides.py SceneName
Present: manim-slides present SceneName
"""

from manim import *
from manim_slides import Slide, ThreeDSlide


class CanvasSlide(Slide):
    """Demonstrates Canvas for persistent elements like title and slide number."""

    def update_slide_number(self):
        """Update the slide number in the canvas."""
        self.slide_count += 1
        old_number = self.canvas["slide_number"]
        new_number = Text(
            str(self.slide_count), font_size=24, color=GREY_B
        ).move_to(old_number)
        self.play(Transform(old_number, new_number))

    def construct(self):
        # Set up persistent canvas elements
        title = Text("Canvas Demo", font_size=36).to_corner(UL)
        self.slide_count = 1
        slide_number = Text("1", font_size=24, color=GREY_B).to_corner(DR)
        self.add_to_canvas(title=title, slide_number=slide_number)
        self.play(FadeIn(title), FadeIn(slide_number))

        self.next_slide()

        # Slide 2: Canvas elements persist while content changes
        self.update_slide_number()
        circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.3)
        label = Text("Canvas keeps title and number visible", font_size=24)
        label.next_to(circle, DOWN, buff=0.5)
        self.play(Create(circle), FadeIn(label))

        self.next_slide()

        # Slide 3: Wipe content but keep canvas
        self.update_slide_number()
        square = Square(side_length=2.5, color=RED, fill_opacity=0.3)
        new_label = Text("Content replaced, canvas unchanged", font_size=24)
        new_label.next_to(square, DOWN, buff=0.5)
        self.wipe(
            self.mobjects_without_canvas,
            VGroup(square, new_label),
        )

        self.next_slide()

        # Slide 4: Update canvas title
        self.update_slide_number()
        new_title = Text("Updated Title", font_size=36).to_corner(UL)
        self.play(Transform(self.canvas["title"], new_title))

        self.next_slide()

        # Cleanup: remove canvas and clear
        self.remove_from_canvas("title", "slide_number")
        self.wipe(self.mobjects_without_canvas, [])


class WipeTransitionSlide(Slide):
    """Demonstrates Wipe transitions with various directions."""

    def construct(self):
        # Slide 1
        text1 = Text("Wipe Transition Demo", font_size=48)
        self.play(Write(text1))

        self.next_slide()

        # Wipe left (default direction)
        text2 = Text("Wipe LEFT (default)", font_size=36, color=BLUE)
        self.wipe(text1, text2)

        self.next_slide()

        # Wipe up
        text3 = Text("Wipe UP", font_size=36, color=GREEN)
        self.wipe(text2, text3, direction=UP)

        self.next_slide()

        # Wipe diagonal
        text4 = Text("Wipe DOWN + RIGHT", font_size=36, color=RED)
        self.wipe(text3, text4, direction=DOWN + RIGHT)

        self.next_slide()

        # Wipe with return_animation for custom control
        text5 = Text("Custom wipe via return_animation", font_size=36, color=YELLOW)
        anim = self.wipe(text4, text5, direction=UP + LEFT, return_animation=True)
        self.play(anim, run_time=1.5)

        self.next_slide()

        # Wipe to empty (clear all)
        self.wipe(text5, [])


class ZoomTransitionSlide(Slide):
    """Demonstrates Zoom transitions between slide content."""

    def construct(self):
        # Slide 1
        title = Text("Zoom Transition Demo", font_size=48)
        self.play(Write(title))

        self.next_slide()

        # Zoom in to new content
        content1 = VGroup(
            Text("Zoom replaces content", font_size=32),
            Text("with a scale + fade effect", font_size=24, color=GREY_B),
        ).arrange(DOWN, buff=0.3)
        self.zoom(title, content1)

        self.next_slide()

        # Zoom out to new content
        content2 = Text("Zoom out effect", font_size=40, color=BLUE)
        anim = self.zoom(content1, content2, out=True, scale=10.0, return_animation=True)
        self.play(anim)

        self.next_slide()

        # Zoom to final
        final = Text("End of demo", font_size=48)
        self.zoom(content2, final)


class ThreeDSlideExample(ThreeDSlide):
    """Demonstrates 3D slides with camera rotation."""

    def construct(self):
        # Set up 3D scene
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes)

        # Slide 1: Show 3D axes
        title = Text("3D Slide Demo", font_size=36)
        self.add_fixed_in_frame_mobjects(title)
        title.to_corner(UL)
        self.play(FadeIn(title))

        self.next_slide()

        # Slide 2: Add a surface
        surface = Surface(
            lambda u, v: axes.c2p(u, v, np.sin(u) * np.cos(v)),
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            resolution=(30, 30),
        )
        surface.set_style(fill_opacity=0.6)
        surface.set_fill_by_value(axes=axes, colorscale=[(BLUE, -1), (GREEN, 0), (RED, 1)])
        self.play(Create(surface), run_time=2)

        self.next_slide()

        # Slide 3: Ambient camera rotation (loops)
        self.begin_ambient_camera_rotation(rate=60 * DEGREES / 4)
        self.next_slide(loop=True)
        self.wait(4)

        # Slide 4: Stop rotation
        self.next_slide()
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=2)


class MovingCameraSlide(Slide, MovingCameraScene):
    """Base class combining Slide with MovingCameraScene."""
    pass


class MovingCameraSlideExample(MovingCameraSlide):
    """Demonstrates custom scene subclassing with MovingCameraScene."""

    def construct(self):
        self.camera.frame.save_state()

        # Create a large scene with multiple elements
        axes = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = axes.plot(lambda x: np.sin(x) * 2 + 5, color=BLUE, x_range=[0, 3 * PI])
        dot_start = Dot(axes.i2gp(graph.t_min, graph), color=GREEN)
        dot_end = Dot(axes.i2gp(graph.t_max, graph), color=RED)
        start_label = Text("Start", font_size=20).next_to(dot_start, UP)
        end_label = Text("End", font_size=20).next_to(dot_end, UP)

        self.add(axes, graph, dot_start, dot_end, start_label, end_label)

        self.next_slide()

        # Zoom into start point
        self.play(
            self.camera.frame.animate.scale(0.4).move_to(dot_start),
            run_time=2,
        )

        self.next_slide()

        # Pan to end point
        self.play(
            self.camera.frame.animate.move_to(dot_end),
            run_time=3,
        )

        self.next_slide()

        # Restore full view
        self.play(Restore(self.camera.frame), run_time=2)

---
name: custom-scenes
description: ThreeDSlide, multiple inheritance with Manim scenes, and custom Slide subclasses
metadata:
  tags: ThreeDSlide, MovingCameraScene, subclass, inheritance, 3D, custom
---

# Custom Scenes in manim-slides

manim-slides supports `ThreeDSlide` for 3D presentations and allows creating custom Slide subclasses by combining `Slide` with any ManimCE Scene type through multiple inheritance.

## ThreeDSlide

A built-in class that combines `Slide` with ManimCE's `ThreeDScene`, providing 3D camera controls alongside slide functionality.

```python
from manim import *
from manim_slides import ThreeDSlide

class My3DPresentation(ThreeDSlide):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere(radius=1, color=BLUE)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes)
        self.play(Create(sphere))

        self.next_slide()
        self.begin_ambient_camera_rotation(rate=75 * DEGREES / 4)
        self.wait(4)

        self.next_slide()
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(sphere))
```

### ThreeDSlide with Loops

Combine 3D camera rotation with looping slides for dramatic effect.

```python
from manim import *
from manim_slides import ThreeDSlide

class Rotating3DExample(ThreeDSlide):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle(radius=3, color=BLUE)
        dot = Dot(color=RED)

        self.add(axes)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(GrowFromCenter(circle))
        self.begin_ambient_camera_rotation(rate=75 * DEGREES / 4)

        self.next_slide()
        self.next_slide(loop=True)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.next_slide()

        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(dot.animate.move_to(ORIGIN))
```

## Multiple Inheritance with ManimCE Scenes

Create custom Slide subclasses by inheriting from both `Slide` and any ManimCE Scene type. `Slide` must come first in the MRO (method resolution order).

### Pattern

```python
from manim import *
from manim_slides import Slide

class CustomSlide(Slide, SomeManimScene):
    pass
```

### MovingCameraSlide

Combine slide functionality with camera movement (zoom, pan).

```python
from manim import *
from manim_slides import Slide

class MovingCameraSlide(Slide, MovingCameraScene):
    pass

class CameraZoomPresentation(MovingCameraSlide):
    def construct(self):
        self.camera.frame.save_state()

        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=WHITE, x_range=[0, 3 * PI])
        dot_start = Dot(ax.i2gp(graph.t_min, graph))
        dot_end = Dot(ax.i2gp(graph.t_max, graph))
        self.add(ax, graph, dot_start, dot_end)

        self.next_slide()
        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_start))

        self.next_slide()
        self.play(self.camera.frame.animate.move_to(dot_end))

        self.next_slide()
        self.play(Restore(self.camera.frame))
        self.wait()
```

### Other Scene Combinations

The same pattern works with any ManimCE Scene subclass.

```python
from manim import *
from manim_slides import Slide

# ZoomedScene for picture-in-picture zooming
class ZoomedSlide(Slide, ZoomedScene):
    pass

class ZoomLensPresentation(ZoomedSlide):
    def construct(self):
        dot = Dot(ORIGIN)
        self.add(dot)
        self.activate_zooming()
        self.play(dot.animate.shift(RIGHT))
        self.next_slide()
        self.play(dot.animate.shift(UP))
```

## Creating Reusable Slide Subclasses

Build presentation-specific base classes that encapsulate repeated setup logic.

```python
from manim import *
from manim_slides import Slide

class BrandedSlide(Slide):
    """Base class with consistent branding across slides."""

    def setup(self):
        super().setup()
        self.wait_time_between_slides = 0.1
        self.slide_count = 0

        self.title_text = Text("My Company").scale(0.5).to_corner(UL)
        self.slide_num = Text("0").scale(0.4).to_corner(DR)
        self.add_to_canvas(
            title=self.title_text,
            slide_num=self.slide_num,
        )
        self.add(self.title_text, self.slide_num)

    def advance(self, notes=""):
        """Mark slide boundary and update slide number."""
        self.slide_count += 1
        new_num = Text(str(self.slide_count)).scale(0.4).to_corner(DR)
        self.play(Transform(self.canvas["slide_num"], new_num))
        self.next_slide(notes=notes)

    def clear_content(self):
        """Remove all non-canvas content."""
        self.wipe(self.mobjects_without_canvas, [])

class ActualPresentation(BrandedSlide):
    def construct(self):
        intro = Text("Welcome!")
        self.play(Write(intro))
        self.advance(notes="Introduction slide")

        topic = Text("Topic 1")
        self.wipe(self.mobjects_without_canvas, topic)
        self.advance(notes="First topic")

        self.clear_content()
        self.remove_from_canvas("title", "slide_num")
        self.play(
            FadeOut(self.title_text),
            FadeOut(self.slide_num),
        )
        self.play(Write(Text("Thank you!")))
```

## setup() Method

Use `setup()` for initialization that runs before `construct()`. Always call `super().setup()` when overriding.

```python
from manim import *
from manim_slides import Slide

class SetupExample(Slide):
    def setup(self):
        super().setup()
        self.camera.background_color = "#1a1a2e"
        self.wait_time_between_slides = 0.1

    def construct(self):
        text = Text("Custom background!", color=WHITE)
        self.play(Write(text))
```

## Best Practices

1. **Place `Slide` first in the inheritance list** -- `class MySlide(Slide, MovingCameraScene)` ensures correct method resolution order; reversing the order may cause unexpected behavior.
2. **Define intermediate classes for reuse** -- create `class MovingCameraSlide(Slide, MovingCameraScene): pass` once and inherit from it in multiple presentations rather than repeating the multiple inheritance.
3. **Use `setup()` for consistent initialization** -- put canvas registration, background color, and `wait_time_between_slides` in `setup()` so `construct()` focuses on content.
4. **Always call `super().setup()`** -- when overriding `setup()`, call the parent to ensure both Slide and the Manim scene type initialize correctly.
5. **Prefer `ThreeDSlide` over manual `Slide + ThreeDScene`** -- the built-in `ThreeDSlide` is tested and maintained; use manual inheritance only for scene types that do not have a built-in Slide variant.

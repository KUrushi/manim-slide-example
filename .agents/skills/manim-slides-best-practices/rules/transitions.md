---
name: transitions
description: Wipe and Zoom transition methods and animation classes in manim-slides
metadata:
  tags: wipe, zoom, transition, animation, direction, Wipe, Zoom
---

# Transitions in manim-slides

manim-slides provides two built-in transition methods (`wipe()` and `zoom()`) and their corresponding animation classes (`Wipe` and `Zoom`) for smooth slide-to-slide content switching.

## wipe() Method

Slides old objects off-screen while sliding new objects in from the opposite direction.

```python
def wipe(
    *args,
    direction: np.ndarray = LEFT,
    return_animation: bool = False,
    **kwargs
) -> Wipe | None
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `*args` | Mobject(s) | - | Old and new Mobjects (positional) |
| `direction` | np.ndarray | LEFT | Direction old objects exit (new enter from opposite) |
| `return_animation` | bool | False | Return animation object instead of playing |
| `**kwargs` | Any | - | Extra arguments passed to `self.play()` |

### Basic Usage

```python
from manim import *
from manim_slides import Slide

class WipeBasicExample(Slide):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        square = Square(side_length=3, color=RED)

        self.play(FadeIn(circle))
        self.next_slide()

        self.wipe(circle, square)
        self.next_slide()

        text = Text("Done!")
        self.wipe(square, text, direction=UP)
```

### Direction Options

```python
from manim import *
from manim_slides import Slide

class WipeDirectionExample(Slide):
    def construct(self):
        slides = [
            Text("Left (default)"),
            Text("Right"),
            Text("Up"),
            Text("Down"),
            Text("Diagonal"),
        ]
        directions = [LEFT, RIGHT, UP, DOWN, DOWN + RIGHT]

        self.play(Write(slides[0]))
        for i in range(1, len(slides)):
            self.next_slide()
            self.wipe(slides[i - 1], slides[i], direction=directions[i])
```

### Wipe with Canvas

Use `mobjects_without_canvas` to wipe all non-persistent content.

```python
from manim import *
from manim_slides import Slide

class WipeCanvasExample(Slide):
    def construct(self):
        title = Text("Title").to_edge(UP)
        self.add_to_canvas(title=title)
        self.play(FadeIn(title))

        content = Circle(color=GREEN)
        self.play(Create(content))
        self.next_slide()

        new_content = Square(color=YELLOW)
        self.wipe(self.mobjects_without_canvas, new_content)
        self.next_slide()

        self.wipe(self.mobjects_without_canvas, [])
```

### return_animation

Get the animation object for manual control or combination with other animations.

```python
from manim import *
from manim_slides import Slide

class WipeReturnExample(Slide):
    def construct(self):
        old = Text("Old content")
        new = Text("New content")
        self.play(Write(old))
        self.next_slide()

        anim = self.wipe(old, new, return_animation=True)
        self.play(anim, run_time=2)
```

## zoom() Method

Transitions by fading and scaling between old and new objects.

```python
def zoom(
    *args,
    return_animation: bool = False,
    **kwargs
) -> Zoom | None
```

### Basic Usage

```python
from manim import *
from manim_slides import Slide

class ZoomBasicExample(Slide):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        square = Square(side_length=3, color=RED)

        self.play(FadeIn(circle))
        self.next_slide()

        self.zoom(circle, square)
        self.next_slide()

        self.zoom(square, circle)
```

## Wipe Animation Class

For direct control, import and use the `Wipe` class with `self.play()`.

```python
from manim import *
from manim_slides import Slide
from manim_slides.slide.animation import Wipe

class WipeClassExample(Slide):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        square = Square(side_length=3, color=RED)

        self.play(FadeIn(circle))
        self.next_slide()
        self.play(Wipe(circle, square, shift=3 * LEFT))
```

Constructor parameters:

| Parameter | Type | Default | Description |
|---|---|---|---|
| `current` | Sequence[Mobject] \| None | - | Objects to remove |
| `future` | Sequence[Mobject] \| None | - | Objects to add |
| `shift` | np.ndarray | - | Direction and distance of the wipe |
| `fade_in_kwargs` | Mapping \| None | None | Extra kwargs for FadeIn |
| `fade_out_kwargs` | Mapping \| None | None | Extra kwargs for FadeOut |

## Zoom Animation Class

The `Zoom` class provides scale-based transitions.

```python
from manim import *
from manim_slides import Slide
from manim_slides.slide.animation import Zoom

class ZoomClassExample(Slide):
    def construct(self):
        small = Circle(radius=1, color=GREEN)
        big = Circle(radius=3, color=YELLOW)

        self.play(FadeIn(small))
        self.next_slide()
        self.play(Zoom(small, big, scale=2.0))
        self.next_slide()
        self.play(Zoom(big, small, scale=0.5, out=True))
```

Constructor parameters:

| Parameter | Type | Default | Description |
|---|---|---|---|
| `current` | Sequence[Mobject] \| None | - | Objects to remove |
| `future` | Sequence[Mobject] \| None | - | Objects to add |
| `scale` | float | - | Scale factor for the transition |
| `out` | bool | False | Zoom out instead of in |
| `fade_in_kwargs` | Mapping \| None | None | Extra kwargs for FadeIn |
| `fade_out_kwargs` | Mapping \| None | None | Extra kwargs for FadeOut |

## Best Practices

1. **Prefer `wipe()` and `zoom()` methods over animation classes** -- the convenience methods handle playing automatically and integrate with canvas; use the classes only when you need fine-grained control or want to combine with other animations.
2. **Use `direction` to convey narrative flow** -- LEFT for forward progression, RIGHT for going back, UP for building on ideas, DOWN for drilling into detail.
3. **Combine transitions with `mobjects_without_canvas`** -- always pass `self.mobjects_without_canvas` as the first argument when replacing all slide content to preserve canvas objects.
4. **Use `return_animation=True` when combining transitions** -- this lets you play the transition alongside other animations or control `run_time` explicitly.
5. **Place `next_slide()` after transitions** -- call `next_slide()` after a wipe/zoom to mark the boundary, so the new content forms a distinct slide.

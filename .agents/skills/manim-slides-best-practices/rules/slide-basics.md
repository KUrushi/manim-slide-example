---
name: slide-basics
description: Slide class basics, next_slide() parameters, and core slide workflow in manim-slides
metadata:
  tags: slide, next_slide, loop, auto_next, playback_rate, notes, scene
---

# Slide Basics in manim-slides

The `Slide` class is the core of manim-slides. It extends ManimCE's `Scene` with a single key addition: the `next_slide()` method that divides your animation into presentable slides.

## Slide vs Scene

`Slide` inherits from `Scene`, so all standard Manim methods work unchanged. The only difference is the ability to create slide boundaries with `next_slide()`.

```python
from manim import *
from manim_slides import Slide

class MyPresentation(Slide):
    def construct(self):
        title = Text("Hello, Slides!")
        self.play(Write(title))
        self.next_slide()

        subtitle = Text("Second slide").next_to(title, DOWN)
        self.play(FadeIn(subtitle))
```

Converting an existing Scene to Slide requires only two changes:
1. Import `Slide` from `manim_slides`
2. Change the parent class from `Scene` to `Slide`
3. Insert `self.next_slide()` calls where you want slide breaks

## next_slide() Method

The primary method for controlling slide behavior. It marks a boundary between slides and sets options for the **next** slide (the animations that follow the call).

```python
def next_slide(
    *,
    loop: bool = False,
    auto_next: bool = False,
    playback_rate: float = 1.0,
    reversed_playback_rate: float = 1.0,
    notes: str = '',
    dedent_notes: bool = True,
    skip_animations: bool = False,
    src: Path | None = None,
) -> None
```

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `loop` | bool | False | Loop the next slide's animations infinitely |
| `auto_next` | bool | False | Auto-advance when animations finish (HTML/RevealJS only) |
| `playback_rate` | float | 1.0 | Forward playback speed (present mode only) |
| `reversed_playback_rate` | float | 1.0 | Reverse playback speed (present mode only) |
| `notes` | str | '' | Markdown speaker notes for the next slide |
| `dedent_notes` | bool | True | Auto-dedent notes text |
| `skip_animations` | bool | False | Exclude next slide from output |
| `src` | Path \| None | None | Path to external video file (v5.5.0+) |

**Important:** `next_slide()` is automatically inserted at the start and end of `construct()`. You do not need to call it at the very beginning or very end.

## Looping Slides

Wrap animations in `next_slide(loop=True)` ... `next_slide()` to create a loop. The loop plays until the presenter advances.

```python
from manim import *
from manim_slides import Slide

class LoopExample(Slide):
    def construct(self):
        dot = Dot(color=BLUE, radius=1)
        self.play(FadeIn(dot))

        self.next_slide(loop=True)
        self.play(Indicate(dot, scale_factor=2))
        self.next_slide()

        self.play(FadeOut(dot))
```

## Auto-Advancing Slides

Use `auto_next=True` for slides that should advance without user input. Works in HTML/RevealJS export.

```python
from manim import *
from manim_slides import Slide

class AutoNextExample(Slide):
    def construct(self):
        square = Square(color=RED)
        self.play(GrowFromCenter(square))

        self.next_slide(auto_next=True)
        self.play(Wiggle(square))

        self.next_slide()
        self.play(FadeOut(square))
```

## Speaker Notes

Attach Markdown-formatted notes to slides for presenter reference.

```python
from manim import *
from manim_slides import Slide

class NotesExample(Slide):
    def construct(self):
        self.next_slide(notes="Introduce the topic here")
        title = Text("Introduction")
        self.play(Write(title))

        self.next_slide(notes="Explain the **key concept** in detail")
        body = Text("Key Concept").next_to(title, DOWN)
        self.play(FadeIn(body))
```

## Playback Rate

Control animation speed during presentation.

```python
from manim import *
from manim_slides import Slide

class PlaybackRateExample(Slide):
    def construct(self):
        circle = Circle(color=GREEN)
        self.play(Create(circle))

        self.next_slide(playback_rate=2.0)
        self.play(circle.animate.shift(RIGHT * 3), run_time=2)

        self.next_slide(playback_rate=0.5)
        self.play(circle.animate.shift(LEFT * 3), run_time=2)
```

## Animation Skipping

Skip sections during development to speed up rendering.

```python
from manim import *
from manim_slides import Slide

class SkipExample(Slide):
    def construct(self):
        self.play(Write(Text("First slide")))

        self.start_skip_animations()
        self.next_slide()
        self.play(Write(Text("Skipped slide")))
        self.stop_skip_animations()

        self.next_slide()
        self.play(Write(Text("Final slide")))
```

## wait_time_between_slides

Set a small wait time to eliminate visual gaps between slides during presentation.

```python
from manim import *
from manim_slides import Slide

class SmoothTransitionExample(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1
        circle = Circle()
        self.play(Create(circle))
        self.next_slide()
        self.play(FadeOut(circle))
```

## Best Practices

1. **Do not call `next_slide()` at the very start or end of `construct()`** -- it is added automatically and duplicating it creates empty slides.
2. **Place `next_slide()` before the animations it configures** -- options like `loop` and `notes` apply to the animations that follow the call, not those before it.
3. **Use `loop=True` with a matching `next_slide()` after** -- always close a loop block with a plain `next_slide()` so the presenter can advance past it.
4. **Set `wait_time_between_slides = 0.1`** -- this eliminates visual gaps between slides during presentation without noticeable delay.
5. **Use `start_skip_animations()` during development** -- skip already-finished sections to speed up iteration on later slides.
6. **Keep speaker notes concise** -- notes support Markdown formatting; use bullet points for quick reference during presentation.

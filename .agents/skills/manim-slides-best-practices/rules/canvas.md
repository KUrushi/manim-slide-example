---
name: canvas
description: Canvas management for persistent objects across slides in manim-slides
metadata:
  tags: canvas, add_to_canvas, remove_from_canvas, mobjects_without_canvas, persistent
---

# Canvas in manim-slides

The Canvas system manages objects that persist across multiple slides, such as titles, slide numbers, logos, or navigation elements. Canvas objects are excluded from bulk transitions, allowing you to replace slide content while keeping persistent elements in place.

## Canvas API

### add_to_canvas()

Register named Mobjects that should persist across slides.

```python
# Signature
def add_to_canvas(**objects: Mobject) -> None
```

Objects are added as keyword arguments where the key becomes the name used to reference or remove them later.

```python
from manim import *
from manim_slides import Slide

class CanvasAddExample(Slide):
    def construct(self):
        title = Text("My Presentation").to_corner(UL)
        page_num = Text("1").to_corner(DR)
        self.add_to_canvas(title=title, page_num=page_num)
        self.play(FadeIn(title), FadeIn(page_num))

        self.next_slide()
        body = Text("Slide content here")
        self.play(Write(body))
```

### canvas Property

Access the name-to-Mobject mapping for all canvas objects.

```python
# Returns MutableMapping[str, Mobject]
@property
def canvas() -> MutableMapping[str, Mobject]
```

Use this to read or modify canvas objects by name.

```python
from manim import *
from manim_slides import Slide

class CanvasAccessExample(Slide):
    def construct(self):
        title = Text("Original Title").to_corner(UL)
        self.add_to_canvas(title=title)
        self.play(FadeIn(title))

        self.next_slide()
        new_title = Text("Updated Title").to_corner(UL)
        self.play(Transform(self.canvas["title"], new_title))
```

### canvas_mobjects Property

Get all canvas Mobject values (without names).

```python
@property
def canvas_mobjects() -> ValuesView[Mobject]
```

### remove_from_canvas()

Remove named objects from the canvas.

```python
def remove_from_canvas(*names: str) -> None
```

```python
from manim import *
from manim_slides import Slide

class CanvasRemoveExample(Slide):
    def construct(self):
        title = Text("Title").to_corner(UL)
        subtitle = Text("Subtitle").to_corner(UR)
        self.add_to_canvas(title=title, subtitle=subtitle)
        self.play(FadeIn(title), FadeIn(subtitle))

        self.next_slide()
        self.remove_from_canvas("subtitle")
        self.play(FadeOut(subtitle))
```

### mobjects_without_canvas

Get all scene Mobjects excluding canvas objects. Essential for transitions that should replace slide content but preserve persistent elements.

```python
@property
def mobjects_without_canvas() -> Sequence[Mobject]
```

## Common Patterns

### Title and Slide Number

The most common canvas pattern: a persistent title and page counter.

```python
from manim import *
from manim_slides import Slide

class TitleAndNumberExample(Slide):
    def update_slide_number(self):
        self.slide_count += 1
        old_num = self.canvas["slide_number"]
        new_num = Text(str(self.slide_count)).to_corner(DL)
        self.play(Transform(old_num, new_num))

    def construct(self):
        self.slide_count = 1
        title = Text("Presentation Title").to_corner(UL)
        slide_number = Text("1").to_corner(DL)
        self.add_to_canvas(title=title, slide_number=slide_number)
        self.play(FadeIn(title), FadeIn(slide_number))

        self.next_slide()
        self.update_slide_number()
        circle = Circle(color=BLUE)
        self.play(Create(circle))

        self.next_slide()
        self.update_slide_number()
        square = Square(color=RED)
        self.wipe(self.mobjects_without_canvas, square)

        self.next_slide()
        self.update_slide_number()
        self.play(Transform(
            self.canvas["title"],
            Text("New Section").to_corner(UL)
        ))
```

### Wipe with Canvas Preservation

Use `mobjects_without_canvas` with `wipe()` to replace all slide content while keeping canvas objects.

```python
from manim import *
from manim_slides import Slide

class WipeWithCanvasExample(Slide):
    def construct(self):
        header = Text("Chapter 1").to_edge(UP)
        self.add_to_canvas(header=header)
        self.play(FadeIn(header))

        content_a = Text("First content")
        self.play(Write(content_a))
        self.next_slide()

        content_b = Text("Second content")
        self.wipe(self.mobjects_without_canvas, content_b)
        self.next_slide()

        self.wipe(self.mobjects_without_canvas, [])
        self.remove_from_canvas("header")
        self.play(FadeOut(header))
```

### Cleanup at End

Always remove canvas objects before the presentation ends to avoid leftover artifacts.

```python
from manim import *
from manim_slides import Slide

class CleanupExample(Slide):
    def construct(self):
        logo = ImageMobject("logo.png").to_corner(DR).scale(0.3)
        self.add_to_canvas(logo=logo)
        self.add(logo)

        self.play(Write(Text("Main content")))
        self.next_slide()

        self.remove_from_canvas("logo")
        self.wipe(self.mobjects_without_canvas, [])
        self.play(FadeOut(logo))
        self.play(Write(Text("Thank you!")))
```

## Best Practices

1. **Use descriptive canvas names** -- names like `title`, `slide_number`, and `header` make code self-documenting and easy to reference later with `self.canvas["name"]`.
2. **Always use `mobjects_without_canvas` for bulk transitions** -- when calling `wipe()` or replacing all content, use this property instead of manually listing objects to avoid accidentally removing persistent elements.
3. **Remove canvas objects before they become unnecessary** -- call `remove_from_canvas()` when a persistent element is no longer needed (e.g., section changes) to keep the canvas clean.
4. **Add canvas objects early in `construct()`** -- register persistent elements before creating slide content so they are properly tracked from the start.
5. **Combine canvas with helper methods** -- extract repeated patterns like slide number updates into helper methods to keep `construct()` readable.

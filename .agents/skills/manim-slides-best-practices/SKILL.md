---
name: manim-slides-best-practices
description: |
  Trigger when: (1) User mentions "manim-slides" or "manim slides" or "Slide" class from manim_slides, (2) Code contains `from manim_slides import Slide`, (3) User runs `manim-slides` CLI commands, (4) User wants to create a presentation or slideshow using Manim, (5) Working with next_slide(), Canvas, Wipe, Zoom, or manim-slides-specific features.

  Best practices for manim-slides - the tool that turns Manim animations into presentation slides. Covers Slide class, next_slide() API, Canvas management, transitions (Wipe/Zoom), CLI usage (render/present/convert), export to HTML/PDF/PPTX, and presentation design principles (gaze control, information density, color philosophy, font strategy).

  NOT for vanilla Manim animation (use manimce-best-practices instead). NOT for planning video content (use manim-composer instead).
---

## How to use

Read individual rule files for detailed API documentation and code examples:

### Core Concepts
- [rules/slide-basics.md](rules/slide-basics.md) - Slide class, next_slide() API, loop, auto_next, notes, playback_rate
- [rules/canvas.md](rules/canvas.md) - Canvas management, persistent objects across slides
- [rules/transitions.md](rules/transitions.md) - Wipe and Zoom transitions, animation classes

### Configuration & CLI
- [rules/cli.md](rules/cli.md) - render, present, convert commands, export formats (HTML/PDF/PPTX)
- [rules/custom-scenes.md](rules/custom-scenes.md) - ThreeDSlide, MovingCameraScene subclassing

## Presentation Design

Design references for creating effective presentations:

- [references/presentation-design.md](references/presentation-design.md) - Gaze control, information density, color, font strategy, pyramid structure, staircase method
- [references/slide-design-checklist.md](references/slide-design-checklist.md) - Pre-presentation checklist for structure, visual design, animation, and technical quality

## Working Examples

Complete, tested example files demonstrating common patterns:

- [examples/basic_slides.py](examples/basic_slides.py) - Basic slides, loops, auto-next, speaker notes, playback rate
- [examples/advanced_slides.py](examples/advanced_slides.py) - Canvas, Wipe/Zoom transitions, 3D slides, custom scenes
- [examples/presentation_design.py](examples/presentation_design.py) - Minimal info, visual hierarchy, progressive reveal, monochrome design

## Slide Templates

Copy and modify these templates to start new projects:

- [templates/basic_slide.py](templates/basic_slide.py) - Simple slide template
- [templates/presentation_slide.py](templates/presentation_slide.py) - Full presentation with Canvas (title, slide numbers)
- [templates/threed_slide.py](templates/threed_slide.py) - 3D slide template

## Quick Reference

### Basic Slide Structure
```python
from manim import *
from manim_slides import Slide

class MySlide(Slide):
    def construct(self):
        title = Text("Hello, manim-slides!")
        self.play(Write(title))
        self.next_slide()

        subtitle = Text("Next slide", font_size=28)
        self.play(FadeIn(subtitle))
```

### Key Commands
```bash
# Render slides
manim-slides render slides.py MySlide

# Present (live)
manim-slides present MySlide

# Export to HTML (single file, offline)
manim-slides convert --one-file --offline MySlide output.html

# Export to PowerPoint
manim-slides convert --to=pptx MySlide output.pptx
```

### next_slide() Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `loop` | bool | False | Loop this slide's animations |
| `auto_next` | bool | False | Auto-advance (HTML only) |
| `playback_rate` | float | 1.0 | Playback speed |
| `notes` | str | '' | Markdown speaker notes |
| `skip_animations` | bool | False | Skip this slide |
| `src` | Path | None | External video file (v5.5.0+) |

### Presentation Design Principles
1. **One idea per slide** - if it can't be grasped in 2 seconds, split it
2. **Conclusion first** - present the conclusion within the first 10% of slides
3. **Monochrome + 1 accent** - design in black/white, add at most 1 color
4. **One font family** - use size and weight for hierarchy, never mix fonts
5. **Subtle animations only** - FadeIn, Write, Create for disclosure, not spectacle
6. **Gaze control** - every element's position and timing guides the eye intentionally

### Common Pitfalls to Avoid
1. **Overloading slides** - resist putting multiple concepts on one slide
2. **Flashy effects** - avoid SpinInFromNothing, ApplyWave etc. for emphasis
3. **Forgetting next_slide()** - without it, all animations play as one continuous video
4. **Color overuse** - more than 1 accent color scatters attention
5. **Ignoring Canvas** - use Canvas for persistent elements (titles, page numbers) instead of re-creating them

### Installation
```bash
# Install manim-slides with Qt support (required for present)
pip install "manim-slides[manim,pyside6-full]"

# Verify installation
manim-slides checkhealth
```

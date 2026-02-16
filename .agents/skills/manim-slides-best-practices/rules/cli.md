---
name: cli
description: CLI commands for rendering, presenting, and converting manim-slides presentations
metadata:
  tags: cli, render, present, convert, html, pdf, pptx, export
---

# CLI Commands in manim-slides

manim-slides provides three main CLI commands: `render` to build animations, `present` to display them interactively, and `convert` to export to HTML, PDF, or PPTX.

## manim-slides render

Wraps ManimCE's renderer to produce slide-compatible output.

```bash
# Basic render
manim-slides render example.py MySlide

# High quality
manim-slides render -qh example.py MySlide

# Multiple scenes
manim-slides render example.py Slide1 Slide2

# ManimGL mode
manim-slides render --GL example.py MySlide
```

All standard ManimCE flags are passed through (e.g., `-qh` for high quality, `-ql` for low quality, `-a` for all scenes).

## manim-slides present

Displays rendered slides as an interactive presentation with keyboard/mouse controls.

```bash
# Basic presentation
manim-slides present MySlide

# Shorthand (present is the default command)
manim-slides MySlide

# Full-screen mode
manim-slides present -F MySlide

# Start from a specific slide
manim-slides present --start-at 0,2 MySlide

# Hide mouse cursor
manim-slides present -H MySlide

# Multiple scenes in sequence
manim-slides present Slide1 Slide2

# Exit after last slide
manim-slides present --exit-after-last-slide MySlide
```

### Key Options

| Option | Description |
|---|---|
| `-F, --full-screen` | Full-screen presentation |
| `-H, --hide-mouse` | Hide mouse cursor |
| `--start-at <SCENE,SLIDE>` | Start at specific scene and slide index |
| `--start-paused` | Begin in paused state |
| `-S, --screen <NUMBER>` | Select display for presentation |
| `--playback-rate <RATE>` | Override playback speed |
| `--exit-after-last-slide` | Auto-exit at the end |
| `--next-terminates-loop` | Next button stops looping slides |
| `--hide-info-window` | Hide the presenter info panel |
| `--show-info-window` | Show the presenter info panel |
| `--info-window-screen <N>` | Display for the info panel |
| `--aspect-ratio {keep,ignore}` | Aspect ratio handling |
| `--folder <DIR>` | Custom slides directory |

## manim-slides convert

Export slides to distributable formats: HTML, PDF, PPTX, or ZIP.

### HTML Export

```bash
# Basic HTML (RevealJS-based)
manim-slides convert MySlide output.html

# Self-contained single file
manim-slides convert --one-file MySlide output.html

# Offline-capable single file
manim-slides convert --one-file --offline MySlide output.html

# With RevealJS options
manim-slides convert -cslide_number=true -ctransition=fade MySlide output.html

# Custom template
manim-slides convert --use-template my_template.html MySlide output.html

# Show available config
manim-slides convert --to=html --show-config

# Show default template
manim-slides convert --to=html --show-template
```

### PDF Export

```bash
# Basic PDF (last frame of each slide)
manim-slides convert --to=pdf MySlide output.pdf
```

### PPTX Export

```bash
# PowerPoint export
manim-slides convert --to=pptx MySlide output.pptx
```

### ZIP Export

```bash
# HTML with assets in a zip archive
manim-slides convert --to=zip MySlide output.zip
```

## Export Format Comparison

| Feature | present | HTML | PPTX | PDF |
|---|---|---|---|---|
| Animation playback | Yes | Yes | Yes | No |
| Loop support | Yes | Yes | Yes | No |
| Auto-advance | Yes | Yes | Yes | N/A |
| Reverse playback | Yes | No | No | No |
| Pause animation | Yes | Yes | No | No |
| Speaker notes | Yes | Yes | No | No |
| Customization | Low | High | Low | Low |
| Requirements | Python + Qt | Browser | Office app | PDF reader |
| Single file | N/A | `--one-file` | Always | Always |

## Utility Commands

```bash
# Check environment and dependencies
manim-slides checkhealth

# List available scenes in a file
manim-slides list-scenes

# Initialize config file (.manim-slides.toml)
manim-slides init

# Configuration wizard
manim-slides wizard
```

## Typical Workflow

A complete render-to-export workflow:

```bash
# 1. Render the presentation
manim-slides render -qh presentation.py MySlide

# 2. Preview interactively
manim-slides present MySlide

# 3. Export for distribution
manim-slides convert --one-file --offline MySlide presentation.html

# 4. (Optional) PDF backup
manim-slides convert --to=pdf MySlide presentation_backup.pdf
```

## Best Practices

1. **Use `--one-file --offline` for HTML distribution** -- this embeds all assets and JS/CSS into a single self-contained file that works without internet access.
2. **Render in high quality (`-qh`) for final exports** -- use low quality (`-ql`) during development for faster iteration, then switch to high quality for the final version.
3. **Use `present` for rehearsal before converting** -- the interactive presenter lets you verify timing, loops, and transitions before committing to a static export format.
4. **Prefer HTML over PPTX for animation-heavy presentations** -- PPTX export is experimental and may have memory issues with many slides; HTML preserves all animation features.
5. **Use PDF as a backup only** -- PDF loses all animations; generate it alongside HTML as a fallback for environments without browser access.
6. **Run `manim-slides checkhealth` after installation** -- verify that all dependencies (Qt bindings, ManimCE) are correctly installed before starting work.

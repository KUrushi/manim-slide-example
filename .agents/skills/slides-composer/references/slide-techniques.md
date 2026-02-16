# Slide Techniques for manim-slides

Effective design techniques for creating individual slides and sequences.

---

## Layout Patterns

### Centered Statement

The simplest and most powerful layout: one sentence, centered.

```
┌─────────────────────────────────┐
│                                 │
│                                 │
│       KEY MESSAGE HERE          │
│       (large, bold)             │
│                                 │
│                                 │
└─────────────────────────────────┘
```

**When to use:** Conclusions, key takeaways, transitions between sections.

### Title + Body

Standard content slide with a heading and supporting content.

```
┌─────────────────────────────────┐
│  SECTION LABEL     (tertiary)   │
├─────────────────────────────────┤
│  Main heading      (primary)    │
│                                 │
│  Supporting text   (secondary)  │
│  or diagram                     │
│                                 │
└─────────────────────────────────┘
```

**When to use:** Most content slides.

### Side-by-Side Comparison

Two elements placed horizontally for contrast or connection.

```
┌───────────────┬───────────────┐
│               │               │
│   Element A   │   Element B   │
│               │               │
│   (labeled)   │   (labeled)   │
│               │               │
└───────────────┴───────────────┘
```

**When to use:** Before/after, option comparison, concept duality.

### Diagram Focus

A single diagram or figure that tells the story.

```
┌─────────────────────────────────┐
│  LABEL                          │
├─────────────────────────────────┤
│                                 │
│     ┌───┐  ──>  ┌───┐          │
│     │ A │       │ B │          │
│     └───┘  <──  └───┘          │
│                                 │
│  Caption text  (tertiary)       │
└─────────────────────────────────┘
```

**When to use:** Process flows, architecture, relationships.

### Progressive List

Bullet points revealed one at a time.

```
Step 1:                    Step 2:                    Step 3:
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│  Heading         │      │  Heading         │      │  Heading         │
│                  │      │                  │      │                  │
│  1. First point  │      │  1. First point  │      │  1. First point  │
│                  │      │  2. Second point │      │  2. Second point │
│                  │      │                  │      │  3. Third point  │
└──────────────────┘      └──────────────────┘      └──────────────────┘
```

**When to use:** Multiple supporting reasons, step-by-step processes.

---

## Progressive Disclosure Techniques

### Build-Up

Add elements one by one, keeping previous elements visible.

```python
# Show title
self.play(FadeIn(title))
self.next_slide()

# Add first point (title stays)
self.play(FadeIn(point1, shift=RIGHT * 0.3))
self.next_slide()

# Add second point (title + point1 stay)
self.play(FadeIn(point2, shift=RIGHT * 0.3))
```

### Replace

Swap one element for the next using transitions.

```python
# Show concept A
self.play(FadeIn(concept_a))
self.next_slide()

# Replace with concept B
self.wipe(concept_a, concept_b)
self.next_slide()
```

### Transform

Morph one representation into another to show relationships.

```python
# Show initial state
self.play(Create(diagram_simple))
self.next_slide()

# Transform to show evolution
self.play(Transform(diagram_simple, diagram_detailed))
```

### Highlight & Dim

Draw attention to one part by dimming everything else.

```python
# All elements visible
self.next_slide()

# Highlight target, dim rest
self.play(
    target.animate.set_color(ACCENT),
    *[other.animate.set_opacity(0.3) for other in rest],
)
```

---

## Visual Hierarchy Techniques

### Size-Based Hierarchy

```python
# Level 1: Core message (eyes land here first)
Text("Main Point", font_size=52, weight=BOLD)

# Level 2: Supporting context
Text("Explanation text", font_size=32)

# Level 3: Supplementary detail
Text("Source: data from 2024", font_size=18, color=GREY_C)
```

### Position-Based Hierarchy

- **Center**: Primary focus
- **Upper area**: Context, section labels
- **Lower area**: Details, captions
- **Left-to-right**: Reading flow, process flow, causation

### Color-Based Hierarchy

```python
ACCENT = "#3B82F6"  # Single accent for emphasis

Text("Key term", color=ACCENT)        # Attention here
Text("Normal text", color=WHITE)       # Standard reading
Text("Context", color=GREY_B)          # Acknowledged, skippable
Text("Label", color=GREY_C)            # Supplementary
```

---

## Transition Techniques

### Between Slides (within a section)

- `FadeIn` / `FadeOut`: Standard, subtle
- `self.wipe()`: Clean replacement, good for content slides
- Progressive reveal within the same visual context

### Between Sections

- Wipe transition with new section label
- Brief "blank" pause (clear everything, then introduce new section)
- Canvas title update to signal new section

### Emphasis Transitions

- `Indicate()`: Brief flash to draw attention
- `Circumscribe()`: Circle around important element
- Color change on key term

---

## Mathematical Content

### Equations

```python
# Build equations progressively
step1 = MathTex(r"f(x) = x^2")
self.play(Write(step1))
self.next_slide()

step2 = MathTex(r"f'(x) = 2x")
self.play(TransformMatchingTex(step1, step2))
```

### Graphs

```python
# Show function graph with labeled axes
axes = Axes(x_range=[-3, 3], y_range=[-2, 5])
graph = axes.plot(lambda x: x**2, color=ACCENT)
self.play(Create(axes), Create(graph))
```

### Diagrams with Math

Keep mathematical content clean:
- One equation per slide
- Build derivations step by step across slides
- Use color to track terms across transformations

---

## Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Multiple ideas per slide | Split into separate slides |
| Wall of bullet points | One point per slide, use progressive reveal |
| Decorative animations | Only animate for timing control |
| Multiple accent colors | Single accent color, consistent meaning |
| Mixed font families | One family, vary size and weight |
| Content near edges | Keep within safe margins |
| Reading the slide aloud | Speaker notes add context; slides show structure |
| Showing data without interpretation | State the insight, then show the supporting data |

# Presentation Design Best Practices

Effective presentation design principles applied to manim-slides.
Every design decision serves one goal: the audience perceives information
in exactly the order and emphasis the presenter intends.

---

## Gaze Control

The goal is that 100 out of 100 audience members perceive slide information
in the same sequence, without the presenter saying a word.

### Principles

- Design each slide so that the eye naturally follows a planned path (1 -> 2 -> 3)
- Use font size and weight to express importance and guide scanning order
- Eliminate visual noise that causes the eye to wander
- Large + bold = read first; large + thin = acknowledged but skippable; small = supplementary

### Application in manim-slides

- Control element appearance order with `self.play()` sequencing
- Use `FadeIn`, `Write` to reveal information step by step
- Place the most important element where the eye lands first (center or top-left)
- Use `next_slide()` to gate information: one concept per slide advance

---

## Information Density

### The Rule

One slide, one idea. If a slide cannot be grasped at a glance, it contains too much.

### Why It Matters

- Overloaded slides break gaze control -- the eye has too many targets
- Audiences who fail to absorb a slide start "skimming" all subsequent slides
- This judgment often happens within the first 3 minutes of the presentation

### Application in manim-slides

- Limit each slide to a single text block or a single diagram
- Split complex content across multiple slides with `next_slide()` between stages
- Use progressive disclosure animations instead of showing a finished diagram
- Judge by "can I understand this in under 2 seconds?" not by line count

---

## Color Philosophy

### Monochrome First

- Design everything in black and white (or a single neutral palette) first
- A great presentation works even without any color
- Color recognition is cognitively expensive and scatters attention

### Accent Color Rules

| Rule | Description |
|------|-------------|
| One color only | Use at most 1 accent color across the entire presentation |
| Consistent meaning | The accent color always signals the same thing (e.g., "key point") |
| Avoid corporate defaults | Familiar colors lose their attention-grabbing effect |

### Recommended: Apple HIG Dark Mode Palette

For dark-background presentations, use Apple Human Interface Guidelines system colors
for reliable contrast and readability:

```python
# Apple HIG Dark Mode カラーパレット
ACCENT = "#0A84FF"          # systemBlue (Dark)
TEXT_PRIMARY = "#FFFFFF"     # label — use for ALL readable text
TEXT_SECONDARY = "#8E8E93"   # systemGray — decorative/structural only
TEXT_TERTIARY = "#636366"    # systemGray2 — slide numbers, subtle labels
BG_COLOR = "#1C1C1E"        # secondarySystemBackground
HIG_GREEN = "#30D158"        # systemGreen — success indicators
HIG_YELLOW = "#FFD60A"       # systemYellow — warnings/highlights
HIG_RED = "#FF453A"          # systemRed — errors/close buttons
```

### Critical: Text Color Hierarchy on Dark Backgrounds

| Use case | Color | Rationale |
|----------|-------|-----------|
| All body text, labels, descriptions | `TEXT_PRIMARY` (white) | Must be readable without effort |
| Box borders, code comments, structural lines | `TEXT_SECONDARY` (gray) | Not meant to be read as prose |
| Slide numbers, step labels only | `TEXT_TERTIARY` (dark gray) | Minimal decorative role |
| Key terms, commands, emphasis | `ACCENT` (blue) | Draws attention intentionally |

**Common mistake:** Using `TEXT_SECONDARY` for body text. Gray text (#8E8E93) on
dark backgrounds (#1C1C1E) has a contrast ratio of only ~4.9:1 — barely WCAG AA.
It becomes effectively unreadable on projected screens. **Default to white for
any text the audience needs to read.**

### Application in manim-slides

```python
# Define once, use everywhere
ACCENT = "#0A84FF"  # single accent color (Apple systemBlue Dark)

# Base palette: white text on dark background
title.set_color(TEXT_PRIMARY)    # WHITE — always readable
body.set_color(TEXT_PRIMARY)     # WHITE — audiences must read this
comment.set_color(TEXT_SECONDARY) # gray — only for non-essential decoration

# Accent only for emphasis
key_term.set_color(ACCENT)
```

- Set background and text as a high-contrast pair (white on near-black)
- **Use white (`TEXT_PRIMARY`) for ALL text the audience needs to read**
- Reserve gray (`TEXT_SECONDARY`) only for decorative elements (box borders, code comments)
- Reserve the accent color strictly for elements that must stand out
- Never use more than one hue for emphasis

---

## Font Strategy

### Selection Criteria

- For Japanese text: choose a font with uniform density (even grey-tone across characters)
- Prioritize font families that offer many weight variations (light through bold)
- For Latin text: standard sans-serif fonts naturally form uniform "blocks"

### The "Block" Theory

- When characters have uniform density and lighter weight, the brain perceives text
  as a single block (object) rather than individual characters
- This lets the audience grasp structure first, then read details
- Achieve this by: larger size + thinner weight for section-level text

### Information Hierarchy via Size and Weight

| Level | Size | Weight | Role |
|-------|------|--------|------|
| Primary | Large | Bold | Core message -- read first |
| Secondary | Large | Light/Thin | Important context -- glanced then skipped |
| Tertiary | Small | Regular | Supporting detail -- read last |

### Rules

- **One font family per presentation** -- mixing fonts creates cognitive friction
- English labels (phase names, strategy titles) in all-caps or all-lowercase to
  make them function as visual objects rather than readable text
- Use at least 3 levels of size/weight hierarchy

### Application in manim-slides

```python
# Consistent font family
Text("Main Point", font_size=48, weight=BOLD)
Text("Supporting detail", font_size=28, weight=LIGHT)
```

---

## Logical Structure: Pyramid Principle

### The Rule

Place the conclusion at the top; stack supporting reasons below.

- Present the conclusion within the first 10% of slides
- Decision-makers want the answer first: concrete, essential, immediate
- 99% of presentations are "trapezoids" -- the top (conclusion) is missing

### Structure

```
        [ Conclusion ]          <-- slide 1-2
       /              \
   [Reason A]    [Reason B]     <-- slides 3-6
   /        \    /        \
[Detail] [Detail] [Detail] [Detail]  <-- remaining slides
```

### Reference

- *The Pyramid Principle* (Barbara Minto)

### Application in manim-slides

- Open with a title slide, then immediately state the conclusion
- Follow with reason slides (aim for ~3 reasons)
- Each section also starts with its own mini-conclusion before details

---

## Consensus Building: The Staircase Method

Build agreement step by step, alternating between shared ground and new proposals.

### Process

1. **Start with undeniable facts** -- "We are on day 35 of the project"
2. **Establish agreement habit** -- stack several agreed-upon points early
3. **Step up** -- introduce a new idea after each agreement plateau
4. **Support each step** -- provide ~3 reasons for every new proposal
5. **Repeat** -- agree -> step up -> agree -> step up
6. **Self-sustaining** -- after 3-4 steps, the audience expects to agree

### Combining with the Pyramid

- Pyramid structure (conclusion first) and Staircase method (agreement-building) coexist
- Early conclusion establishes direction; agreement steps build buy-in
- Tune the balance based on audience familiarity and receptiveness

### Application in manim-slides

- Begin with slides confirming shared context (facts, prior agreements)
- Before each new proposal slide, insert a brief recap of what was agreed
- After a proposal, follow with a "3 reasons" slide set

---

## Prohibited Practices

| Practice | Why It Is Harmful |
|----------|-------------------|
| Flashy effects (flying text, explosions) | Transfers control from presenter to machine; audience disengages |
| Information overload per slide | Breaks gaze control; triggers skimming behavior |
| Multiple font families | Creates cognitive friction from visual inconsistency |
| Excessive color use | Color recognition is expensive; scatters attention |
| Pre-distributing handouts | Destroys gaze control (audience reads ahead) |
| Presenter standing idle during video | Surrenders authority; hard to reclaim attention |

### Application in manim-slides

- Use manim's animation capabilities **only** for progressive disclosure
- Preferred animations: `FadeIn`, `Write`, `Create` (subtle, information-focused)
- Avoid: `SpinInFromNothing`, `ApplyWave`, `GrowFromCenter` without clear purpose
- The purpose of every animation is "control when information appears," never "impress"

---

## Animation Pitfalls

### SurroundingRectangle Does Not Follow Movement

`SurroundingRectangle` is computed at creation time and **does not track** the
target mobject during animations. If you highlight an element then animate it
moving, the rectangle stays in place and the element "breaks through" the frame.

**Wrong:**
```python
highlight = SurroundingRectangle(bar)
self.play(Create(highlight))
self.play(bar.animate.shift(RIGHT * 2))  # bar moves, highlight stays!
self.play(FadeOut(highlight))
```

**Correct — remove highlight before movement:**
```python
highlight = SurroundingRectangle(bar)
self.play(Create(highlight))
self.play(FadeOut(highlight))           # remove FIRST
self.play(bar.animate.shift(RIGHT * 2)) # then move
```

### Text Inside Boxes — Size and Width Balance

When placing text inside `RoundedRectangle` boxes, always verify that the text
fits within the box boundaries. Manim does not clip overflow.

- **Measure first**: Calculate text width relative to box width before rendering
- **Use smaller font sizes** for longer text strings (18px for terminal commands)
- **Widen the box** if content naturally requires more space
- **Left-align with explicit margin**: Use `align_to()` with a computed left edge
- **Verify with Playwright MCP**: Render → convert to HTML → screenshot each slide

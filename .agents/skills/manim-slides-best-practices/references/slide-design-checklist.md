# Slide Design Checklist

Quick-reference checklist for designing presentations with manim-slides.
Run through each category before finalizing your slides.

---

## 1. Structure & Logic

- [ ] Conclusion appears within the first 10% of total slides
- [ ] Overall structure follows the pyramid: conclusion -> reasons -> details
- [ ] Each section opens with its own mini-conclusion
- [ ] Opening slides establish shared facts for consensus building
- [ ] Every new proposal is supported by ~3 reasons
- [ ] Staircase flow: agree -> step up -> agree -> step up

---

## 2. Visual Design

### Information Density

- [ ] Each slide conveys exactly one idea
- [ ] Any slide can be understood at a glance (under 2 seconds)
- [ ] Complex content is split across multiple slides, not crammed into one
- [ ] No "wall of text" slides

### Color

- [ ] Base design works in monochrome (no color dependency)
- [ ] At most 1 accent color is used across the entire presentation
- [ ] Accent color meaning is consistent (always highlights the same kind of element)
- [ ] No gratuitous color variation between slides

### Font

- [ ] Only 1 font family is used throughout the presentation
- [ ] At least 3 levels of size/weight hierarchy exist (primary, secondary, tertiary)
- [ ] English labels use uniform casing (all-caps or all-lowercase)
- [ ] Japanese text uses a font with even character density

### Layout

- [ ] Eye flow path is intentional on every slide (1 -> 2 -> 3)
- [ ] Important elements are positioned where the eye lands first
- [ ] No visual clutter or decorative elements that do not encode information
- [ ] Consistent margins and alignment across all slides

---

## 3. Animation & Transitions

### Progressive Disclosure

- [ ] Information appears in stages, not all at once
- [ ] Appearance order matches the intended reading order
- [ ] Each animation step adds exactly one new concept or element

### Effect Discipline

- [ ] Only subtle animations are used: `FadeIn`, `Write`, `Create`, `Transform`
- [ ] No flashy or decorative effects (`SpinInFromNothing`, `ApplyWave`, etc.)
- [ ] Every animation has a clear informational purpose
- [ ] Animation is "timing control," not "visual spectacle"

### Pacing

| Animation Type | Recommended Duration |
|----------------|----------------------|
| Text appearance | 0.5 - 1.5s |
| Diagram build | 1 - 2s |
| Transform / morph | 1 - 2s |
| Pause for reading | 0.5 - 1s |

---

## 4. manim-slides Technical Checks

### Slide Boundaries

- [ ] `self.next_slide()` is placed at every logical pause point
- [ ] First call to `self.next_slide()` appears before any content (title slide gate)
- [ ] No slide contains more than one major concept between `next_slide()` calls
- [ ] Loop slides use `self.next_slide(loop=True)` where continuous animation is needed

### Canvas & Layout

- [ ] Canvas coordinates are used consistently (`UP`, `DOWN`, `LEFT`, `RIGHT`)
- [ ] `VGroup` is used to align and position related elements as a unit
- [ ] `.arrange()`, `.next_to()`, `.align_to()` are used for systematic placement
- [ ] Text and objects do not overlap or extend beyond visible frame edges

### Code Organization

- [ ] One `Slide` subclass per presentation
- [ ] `construct()` method is organized into clear sections (setup, content per slide)
- [ ] Colors and font sizes are defined as constants at the top
- [ ] Reusable elements (headers, dividers) are factored into helper methods

### Export & Rendering

- [ ] Presentation renders without errors: `manim render <file>.py <ClassName>`
- [ ] Slide export works: `manim-slides convert <ClassName> output.html`
- [ ] HTML output is tested in a browser for correct slide transitions
- [ ] Resolution is appropriate for the target display (1920x1080 recommended)

---

## Quick Decision Flowchart

```
Should I add this element to the current slide?

  Is it essential to the one idea on this slide?
    YES -> Add it
    NO  -> Does it support the one idea?
      YES -> Add as tertiary (small, light weight)
      NO  -> Move to a separate slide or remove entirely

Should I animate this?

  Does the animation control when the audience sees information?
    YES -> Use a subtle animation (FadeIn, Write)
    NO  -> Is it a transformation showing a relationship?
      YES -> Use Transform or TransformMatchingTex
      NO  -> Do not animate; place it statically

Should I use color here?

  Is this the single most important element on the slide?
    YES -> Use the accent color
    NO  -> Keep it monochrome
```

---

## Pre-Presentation Final Review

1. Watch the entire presentation from slide 1 to the end
2. On each slide, check: "Where does my eye go first? Is that where it should go?"
3. Count total colors used -- should be 2 (base + accent) at most
4. Count font families used -- should be exactly 1
5. Verify every slide passes the "2-second glance" test
6. Confirm the conclusion appears before slide number `total_slides * 0.1`

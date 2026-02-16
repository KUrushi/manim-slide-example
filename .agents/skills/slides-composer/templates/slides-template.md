# [Presentation Title]

## Overview
- **Topic**: [Core subject]
- **Key Message**: [The single sentence the audience should remember]
- **Target Audience**: [Who they are and what they already know]
- **Setting**: [Conference talk / team meeting / lecture / pitch]
- **Duration**: [X minutes, ~Y slides]
- **Audience Action**: [What the audience should do/think/feel after the presentation]

## Presentation Structure
[2-3 sentences describing the logical flow: conclusion -> reasons -> evidence]

### Pyramid Overview
```
        [ Conclusion ]              <-- slides 1-2
       /              \
   [Reason A]    [Reason B]         <-- slides 3-8
   /        \    /        \
[Detail] [Detail] [Detail] [Detail] <-- remaining slides
```

---

## Slide 1: Title
**Type**: Title slide
**Purpose**: Establish topic and speaker credibility

### Content
- Presentation title (Primary: large, bold)
- Speaker name / affiliation (Tertiary: small)
- Date or event name (Tertiary: small)

### Visual Elements
- [Layout description]
- [Background, styling notes]

### Speaker Notes
[What the presenter says while this slide is shown]

### Technical Notes
- [manim-slides classes/methods to use]
- [Canvas setup if needed]

---

## Slide 2: Conclusion / Key Message
**Type**: Conclusion slide
**Purpose**: State the main takeaway immediately (Pyramid Principle)

### Content
- Key message in one sentence (Primary: large, bold, accent color)
- Brief context or framing (Secondary: medium)

### Visual Elements
- [Layout description]

### Speaker Notes
[Opening statement that hooks the audience and delivers the conclusion]

### Technical Notes
- [Implementation notes]

---

## Slide 3: [Slide Title]
**Type**: [Shared ground / Reason / Detail / Evidence / Transition]
**Purpose**: [What this slide accomplishes]

### Content
- [Single idea expressed on this slide]
- [Supporting element if any]

### Visual Elements
- [Mobjects, diagrams, equations]
- [Progressive disclosure steps]
- [Position/layout]

### Speaker Notes
[Key talking points, tone, timing]

### Technical Notes
- [Specific manim-slides API: next_slide(), Canvas, Wipe, etc.]
- [Animation choices and durations]

---

## Slide 4: [Slide Title]
**Type**: [Type]
**Purpose**: [Purpose]

### Content
- [Content]

### Visual Elements
- [Elements]

### Speaker Notes
[Notes]

### Technical Notes
- [Notes]

---

[Add more slides as needed]

---

## Slide N: Closing
**Type**: Closing slide
**Purpose**: Reinforce the key message and prompt audience action

### Content
- Restate key message (Primary: large, bold)
- Call to action or next step (Secondary: medium)
- Contact info if appropriate (Tertiary: small)

### Visual Elements
- [Layout description]

### Speaker Notes
[Closing remarks, transition to Q&A if applicable]

### Technical Notes
- [Implementation notes]

---

## Design Specification

### Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Background | [e.g., Dark grey] | #111111 | Scene background |
| Text Primary | [e.g., White] | #FFFFFF | Main text, headings |
| Text Secondary | [e.g., Light grey] | #999999 | Supporting text |
| Text Tertiary | [e.g., Medium grey] | #666666 | Labels, captions |
| Accent | [e.g., Blue] | #3B82F6 | Emphasis, key terms (single color only) |

### Font Strategy

| Level | Size | Weight | Role | Example |
|-------|------|--------|------|---------|
| Primary | 48-56 | Bold | Core message | Key statement |
| Secondary | 28-36 | Regular | Supporting info | Explanation text |
| Tertiary | 16-20 | Regular | Supplementary | Labels, section markers |

### Canvas Elements
[Persistent elements across slides, managed by Canvas]
- [e.g., Presentation title in corner (font_size=24)]
- [e.g., Slide number in bottom-right (font_size=20, GREY_B)]

---

## Staircase Flow

Map showing consensus-building progression:

| Slide | Type | Agreement Level |
|-------|------|-----------------|
| 1 | Title | -- |
| 2 | Conclusion | Key message stated |
| 3-4 | Shared ground | "We all agree that..." |
| 5-6 | Reason A | First supporting argument |
| 7-8 | Evidence for A | Concrete proof |
| 9-10 | Reason B | Second supporting argument |
| ... | ... | Building toward full agreement |
| N | Closing | Restate conclusion, call to action |

---

## Transition Plan

### Slide Transitions
- Slide 1 -> 2: [Wipe / FadeOut+FadeIn / Transform]
- Slide 2 -> 3: [Transition type]
- [Continue for all transitions]

### Recurring Elements
- [Elements that persist via Canvas]
- [Visual motifs that provide continuity]

---

## Implementation Order

Suggested order for building slides (accounting for dependencies):

1. **Canvas setup** - Persistent elements (title bar, slide numbers)
2. **Title slide** - Opening
3. **Conclusion slide** - Key message
4. **Content slides** - In presentation order
5. **Closing slide** - Final
6. **Transitions** - Polish connections between slides

### Shared Components
Objects or code that should be defined once and reused:
- [Component 1]: used in Slides X, Y, Z
- [Component 2]: used in Slides A, B

---

## Checklist

Before finalizing the plan:

- [ ] Conclusion appears within the first 10% of slides
- [ ] Each slide conveys exactly one idea
- [ ] Every slide passes the "2-second glance" test
- [ ] At most 1 accent color is used
- [ ] Only 1 font family is used
- [ ] Progressive disclosure is planned (not showing everything at once)
- [ ] Staircase flow builds consensus step by step
- [ ] Animations serve timing control, not spectacle
- [ ] Speaker notes are provided for every slide

---

## Open Questions / Decisions Needed

- [ ] [Question about scope, content, or design direction]
- [ ] [Another decision point]

---

## Reference Material

- [Source material, papers, data]
- [Inspiration presentations]
- [Related resources]

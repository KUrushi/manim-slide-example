---
name: slides-composer
description: |
  Trigger when: (1) User wants to create a presentation or slide deck, (2) User has a vague topic they want to present, (3) User wants to plan a manim-slides presentation, (4) User asks to "compose" or "plan" slides or a talk, (5) User mentions wanting to explain something in a presentation format.

  Transforms vague presentation ideas into detailed slide-by-slide plans (slides.md). Conducts research, asks clarifying questions about audience/purpose/scope, and outputs comprehensive slide specifications ready for implementation with manim-slides.

  Use this BEFORE writing any manim-slides code. This skill plans the presentation; use manim-slides-best-practices for implementation.
---

## Workflow

### Phase 1: Understand the Topic

1. **Research the topic** deeply before asking questions
   - Use web search to understand the core concepts
   - Identify what the audience needs to take away
   - Determine the key message -- the single sentence that summarizes the entire talk
   - Note common misconceptions or objections the audience might have

2. **Identify the core argument**
   - What is the conclusion the audience should reach?
   - What evidence or reasoning supports it?
   - What makes this topic relevant to the audience right now?

### Phase 2: Clarify with User

**IMPORTANT: Always use the `AskUserQuestion` tool** to ask clarifying questions. Do NOT simply list questions in plain text. The `AskUserQuestion` tool provides structured options that make it easier for the user to respond quickly and precisely. Use it whenever you need to:
- Resolve ambiguity about the topic, audience, or scope
- Offer choices between presentation patterns or design approaches
- Confirm assumptions before proceeding to Phase 3

Ask targeted questions (not all at once -- adapt based on responses):

**Audience & Context**
- Who is the audience? (e.g., engineers, executives, students, general public)
- What do they already know about this topic?
- What is the setting? (conference talk, team meeting, lecture, pitch)
- How long is the time slot? (5 min lightning talk, 20 min presentation, 45 min lecture)

**Purpose & Scope**
- What should the audience **do** after this presentation? (decide, learn, agree, act)
- Any specific aspects to emphasize or skip?
- Are there constraints? (must cover X, must not mention Y)

**Style Preferences**
- Color scheme preferences? (default: monochrome + 1 accent)
- Include mathematical content? Diagrams? Code?
- Formality level? (casual team share, formal conference talk)

### Phase 3: Create slides.md

Apply the **Pyramid Principle**: conclusion first, then supporting reasons, then details.
Apply the **Staircase Method**: build consensus step by step (agree -> step up -> agree).

Output a comprehensive `slides.md` file with the structure defined in [templates/slides-template.md](templates/slides-template.md).

**IMPORTANT: Language Requirement**

All slide content in the output `slides.md` MUST be written in **Japanese**. This includes:
- Slide titles and headings
- Body text and bullet points
- Speaker notes
- Diagram labels and captions
- Key messages and conclusions

Only the following may remain in their original language:
- Code snippets and technical identifiers (variable names, CLI commands)
- Proper nouns and brand names where a Japanese translation would be unnatural
- Mathematical notation

This rule applies regardless of the language the user uses to describe their topic. Even if the user provides instructions in English, the generated slide content must be in Japanese.

## Presentation Design Principles

Apply these principles when composing slides:

### Pyramid Principle (Conclusion First)

- Place the conclusion within the first 10% of slides
- Stack supporting reasons below: conclusion -> reasons -> details
- Each section also opens with its own mini-conclusion
- Decision-makers want the answer first: concrete, essential, immediate

### Staircase Method (Build Consensus)

- Start with undeniable facts the audience already agrees with
- Establish an agreement habit with several shared-ground points early
- Introduce new ideas only after agreement plateaus
- Support each new proposal with ~3 reasons
- Repeat: agree -> step up -> agree -> step up

### Gaze Control

- Design each slide so the eye follows a planned path
- Font size and weight express importance and scanning order
- Control element appearance order with animation sequencing
- One concept per slide advance (`next_slide()`)

### Information Density

- One slide, one idea -- if it cannot be grasped in 2 seconds, split it
- Limit each slide to a single text block or a single diagram
- Use progressive disclosure instead of showing everything at once

### Monochrome + 1 Accent

- Design everything in monochrome first
- A great presentation works without color
- Use at most 1 accent color, consistently meaning the same thing

### Font Strategy

- One font family per presentation
- Use size and weight for hierarchy, never mix fonts
- 3 levels: Primary (large+bold), Secondary (large+light), Tertiary (small+regular)

### Animation Discipline

- Animations are for **timing control**, not spectacle
- Preferred: `FadeIn`, `Write`, `Create`, `Transform`
- Forbidden: `SpinInFromNothing`, `ApplyWave`, `GrowFromCenter` without clear purpose
- Every animation answers: "when should the audience see this?"

## References

- [references/presentation-patterns.md](references/presentation-patterns.md) - Common presentation structures and narrative patterns
- [references/slide-techniques.md](references/slide-techniques.md) - Effective slide design techniques
- [references/slide-examples.md](references/slide-examples.md) - Example slides.md excerpts

## Templates

- [templates/slides-template.md](templates/slides-template.md) - Blank slides.md template

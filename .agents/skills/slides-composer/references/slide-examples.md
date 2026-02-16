# Slide Examples

Example slides.md excerpts for common presentation types.

---

## Example 1: Technical Proposal (Pyramid Pattern)

### Overview
- **Topic**: Migrating from REST to GraphQL
- **Key Message**: GraphQL reduces frontend development time by 40% for our use case
- **Target Audience**: Engineering team leads (know REST, heard of GraphQL)
- **Duration**: 20 minutes, ~15 slides
- **Audience Action**: Approve the migration plan for Q2

### Slide 1: Title
**Type**: Title slide

**Content**
- "GraphQL Migration Proposal" (Primary)
- "Engineering All-Hands / 2024-03" (Tertiary)

**Speaker Notes**
Brief greeting, set context for why this topic is on the agenda.

---

### Slide 2: Conclusion
**Type**: Conclusion slide

**Content**
- "GraphQL cuts our frontend dev time by 40%" (Primary, accent)
- "Based on 3-month pilot with the Dashboard team" (Secondary)

**Speaker Notes**
State the conclusion immediately. "I'll show you the data, but here's the bottom line."

---

### Slide 3: Shared Ground
**Type**: Shared ground (Staircase)

**Content**
- "Current pain: average API integration takes 3 days" (Primary)

**Speaker Notes**
Start with a fact everyone agrees on. "We've all felt this."

---

### Slide 4: Shared Ground
**Type**: Shared ground (Staircase)

**Content**
- "Most time is spent on: over-fetching, multiple endpoints, response shaping" (Secondary)
- Simple diagram: Client -> [3 endpoints] -> Client merges data

**Speaker Notes**
Build agreement. "Sound familiar?"

---

### Slide 5: Step Up - Reason 1
**Type**: Reason

**Content**
- "Single endpoint = single round trip" (Primary)
- Diagram: Client -> [1 GraphQL endpoint] -> Client gets exact shape

**Speaker Notes**
First new idea, supported by the agreed-upon pain point.

---

### Slide 6: Evidence for Reason 1
**Type**: Detail

**Content**
- "Dashboard team: 3 days -> 1.8 days per integration" (Primary, accent)
- Bar chart comparison

**Speaker Notes**
Concrete data supporting the claim.

---

## Example 2: Educational Lecture (Teaching Pattern)

### Overview
- **Topic**: Understanding Big O Notation
- **Key Message**: Big O describes how algorithms scale, not how fast they are
- **Target Audience**: CS students (know basic programming, first algorithms course)
- **Duration**: 30 minutes, ~25 slides
- **Audience Action**: Correctly identify time complexity of simple algorithms

### Slide 1: Title
**Type**: Title slide

**Content**
- "Big O Notation" (Primary)
- "Algorithms 101 / Week 3" (Tertiary)

---

### Slide 2: Hook
**Type**: Hook

**Content**
- "Which is faster?" (Primary)
- Two code snippets side by side (diagram)

**Speaker Notes**
Pose a question that seems obvious but isn't. "Most people get this wrong..."

---

### Slide 3: Intuition
**Type**: Foundation

**Content**
- "Speed depends on input size" (Primary)
- Graph showing two algorithms crossing (diagram)

**Speaker Notes**
"It's not about which is faster today. It's about which is faster as data grows."

---

### Slide 4: Definition
**Type**: Core concept

**Content**
- "O(f(n)) = growth rate as n -> infinity" (Primary)
- MathTex: formal definition (Secondary)

**Speaker Notes**
Introduce the formal notation. Keep it to one definition.

---

### Slide 5: O(1) Example
**Type**: Example

**Content**
- "Array access: always 1 step" (Primary)
- Animation: array with index lookup (diagram)

**Speaker Notes**
Start with the simplest case.

---

### Slide 6: O(n) Example
**Type**: Example

**Content**
- "Linear search: check each element" (Primary)
- Animation: scanning through array (diagram)

**Speaker Notes**
Build up from O(1). "What if we have to check every element?"

---

## Example 3: Lightning Talk (Compressed Pyramid)

### Overview
- **Topic**: Why We Adopted Conventional Commits
- **Key Message**: Conventional commits enabled automated releases and saved 2 hours/week
- **Target Audience**: Developers at a meetup (know git, may not know conventional commits)
- **Duration**: 5 minutes, ~8 slides
- **Audience Action**: Consider adopting conventional commits in their projects

### Slide 1: Title
**Type**: Title slide

**Content**
- "Conventional Commits" (Primary)
- "Lightning Talk / DevMeetup" (Tertiary)

---

### Slide 2: Conclusion
**Type**: Conclusion slide

**Content**
- "Structured commit messages -> automated releases" (Primary, accent)

**Speaker Notes**
Get straight to the point. 5 minutes means no warm-up.

---

### Slide 3: Problem
**Type**: Shared ground

**Content**
- "Release day is painful" (Primary)
- "Manual changelog, version bump, tag, publish" (Secondary)

---

### Slide 4: Solution
**Type**: Reason

**Content**
- `feat: add user auth` (code example, accent)
- `fix: resolve login timeout` (code example)
- "Prefix tells the tool what happened" (Secondary)

---

### Slide 5: Result
**Type**: Evidence

**Content**
- "2 hours/week -> 0" (Primary, accent)
- "semantic-release handles everything" (Secondary)

---

### Slide 6: How to Start
**Type**: Call to action

**Content**
- "1. Install commitlint" (Progressive reveal)
- "2. Add husky hook" (Progressive reveal)
- "3. Set up semantic-release" (Progressive reveal)

---

### Slide 7: Closing
**Type**: Closing

**Content**
- "Structure your commits. Automate your releases." (Primary, accent)

---

## Design Specification Example

### Color Palette (shared across all examples)

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Background | Dark grey | #111111 | Scene background |
| Text Primary | White | #FFFFFF | Headings, key text |
| Text Secondary | Light grey | #999999 | Supporting text |
| Text Tertiary | Medium grey | #666666 | Labels, dates |
| Accent | Blue | #3B82F6 | Key metrics, emphasis |

### Font Strategy

| Level | Size | Weight | Usage |
|-------|------|--------|-------|
| Primary | 48 | Bold | One idea per slide |
| Secondary | 28 | Regular | Explanation |
| Tertiary | 18 | Regular | Labels, metadata |

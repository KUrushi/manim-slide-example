# Skill Structure Analysis

Existing skills (`manimce-best-practices`, `manim-composer`) from `.agents/skills/` directory analysis.

---

## 1. SKILL.md Structure

### Front Matter (YAML)

Both skills use YAML front matter with two required fields:

```yaml
---
name: <skill-name>       # kebab-case identifier
description: |
  Trigger when: (1) ... (2) ... (3) ...

  <Description of what the skill does.>

  <Scope notes / what it does NOT cover.>
---
```

**Key patterns:**
- `name`: kebab-case, matches directory name
- `description`: Multi-line block scalar (`|`). First paragraph is **trigger conditions** in numbered list. Second paragraph is **what the skill does**. Third paragraph (optional) is **scope exclusions** (NOT for...).
- No `trigger:` or `instructions:` fields. The description itself encodes trigger conditions inline.

### Body (Markdown)

**manimce-best-practices pattern** (Reference/API skill):
1. `## How to use` -- Navigational index linking to all rules
   - Grouped into subsections by category (Core Concepts, Text & Math, etc.)
   - Each entry is a markdown link to a rules file with brief description
2. `## Working Examples` -- Links to example files
3. `## Scene Templates` -- Links to template files
4. `## Quick Reference` -- Inline code snippets for most common patterns
   - Basic Scene Structure (code block)
   - Render Command (code block)
   - Key Differences from alternatives (table)
   - Jupyter Notebook Support
   - Common Pitfalls to Avoid (numbered list)
   - Installation
   - Useful Commands

**manim-composer pattern** (Workflow/Process skill):
1. `## Workflow` -- Step-by-step process
   - Phase 1, Phase 2, Phase 3 with detailed instructions
   - Includes clarifying questions to ask the user
2. `## [Design Principles]` -- Domain-specific guidelines
   - Sub-sections with principles
3. `## References` -- Links to reference files
4. `## Templates` -- Links to template files

### Commonalities
- Both use `##` for top-level sections, `###` for sub-sections
- Both link to sub-files (rules/references/templates/examples) using relative markdown links
- Both include inline code examples in the SKILL.md itself as quick references

---

## 2. rules/ vs references/ Usage

### rules/ (manimce-best-practices)

**Purpose:** API reference and "how to use" documentation for specific technical topics.

**Format per file:**
```yaml
---
name: <topic>
description: <one-line description>
metadata:
  tags: <comma-separated tags>
---
```

**Content structure:**
1. `# <Topic> in Manim` -- Title
2. Brief explanation paragraph
3. Multiple `##` sections organized by sub-topic
4. Each section contains:
   - Explanation text
   - Python code blocks with working examples
   - Parameter documentation
   - Class method listings
5. `## Best Practices` -- Numbered list of dos and don'ts (always at the end)

**Characteristics:**
- 23 rule files covering distinct API areas
- Each file is self-contained for its topic
- Heavy use of code blocks (every concept illustrated with code)
- Files are 80-260 lines each
- Front matter has `metadata.tags` for discoverability
- All examples use `from manim import *` import convention
- Examples typically show a complete Scene class

### references/ (manim-composer)

**Purpose:** Domain knowledge, design patterns, and creative guidance (not API docs).

**Format:** Pure markdown with no front matter.

**Content structure:**
- `narrative-patterns.md`: Narrative structures (6 patterns with structure/examples/hooks)
- `visual-techniques.md`: Visual design principles, animation techniques, layout patterns, color palettes
- `scene-examples.md`: Example scene breakdowns showing the scenes.md format in action

**Characteristics:**
- 3 reference files providing creative/conceptual guidance
- More prose-oriented than rules (less code)
- Contains decision frameworks, not API references
- Uses tables, diagrams (ASCII), and structured lists
- Scene examples demonstrate the output format the skill produces

### Summary: rules/ vs references/
| Aspect | rules/ | references/ |
|--------|--------|-------------|
| Content type | API/technical "how to" | Creative/conceptual guidance |
| Front matter | YAML with name, description, metadata.tags | None |
| Code density | Very high (every concept with code) | Low-medium (selective code snippets) |
| Self-contained | Yes, each file stands alone | Yes, but may cross-reference |
| Ends with | "Best Practices" list | Varies |
| Naming | Topic-based (e.g., `animations.md`) | Purpose-based (e.g., `narrative-patterns.md`) |

---

## 3. examples/ vs templates/ Usage

### examples/ (manimce-best-practices)

**Purpose:** Complete, working code demonstrating common patterns. Learning by example.

**Format:** Python files (.py) with full Scene implementations.

**Content structure per file:**
```python
"""
<Title> for Manim Community

<Description of what this file demonstrates.>
Adapted from 3b1b patterns for ManimCE.

Run with: manim -pql <filename>.py SceneName
"""

from manim import *

class SceneName1(Scene):
    """Docstring explaining what this demonstrates."""
    def construct(self):
        # ... complete implementation
```

**Characteristics:**
- 6 example files covering: basic animations, math visualization, updater patterns, graph plotting, 3D visualization, Lorenz attractor
- Each file contains **multiple Scene classes** (3-10 per file)
- Every scene is **fully functional** (can be rendered directly)
- Include docstrings explaining what each scene demonstrates
- File-level docstring includes the render command
- Files range from ~60 to ~370 lines
- Use external imports when needed (numpy, scipy)
- Demonstrate **patterns** (multiple ways to achieve similar results)

### templates/ (both skills)

**manimce-best-practices templates/ (.py files):**

**Purpose:** Starting points to copy-and-modify. Skeleton code.

**Format:** Python files with commented sections.

```python
"""
<Template Name> for Manim Community

<When to use this template.>

Render: manim -pql your_file.py YourScene
"""

from manim import *

class YourScene(SceneType):
    """
    <Description>.
    Attributes to configure / Inherits from...
    """
    def construct(self):
        # ============================================================
        # SETUP: <description>
        # ============================================================
        ...

        # ============================================================
        # ANIMATION: <description>
        # ============================================================
        ...

        # ============================================================
        # CLEANUP: <description>
        # ============================================================
        ...
```

**Characteristics:**
- 3 template files: basic_scene, camera_scene, threed_scene
- Each is a **single Scene class** (unlike examples which have multiple)
- Uses prominent `# ====` section dividers with phase labels (SETUP, ANIMATION, CLEANUP)
- Class name uses `Your` prefix (e.g., `YourScene`, `YourCameraScene`)
- Contains commented-out optional code (e.g., `# self.camera.background_color = ...`)
- Includes the render command at the bottom as a comment
- Provides docstrings explaining what the parent class provides

**manim-composer templates/ (.md files):**

**Purpose:** Blank document structure to fill in. Output format specification.

**Format:** Markdown template with placeholders.

```markdown
# [Video Title]

## Overview
- **Topic**: [Core mathematical/scientific concept]
- **Hook**: [Opening question...]
...

## Scene 1: [Scene Name]
**Duration**: ~X seconds
...
```

**Characteristics:**
- 1 template file: `scenes-template.md`
- Uses `[placeholder]` notation for values to fill in
- Defines the exact output structure the skill should produce
- Includes all sections with their expected format

### Summary: examples/ vs templates/
| Aspect | examples/ | templates/ |
|--------|-----------|------------|
| Purpose | Learning / demonstration | Starting point for new work |
| Completeness | Fully implemented, runnable | Skeleton with placeholders/comments |
| Scenes per file | Multiple (3-10) | Single |
| Comments | Docstrings, explanatory | Section dividers, TODO-style |
| Naming | Descriptive (basic_animations.py) | Generic (basic_scene.py) |
| File type | .py for code skills, could be .md | .py or .md depending on skill output |

---

## 4. File Format and Style Conventions

### Markdown Files (rules/, references/)
- Front matter: YAML between `---` delimiters (rules only)
- Headings: `#` for title, `##` for sections, `###` for sub-sections
- Code blocks: Triple backtick with language identifier (```python, ```bash, ```ini)
- Lists: `-` for unordered, `1.` for ordered
- Tables: Standard markdown tables with header separator
- Line length: No strict limit, wraps naturally
- File names: kebab-case for multi-word (e.g., `creation-animations.md`, `narrative-patterns.md`)

### Python Files (examples/, templates/)
- Module docstring at top (triple-quote) with title, description, render command
- Class docstring (one-line or brief)
- Import: `from manim import *` always first
- Additional imports: `import numpy as np`, `from scipy.integrate import solve_ivp`
- Class naming: PascalCase
- File naming: snake_case (e.g., `basic_animations.py`, `threed_scene.py`)

### Skill Directory Structure
```
.agents/skills/<skill-name>/
  SKILL.md              # Required: Main skill definition
  rules/                # Optional: API/technical reference files (.md)
  references/           # Optional: Conceptual/creative guidance files (.md)
  examples/             # Optional: Complete working code demos (.py)
  templates/            # Optional: Skeleton/starting-point files (.py or .md)
```

---

## 5. Trigger Condition Patterns

Both skills encode triggers in the `description` field of the YAML front matter.

### manimce-best-practices triggers:
```
Trigger when:
(1) User mentions "manim" or "Manim Community" or "ManimCE"
(2) Code contains `from manim import *`
(3) User runs `manim` CLI commands
(4) Working with Scene, MathTex, Create(), or ManimCE-specific classes
```
- Pattern: keyword matching (tool names, import patterns, class names)
- Scope exclusion: "NOT for ManimGL/3b1b version"

### manim-composer triggers:
```
Trigger when:
(1) User wants to create an educational/explainer video
(2) User has a vague concept they want visualized
(3) User mentions "3b1b style" or "explain like 3Blue1Brown"
(4) User wants to plan a Manim video or animation sequence
(5) User asks to "compose" or "plan" a math/science visualization
```
- Pattern: intent matching (wants to create, has a concept, asks to plan)
- Scope guidance: "Use this BEFORE writing any Manim code"

### Trigger Condition Best Practices
1. Use numbered list format `(1) ... (2) ...`
2. Include both **keyword triggers** (specific terms to match) and **intent triggers** (what the user wants to do)
3. Specify **scope exclusions** when there are related skills that might overlap
4. Specify **ordering guidance** when the skill should be used before/after another skill

---

## 6. Patterns to Follow When Creating New Skills

### Required Files
1. **SKILL.md** with YAML front matter containing:
   - `name`: kebab-case matching directory name
   - `description`: Trigger conditions + skill description + scope notes

### SKILL.md Body Structure
Choose based on skill type:

**For API/Reference skills (like manimce-best-practices):**
1. Navigation index (`## How to use`) linking to all sub-files
2. Working examples links
3. Templates links
4. Quick reference with inline code

**For Workflow/Process skills (like manim-composer):**
1. Workflow phases (`## Workflow`)
2. Design principles/guidelines
3. References links
4. Templates links

### Sub-directories (optional, use as needed)

| Directory | When to use | File format |
|-----------|-------------|-------------|
| `rules/` | API/technical reference topics | .md with YAML front matter (name, description, metadata.tags) |
| `references/` | Creative/conceptual guidance | .md without front matter |
| `examples/` | Complete working demonstrations | .py with module docstring, multiple scenes |
| `templates/` | Starting points for user's work | .py or .md with placeholders and section dividers |

### Rule File Pattern (for rules/)
```yaml
---
name: <topic>
description: <one-line summary>
metadata:
  tags: <tag1>, <tag2>, <tag3>
---

# <Topic> in <Domain>

<Brief explanation.>

## <Sub-topic 1>

<Explanation with code blocks.>

## <Sub-topic 2>

...

## Best Practices

1. **<Practice>** - <Explanation>
2. ...
```

### Example File Pattern (for examples/)
```python
"""
<Topic> Patterns for <Domain>

<Description of what this demonstrates.>

Run with: <command>
"""

from <library> import *

class PatternName1(BaseClass):
    """<What this demonstrates>."""
    def method(self):
        # Complete, runnable implementation
        pass

class PatternName2(BaseClass):
    """<What this demonstrates>."""
    def method(self):
        pass
```

### Template File Pattern (for templates/)
```python
"""
<Template Name> for <Domain>

<When to use this.>

Run: <command>
"""

from <library> import *

class YourClassName(BaseClass):
    """
    <Description>.
    <What the base class provides>.
    """
    def method(self):
        # ============================================================
        # SECTION NAME: Description
        # ============================================================
        pass
```

### General Conventions
1. Keep SKILL.md under ~150 lines (link to sub-files for detail)
2. Each rule/reference file should be self-contained (80-260 lines)
3. Examples should be runnable without modification
4. Templates should be copiable and modifiable
5. Use consistent color conventions within a skill domain
6. End rule files with a "Best Practices" section (4-6 numbered items)
7. Include render/run commands in docstrings and comments
8. File naming: kebab-case for .md, snake_case for .py

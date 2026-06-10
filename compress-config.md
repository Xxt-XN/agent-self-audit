# CLAUDE.md Health Check Configuration

Companion to self-audit SKILL.md Item 1 Full mode. All thresholds, weights, and exclusion lists live here. SKILL.md only references this file. Human-editable — tune to your team's tolerance.

## 1. Dimension Weights

| Dimension | Weight | Description |
|-----------|--------|-------------|
| D1 Section Balance | 25% | max_section_lines / total_lines — one section dominating everything? |
| D2 Structure Granularity | 20% | count of `## ` sections — monolithic blob or proper structure? |
| D3 Prose Density | 25% | prose_lines / qualifying_lines — wall of text vs structured content? |
| D4 Reference Ratio | 15% | lines_with_file_refs / total_lines — does content delegate to rules/memory files? |
| D5 Line Count Modifier | 15% | contextual amplifier — only activates when D1-D4 have structural issues |

## 2. Prose Density Rules

A line is PROSE if ALL are true:
1. Not blank
2. Not inside a code block (between ``` markers)
3. Not a table row (does not match `|.*|` pattern)
4. Not a list item (does not start with `- `, `* `, `+ `, or `\d+\. `)
5. Not a heading (does not start with `#`)
6. Not a horizontal rule (`---`, `***`, `___`)
7. Not a blockquote (does not start with `>`)

prose_density = prose_lines / qualifying_lines, where qualifying_lines = non-blank lines excluding code block content.

Thresholds:
- <= 0.30 → OK (well-structured)
- 0.31-0.50 → WARNING (significant prose)
- > 0.50 → CRITICAL (wall of text)

## 3. D1-D5 Scoring Tables

### D1: Section Balance
| max_section/total | Score |
|-------------------|-------|
| < 0.25 | 0 |
| 0.25-0.40 | 1 |
| > 0.40 | 2 |

### D2: Structure Granularity
| ## section count | Score |
|------------------|-------|
| 5-15 | 0 |
| 3-4 or 16-20 | 1 |
| < 3 or > 20 | 2 |

### D3: Prose Density (worst section)
| prose_density | Score |
|---------------|-------|
| <= 0.30 | 0 |
| 0.31-0.50 | 1 |
| > 0.50 | 2 |

### D4: Reference Ratio
| ref_lines/total | Score |
|------------------|-------|
| > 0.05 | 0 |
| 0.02-0.05 | 1 |
| <= 0.02 | 2 |

### D5: Line Count Modifier
| Condition | Score |
|-----------|-------|
| total_lines < 100 | 0 |
| 100 <= total_lines < 300 AND worst(D1-D4) > 0 | min(1, total_lines/300) |
| total_lines >= 300 AND worst(D1-D4) == 0 | 0 (structural perfection → no penalty) |
| total_lines >= 300 AND worst(D1-D4) >= 1 | 1.5 |

## 4. A-F Grade Boundaries

| Score Range | Grade | Meaning |
|-------------|-------|---------|
| 0.00-0.50 | A | Healthy structure, no action needed |
| 0.51-1.00 | B | Minor issues, monitor |
| 1.01-1.50 | C | Actionable issues, plan fix |
| 1.51-2.00 | D | Serious structural problems |
| > 2.00 | F | Systemic failure, needs immediate refactor |

## 5. Jaccard Dedup Config

Threshold: 0.45

Exclusion list — these section pairs are intentionally related, NOT duplicates:
- "Skill Invocation Strategy (Mandatory)" ↔ "Boss Skill Invocation Protocol (Action Gate)"
- "Three Questions Before Every Action" ↔ "Mandatory Pre-Submit Validation"

## 6. Split/Compress/Merge Priority

| Priority | Rule | Condition |
|----------|------|-----------|
| 1 (FIRST) | Split | Section > 25% of total OR total sections < 4 → Move to rules/<domain>.md |
| 2 | Compress | prose_density > 0.40 for any section → Rewrite tersely |
| 3 | Merge | Section < 15 lines AND shares domain with adjacent → Merge |

Conflict resolution: If Split + Compress both apply → Split first (structural fix), then evaluate split-out file for compression.

## 7. Min-Section Gate

Sections < 15 lines → flag as "fragment section" (F-CMD-004). Suggest merge with adjacent same-domain section.

## 8. Domain Keyword Table

| Domain | Keywords | Target Dir |
|--------|----------|------------|
| Pipeline | pipeline, delegate, gate, solo, dispatch, agent, feilue, moushi, gongjiang, mingjing, yushi, handoff, 希小台 | rules/ |
| Environment | python, node, git, terminal, encoding, PATH, batch, powershell, LibreOffice, OOXML | rules/ |
| Coding Standards | pitfall, coding, edit, write, validation, verify, test, lint, compile | rules/ |
| Process | question, step, checklist, validation, pre-submit, self-check, ritual, session | rules/ |
| Skills | skill, invoke, protocol, mandate, strategy, trigger, SKILL.md | skills/ |
| Config | model, routing, haiku, sonnet, opus, deepseek, language, settings | (keep in CLAUDE.md) |
| Reference | tool, script, merge, ppt, hook, custom, path, rules/ | (keep in CLAUDE.md) |

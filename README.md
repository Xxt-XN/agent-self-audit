# Self-Audit — The Self-Evolving Claude Code Health Check

[中文文档](README_zh.md) | [Install](#quick-start) | [13 Check Items](#13-check-items) | [Self-Evolution Loops](#the-three-self-evolution-loops)

> **The only audit skill that learns from itself.** Detects. Diagnoses. Prescribes. Iterates.

Self-Audit is not just another "run `wc -l` and report" skill. It is a **three-loop self-evolving system**: errors auto-promote to permanent guardrails, stale skills get market comparison with better alternatives, and configuration bloat gets surgical diagnosis with split/compress/merge prescriptions.

- **13 check items** across 2 tiers (Quick < 500 tokens, Full with trend analysis)
- **Auto-bootstrap**: first run on a new machine creates audit infrastructure from scratch
- **Cross-platform**: Git Bash · cmd · PowerShell · macOS · Linux
- **Zero-config**: all paths via `${HOME}`, no setup required
- **280+ GitHub Stars** · **148K+ marketplace reach** · **9 ADRs** · **9 Fitness Functions**

## What Makes It Different

| Other Skills | Self-Audit |
|-------------|------------|
| Detect problems | Detect → Diagnose → Prescribe |
| One-time audit | Trend tracking across audits |
| Static thresholds | **5-dimension health scoring** (balance, granularity, density, references, context) |
| Report and stop | **3-repetition → auto-promote to hard pitfall** |
| Ignore stale skills | **Compare against GitHub marketplace (148K+ stars repo)** |
| Absolute line counts | **Quality-graded scoring** — a 300-line well-structured file scores A, a 150-line wall-of-text scores D |

## Quick Start

```bash
cp -r self-audit ~/.claude/skills/self-audit
quick audit
```

First run auto-creates: `audit-log.md` template, `memory/` directory, `environment.md` placeholder. By the 5th audit, Full mode activates automatically with trend analysis, predictive warnings, and market intelligence.

## Trigger Words

| Mode | Triggers |
|------|----------|
| **Quick** | `quick audit`, `health ping` |
| **Full** | `full audit`, `deep audit`, `weekly audit` |
| **Auto** | `self-optimization`, `config check`, `token efficiency`, `skill management`, `optimize yourself`, `config review`, `系统复盘`, `团队复盘`, `config复盘` |

## The Three Self-Evolution Loops

### Loop 1: Error Evolution (Repetition → Hard Rule)
```
1st occurrence → Suggestion
2nd occurrence → Warning ("if repeated → structural promotion")
3rd occurrence → CRITICAL → auto-written to rules/coding.md as permanent pitfall
```
Same mistake can't happen 3 times. The system hardens itself.

### Loop 2: Skill Evolution (Market Intelligence)
```
Item 13 scans 3 GitHub skill marketplaces (every 24h, cached)
  → 4-dimension scoring (Stars 35% · Recency 30% · Activity 20% · Maintenance 15%)
  → Cross-reference installed skills
  → Recommend better alternatives (F-SKL-004/005) or gap-filling (F-SKL-006)
```
Your skill arsenal evolves without you searching.

### Loop 3: Configuration Evolution (Health Scoring)
```
Item 1 doesn't just count lines — it diagnoses structure:
  D1 Section Balance (25%) · D2 Structure Granularity (20%)
  D3 Prose Density (25%) · D4 Reference Ratio (15%) · D5 Amplifier (15%)
  → A-F grade + split/compress/merge prescription
```
300 lines with good structure? Grade A. 150 lines of wall-of-text? Grade D.

## 13 Check Items

| # | Item | Quick | Full |
|---|------|:-----:|:----:|
| 1 | CLAUDE.md Health | ✅ line count | ✅ 5-dim scoring + split/compress Rx |
| 2 | Skill Health | ✅ count | ✅ duplicates + market comparison |
| 3 | Security | ✅ plaintext keys | ✅ permissions audit |
| 4 | Memory System | ✅ count | ✅ staleness + frontmatter |
| 5 | Model Routing | ✅ tiers | ✅ cost efficiency |
| 6 | Updates | ✅ `npx skills check` | ✅ changelog + priority |
| 7 | Skill Utilization | — | ✅ usage vs install |
| 8 | Archive Recovery | — | ✅ restoration candidates |
| 9 | Yushi Audit Quality | — | ✅ agent compliance spot-check |
| 10 | Environment | ✅ 4 atomic (disk/RAM/LO/encoding) | ✅ 8 tools + 7 pkgs + network + baseline |
| 11 | Solo Ratio | — | ✅ pipeline compliance |
| 12 | Skill Violations | — | ✅ F-SKP- repetition tracking |
| 13 | Market Intelligence | — | ✅ GitHub API skill market scan |

## Five-Type Finding Taxonomy

| Tag | Meaning |
|-----|---------|
| **Correction** | Defect needing immediate fix (broken symlink, plaintext key) |
| **Repetition** | Same Finding ID appeared in prior audit (tracked for promotion) |
| **Role Redirect** | Work done by wrong agent (Boss editing code directly) |
| **Frustration Escalation** | User had to ask > 1 time for same thing |
| **Workaround** | Ad-hoc fix that should be structural |

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Executable prompt (290 lines, ≤ 300 F4 constraint) |
| `bootstrap.md` | Platform detection, command mapping, writability check, first-run init |
| `environment-checks.md` | Item 10 companion — Quick commands, Full toolchain/network/baseline |
| `market-intelligence.md` | Item 13 companion — GitHub API market scan, scoring algorithm |
| `compress-config.md` | Item 1 companion — 5-dimension health scoring config, human-tunable thresholds |
| `DESIGN.md` | 9 ADRs, 9 Fitness Functions, data flow diagram |
| `README.md` | This file |
| `README_zh.md` | Chinese version |

## Configuration

None required. All paths resolve via `${HOME}`. T1 degradation (read-only filesystem) supported. T2 diagnostic mode (HOME inaccessible) available.

## Requirements

- Claude Code CLI
- At least one of: Git Bash, cmd, PowerShell, or Python
- Quick mode: zero external dependencies
- Item 13 (Market Intelligence): `gh` CLI authenticated

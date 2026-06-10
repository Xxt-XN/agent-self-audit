# Self-Audit — The Self-Evolving Agent Health Check

[中文文档](README_zh.md) | [Install](INSTALL.md) | [13 Checks](#13-check-items) | [Evolution Loops](#the-three-self-evolution-loops) | [Supported Tools](#supported-tools)

> **The only audit skill that learns from itself.** Detects → Diagnoses → Prescribes → Iterates.

Your agent configuration rots silently. Rules files bloat week by week. Skills pile up unused. Security settings drift. Environment tools go missing. Self-Audit catches all of it — then prescribes exactly what to do — then learns from every audit to get smarter.

**Works everywhere the agentskills.io standard is supported.**

---

## What Makes It Different

| Typical Audit Skills | Self-Audit |
|---------------------|------------|
| Count lines and report | **5-dimension health scoring** — a 300-line well-structured file scores A, a 150-line wall-of-text scores D |
| Detect problems, stop | **Detect → Diagnose → Prescribe** — split/compress/merge instructions |
| Run once and forget | **Trend tracking across audits** — growth rates, predictive warnings |
| Static thresholds | **Contextual scoring** — line count is an amplifier, never a false positive |
| Ignore stale tools | **Market intelligence** — scans GitHub skill marketplaces for better alternatives |
| Report and wait | **3-repetition auto-promotion** — recurring issues become permanent guardrails |

---

## The Three Self-Evolution Loops

### Loop 1: Error → Hard Rule
```
1st occurrence → Suggestion
2nd occurrence → Warning ("if repeated → structural promotion")
3rd occurrence → CRITICAL → auto-written as permanent pitfall
```
Same mistake can't happen three times. The system hardens itself.

### Loop 2: Skills → Market Comparison
```
Every 24h: scan 3 GitHub skill marketplaces (148K+ stars of data)
  → Score repos: Stars 35% · Recency 30% · Activity 20% · Maintenance 15%
  → Cross-reference installed skills against market alternatives
  → Recommend upgrades and gap-fills
```
Your skill arsenal evolves without you searching.

### Loop 3: Configuration → Health Prescription
```
Parse every section · track growth · detect duplication (Jaccard 0.45)
  → 5-dimension grade: Balance · Granularity · Density · References · Amplifier
  → Specific Rx: "Move lines 20–76 to rules/environment.md" (not just "your file is too long")
```
Heavy configurations diagnosed surgically.

---

## 13 Check Items

| # | What It Checks | Quick | Full |
|---|---------------|:-----:|:----:|
| 1 | Configuration Health | ✅ line count | ✅ 5-dim scoring + split/compress Rx |
| 2 | Skill Inventory | ✅ count | ✅ duplicates + market comparison |
| 3 | Security | ✅ plaintext keys | ✅ permissions audit |
| 4 | Memory System | ✅ count | ✅ staleness + structure |
| 5 | Model Routing | ✅ tiers | ✅ cost efficiency |
| 6 | Updates Available | ✅ `npx skills check` | ✅ changelog + priority |
| 7 | Skill Utilization | — | ✅ usage rates vs install count |
| 8 | Archive Recovery | — | ✅ restoration candidates |
| 9 | Agent Audit Quality | — | ✅ compliance spot-checks |
| 10 | Environment | ✅ 4 atomic checks | ✅ 8 tools + 7 pkgs + network + baseline |
| 11 | Solo Work Ratio | — | ✅ pipeline compliance |
| 12 | Skill Violations | — | ✅ repetition tracking |
| 13 | Market Intelligence | — | ✅ GitHub marketplace scan every 24h |

---

## Zero to Full Audit — Automatic

```
First run: auto-creates audit-log.md, memory/ directory, environment.md placeholder
Second run: tracks deltas from first snapshot
Third run: partial trends available
Fifth run: Full mode activates — trends + predictions + market intelligence all online
```

No config. No setup. Every run unlocks more capability.

---

## Supported Tools

Self-Audit follows the [agentskills.io](https://agentskills.io) standard. Installation is a single folder copy.

| Tool | Install Path | Trigger |
|------|-------------|---------|
| Claude Code | `~/.claude/skills/self-audit/` | `quick audit` |
| Codex CLI | `~/.codex/skills/self-audit/` | `$self-audit quick audit` |
| Cursor | `~/.cursor/skills/self-audit/` | Smart match (say `quick audit`) |
| Windsurf | `~/.codeium/windsurf/skills/self-audit/` | Cascade auto-match |
| Gemini CLI | `~/.gemini/skills/self-audit/` | Smart match |

See [INSTALL.md](INSTALL.md) for one-command install per tool.

---

## Two Tiers

| | Quick | Full |
|---|-------|------|
| Check items | 1-6 + Item 10-Quick | All 13 |
| Token cost | < 500 | ~2000-4000 |
| Environment | 4 atomic (disk/RAM/LO/encoding) | Full toolchain + network + baseline |
| Trends & predictions | No | Yes |
| Market intelligence | No | Yes (24h cached) |
| Activates | Any trigger, < 5 prior audits | `full audit` or ≥ 5 prior audits |

---

## Finding Taxonomy

Every issue gets a permanent ID tracked across audits:

| Type | What It Means |
|------|---------------|
| **Correction** | Broken symlink, plaintext key, missing tool — fix now |
| **Repetition** | Same ID appeared before — tracked for 3-strike promotion |
| **Role Redirect** | Wrong agent doing the work — pipeline violation |
| **Frustration Escalation** | User asked for this twice — process gap |
| **Workaround** | Ad-hoc patch that needs structural fix |

---

## Edge Cases Handled

- **New machine, zero config**: Bootstraps entire audit infrastructure from scratch
- **Read-only filesystem**: Degrades to T1 mode (Quick only, no file writes, diagnostic notice)
- **No HOME access**: Terminates cleanly with `insufficient-context` message
- **Windows cmd.exe**: Auto-detects platform, maps `wc -l` → `find /c /v`, `grep` → `findstr`
- **No GitHub auth**: Item 13 skips gracefully, rest of audit runs
- **No Python**: Quick mode uses pure shell; only Full mode toolchain checks need Python

---

## Files

| File | Role |
|------|------|
| `SKILL.md` | Executable prompt (290 lines) |
| `bootstrap.md` | Platform detection, degradation tiers, first-run init |
| `environment-checks.md` | Item 10 — toolchain, packages, network, baseline |
| `market-intelligence.md` | Item 13 — GitHub marketplace scan, scoring algorithm |
| `compress-config.md` | Item 1 — health scoring weights, thresholds (human-tunable) |
| `DESIGN.md` | 9 ADRs, 9 fitness functions, data flow |
| `README.md` | You are here |
| `README_zh.md` | Chinese docs |
| `INSTALL.md` | Per-tool install commands |

---

## Quick Start

```bash
git clone https://github.com/Xxt-XN/claude-code-self-audit.git
cp -r claude-code-self-audit ~/.claude/skills/self-audit   # or your tool's path
quick audit
```

First run bootstraps everything. Fifth run unlocks Full mode with trends, predictions, and market intelligence.

---

<br>
<div align="center">
<strong>Evolve your agent configuration. One audit at a time.</strong>
</div>

# Self-Audit

Agent configuration health checks for AI code assistants. Detects bloat, drift, security issues, and skill gaps — then prescribes fixes.

[中文文档](README_zh.md) | [Install](INSTALL.md)

## Install

**Claude Code:**

```bash
git clone https://github.com/Xxt-XN/agent-self-audit.git ~/.claude/skills/self-audit
```

Trigger with `quick audit` or `/self-audit`. First run bootstraps everything. Full mode unlocks after 5 audits.

**Other tools** (agentskills.io standard):

| Tool | Install Path | Trigger |
|------|-------------|---------|
| Codex CLI | `~/.codex/skills/self-audit/` | `$self-audit quick audit` |
| Cursor | `~/.cursor/skills/self-audit/` | Say `quick audit` |
| Windsurf | `~/.codeium/windsurf/skills/self-audit/` | Cascade auto-match |
| Gemini CLI | `~/.gemini/skills/self-audit/` | Say `quick audit` |

See [INSTALL.md](INSTALL.md) for details.

## Usage

Two tiers:

| | Quick | Full |
|---|-------|------|
| Check items | 1-6 + Item 10-Quick | All 13 |
| Token cost | < 500 | ~2000-4000 |
| Environment | 4 atomic checks | Full toolchain + network + baseline |
| Trends & predictions | No | Yes |
| Market intelligence | No | Yes (24h cached) |
| Activates | Any trigger, < 5 prior audits | `full audit` or >= 5 prior audits |

Audits auto-escalate. After 3 runs, trends become available. After 5, Full mode activates with predictions and market intelligence. No config required.

## 13 Check Items

| # | Check | Quick | Full |
|---|-------|:-----:|:----:|
| 1 | Configuration Health | line count | 5-dim scoring + split/compress Rx |
| 2 | Skill Inventory | count | duplicates + market comparison |
| 3 | Security | plaintext keys | permissions audit |
| 4 | Memory System | count | staleness + structure |
| 5 | Model Routing | tiers | cost efficiency |
| 6 | Updates Available | `npx skills check` | changelog + priority |
| 7 | Skill Utilization | — | usage rates vs install count |
| 8 | Archive Recovery | — | restoration candidates |
| 9 | Agent Audit Quality | — | compliance spot-checks |
| 10 | Environment | 4 atomic checks | 8 tools + 7 pkgs + network + baseline |
| 11 | Solo Work Ratio | — | pipeline compliance |
| 12 | Skill Violations | — | repetition tracking |
| 13 | Market Intelligence | — | GitHub marketplace scan every 24h |

## Finding Taxonomy

Every issue gets a permanent ID tracked across audits:

| Type | Meaning |
|------|---------|
| Correction | Broken symlink, plaintext key, missing tool — fix now |
| Repetition | Same ID appeared before — tracked for 3-strike promotion |
| Role Redirect | Wrong agent doing the work — pipeline violation |
| Frustration Escalation | User asked twice — process gap |
| Workaround | Ad-hoc patch needing structural fix |

Issues self-escalate: first occurrence suggests, second warns, third auto-promotes to a permanent hard rule.

## Files

| File | Role |
|------|------|
| `SKILL.md` | Executable prompt |
| `bootstrap.md` | Platform detection, degradation tiers, first-run init |
| `environment-checks.md` | Toolchain, packages, network, baseline |
| `market-intelligence.md` | GitHub marketplace scan and scoring |
| `compress-config.md` | Health scoring weights and thresholds |
| `DESIGN.md` | 10 ADRs, 10 fitness functions, data flow |
| `README.md` | You are here |
| `README_zh.md` | Chinese documentation |
| `anti-hallucination-gate.md` | Anti-hallucination gate for findings |
| `INSTALL.md` | Per-tool install commands |

---

[中文文档](README_zh.md) — Full Chinese documentation

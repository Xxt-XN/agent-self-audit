---
name: self-audit
description: "AI coding assistant health check and configuration audit. Detects bloat, drift, security issues, skill gaps, and pipeline violations. Quick mode (6+1 items, under 500 tokens) or Full mode (13 items with trend analysis, predictive warnings, and market intelligence). Use for: system health check, config audit, diagnostic, drift detection, compliance review, self-optimization. 用于：系统健康检查、配置审计、诊断、漂移检测、合规审查、自我优化。"
triggers: "quick audit, full audit, deep audit, weekly audit, health check, system check, run audit, audit config, audit system, check config, check my config, config check, config review, check setup, check health, check my setup, diagnose, diagnostic, drift check, drift detection, self audit, self check, self optimization, optimize yourself, self optimize, skill management, skill check, check skills, token efficiency, compliance check, pipeline audit, health ping, 快速审计, 完整审计, 深度审计, 每周审计, 健康检查, 系统检查, 运行审计, 审计配置, 配置检查, 检查配置, 系统复盘, 团队复盘, config复盘, 自检, 自我审计, 诊断, 状态检查, 漂移检测, 合规审查, 自我优化, 技能管理, 令牌效率"
---

## Bootstrap (pre-flight)

Before running any checks, execute the bootstrap sequence. Read `~/.claude/skills/self-audit/bootstrap.md` for platform detection, command mapping, writability check, and first-run initialization. On T2 termination or T1 degradation, adjust audit mode accordingly before proceeding.

# Self Audit v2

## Mode Selection

**0. Self-Audit Integrity.** Run `wc -l ~/.claude/skills/self-audit/SKILL.md`. If >300 lines → WARNING: self-audit SKILL.md itself exceeds limit. Report as F-SLF-001.

When self-audit is invoked, determine mode by checking trigger words AND prior audit count:

| Trigger Words | Prior Audits | Mode |
|---------------|-------------|------|
| quick audit / health ping | any | Quick |
| full audit / deep audit / weekly audit | any | Full |
| self-optimization / config check / token efficiency / skill management / optimize yourself / config review | <3 total prior audits | Quick |
| self-optimization / config check / token efficiency / skill management / optimize yourself / config review | >=3 total prior audits | Full |
| no explicit mode word | <5 prior audits | Quick |
| no explicit mode word | >=5 prior audits | Full |

To determine prior audit count, read `~/.claude/memory/audit-log.md` and count lines matching "| <date> |" format under the "## Pipeline Run Log" section.

**Quick mode**: items 1-6 + item 10-Quick (4 atomic env checks). **Full mode**: items 1-13 + trend analysis + predictive warnings.

## Anti-Hallucination Gate

Read `~/.claude/skills/self-audit/anti-hallucination-gate.md` before emitting ANY finding. All 4 gates (AH-1 through AH-4) must pass. Failure = suppress the finding.

## Agent Roles
Boss (协调/决策/视觉审查) · Yushi (流程合规督查) · Gongjiang (代码/文档生成)
Full roster & collaboration modes: `~/.claude/rules/team.md`

## Dynamic Paths

Resolve `~` at runtime. Core paths (full list in bootstrap.md Section 4):
- Main config: `~/.claude/CLAUDE.md`, `~/.claude/settings.json`
- Rules: `~/.claude/rules/coding.md`, `~/.claude/rules/team.md`, `~/.claude/rules/pitfalls-archive.md`
- Memory: `~/.claude/memory/` (audit-log, environment, skill-usage-inventory, .archive/)
- Agents: `~/.claude/agents/yushi.md`
- Skills: `~/.claude/skills/`, `~/.agents/skills/`

## Overall Grade
Computed from worst finding across all items. ACCEPTED findings excluded.
| Grade | Condition |
|-------|-----------|
| A | 0 Critical, 0 Warning. All items OK or N/A. |
| B | 0 Critical, 1-2 Warnings. Minor issues, no systemic risk. |
| C | 1 Critical OR 3+ Warnings. |
| D | 2-3 Critical. Multiple serious issues. |
| F | 4+ Critical, OR any item FAIL, OR F-SLF-001. Systemic failure. |

## Baseline Load

Before running checks, read audit-log entries. Branch by count:
- **0 entries**: Bootstrap. Output 'No prior audits. Trends unavailable.' Set growth rates to 0.
- **1-2 entries**: Partial trend. Compute from available entries. Flag limited sample.
- **3+ entries**: Full trend. Compute (current - previous_avg) / previous_avg. Flag if any metric grew >10% per audit.

Extract: CLAUDE.md line count, total skill count, Critical/Warning/Suggestion counts from each entry.

## Five-Type Taxonomy

Every finding MUST carry exactly one taxonomy tag AND one Finding ID. This enables structured trend analysis and reliable repetition detection across audits.

| Tag | Meaning | Example |
|-----|---------|---------|
| Correction | Defect that needs immediate fix | Broken symlink, missing file, API key plaintext |
| Repetition | Same Finding ID appeared in prior audit | CLAUDE.md growing same section as last audit |
| Role Redirect | Work done by wrong agent/role | Boss editing code directly, bypassing Gongjiang |
| Frustration Escalation | User had to ask >1 time for same thing | Same request repeated across messages |
| Workaround | Ad-hoc fix that should be structural | copy-paste validation instead of hook |

## Finding ID System

| Check Item | Prefix | IDs |
|------------|--------|-----|
| 1. CLAUDE.md | F-CMD- | 001: exceeding threshold, 002: duplicate content (Jaccard >0.45), 003: compression candidate (prose >0.50), 004: fragment section <15 lines |
| 2. Skill Health | F-SKL- | 001: duplicate across sources, 002: broken symlink, 003: >25 total, 004: stale+better alt exists (Item 13), 005: active+better alt exists (Item 13), 006: skill category gap (Item 13) |
| 3. Security | F-SEC- | 001: plaintext API key, 002: skipDangerousPrompt, 003: unverified plugin |
| 4. Memory | F-MEM- | 001: MEMORY.md >200 lines, 002: missing frontmatter, 003: stale files |
| 5. Model Routing | F-MDL- | 001: identical tiers, 002: outdated model names |
| 6. Updates | F-UPD- | 001: >3 outdated skills, 002: security update, 003: breaking change |
| 7. Skill Utilization | F-USE- | 001: zero-usage >30d, 002: similar skills >2, 003: total >25 |
| 8. Archive | F-ARC- | 001: restore candidate, 002: stale archive |
| 9. Yushi Audit | F-YUS- | 001: spot-check fail, 002: oversight quality decline, 003: missed SKILL VIOLATION |
| 10. Environment | F-ENV- | 001: LibreOffice missing (Quick), 002: encoding conflict (Quick), 003: disk <20GB (Quick), 004: network unreachable (Full), 005: critical pkg missing (Full), 006: RAM <8GB (Quick), 007: stale baseline >90d (Full) |
| 11. Solo Ratio | F-SOL- | 001: ratio >20%, 002: rising trend, 003: >50% critical |
| 12. Skill Violation | F-SKP- | 001: same skill skipped 2+ times, 002: Protocol Gate text missing |
| --. Bootstrap | B- | 001: yushi agent not found (suggestion only, not a finding) |
**Rule**: Every finding MUST include its Finding ID. For repetition, match by ID (e.g., F-MDL-001), not by prose similarity.

## Accepted Exceptions

Some findings are known and deliberately accepted by the user. These should NOT trigger repetition counting or promotion.

Before counting repetitions, read `~/.claude/memory/audit-log.md` and check the "## Accepted Exceptions" table. Skip any finding whose ID appears there.

Users add exceptions by editing audit-log.md directly:
```
| F-SEC-001 | API key plaintext | Accepted 2026-05-16 | User confirmed: not changing |
```

If a finding is in Accepted Exceptions, report it as "ACCEPTED (not counted)" with severity reduced to Suggestion.

## Checks

### 1. CLAUDE.md Size & Trend

**Quick**: `wc -l ~/.claude/CLAUDE.md` — line count only. Do NOT read the file. (~12 tokens)
**Full**: Read companion `~/.claude/skills/self-audit/compress-config.md`. Parse CLAUDE.md sections by `## ` headers. Compute 5-dim health score: D1 Section Balance(25%), D2 Structure Granularity(20%), D3 Prose Density(25%), D4 Reference Ratio(15%), D5 Line Count Modifier(15%). A-F grade per config thresholds. Jaccard dedup check (>=0.45, excl list). Min-section gate (<15 lines → F-CMD-004). 3-audit trend, +30d predict. Emit F-CMD-001~004 per trigger conditions.
| Symptom | Cause | Verify | Fix |
|---------|-------|--------|-----|
| Growth +10-20/wk | Yushi depositing pitfalls | Grep "Pitfall" in CLAUDE.md | caveman-compress; cap at 20 |
| Spike +30+ | New feature/rules added | Grep new "## " headers | Split to domain file under rules/ |
| Jaccard >0.45 (check excl list in config) | Duplicate content | Diff sections | Merge; keep specific version |
| Fragment section <15 lines | Over-granular ## split | Check section count vs total lines | Merge with adjacent same-domain section |

### 2. Skill Health

**Quick**: `ls ~/.claude/skills/ | wc -l` + `ls ~/.agents/skills/ | wc -l`. Count only. Do NOT read lockfile. Do NOT check duplicates. (~15 tokens)
**Full**: Read lockfile. Count enabled/disabled. Stale-skill detection (>60d unused). Overlap analysis between user-level and plugin-provided skills. Taxonomy tag, Finding ID.

### 3. Security Issues

**Quick**: `grep -c "sk-" ~/.claude/settings.json` (plaintext key check) + `grep "skipDangerousModePermissionPrompt" ~/.claude/settings.json` (dangerous mode check). Do NOT read full file. Two-line output. (~30 tokens)
**Full**: Read full settings.json. Plugin source verification. Permission audit. Taxonomy tag, Finding ID.

### 4. Memory System

**Quick**: `ls ~/.claude/memory/ | wc -l` (file count). `wc -l ~/.claude/memory/MEMORY.md` (MEMORY.md size). Do NOT read file contents. (~20 tokens)
**Full**: Read all memory files. Per-file staleness report (>60d). Frontmatter completeness check. Memory-to-pitfall cross-reference. Taxonomy tag, Finding ID.

### 5. Model Routing

**Quick**: `grep "ANTHROPIC_DEFAULT_" ~/.claude/settings.json` — check if 3 tiers are distinct. Do NOT read full file. (~15 tokens)
**Full**: Read full settings. Cost-efficiency analysis. Model allocation optimization suggestions. Taxonomy tag, Finding ID.

### 6. Plugin & Skill Updates

**Quick**: `npx skills check 2>&1 || echo N/A` — count only. Do NOT run update. (~20 tokens)
**Full**: Run full check + update. Per-plugin changelog. Breaking-change warnings. Update priority order. Taxonomy tag, Finding ID.

### 7. Skill Utilization

**Full only** (items 7-11 are Full mode only). Read `~/.claude/memory/skill-usage-inventory.md`. Cross-reference installed skills vs invocation count. Flag skills with 0 usage after 30d, flag >2 similar skills, flag total >25. Add invocation trend (3-audit), per-skill ROI estimate, consolidation recommendations. Taxonomy tag, Finding ID.

| Symptom | Cause | Verify | Fix |
|---------|-------|--------|-----|
| Zero usage after 30d | Wrong domain, never triggered | Check invocation log | Disable or force first use |
| Similar skills >2 | Install without comparison | Compare SKILL.md files | Consolidate |

### 8. Archive Recovery

**Full only**. List `~/.claude/memory/.archive/` (archived memory count). Read `~/.claude/rules/pitfalls-archive.md` (archived pitfalls). Flag archived items recurring in recent conversations. Add restoration candidate report, archive age distribution, cross-reference with active pitfalls. Taxonomy tag, Finding ID.

### 9. Yushi Audit

**Full only**. Pre-check: test -f ~/.claude/agents/yushi.md. If missing → SKIP, queue Bootstrap Suggestion B-001.

Read latest Yushi report from audit-log or conversation history. Randomly pick 3 items Yushi claimed to check. Personally re-verify each item: Did Yushi actually read the required files? Are conclusions consistent with data? Report PASS/FAIL per item.

**Full only**. Spot-check Yushi work quality. If >1 FAIL -> flag as Yushi oversight quality decline. Taxonomy tag.

### 10. Environment Snapshot

**Quick** (4 atomic checks, ~65 tokens): Run inline checks for (a) disk space <20GB → F-ENV-003, (b) RAM <8GB → F-ENV-006, (c) LibreOffice missing → F-ENV-001, (d) PYTHONIOENCODING unset/GBK → F-ENV-002. Use python one-liners for disk/RAM, `test -f` for LibreOffice path, `echo $PYTHONIOENCODING` for encoding. Output: 4-line status. See `~/.claude/skills/self-audit/environment-checks.md` for exact commands.

**Full**: Read `~/.claude/skills/self-audit/environment-checks.md`. Execute: version parsing (8 tools), pip package check (7 packages), network connectivity (read ANTHROPIC_BASE_URL from settings.json → TCP connect), baseline comparison (load environment-baseline.md, diff against current). Flag: F-ENV-001~007 per trigger conditions. Write new snapshot to `~/.claude/memory/environment.md` if tool versions changed or disk/RAM ±20%.

### 11. Solo vs Pipeline Ratio

Scan current session transcript. Count Boss direct Write/Edit calls vs Gongjiang invocations. Compute solo ratio = Boss edits / (Boss edits + Gongjiang invocations).

**Full only**. Report ratio with verdict: PASS (<=20%), WARNING (20-50%), FAIL (>50%). Cross-reference against team.md Gate Check rules.

| Symptom | Cause | Verify | Fix |
|---------|-------|--------|-----|
| Solo ratio >20% | Small tasks degraded to solo | Check transcript for Edit/Write | Enforce gate check |
| Solo ratio rising trend | Pipeline avoidance habit | Compare 3-audit trend | Add PreToolUse hook reminder |

### 12. Yushi F-SKP Cross-Validation (F-YUS-)

**Full only**. Pre-check: test -f ~/.claude/agents/yushi.md. If missing → SKIP (B-001 already queued by Item 9).

**Full only.** Cross-validates Yushi detects SKILL VIOLATION correctly. Does NOT execute promotions.

**Procedure:**
1. Read audit-log.md, scan last 5 Pipeline Run Log entries
2. For each entry with "SKILL VIOLATION" or "skill" in Key Finding → check if Yushi produced F-SKP entry in same run
3. If SKILL VIOLATION present but no Yushi F-SKP entry → F-YUS-003(WARN): "Yushi missed SKILL VIOLATION in run <timestamp>"
4. Do NOT classify violations or execute promotions. This item only validates Yushi detection coverage.

Distinct from Check 9: Check 9 random-spot-checks Yushi's general oversight quality; this check specifically validates SKILL VIOLATION detection coverage.

**Boundary**: F1 gate (Step 3 + Yushi Promotion Review) handles promotion execution. This item only checks coverage.

### 13. Skill Market Intelligence

**Full only**. 24h TTL-gated market scan. Read `~/.claude/skills/self-audit/market-intelligence.md`. Scan 3 skill marketplace repos via GitHub API (`gh api`), score repos (stars 35% + recency 30% + activity 20% + maintenance 15%), cross-reference installed skills vs market. Emit F-SKL-004 (stale+better alt), F-SKL-005 (active+better alt), F-SKL-006 (category gap). Cache results in `~/.claude/memory/skill-market-intelligence.json`. Skip if `gh auth status` fails (no GitHub auth) or network unavailable without cache. Recommendations only — never auto-install.

## Repetition Detection & Structural Promotion

### Load Accepted Exceptions
Read audit-log "## Accepted Exceptions" → build skip-list.
### Match Findings by ID
Match each finding by Finding ID against prior 3 audits. ID in skip-list → ACCEPTED (Suggestion).
### Flag for Promotion (3rd repetition)
1st → Suggestion. 2nd → Warning. 3rd → CRITICAL (PROMOTION PENDING):
```
PROMOTION PENDING: <Finding ID> (<description>) — 3rd repetition on <dates>.
Gate: Yushi → Boss confirm → write to coding.md.
```
Append to audit-log "## Promotion Pending" table. Yushi handles execution; do NOT write directly to coding.md.

## Cross-Item Conflict Detection
1. **CLAUDE.md bloat vs memory starve**: MEM<5 & CLAUDE>150 → content aggregating in CLAUDE.
2. **Skill inflation**: Skills +>3/30d & 0 utilization → install without use. Cap/disable.
3. **Solo + no safety prompt**: Solo >30% & skipDangerous → dangerous autonomy. Require gate-check prompt.

## Output Format

All findings emitted in ONE batched report. No one-at-a-time output.

```
# Self Audit Report --- YYYY-MM-DD HH:MM
**Mode**: [Quick | Full]
**Overall**: [A/B/C/D/F]

## Findings
| # | Item | Rating | Taxonomy | Detail |
|---|------|--------|----------|--------|
| 1 | CLAUDE.md Size | OK/WARN/CRIT | <tag> | <line count> lines, <summary> |
| 2 | Skill Health | ... | ... | ... |
...through item N...
## Trend Summary
- CLAUDE.md: <count>-><count>-><count> (3 audits), direction [growing/stable/shrinking]
- Skills: <count>-><count>-><count>, direction [...]
- Solo ratio: <pct>-><pct>-><pct>, direction [...]
- Critical findings: <count>-><count>-><count>
## Predictive Warnings
[Full mode only] Based on trends, predict issues in next 30d:
- <item>: expected to reach <threshold> by <date> --- pre-emptive fix: <action>
## Structural Promotions
[Show what was promoted, to what rule, written where]
- Before: <finding> appeared in audit N-2, N-1, N as <severity>
- After: promoted to hard pitfall #X in rules/coding.md
- Documented: audit-log.md "## Structural Promotions" table
## Bootstrap Suggestions
[Conditional: appears when yushi.md missing. Provides setup guidance + minimal template path + dismissal instructions. See bootstrap.md Section 6.]
## Managed Items (no longer checked)
[List findings previously promoted. These are now hard rules, not audit items.]
- pitfall #N: <issue> — promoted on <date>
## Cross-Item Conflicts
[If conflicts detected]
- <conflict type>: <detail> -> <resolution>
## Actions Taken
- [List fixes actually executed this run]
```
## Recording

1. Append ONE line to `~/.claude/memory/audit-log.md` under "## Pipeline Run Log":
   ```
   | YYYY-MM-DD HH:MM | self-audit (<mode>) | self-audit | <PASS/FAIL> | <N> findings | <key finding IDs> |
   ```
   Include Finding IDs in the key finding column: e.g., "F-CMD-001(CRIT), F-SEC-001(ACCEPTED)"

2. If environment changed, update `~/.claude/memory/environment.md` with new snapshot.
3. If any 3rd-repetition promotion was FLAGGED (PROMOTION PENDING):
   a. Append to "## Promotion Pending" in audit-log.md (already done in Step 3)
   b. Yushi handles execution (see yushi.md "Promotion Gate")
   c. After Yushi executes, VERIFY pitfall was written to coding.md with grep
4. If any finding was marked ACCEPTED, ensure its Finding ID is in "## Accepted Exceptions" in audit-log.md.
5. If the "## Accepted Exceptions" section does not exist in audit-log.md, create it with header:
   ```
   ## Accepted Exceptions
   | Finding ID | Description | Accepted Date | Reason |
   |------------|-------------|---------------|--------|
   ```

## Handoff

## 希小台 Handoff
- **From**: self-audit
- **To**: Boss
- **Key Output**: Self-audit report with <N> findings
- **File**: tap-comms/handoff/selfaudit-to-boss.md

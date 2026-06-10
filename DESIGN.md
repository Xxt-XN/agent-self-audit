# Self-Audit v2 — Design Reference

## Architecture Decision Records

### ADR-1: Batched Output
**Decision**: All findings emitted in a single aggregate report, not one-at-a-time.
**Rationale**: Streaming individual findings causes token fragmentation and defeats trend analysis. Batched output enables cross-item conflict detection (3 rules), trend comparison against prior audits, and predictive warnings — none of which are possible if items report incrementally.
**Alternatives considered**: Streaming per-item (rejected: no trend visibility, no conflict detection), two-pass (rejected: doubles token cost for no gain).

### ADR-2: Five-Type Taxonomy
**Decision**: Every finding tagged with exactly one of: Correction / Repetition / Role Redirect / Frustration Escalation / Workaround.
**Rationale**: Unlabeled findings accumulate as noise. Taxonomy enables: (a) trend analysis by type, (b) structural promotion of Repetition findings, (c) prioritization (Correction > Repetition > others), (d) Yushi oversight of process quality. Five types was chosen after analysis: too few = meaningless blur, too many = classification overhead.
**Alternatives considered**: Three-type (rejected: conflates Workaround with Correction), seven-type (rejected: classification burden > benefit).

### ADR-3: 3-Repetition Promotion Gate
**Decision**: A finding must appear in 3 distinct audits before auto-promotion to hard pitfall. Not 2, not 5.
**Rationale**: Two occurrences could be coincidence (same corrective action not yet applied). Five is too slow — by then, the issue has caused damage across multiple sessions. Three is the Goldilocks number: enough evidence to confirm it is systemic, early enough to prevent further damage.
**Alternatives considered**: 2-repetition (rejected: false positives from unapplied fixes), 5-repetition (rejected: too slow, damage accumulates).

### ADR-4: Quick/Full Mode Split
**Decision**: Two tiers — Quick (6 items, <500 tokens) and Full (11 items + trends + predictive). Mode selected by trigger word + prior audit count.
**Rationale**: Running all 11 items on every "config check" is wasteful. Quick mode covers the essentials fast. Full mode runs after >=3 prior audits or on explicit "full/deep/weekly" triggers. Prior audit count ensures new users get Quick (fast feedback) while mature users get Full automatically (trend analysis needs baseline data).
**Alternatives considered**: Single-mode always-full (rejected: token waste), three-tier (rejected: unnecessary complexity vs two-tier).

### ADR-5: Dynamic ${HOME} Paths
**Decision**: All file paths use ${HOME} variable, resolved at runtime. No hardcoded user directory paths.
**Rationale**: Hardcoded paths break on any machine change, user rename, or cross-platform use. The ${HOME} convention is natively supported by Claude Code's path resolution and makes the skill portable. This also supports team deployment where home directories differ.
**Alternatives considered**: Hardcoded paths (rejected: fragile), relative paths (rejected: skill context cwd is unpredictable).

## Fitness Functions

These quantitative tests measure self-audit quality over time. Run after every Full audit:

| # | Function | Target | Measurement |
|---|----------|--------|-------------|
| F1 | Finding Repeat Rate | <20% | (findings also in prior audit) / total findings |
| F2 | Predictive Accuracy | >70% | (predictions that materialized) / total predictions, rolling 3-audit window |
| F3 | Token-to-Insight Ratio | <200 tokens per finding | Total audit tokens / count of non-trivial findings |
| F4 | SKILL.md Line Count | <=300 | wc -l of this file |

**F1** measures whether prior fixes actually worked. High repeat rate = fixes are cosmetic, not structural.
**F2** validates the predictive model (Full mode only). If predictions consistently miss, the trend analysis model needs recalibration.
**F3** ensures audit efficiency. If the audit itself becomes a token hog, it defeats the purpose.
| F5 | Bootstrap Degradation Rate | <5% | T1 occurrences / total self-audit runs |
| F6 | Platform Coverage | 3/3 platforms pass | All platforms run Quick mode without unhandled errors |
| F7 | Environment Check Coverage | All 7 F-ENV IDs documented in environment-checks.md | grep -c "F-ENV-00[1-7]" environment-checks.md |
| F8 | SKILL.md Line Budget | <=300 lines after each change | wc -l SKILL.md, fail if >300 |
| F9 | Market Intel Cache Freshness | Cache age <= 48h | Python check on generated_at field |

**F4** is a hard constraint: SKILL.md is a prompt Claude reads every audit, not a reference doc.
**F5** tracks how often self-audit falls back to T1 read-only mode — high rate signals environment configuration issues.
**F6** ensures the platform mapping table is correct — new platform support is verified by actually running Quick mode on that platform.

## Data Flow

```
Trigger word detected
        |
        v
[Bootstrap Interceptor] --- NEW: platform detect, cmd map, writability, first-run init
        |                   T2 termination / T1 force Quick mode
        v
[Mode Selector] --- reads prior audit count from audit-log.md
        |
        v
[Baseline Loader] --- reads 3 most recent audit entries -> metrics + growth rates
        |
        v
[Check Runner] --- Quick: items 1-6 + Item 10-Quick | Full: items 1-13
        |              Each check: Read -> Verify -> Tag (taxonomy) -> Score
        v
[Repetition Detector] --- compare findings vs prior audits -> count repetitions
        |                   1st=Suggestion, 2nd=Warning, 3rd=CRITICAL+auto-promote
        v
[Cross-Item Conflict Detector] --- 3 rules: bloat vs starve, skill inflation, solo+no-safety
        |
        v
[Report Generator] --- single batched output: findings table + trends + predictions + promotions + conflicts
        |
        v
[Recorder] --- append audit-log.md line, update environment.md if changed, record promotions
        |
        v
[Handoff] --- 希小台！self-audit任务结束！
```

## Design Rationale

Self-audit v2 upgrades the original from a flat checklist to a learning system. The key insight: a checklist that finds the same issues every week is a broken checklist. v2 adds:

1. **Memory across audits** — baseline loading + trend analysis means each audit builds on prior ones
2. **Structural learning** — 3-repetition promotion turns recurring findings into permanent guardrails
3. **Cross-cutting visibility** — conflict detection catches systemic problems invisible to per-item checks
4. **Predictive capability** — trend extrapolation warns before thresholds are breached
5. **Self-measurement** — fitness functions quantify whether the audit itself is improving the system

The taxonomy, repetition tracking, and promotion gate together form a closed feedback loop: find -> tag -> track -> promote -> prevent.

### ADR-6: Separated Bootstrap with Multi-Tier Degradation

**Decision**: Bootstrap logic (platform detection, command mapping, writability check, first-run initialization) lives in a separate `bootstrap.md` companion file. SKILL.md references it with 2 lines at the top. Three-tier degradation: T0 (full function), T1 (read-only Quick mode), T2 (terminate with diagnostic).

**Rationale**: Adding bootstrap inline to SKILL.md would push it to ~321 lines, exceeding the F4 fitness constraint of 300 lines. Separation keeps SKILL.md at 291 lines while providing all bootstrap functionality. Three-tier degradation ensures self-audit produces useful output even on read-only filesystems (T1) or provides clear diagnostic when completely inaccessible (T2).

**Alternatives considered**:

| Option | Pros | Cons | Why rejected |
|--------|------|------|-------------|
| Inline all in SKILL.md + raise F4 to 330 | Single file | F4 threshold inflation hides bloat; next feature pushes to 350 | Constraints lose meaning |
| Skip bootstrap, per-check error handling | No new file | Scattered, inconsistent; each check handles 3 platforms independently | Fragile |
| Fail-fast on env issues | Simplest | Unusable on read-only FS; no diagnostic | Self-audit becomes LESS available |
| Drop F4 entirely | Max flexibility | Removes only brake on SKILL.md bloat | F4 is a valid fitness constraint |

**Consequences**: Bootstrap concerns are cleanly separated. F4 constraint remains at 300 lines. T1 degradation allows core checks to run in constrained environments. Two files to maintain (SKILL.md + bootstrap.md) instead of one.

### ADR-7: environment-checks.md Companion File

**Decision**: Environment check logic (Item 10 Quick commands, Full version parsing, network connectivity, baseline lifecycle) lives in a new companion file `environment-checks.md`. SKILL.md Item 10 describes what to check at high level; environment-checks.md contains exact commands, parse patterns, and baseline lifecycle rules. bootstrap.md is NOT modified — environment checks are runtime behavior, not bootstrap gating.

**Rationale**: Adding all environment checks inline to SKILL.md would push it past the 300-line F4 constraint. Placing them in bootstrap.md would violate separation of concerns (bootstrap = can-we-run, environment = what-does-the-system-look-like). ADR-6 already established the companion-file pattern with bootstrap.md. This follows the same pattern for environment.

**Alternatives considered**:

| Option | Pros | Cons | Why rejected |
|--------|------|------|-------------|
| Inline all in SKILL.md | Single file | SKILL.md → ~317 lines, violates F4 (≤300) | F4 is a hard constraint |
| Add to bootstrap.md Section 6 | Fewer new files | Confuses bootstrap (pre-flight gate) with environment (runtime check) | Violates separation of concerns |
| New environment-checks.md (chosen) | Clean separation, F4 compliant, extensible | Three companion files to maintain | Chosen — ADR-6 precedent established |

**Consequences**: Three-file architecture (SKILL + bootstrap + environment-checks). Each has clear responsibility. New environment checks added to environment-checks.md without touching SKILL.md.

### ADR-8: Skill Market Intelligence via GitHub API

**Decision**: Market intelligence data sourced from GitHub API (`gh api`) instead of `npx skills find` (interactive, no structured output). Three skill marketplace repos scanned: anthropics/skills, thatjuan/agent-skills, PeterHdd/agent-skills. 4-dimension weighted scoring: Stars (35%), Recency (30%), Activity (20%), Maintenance (15%). Stars normalized by log10 to prevent single-repo dominance. Results cached in JSON with 24h TTL.

**Rationale**: `npx skills find` is an interactive TUI — no JSON output, no programmatic access to install counts or Stars. GitHub API provides structured JSON with stargazers_count, pushed_at, archived, open_issues_count — all the signals needed for objective market scoring. Log-normalization is critical: without it, anthropics/skills (148K stars) would drown all other signals.

**Alternatives considered**:

| Option | Pros | Cons | Why rejected |
|--------|------|------|-------------|
| `npx skills find` | User-familiar CLI | Interactive TUI, no structured data, no Stars/installs | Scoring pipeline unimplementable |
| Web scraping skills.sh | Could get leaderboard data | CSS selectors fragile, no Stars | Maintenance burden > value |
| GitHub API (chosen) | Structured JSON, Stars/dates/issues, non-interactive | Rate limit 5000/h, requires gh auth | Best available signal source |

**Consequences**: Market intelligence becomes fully automated and auditable. Companion file `market-intelligence.md` + cache `skill-market-intelligence.json` added. Stars replaces installs as popularity proxy (acceptable trade-off: installs data doesn't exist for skills). Three new Finding IDs: F-SKL-004/005/006.

### ADR-9: Multi-Dimensional Health Scoring replaces Absolute Line-Count Thresholds

**Decision**: Replace `<=120 OK / 120-200 WARN / >200 CRIT` hardcoded thresholds with a 5-dimension weighted health scoring system (D1: Section Balance 25%, D2: Structure Granularity 20%, D3: Prose Density 25%, D4: Reference Ratio 15%, D5: Line Count Modifier 15%). Line count alone never triggers CRIT — it amplifies existing structural issues. All thresholds, weights, and rules stored in companion file `compress-config.md`. New Finding ID F-CMD-004 for fragment sections.

**Rationale**: Absolute line-count thresholds are punitive for mature teams where CLAUDE.md naturally grows through accumulated rules and pitfall deposits. A well-structured 300-line file is healthier than a chaotic 150-line file. The old system cannot distinguish between them. User requirement: structural quality should determine health grade, not raw line count. The companion file pattern (ADR-6/7/8) keeps thresholds human-editable without touching SKILL.md.

**Alternatives considered**:

| Option | Pros | Cons | Why rejected |
|--------|------|------|-------------|
| Keep 120/200 with org-flag override | Simple | User explicitly rejected absolute thresholds; manual override compounds maintenance | Does not address user requirement |
| ML-based anomaly detection | Adaptive | Over-engineered for 250-line config; no training data | Complexity budget exceeded |
| 5-dim weighted scoring (chosen) | Quality-graded, no false CRIT on structured growth, human-tunable | More complex than wc -l; companion file maintenance | Chosen — best balance of accuracy and transparency |

**Consequences**: Teams can grow CLAUDE.md naturally. Diagnoses are actionable: "Section X has prose density 0.55, compress it" vs "your file is over 200 lines." Companion config file `compress-config.md` added. ADR-6/7/8/9 now form a consistent companion-file pattern for self-audit extensibility.

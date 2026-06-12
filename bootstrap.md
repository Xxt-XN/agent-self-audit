# Self-Audit Bootstrap

## 1. Platform Detection

Detect shell type and set `SHELL_TYPE`:
- `$BASH_VERSION` non-empty → `bash`
- `$COMSPEC` non-empty AND no bash → `cmd`
- `$PSModulePath` non-empty → `powershell`
- Default → `bash`

## 2. Command Mapping

| Operation | Bash (Git Bash/macOS/Linux) | cmd.exe | PowerShell |
|-----------|---------------------------|---------|------------|
| Line count | `wc -l <file>` | `find /c /v "" <file>` | `(Get-Content <file>).Count` |
| File count | `ls <dir> \| wc -l` | `dir /b <dir> \| find /c /v ""` | `(Get-ChildItem <dir>).Count` |
| Pattern match count | `grep -c <pat> <file>` | `findstr "<pat>" <file> \| find /c /v ""` | `(Select-String <pat> <file>).Count` |
| Pattern search | `grep <pat> <file>` | `findstr "<pat>" <file>` | `Select-String <pat> <file>` |
| Directory create | `mkdir -p <dir>` | `mkdir <dir>` | `New-Item -Force -Type Dir <dir>` |
| Plugin check | `npx skills check` | `npx skills check` | `npx skills check` |

## 3. Writable Check — Degradation Tier

```
1. test -d ~/.claude/memory/ ?
   ├── YES AND test -w ~/.claude/memory/ → T0 (full function)
   ├── YES BUT NOT writable → T1 (Quick mode, no file I/O)
   └── NO → mkdir attempt
            ├── SUCCESS → T0
            └── FAIL → T1
2. test -d ~/.claude/ ?
   └── NO → T2 (terminate: "insufficient-context: Cannot access ~/.claude/")
```

| Tier | Condition | Behavior |
|------|-----------|----------|
| T0 | memory/ exists and writable | Normal Quick/Full audit |
| T1 | memory/ exists but NOT writable, OR mkdir failed | Force Quick mode, skip all file I/O, append Degradation Notice |
| T2 | .claude/ directory inaccessible | Terminate with diagnostic |

## 4. First-Run Initialization (T0 only)

Run only when T0. Each step is atomic (`test -f || create`):

```
1. test -d ~/.claude/memory/ || mkdir -p ~/.claude/memory/
2. test -f ~/.claude/memory/audit-log.md || write audit-log.md template
3. test -f ~/.claude/memory/environment.md || touch environment.md
4. test -f ~/.claude/memory/skill-usage-inventory.md || touch skill-usage-inventory.md
```

For audit-log.md template, write the minimal structure:
```markdown
# Self Audit

## Pipeline Run Log

| Timestamp | Task | Pipeline | Result | Issues | Key Finding |
|-----------|------|----------|--------|--------|-------------|

## Accepted Exceptions
| Finding ID | Description | Accepted Date | Reason |
|------------|-------------|---------------|--------|

## Structural Promotions
| Date | Finding | Promoted To | Repetition History |
|------|---------|-------------|-------------------|
```

## 5. Degradation Notice Template (append to report when T1)

```
## Degradation Notice
**Tier**: T1 — Read-only audit
**Cause**: ~/.claude/memory/ is not writable.
**Effect**: File I/O disabled. Audit results not persisted. Only Quick mode checks 1-6 ran.
**Fix**: Ensure ~/.claude/memory/ is writable, then re-run audit.
```

## 6. Bootstrap Suggestions (Full mode)

Advisory guidance for missing optional components. Never auto-creates — only recommends. Follows Item 13 principle.

### B-001: yushi.md Not Found

**Trigger**: Full mode AND `test -f ~/.claude/agents/yushi.md` returns false.
**Action**: In report, append "## Bootstrap Suggestions" section with:
1. Impact: "Items 9 (Yushi Audit Quality) and 12 (Skill Violation Tracking) were skipped."
2. What Yushi does: "Independent overseer checks team compliance — catches skipped skills, missing handoffs, solo-mode bypasses."
3. How to enable: "Create `~/.claude/agents/yushi.md`. A minimal template is in `~/.claude/agents/yushi-minimal-template.md` — copy it and customize."
4. Dismissal: "To permanently silence this suggestion: add `| B-001 | yushi agent not created | <today> | User declined |` to your audit-log.md under `## Accepted Exceptions`. Or simply create the agent file."
5. Note: "Agent system is optional. This suggestion reappears each Full audit until resolved."

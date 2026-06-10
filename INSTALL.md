# Self-Audit — Installation Guide

Self-Audit follows the [agentskills.io](https://agentskills.io) standard. It works on any AI code assistant that supports the skills protocol.

## One-Line Install (any platform)

```bash
# Clone to your user skills directory, then rename the folder to self-audit
# Replace <TOOL_PATH> with your tool's path from the table below
git clone https://github.com/Xxt-XN/claude-code-self-audit.git ~/self-audit-temp && mkdir -p <TOOL_PATH> && cp -r ~/self-audit-temp/* <TOOL_PATH>/ && rm -rf ~/self-audit-temp
```

## Tool-Specific Paths

| Tool | Install Command |
|------|----------------|
| **Claude Code** | `cp -r self-audit ~/.claude/skills/self-audit` |
| **Codex CLI** | `cp -r self-audit ~/.codex/skills/self-audit` |
| **Cursor** | `cp -r self-audit ~/.cursor/skills/self-audit` |
| **Windsurf** | `cp -r self-audit ~/.codeium/windsurf/skills/self-audit` |
| **Gemini CLI** | `cp -r self-audit ~/.gemini/skills/self-audit` |

## Platform-Specific Notes

### Claude Code
- Trigger: `/self-audit` or say `quick audit`, `full audit`, `weekly audit`
- Skill loaded automatically when trigger word matches

### Codex CLI
- Trigger: `$self-audit` then say `quick audit`
- Codex uses `$` prefix for explicit skill invocation

### Cursor
- Skills in beta as of 2026. Ensure "Agent Skills" feature is enabled
- Trigger: speak naturally — Cursor auto-matches based on skill description

### Windsurf
- Skills managed through Cascade. Place in `.windsurf/skills/` for project-level
- Trigger: speak naturally — Cascade auto-matches

### Gemini CLI
- Experimental skills support. Place in `~/.gemini/skills/`
- Trigger: speak naturally

## Quick Start (after install)

```
quick audit
```

First run auto-creates: `audit-log.md`, `memory/` directory, `environment.md` placeholder.

## Requirements (all platforms)

- Shell access (Git Bash, bash, zsh, cmd, or PowerShell)
- Python 3 (optional — enables advanced checks)
- `gh` CLI (optional — enables Item 13 market intelligence)

## File Structure After Install

```
self-audit/
├── SKILL.md                  ← Main executable prompt
├── bootstrap.md              ← Platform detection, first-run init
├── environment-checks.md     ← Toolchain + network + baseline
├── market-intelligence.md    ← GitHub skill marketplace scan
├── compress-config.md        ← CLAUDE.md health scoring config
├── DESIGN.md                 ← Architecture decisions (9 ADRs)
├── README.md                 ← English docs
└── README_zh.md              ← Chinese docs
```

## Troubleshooting

### "Skill not found" or doesn't trigger
- Ensure the folder is named exactly `self-audit`
- Ensure `SKILL.md` is inside the folder
- Restart your AI tool after installation

### Quick mode works, Full mode SKIPs items
- This is normal on first install. Full mode progressively unlocks after 3+ audits
- Item 13 (market intelligence) requires `gh auth login`

### Shell command errors (Windows)
- Use Git Bash. cmd.exe and PowerShell use different commands
- Self-audit auto-detects platform and maps commands accordingly

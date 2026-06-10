# Skill Market Intelligence

Companion to self-audit SKILL.md Item 13. Full mode only. 24h TTL-gated. Reads 3 skill marketplace repos via GitHub API, scores them, compares against installed skills.

## Data Sources

| # | Repo | Type | Skills Path |
|---|------|------|-------------|
| 1 | anthropics/skills | Official | skills/ |
| 2 | thatjuan/agent-skills | Community | (root -- try skills/ first, fallback to root) |
| 3 | PeterHdd/agent-skills | Community | skills/ |

## Scoring Algorithm (Repo-Level)

Score = 0.35 x stars_norm + 0.30 x recency_norm + 0.20 x activity_norm + 0.15 x maintenance

- **stars_norm**: min(1.0, log10(stars + 1) / log10(max_stars_in_batch + 1))
- **recency_norm**: max(0, 1.0 - days_since_push / 365)
- **activity_norm**: min(1.0, open_issues / 50)
- **maintenance**: archived -> 0, else -> 1.0

## Scan Procedure

1. Read `~/.claude/memory/skill-market-intelligence.json`. If cache exists AND age < 24h -> use cache, skip scan.
2. For each source repo:
   a. `gh api repos/<owner>/<repo> --jq '{stars: .stargazers_count, pushed: .pushed_at, archived: .archived, issues: .open_issues_count}'`
   b. `gh api repos/<owner>/<repo>/contents/skills --jq '.[].name'` (if 404 -> try root: `gh api repos/<owner>/<repo>/contents --jq '.[] | select(.type=="dir" and (.name | startswith(".") | not)) | .name'`)
   c. Wait 200ms between API calls
3. Compute scores per repo.
4. Cross-reference: installed skills (from `~/.claude/skills/` + `~/.agents/skills/`) vs market skills.
5. Emit findings:
   - F-SKL-004 (WARN): installed skill unused >30d AND same-name skill exists in a higher-scored market repo
   - F-SKL-005 (INFO): installed skill is active BUT same-name skill exists in significantly higher-scored repo (score diff >= 0.3)
   - F-SKL-006 (INFO): market category has popular skills (stars >= 100) but team has zero installed in that category
6. Write cache to `~/.claude/memory/skill-market-intelligence.json`.

## Error Handling

| Error | Behavior |
|-------|----------|
| Rate limit < 5 remaining | Skip remaining repos, use cache |
| Network timeout | Use cache if exists, else skip Item 13 |
| Repo 404 | Mark as "not_found", skip |
| Auth failure (`gh auth status` non-zero) | Skip Item 13 entirely |
| Cache parse error | Regenerate from scratch |
| Partial success (N/3 repos fetched) | Use available results + warn |

## Categories for Gap Detection

| Category | Keywords |
|----------|----------|
| document | xlsx, docx, pptx, pdf, markdown |
| frontend | react, vue, html, css, ui, design |
| testing | test, jest, pytest, vitest, playwright |
| security | security, audit, vulnerability |
| devops | deploy, docker, kubernetes, ci-cd |
| data | data, analysis, sql, csv, visualization |
| git | commit, push, pr, branch, git |
| communication | comms, slack, message, internal |

## Cache Format (`skill-market-intelligence.json`)

```json
{
  "generated_at": "ISO8601",
  "ttl_hours": 24,
  "repos": {
    "owner/repo": {
      "stars": 148648,
      "pushed_at": "2026-06-09T20:35:19Z",
      "archived": false,
      "open_issues": 947,
      "score": 0.945,
      "skills": ["xlsx", "docx", "pptx", "pdf", "..."]
    }
  },
  "findings": ["F-SKL-004: ...", "F-SKL-005: ..."]
}
```

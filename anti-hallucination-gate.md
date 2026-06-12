# Anti-Hallucination Gate (AH-GATE)

Invoked before emitting ANY finding in self-audit. If any of the 4 gates fails, suppress the finding and emit NOTHING — do not fabricate evidence, do not guess Finding IDs, do not report from memory.

## AH-1: Source Anchor
- [ ] This finding cites a SPECIFIC read source (file + line range or command output).
- [ ] If the source was NOT read during this audit run -> FAIL. Do not report.

## AH-2: Constraint Check
- [ ] This finding's severity (OK/WARN/CRIT) matches the grading criteria in each check item.
- [ ] This finding's Finding ID exists in the Finding ID System table in SKILL.md. If you cannot find the exact ID -> FAIL. Do not invent IDs.

## AH-3: Mode Boundary
- [ ] Quick mode: finding must come from Items 1-6 or Item 10-Quick. Items 7-13 are out of scope.
- [ ] Full mode: all items in scope. No boundary restriction.
- [ ] If finding violates mode boundary -> FAIL. Do not report.

## AH-4: Falsifiability
- [ ] A reviewer with access to the same files can independently verify this finding.
- [ ] If the finding relies on "what was said in conversation" without a logged transcript -> flag as UNVERIFIABLE, reduce to Suggestion.
- [ ] If the finding is an opinion ("this feels wrong") -> FAIL. Self-audit reports only measurable findings.

## Gate Summary

| Gate | Check | Fail Action |
|------|-------|-------------|
| AH-1 | Source cited and actually read | Suppress finding |
| AH-2 | Severity matches thresholds, ID exists in system | Suppress finding |
| AH-3 | Item scope matches audit mode | Suppress finding |
| AH-4 | Independently verifiable | Downgrade to Suggestion or suppress |

After all items complete, self-check: Count AH-GATE suppressions. If >0, report in Output Format under "## AH-GATE Suppressions" section.

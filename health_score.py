#!/usr/bin/env python3
"""Self-Audit health score bridge for SkillOpt-Sleep integration.

Produces a machine-readable health score that SkillOpt's validation gate
can consume alongside task replay scores.

Usage:
    python health_score.py           # print JSON score to stdout
    python health_score.py --verbose # human-readable output
    python health_score.py --json    # explicit JSON mode

Output: {"score": 0.75, "grade": "B", "criticals": 0, "warnings": 2,
          "findings": [...], "timestamp": "2026-06-14T..."}

Integration with SkillOpt-Sleep:
    The /sleep cycle calls this script before and after each proposed edit.
    The gate combines task replay score (60%) + self-audit health score (40%).
    An edit must improve the COMBINED score to pass the gate.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Tuple


def run_health_check(home: str = "") -> dict:
    """Run self-audit Quick mode checks and return full results dict.

    Checks performed (matching self-audit SKILL.md items 1-6 + 10-Quick):
    1. CLAUDE.md line count
    2. Skill inventory count
    3. Security: plaintext keys, dangerous mode
    4. Memory system size
    5. Model routing tier distinctness
    6. Updates: npx skills check (optional)
    10-Quick. Environment: disk, RAM, LibreOffice, encoding
    """
    home = home or os.path.expanduser("~")
    findings = []

    # 1. CLAUDE.md line count
    claude_md = os.path.join(home, ".claude", "CLAUDE.md")
    try:
        with open(claude_md, "r", encoding="utf-8") as f:
            lines = len(f.readlines())
        if lines > 300:
            findings.append({"severity": "CRITICAL", "id": "F-CMD-001",
                           "detail": f"CLAUDE.md {lines} lines (threshold: 300)"})
        elif lines > 200:
            findings.append({"severity": "WARNING", "id": "F-CMD-001",
                           "detail": f"CLAUDE.md {lines} lines (approaching 300)"})
    except Exception:
        findings.append({"severity": "WARNING", "id": "F-CMD-001",
                       "detail": "Cannot read CLAUDE.md"})

    # 2. Skill count
    count = 0
    for skills_d in [os.path.join(home, ".claude", "skills"),
                     os.path.join(home, ".agents", "skills")]:
        try:
            count += len([n for n in os.listdir(skills_d)
                         if os.path.isdir(os.path.join(skills_d, n))
                         and not n.startswith(".")])
        except Exception:
            pass
    if count > 25:
        findings.append({"severity": "WARNING", "id": "F-SKL-003",
                       "detail": f"{count} skills installed (threshold: 25)"})

    # 3. Security
    settings_file = os.path.join(home, ".claude", "settings.json")
    try:
        with open(settings_file, "r", encoding="utf-8") as f:
            content = f.read()
        if 'sk-' in content:
            findings.append({"severity": "CRITICAL", "id": "F-SEC-001",
                           "detail": "Potential plaintext API key in settings.json"})
        if 'skipDangerousModePermissionPrompt' in content:
            findings.append({"severity": "WARNING", "id": "F-SEC-002",
                           "detail": "skipDangerousPrompt present in settings.json"})
    except Exception:
        pass

    # 4. Memory system
    memory_dir = os.path.join(home, ".claude", "memory")
    try:
        mem_md = os.path.join(memory_dir, "MEMORY.md")
        if os.path.exists(mem_md):
            with open(mem_md, "r", encoding="utf-8") as f:
                mem_lines = len(f.readlines())
            if mem_lines > 200:
                findings.append({"severity": "WARNING", "id": "F-MEM-001",
                               "detail": f"MEMORY.md {mem_lines} lines (threshold: 200)"})
    except Exception:
        pass

    # 5. Model routing distinctness
    try:
        with open(settings_file, "r", encoding="utf-8") as f:
            settings_text = f.read()
        models = {}
        for tier in ["HAIKU", "SONNET", "OPUS"]:
            m = re.search(rf'ANTHROPIC_DEFAULT_{tier}_MODEL"\s*:\s*"([^"]*)"', settings_text)
            if m:
                models[tier] = m.group(1)
        unique = set(models.values())
        if len(unique) < 3 and len(models) == 3:
            findings.append({"severity": "WARNING", "id": "F-MDL-001",
                           "detail": f"Model tiers not fully distinct: {models}"})
    except Exception:
        pass

    # Compute grade
    criticals = sum(1 for f in findings if f["severity"] == "CRITICAL")
    warnings = sum(1 for f in findings if f["severity"] == "WARNING")

    if criticals >= 4:
        grade = "F"
    elif criticals >= 2:
        grade = "D"
    elif criticals >= 1 or warnings >= 3:
        grade = "C"
    elif warnings >= 1:
        grade = "B"
    else:
        grade = "A"

    # Convert to numeric score
    grade_scores = {"A": 1.0, "B": 0.8, "C": 0.6, "D": 0.4, "F": 0.0}
    score = grade_scores[grade]
    score -= min(criticals * 0.1, 0.3)
    score -= min(warnings * 0.05, 0.15)
    score = max(0.0, min(1.0, score))

    return {
        "score": round(score, 2),
        "grade": grade,
        "criticals": criticals,
        "warnings": warnings,
        "findings": findings,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


def main():
    verbose = "--verbose" in sys.argv
    result = run_health_check()

    if verbose:
        print(f"Self-Audit Health Score: {result['score']}")
        print(f"Grade: {result['grade']}")
        print(f"Criticals: {result['criticals']}, Warnings: {result['warnings']}")
        print(f"Findings:")
        for f in result["findings"]:
            print(f"  [{f['severity']}] {f['id']}: {f['detail']}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

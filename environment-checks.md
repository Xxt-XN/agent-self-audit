# Environment Checks

Companion to self-audit SKILL.md Item 10. Referenced by Item 10 Full mode. Do NOT read in Quick mode unless SKILL.md instructs.

## Quick Checks (reproduced from SKILL.md for reference)

### Disk Space
Check: `python -c "import shutil; u=shutil.disk_usage('/'); free=u.free//10**9; total=u.total//10**9; print(f'{free}GB/{total}GB')"`
Threshold: <20GB free → F-ENV-003(CRIT)
Mode: Quick + Full

### RAM
Check (Windows): `python -c "import ctypes; m=ctypes.windll.kernel32.GetPhysicallyInstalledSystemMemory(); print(f'{m//1024//1024}GB')"`
Check (Linux): `grep MemTotal /proc/meminfo | awk '{print $2/1024/1024 "GB"}'`
Threshold: <8GB → F-ENV-006(WARN)
Mode: Quick + Full

### LibreOffice
Check (Windows): `test -f "/c/Program Files/LibreOffice/program/soffice.exe" && echo "OK" || echo "MISSING"`
Check (Linux): `which soffice && echo "OK" || echo "MISSING"`
Threshold: MISSING → F-ENV-001(CRIT)
Mode: Quick + Full

### Encoding
Check: `echo "PYTHONIOENCODING=$PYTHONIOENCODING"` + `python -c "import sys; print(sys.stdout.encoding)"`
Threshold: PYTHONIOENCODING unset OR stdout encoding is gbk → F-ENV-002(WARN)
Mode: Quick + Full

## Full Checks

### Version Parsing Templates

| Tool | Command | Parse Pattern |
|------|---------|---------------|
| Python | `python --version` | `Python (\d+\.\d+\.\d+)` |
| Node.js | `node --version` | `v(\d+\.\d+\.\d+)` |
| Git | `git --version` | `git version (\d+\.\d+\.\d+)` |
| LibreOffice | `soffice --version` | `LibreOffice (\d+\.\d+\.\d+)` |
| Java | `java -version 2>&1` | `version "(\d+\.\d+\.\d+)"` |
| Maven | `mvn --version 2>&1` | `Apache Maven (\d+\.\d+\.\d+)` |
| MySQL | `mysql --version 2>&1` | `Ver (\d+\.\d+\.\d+)` |
| Docker | `docker --version 2>&1` | `Docker version (\d+\.\d+\.\d+)` |

### Key Python Packages

Check: `pip list 2>/dev/null | grep -iE "openpyxl|python-pptx|python-docx|lxml|Pillow|playwright|numpy"`
Missing required package → F-ENV-005(WARN)
- openpyxl: required for xlsx
- python-pptx: required for pptx
- python-docx: required for docx
- lxml: required for OOXML validation

### Network Connectivity

1. Read `${HOME}/.claude/settings.json`
2. Extract `env.ANTHROPIC_BASE_URL` value
3. If not set: report "No custom endpoint configured", skip connectivity test
4. If set: parse host:port from URL (https→443, http→80)
5. Connect: `python -c "import socket; s=socket.socket(); s.settimeout(5); s.connect(('HOST', PORT)); print('OK'); s.close()"`
6. Connection timeout/refused → F-ENV-004(WARN): "Cannot reach ANTHROPIC_BASE_URL: <url>"
7. May also check HTTP_PROXY/HTTPS_PROXY: if set AND connection fails → suggest proxy issue

### Baseline Comparison

1. Load `${HOME}/.claude/memory/environment-baseline.md` if exists
2. Baseline missing → create from current snapshot, report "Baseline initialized (first run)"
3. Compare each tool version/baseline requirement
4. Baseline >90 days stale → F-ENV-007(SUGGESTION)
5. T1 mode → skip baseline update, report "Baseline update skipped (T1 read-only)"

## Finding ID Reference

| ID | Check | Trigger | Severity | Mode |
|----|-------|---------|----------|------|
| F-ENV-001 | LibreOffice | soffice binary not found | CRITICAL | Quick |
| F-ENV-002 | Encoding conflict | PYTHONIOENCODING unset or mismatch | WARNING | Quick |
| F-ENV-003 | Disk space | HOME partition <20GB free | CRITICAL | Quick |
| F-ENV-004 | Network connectivity | ANTHROPIC_BASE_URL unreachable via TCP | WARNING | Full |
| F-ENV-005 | Critical package missing | openpyxl/python-pptx/python-docx/lxml not found | WARNING | Full |
| F-ENV-006 | RAM insufficient | Total system RAM <8GB | WARNING | Quick |
| F-ENV-007 | Baseline stale | environment-baseline.md last modified >90 days ago | SUGGESTION | Full |

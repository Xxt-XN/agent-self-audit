# Self-Audit

Agent 配置健康检查工具。检测膨胀、漂移、安全问题和技能缺口，并给出修复方案。

[English](README.md) | [安装](INSTALL.md)

## 安装

**Claude Code:**

```bash
git clone https://github.com/Xxt-XN/agent-self-audit.git ~/.claude/skills/self-audit
```

使用 `quick audit` 或 `/self-audit` 触发。首次运行自动搭建。Full 模式在 5 次审计后解锁。

**其他工具**（agentskills.io 标准）：

| 工具 | 安装路径 | 触发方式 |
|------|---------|---------|
| Codex CLI | `~/.codex/skills/self-audit/` | `$self-audit quick audit` |
| Cursor | `~/.cursor/skills/self-audit/` | 说 `quick audit` |
| Windsurf | `~/.codeium/windsurf/skills/self-audit/` | Cascade 自动匹配 |
| Gemini CLI | `~/.gemini/skills/self-audit/` | 说 `quick audit` |

详见 [INSTALL.md](INSTALL.md)。

## 使用方式

双档分级：

|  | Quick | Full |
|---|-------|------|
| 检查项 | 1-6 + Item 10-Quick | 全部 13 项 |
| Token 开销 | < 500 | ~2000-4000 |
| 环境检查 | 4 项原子检查 | 全工具链 + 网络 + 基线 |
| 趋势与预测 | 否 | 是 |
| 市场情报 | 否 | 是（24h 缓存） |
| 触发条件 | 任意触发词，< 5 次历史审计 | `full audit` 或 ≥ 5 次历史审计 |

审计自动升级。3 次运行后趋势可用。5 次后 Full 模式激活，包含预测和市场情报。无需配置。

## 13 项检查

| # | 检查项 | Quick | Full |
|---|-------|:-----:|:----:|
| 1 | 配置健康度 | 行数 | 5 维评分 + 拆分/压缩处方 |
| 2 | 技能清单 | 计数 | 重复 + 市场对比 |
| 3 | 安全 | 明文密钥 | 权限审计 |
| 4 | 记忆系统 | 计数 | 过期 + 结构 |
| 5 | 模型路由 | 层级 | 成本效率 |
| 6 | 可用更新 | `npx skills check` | 变更日志 + 优先级 |
| 7 | 技能利用率 | — | 用量 vs 安装量 |
| 8 | 归档恢复 | — | 可恢复候选项 |
| 9 | Agent 审计质量 | — | 合规抽查 |
| 10 | 运行环境 | 4 项原子检查 | 8 工具 + 7 包 + 网络 + 基线 |
| 11 | 独狼比例 | — | 流水线合规 |
| 12 | 技能违规 | — | 重复追踪 |
| 13 | 市场情报 | — | 每 24h GitHub 市场扫描 |

## 问题分类法

每个问题获得唯一的永久 ID，跨审计追踪：

| 类型 | 含义 |
|------|------|
| Correction | 断裂的符号链接、明文密钥、缺失的工具——立即修复 |
| Repetition | 同一 ID 之前出现过——追踪中，三次升级 |
| Role Redirect | 错误角色在执行工作——流水线违规 |
| Frustration Escalation | 同一件事用户说了两次——流程缺口 |
| Workaround | 该结构化的临时补丁 |

问题自我升级：首次建议，二次警告，三次自动写入为永久硬规则。

## 文件结构

| 文件 | 职责 |
|------|------|
| `SKILL.md` | 可执行 Prompt |
| `bootstrap.md` | 平台检测、降级策略、首次初始化 |
| `environment-checks.md` | 工具链、包、网络、基线 |
| `market-intelligence.md` | GitHub 市场扫描和评分 |
| `compress-config.md` | 健康评分权重和阈值 |
| `DESIGN.md` | 9 个 ADR、9 条 Fitness Function、数据流图 |
| `README.md` | 英文文档 |
| `README_zh.md` | 中文文档 |
| `INSTALL.md` | 按工具分的安装命令 |

---

[English](README.md) — English documentation

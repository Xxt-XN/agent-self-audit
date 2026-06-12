# Self-Audit — 自我进化的 Agent 健康检查

[English](README.md) | [安装](INSTALL.md) | [13 项检查](#13-项检查) | [进化循环](#三大自我进化循环) | [支持工具](#支持的工具)

> **唯一会自我学习的审计技能。** 检测 → 诊断 → 开方 → 迭代。

你的 Agent 配置在悄悄腐烂。规则文件一周周膨胀。技能堆积如山却从不使用。安全设置悄悄偏移。环境工具默默消失。Self-Audit 把它们全部揪出来——然后开出具体处方——然后从每次审计中学习，越跑越聪明。

**遵循 agentskills.io 标准，所有支持该标准的 AI 编程工具均可使用。**

---

## 为什么与众不同

| 普通审计技能 | Self-Audit |
|------------|------------|
| 数行数、报数字 | **5 维健康评分**——300 行结构工整得 A，150 行散文墙得 D |
| 发现问题就完了 | **检测 → 诊断 → 开方**——给出拆分/压缩/合并的具体指令 |
| 用完就扔 | **跨审计趋势追踪**——增长率、预测预警 |
| 死板的绝对阈值 | **上下文评分**——行数只是放大器，永远不会因为行数多就误报 |
| 无视过时工具 | **市场情报**——扫描 GitHub 技能市场，推荐更好的替代品 |
| 报告完就结束 | **3 次重复自动升级**——反复出现的问题变成永久规则 |

---

## 三大自我进化循环

### 循环一：错误 → 硬规则
```
第 1 次出现 → Suggestion（建议）
第 2 次出现 → Warning（警告，"再出现则升级"）
第 3 次出现 → CRITICAL → 自动写入为永久 Pitfall
```
同一个错误不会出现第三次。系统会自己变硬。

### 循环二：技能 → 市场对比
```
每 24 小时：扫描 3 个 GitHub 技能市场仓库（148K+ Stars 数据源）
  → 仓库评分：Stars 35% · 更新日期 30% · 活跃度 20% · 维护状态 15%
  → 交叉对比已装技能与市场替代品
  → 推荐升级方向和缺失品类
```
不用手动搜，你的技能库自己进化。

### 循环三：配置 → 健康处方
```
解析每个章节 · 追踪增长 · 检测重复（Jaccard 0.45）
  → 5 维评分：均衡度 · 粒度 · 密度 · 引用率 · 放大器
  → 具体处方："将第 20–76 行移至 rules/environment.md"（而不是"你的文件太长了"）
```
臃肿的配置文件被外科手术式诊断。

---

## 13 项检查

| # | 检查什么 | Quick | Full |
|---|---------|:-----:|:----:|
| 1 | 配置健康度 | ✅ 行数 | ✅ 5 维评分 + 拆分/压缩处方 |
| 2 | 技能清单 | ✅ 计数 | ✅ 重复 + 市场对比 |
| 3 | 安全 | ✅ 明文密钥 | ✅ 权限审计 |
| 4 | 记忆系统 | ✅ 计数 | ✅ 过期 + 结构 |
| 5 | 模型路由 | ✅ 三层区分 | ✅ 成本效率 |
| 6 | 可用更新 | ✅ `npx skills check` | ✅ 变更日志 + 优先级 |
| 7 | 技能利用率 | — | ✅ 用量 vs 安装量 |
| 8 | 归档恢复 | — | ✅ 可恢复候选项 |
| 9 | Agent 审计质量 | — | ✅ 合规抽查 |
| 10 | 运行环境 | ✅ 4 项原子检查 | ✅ 8 工具 + 7 包 + 网络 + 基线 |
| 11 | 独狼比例 | — | ✅ 流水线合规 |
| 12 | 技能违规 | — | ✅ 重复追踪 |
| 13 | 市场情报 | — | ✅ 每 24h GitHub 市场扫描 |

---

## 从零到全功能 — 全自动

```
首次运行：自动创建 audit-log.md、memory/ 目录、environment.md 占位符
第二次：基于首次快照追踪变化
第三次：局部趋势可用
第五次：Full 模式自动激活——趋势 + 预测 + 市场情报全部就位
```

零配置。零设置。每次运行解锁更多能力。

---

## 支持的工具

Self-Audit 遵循 [agentskills.io](https://agentskills.io) 标准。安装只需复制一个文件夹。

| 工具 | 安装路径 | 触发方式 |
|------|---------|---------|
| Claude Code | `~/.claude/skills/self-audit/` | `quick audit` |
| Codex CLI | `~/.codex/skills/self-audit/` | `$self-audit quick audit` |
| Cursor | `~/.cursor/skills/self-audit/` | 智能匹配（说 `quick audit`） |
| Windsurf | `~/.codeium/windsurf/skills/self-audit/` | Cascade 自动匹配 |
| Gemini CLI | `~/.gemini/skills/self-audit/` | 智能匹配 |

详见 [INSTALL.md](INSTALL.md)，每条工具一行安装命令。

---

## 双档分级

| | Quick | Full |
|---|-------|------|
| 检查项 | 1-6 + Item 10-Quick | 全部 13 项 |
| Token 开销 | < 500 | ~2000-4000 |
| 环境检查 | 4 项原子（磁盘/内存/LibreOffice/编码） | 全工具链 + 网络 + 基线 |
| 趋势与预测 | 否 | 是 |
| 市场情报 | 否 | 是（24h 缓存） |
| 触发条件 | 任意触发词，< 5 次历史 | `full audit` 或 ≥ 5 次历史 |

---

## 问题分类法

每个问题获得唯一的永久 ID，跨审计追踪：

| 类型 | 含义 |
|------|------|
| **Correction（修正）** | 断裂的符号链接、明文密钥、缺失的工具——立即修复 |
| **Repetition（重复）** | 同一 ID 之前出现过——追踪中，三次升级 |
| **Role Redirect（角色错位）** | 错误角色在执行工作——流水线违规 |
| **Frustration Escalation（反复提醒）** | 同一件事用户说了两次——流程缺口 |
| **Workaround（临时绕过）** | 该结构化的临时补丁 |

---

## 极端情况全覆盖

- **新电脑，零配置**：从零自举整个审计基础设施
- **只读文件系统**：降级为 T1 模式（仅 Quick，不写文件，附诊断通知）
- **HOME 不可访问**：干净终止，输出 `insufficient-context` 消息
- **Windows cmd.exe**：自动检测平台，`wc -l` → `find /c /v`，`grep` → `findstr`
- **无 GitHub 认证**：Item 13 优雅跳过，其他审计正常运行
- **无 Python**：Quick 模式纯 Shell；仅 Full 模式工具链检查需要 Python

---

## 文件结构

| 文件 | 职责 |
|------|------|
| `SKILL.md` | 可执行 Prompt（290 行） |
| `bootstrap.md` | 平台检测、降级策略、首次初始化 |
| `environment-checks.md` | Item 10——工具链、包、网络、基线 |
| `market-intelligence.md` | Item 13——GitHub 市场扫描、评分算法 |
| `compress-config.md` | Item 1——健康评分权重、阈值（人工可调） |
| `DESIGN.md` | 9 个 ADR、9 条 Fitness Function、数据流图 |
| `README.md` | 英文文档 |
| `README_zh.md` | 你在这里 |
| `INSTALL.md` | 按工具分的安装命令 |

---

## 快速开始

```bash
git clone https://github.com/Xxt-XN/agent-self-audit.git
cp -r agent-self-audit ~/.claude/skills/self-audit   # 或你的工具路径
quick audit
```

首次运行自动搭建一切。第五次运行解锁 Full 模式——趋势、预测、市场情报全部就位。

---

<br>
<div align="center">
<strong>让你的 Agent 配置进化起来。一次审计一步。</strong>
</div>

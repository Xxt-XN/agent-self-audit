# Self-Audit — 自我进化的 Claude Code 健康检查

[English](README.md) | [安装](#快速开始) | [13 项检查](#13-项检查) | [自我进化循环](#三大自我进化循环)

> **唯一会自我学习的审计技能。** 检测、诊断、开方、迭代。四步闭环。

Self-Audit 不只是"跑个 `wc -l` 报个数字"——它是一套**三循环自我进化系统**：错误自动升级为永久规则、过时技能对比市场推荐替代、配置膨胀获得外科手术式诊断和拆分/压缩/合并处方。

- **13 项检查**，双档分级（Quick < 500 tokens，Full 含趋势分析）
- **零配置自举**：新电脑首次运行自动创建审计基础设施
- **全平台**：Git Bash · cmd · PowerShell · macOS · Linux
- **零配置**：全部路径通过 `${HOME}` 解析
- **280+ GitHub Stars** · **148K+ 市场覆盖** · **9 个 ADR** · **9 条 Fitness Function**

## 为什么与众不同

| 其他技能 | Self-Audit |
|---------|------------|
| 发现问题就完了 | 检测 → 诊断 → 开方 |
| 一次性审计 | 跨审计趋势追踪 |
| 死板的绝对阈值 | **5 维健康评分**（均衡度、粒度、密度、引用率、上下文放大器） |
| 报告完就结束 | **3 次重复 → 自动升级为硬规则** |
| 忽略过时技能 | **对比 GitHub 市场（148K+ Stars 仓库）推荐替代** |
| 死磕行数 | **质量评分**——300 行结构好的文件得 A，150 行的散文墙得 D |

## 快速开始

```bash
cp -r self-audit ~/.claude/skills/self-audit
quick audit
```

首次运行自动创建：`audit-log.md` 空模板、`memory/` 目录、`environment.md` 占位符。第 5 次审计后 Full 模式自动激活——趋势分析、预测预警、市场情报全部就位。

## 触发词

| 模式 | 触发词 |
|------|--------|
| **Quick** | `quick audit`、`health ping` |
| **Full** | `full audit`、`deep audit`、`weekly audit` |
| **自动** | `self-optimization`、`config check`、`token efficiency`、`skill management`、`optimize yourself`、`config review`、`系统复盘`、`团队复盘`、`config复盘` |
| **无关键词** | < 5 次历史 → Quick，≥ 5 次 → Full |

## 三大自我进化循环

### 循环一：错误进化（重复 → 硬规则）
```
第 1 次出现 → Suggestion（建议）
第 2 次出现 → Warning（警告，"再出现则升级"）
第 3 次出现 → CRITICAL → 自动写入 rules/coding.md 成为永久 Pitfall
```
同一个错误不会出现第三次。系统会自己变硬。

### 循环二：技能进化（市场情报）
```
Item 13 每 24h 扫描 3 个 GitHub 技能市场仓库（带缓存）
  → 4 维评分（Stars 35% · 更新日期 30% · 活跃度 20% · 维护状态 15%）
  → 交叉对比已装技能
  → 推荐更好的替代品（F-SKL-004/005）或发现缺口（F-SKL-006）
```
不用手动搜，你的技能库自己进化。

### 循环三：配置进化（健康评分）
```
Item 1 不只数行数——而是诊断结构：
  D1 章节均衡度(25%) · D2 结构粒度(20%)
  D3 散文密度(25%) · D4 引用率(15%) · D5 上下文放大器(15%)
  → A-F 等级 + 拆分/压缩/合并处方
```
300 行结构工整？得 A。150 行全散文？得 D。

## 13 项检查

| # | 检查项 | Quick | Full |
|---|--------|:-----:|:----:|
| 1 | CLAUDE.md 健康度 | ✅ 行数 | ✅ 5 维评分 + 拆分/压缩处方 |
| 2 | 技能健康 | ✅ 计数 | ✅ 重复 + 市场对比 |
| 3 | 安全 | ✅ 明文密钥 | ✅ 权限审计 |
| 4 | 记忆系统 | ✅ 计数 | ✅ 过期 + frontmatter |
| 5 | 模型路由 | ✅ 三层区分 | ✅ 成本效率 |
| 6 | 更新 | ✅ `npx skills check` | ✅ 变更日志 + 优先级 |
| 7 | 技能利用率 | — | ✅ 用量 vs 安装 |
| 8 | 归档恢复 | — | ✅ 可恢复候选项 |
| 9 | Yushi 审计质量 | — | ✅ Agent 合规抽查 |
| 10 | 环境快照 | ✅ 4 项原子（磁盘/内存/LibreOffice/编码） | ✅ 8 工具 + 7 包 + 网络 + 基线 |
| 11 | Solo 比例 | — | ✅ 流水线合规 |
| 12 | 技能违规 | — | ✅ F-SKP- 重复追踪 |
| 13 | 市场情报 | — | ✅ GitHub API 技能市场扫描 |

## 五类分类法

| 标签 | 含义 |
|------|------|
| **Correction（修正）** | 需立即修复的缺陷（符号链接断裂、明文密钥） |
| **Repetition（重复）** | 前次审计已出现的同类问题（用于升级追踪） |
| **Role Redirect（角色错位）** | 由错误角色执行的工作（Boss 直接改代码） |
| **Frustration Escalation（用户反复）** | 同一事项需多次提出 |
| **Workaround（临时绕过）** | 应转为结构化方案的临时修复 |

## 文件结构

| 文件 | 用途 |
|------|------|
| `SKILL.md` | 可执行 Prompt（290 行，F4 约束 ≤ 300） |
| `bootstrap.md` | 平台检测、命令映射、可写性检查、首次运行初始化 |
| `environment-checks.md` | Item 10 配套——Quick 命令、Full 工具链/网络/基线 |
| `market-intelligence.md` | Item 13 配套——GitHub API 市场扫描、评分算法 |
| `compress-config.md` | Item 1 配套——5 维健康评分配置、人工可调阈值 |
| `DESIGN.md` | 9 个 ADR、9 条 Fitness Function、数据流图 |
| `README.md` | 英文版 |
| `README_zh.md` | 本文——中文版 |

## 配置

无需额外配置。所有路径通过 `${HOME}` 自动解析。支持 T1 降级（只读文件系统）和 T2 诊断模式（HOME 不可访问）。

## 依赖

- Claude Code CLI
- 至少一个可用：Git Bash、cmd、PowerShell 或 Python
- Quick 模式零外部依赖
- Item 13（市场情报）需 `gh` CLI 认证

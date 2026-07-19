---
type: summary
created: 2026-07-13
updated: 2026-07-13
tags: [AI Agent, 学习路线, 工程实践, MCP, Prompt Caching]
source: "[[raw/casually/2026-04-30-AI-Agent工程师学习路线]]"
---

# AI Agent 工程师学习路线（2026版）

**核心主张**：几乎所有 Agent 学习路线都错了——不是内容错，是顺序错。正确的顺序应该反过来：**先搞懂 Agent 在工程上会坏在哪里，再去学怎么用框架把这些坑填上。**

## 论证逻辑链

### 第一阶段：底层机制（3-5 天，绝对不要跳）

**1. Function Calling / Tool Use 怎么工作**

LLM 不是真的在「调用」工具——它只是根据你给的 schema 描述，输出一段 JSON。你的代码解析 JSON → 调真实函数 → 把结果塞回对话 → 模型继续。整个过程模型完全依赖你写的 schema 描述：描述含糊则传错参数，类型没说清则传错类型。

2026 关键进展：Claude Opus 4.7、GPT-5、Gemini 2.5 Pro、DeepSeek-V3、Qwen3 都已支持**并行工具调用**（parallel tool calls），一次返回多个 tool_use block，链路延迟降到 1/N。

**2. ReAct 循环及其四大失败模式**

| 失败模式 | 现象 | 对策 |
|---------|------|------|
| 死循环 | Observation 不满意一直重试 | 限制重试次数 |
| Context 爆炸 | 循环轮次太多塞满上下文 | 主动剪枝 |
| 早停 | 未拿到关键信息就判定"任务完成" | 关键信息确认机制 |
| **过度思考**（2026 新增） | 推理模型 thought 阶段消耗几千几万 token 钻牛角尖 | `thinking.budget_tokens` 上限；简单任务 `reasoning_effort: minimal` |

**3. Context Window 的物理限制**

长上下文不等于好用。三个必须警惕的现象：Lost in the Middle（中段信息利用率低，关键信息放头尾）、Context Rot（无关上下文越多准确率越低，主动剪枝比无脑塞好）、延迟成本爆炸（1M token 单次请求 TTFT 十几秒，$2-3/请求）。

> Memory 管理在 2026 依然是核心问题，不是因为 context 不够，而是因为长 context 反而更难管。

**4. Prompt Caching（2026 最关键的成本工程）**

Anthropic / OpenAI / Gemini 都支持服务端 KV Cache 持久化——命中后**延迟降 80%、成本降 90%**。

实战要点：system prompt + 工具定义 + 长文档前缀几乎必开 cache；Anthropic 提供 5min / 1h TTL，最多 4 个 cache breakpoints；不要在 cached 前缀里塞时间戳/随机 ID。

**动手练**：不用任何框架，直接调 API，手动解析 tool_use、手动拼 messages 数组，实现 Calculator + Web Search + prompt caching——50 行代码，这一步搞透，后面省掉 80% 的迷茫。

### 第二阶段：框架选型（2026 大变天）

> 很多老路线力推 LangGraph，但 2026 年厂商 SDK 强势崛起——Claude Agent SDK、OpenAI Responses API、Gemini Agent SDK 都在快速成熟。

选择建议：厂商 SDK 做原型快（生态锁定但开发快），LangGraph 控制力强（图结构灵活但门槛高），按阶段选择。

### 第三阶段：核心模块工程深度

**1. Tool 设计与 MCP（2026 必学）**

- **MCP 协议**：Anthropic 2024 开源，2025 被 OpenAI/Google/Cursor/Windsurf 全面采纳。解决「M 个模型 × N 个工具」集成爆炸。五种 primitive：Tools/Resources/Prompts/Sampling/Roots。截至 2026 初社区已有数千个公开 MCP Server。
  > 简历写「熟悉 MCP 协议」+「自己写过一个 MCP Server」，面试官眼睛会亮。

- **BFCL 评估**：Berkeley Function-Calling Leaderboard，2026 工具调用事实评测榜。

- **流式工具调用**：Claude fine-grained tool streaming + OpenAI Responses API 边推理边输出参数，延迟敏感场景必学。

**2. Memory 分层**

| 层 | 实现 | 2026 主流方案 |
|----|------|-------------|
| 短期 | messages + sliding window + 自动 summary | Claude Code 的 /compact 机制 |
| 长期 | 向量库 + 时间衰减 + 重要性加权 | Mem0 / Zep |
| 系统级 | RAG + Reranker + Hybrid Search | Voyage 3 / Qwen3-Embedding / OpenAI text-embedding-3-large |

> 能把这三层画出来 + 说清每层读写策略，面试已经超过大多数候选人。

**3. 可观测性**：LangSmith / Braintrust / Arize Phoenix 都可做 trace；关键指标：Tool 调用成功率、Context 利用率、Token 消耗趋势、幻觉率。

### 第四阶段：做有评估的项目

**2026 最有故事性的项目方向**：Text2SQL on BIRD-SQL、Code Agent on SWE-Bench Verified、Browser Agent on WebArena、Customer Service Agent on τ-bench、GUI Agent on OSWorld。

**简历金标准描述模板**：不只是「我做了一个 X Agent」，而是「在 SWE-Bench Verified 上从基线 32% 优化到 51%，三大手段：改进工具 schema (+8pp) → 反思-修正子图 (+6pp) → prompt caching (成本降 70%，延迟降 70%)」。

### 五个大坑

| 坑 | 核心原因 | 正确做法 |
|----|---------|---------|
| Multi-Agent 不要早学 | 两个 Agent 之间的状态同步/消息传递/循环依赖是陷阱 | 单 Agent + Workflow 优先，Multi-Agent 仅在必要时引入 |
| 不要迷信推理模型 | 简单任务开 thinking 反而拖慢且更贵 | 按任务复杂度分级：`reasoning_effort: minimal/low/medium/high` |
| 不要堆框架 | 简历堆 LangChain+LlamaIndex+AutoGen+Dify+Coze+MCP+A2A | 专精 1-2 个，讲清楚为什么选它 |
| 不要绕过 Prompt Caching | 不开 cache 的 Agent 在生产环境 = 烧钱机器 | system prompt + 工具定义必开 |
| 不要忽视 cost 数据 | 简历光说「准确率提升」不够 | accuracy / latency / cost 三个数据同时讲清楚 |

> 以前学 Agent：底层 → LangGraph → 狂学框架 → 项目；2026 学 Agent 的正确顺序：底层（含 prompt caching / MCP）→ LangGraph + 厂商 SDK → 工程深度（MCP / BFCL）→ 做有评估的项目 + 三维优化（准确率 / 延迟 / 成本）。

## 与知识库其他内容的连接

这篇文章和 [[summaries/面试官视角的AI时代筛选逻辑]] 形成互补——面试官那篇讲的是「面试在筛什么」，这篇讲的是「怎么学才能经得起筛」。共同的结论：**真实工程深度 > 框架数量 > demo 项目**。

## 相关实体与概念

- [[entities/MCP]] — 2026 必学协议，事实工具调用标准
- [[entities/LangGraph]] — 图结构 Agent 编排框架
- [[concepts/Agent-Loop]] — ReAct 循环及四大失败模式
- [[concepts/Agent-Memory]] — 三层记忆架构（短期/长期/系统级）
- [[concepts/Agent-Execution-Environment]] — 观测性、cost 数据的工程基础

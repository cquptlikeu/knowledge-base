---
type: summary
created: 2026-07-07
updated: 2026-07-07
tags: [Karpathy, 知识库, Claude Code, Obsidian, LLM Wiki]
source: "[[raw/casually/2026-04-14-Karpathy-knowledge-base-tutorial]]"
---

# Karpathy LLM Wiki 方法实践教程

**作者**：[[entities/Paula-Baola]]（Paula 寶拉）
**来源**：YouTube 视频
**发布日期**：2026-04-14

## 核心观点

不需要 RAG、不需要向量数据库、不需要复杂管线——只靠 [[entities/Obsidian]] + [[entities/Claude-Code]]，用一堆 Markdown 文件就能做出会自己找连结、自己补缺口的个人知识库。

> 原文金句：*"Drop in two articles, and AI generates this itself — no sorting, no tagging, no database."*
>
> *"Every lookup accumulates into the system."*
>
> *"You'll almost never need to edit the Wiki yourself, because it's the LLM's turf — building and maintaining it is all AI's job."*

## 系统架构

与我们的知识库高度一致（这篇文章和 [[entities/Andrej-Karpathy]] 的原始设计就是我们知识库的直接祖先）：

| 组件 | 作用 |
|------|------|
| **Raw 文件夹** | 原始素材入口，像信箱一样只收不放 |
| **Wiki 文件夹** | LLM 产出的结构化知识 |
| **_index.md** | 知识库目录，AI 查询时先读它而非遍历全库 |
| **_log.md** | 操作日志，记录 AI 做了什么，可追溯、不重复 |
| **CLAUDE.md** | AI 的指令手册——每次启动先读它 |

## 核心流程

### 1. 采集（Ingest）
用 Obsidian Web Clipper 一键抓取网页文章 → 存入 Raw 文件夹 → 跟 Claude 说「有新文章，请采集」→ AI 自动拆解概念和人物，生成 wiki 页面、摘要、标签、交叉链接，更新索引。

### 2. 查询（Query）
自然语言提问——包括跨文章的问题（"Naval 说的特定知识和阅读有什么关系？"）——AI 先用索引定位，再综合多篇文章回答。

### 3. 健康检查（Health Check）
AI 扫描知识库，发现矛盾、知识空白，甚至主动建议 "你在这里的覆盖比较薄，要不要补几篇文章？"

## Graph View：系统最独特的能力

两篇文章放入后，每篇有各自的节点群——但有些节点会**交叉**。"AI 自动发现两篇文章之间的共同点，并把它们连在一起。文章越多，跨文章链接越多，系统越有用。"

## 与传统 RAG 的对比

| 维度 | [[concepts/RAG-vs-LLM-Wiki]] |
|------|
| 实现 | Markdown 文件 + 索引 | 向量数据库 + Embedding |
| 查询机制 | 读索引→按链接定位 | 相似度搜索 |
| 门槛 | 低，几分钟搭建 | 高，需要向量数据库和 ingestion pipeline |
| 规模上限 | ~100 篇 → 个人使用足够 | 数万篇级 |
| 成本 | 只有 AI token | embedding 服务 + 存储 |

## 四个限制（Paula 的诚实评估）

1. **Claude Code 要付费**，Obsidian 免费
2. **采集需要时间**——每篇文章几分钟，一次丢 30 篇需要 10-15 分钟
3. **个人规模**——几十到几百篇文章 OK，上万的文档量需要其他工具
4. **Token 成本随着知识库增长**——更多内容 = 更多 token 进入上下文

## 相关实体与概念

- [[entities/Andrej-Karpathy]] — 思想源头
- [[entities/Paula-Baola]] — 视频作者
- [[entities/Obsidian]] — 笔记工具
- [[entities/Claude-Code]] — AI 引擎
- [[concepts/LLM-Wiki]] — 核心方法论
- [[concepts/RAG-vs-LLM-Wiki]] — 两种知识库范式对比

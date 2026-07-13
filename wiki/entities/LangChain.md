---
type: entity
created: 2026-07-13
updated: 2026-07-13
tags: [AI, 框架, Python, LLM, 同质化]
aliases: [LangChain框架]
---

# LangChain

LLM 应用开发框架，提供 Model I/O、Retrieval、Chains、Agents 等抽象层，是 2024-2026 年最流行的 LLM 应用开发库之一。

## 核心特征

- **模块化抽象**：Model I/O（统一 LLM 接口）、Retrieval（文档加载+向量存储）、Chains（可组合调用链）、Agents（工具调用+推理循环）
- **生态丰富**：与 Chroma、Pinecone、Weaviate 等向量数据库深度集成
- **快速原型**：教程丰富，门槛极低，几行代码即可搭出 RAG 问答系统

## 主要应用场景

- **RAG 知识库**：最常见的应用场景——文档加载 → 分块 → 向量化 → 检索 → 生成回答
- **文档加载器**：对接各类文档格式的加载与解析

## ⚠️ 同质化陷阱

2026 年求职市场的关键问题：**LangChain + Chroma + OpenAI 的基础 RAG 已成为烂大街的模板项目**。

> 今天面了 10 个人，9 个做了 RAG 知识库——面试官

- 教程教的是「标准答案」，标准 = 可复制 = 不稀缺 = 没有议价权
- 仅「我用了 LangChain」在简历上已无信息量——面试官要的是「我在 LangChain 的基础上做了什么自己的优化」
- 差异化路径：多模态 RAG（图片+文档+视频）、垂直行业落地（质检/医疗/法律）、本地化部署（无第三方 API 依赖）

## 与其他实体的关系

- **配合 [[entities/Chroma]]**：最常见的向量数据库组合
- **配合 [[entities/RAG]]**：LangChain 是 RAG 的最常见实现框架
- **父子关系 [[entities/LangGraph]]**：LangGraph 是 LangChain 生态的多 Agent 编排子项目
- **同质化同伙 [[entities/RAG]]**：两者组合构成了「面试官审美疲劳」的核心原因

## 来源

- [[summaries/AI项目避坑与加分项指南]] — 基础 LangChain RAG 已被列为坑
- [[summaries/AI项目差异化方法论]] — 作为「标准答案」案例被分析
- [[summaries/面试官视角的AI时代筛选逻辑]] — 同质化问题在面试中的体现

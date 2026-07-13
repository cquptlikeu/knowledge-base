---
type: entity
created: 2026-07-13
updated: 2026-07-13
tags: [AI, 向量数据库, RAG, Python, 同质化]
aliases: [Chroma DB, Chroma向量数据库]
---

# Chroma

开源嵌入式向量数据库，专为 LLM 应用设计的轻量级存储与检索引擎。因与 LangChain 深度集成和极低的使用门槛，成为 2024-2026 年 RAG 教程中最常用的向量数据库。

## 核心特征

- **零配置**：pip install 即可使用，无需独立服务进程
- **LangChain 原生集成**：LangChain 文档加载 → Chroma 向量存储的 pipeline 被大量教程采用
- **轻量级**：适合本地开发和原型验证

## 主要应用场景

- 原型阶段的 RAG 知识库
- 本地文件语义搜索

## ⚠️ 同质化警示

> 「这个项目我们面的人基本都做过，你跟别人的区别在哪？」——面试官

Chroma + LangChain + OpenAI 的组合已成为 2026 年应届生简历中最常见的模板项目。仅使用这套组合在面试中不再构成差异化。差异化方向：
- 替换为生产级向量数据库（Pinecone、Weaviate、Milvus）并说明选择理由
- 自研混合检索策略（全文+向量+元数据三层融合）

## 与其他实体的关系

- **配合 [[entities/LangChain]]**：最经典的 RAG 原型组合
- **对比 [[entities/RAG]]**：Chroma 是 RAG 的存储层实现，RAG 是架构模式
- **替代品**：Pinecone（生产级云服务）、Weaviate（Hybrid Search）、Milvus（十亿级向量）

## 来源

- [[summaries/AI项目避坑与加分项指南]] — 作为烂大街模板的组成部分
- [[summaries/AI项目差异化方法论]] — 标准答案的典型元素

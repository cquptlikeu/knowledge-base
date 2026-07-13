---
type: entity
created: 2026-07-07
updated: 2026-07-07
tags: [AI, 工具调用, 协议标准, Anthropic]
aliases: [Model Context Protocol, MCP协议]
---

# MCP（Model Context Protocol）

Anthropic 提出并开源的标准化协议，规范大语言模型如何调用外部工具（Tool）的接口格式。

## 核心特征

- **LLM 提供商无关**：工具定义与 LLM 厂商解耦，可无缝切换不同模型（DeepSeek、Ollama、Claude 等）而无需修改工具实现
- **Schema 约束**：要求工具以 JSON Schema 声明输入输出格式，减少模型产生格式错误的概率
- **生态兼容**：采用 MCP 标准的工具可被任何支持 MCP 的 AI 客户端直接调用

## 主要应用场景

- **AI Agent 工具调用**：Agent 通过 MCP 协议规范的接口调用文件系统工具（list_files、search_files、read_file 等）
- **NAS 智能检索**：将 NAS 文件系统的工具能力暴露给大语言模型，实现自然语言驱动的文件操作
- **跨模型平台**：一套工具定义，多个 LLM 后端共享

## 与其他实体的关系

- **配合 [[entities/RAG]]**：MCP 负责工具调用规范，RAG 负责内容检索流水线
- **配合 [[concepts/Agent-Loop]]**：MCP 定义了 Agent 循环中工具调用的接口格式
- **配合 [[entities/authd]]**：每次 MCP 工具调用前经过 authd 的 Permission Hook 权限校验

## 在本架构中的选择理由

> MCP 是当前 LLM 工具调用领域最具生态影响力的标准协议。工具定义与 LLM 厂商解耦，可切换不同的大模型而无需修改工具实现代码。

## 来源

- [[summaries/NAS智能存储平台技术架构]] — 第 4.7 节 AI 技术栈，第 9 章智能服务
- [[summaries/AI项目避坑与加分项指南]] — 2026 年最火的协议，电商运营垂直 Agent 的核心技术亮点
- [[summaries/面试官视角的AI时代筛选逻辑]] — 面试中提及为简历常见标签

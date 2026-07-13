---
type: entity
created: 2026-07-13
updated: 2026-07-13
tags: [AI, Agent, 框架, 多智能体, Microsoft]
aliases: [AutoGen框架]
---

# AutoGen

微软开源的对话式多智能体编排框架。Agent 之间通过对话（conversation）而非显式的图结构来协调任务，适合需要灵活协商和动态路由的 Agent 场景。

## 核心特征

- **对话式编排**：Agent 之间通过自然语言对话协调，而非预定义的流程控制图
- **角色灵活**：Agent 可以动态切换角色（提问者、回答者、评审者），无需提前编写状态机
- **微软生态**：与 Azure OpenAI Service 深度集成，支持企业级部署
- **低门槛**：相比于显式定义流程图，对话式编排的入门成本更低

## 主要应用场景

- **多 Agent 协作**：搜索 Agent + 总结 Agent + 校验 Agent 通过对话协商完成复杂任务
- **代码生成+审查**：一个 Agent 写代码，另一个 Agent 审查并提出修改意见
- **教学场景**：学生 Agent 和教师 Agent 通过对话模拟学习过程

## 与其他实体的关系

- **vs [[entities/LangGraph]]**：AutoGen 用对话编排（灵活但不可预测），LangGraph 用图结构编排（可控但需要显式设计）
- **配合 [[entities/MCP]]**：Agent 可通过 MCP 协议调用外部工具
- **配合 [[concepts/Multi-Agent Collaboration]]**：多 Agent 协作范式的两种实现路径之一

## 来源

- [[summaries/Agent项目的三个落地方向]] — 推荐 AutoGen 作为多 Agent 框架选项

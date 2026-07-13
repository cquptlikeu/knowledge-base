---
type: entity
created: 2026-07-13
updated: 2026-07-13
tags: [AI, Agent, 框架, 多智能体, Python]
aliases: [LangGraph框架]
---

# LangGraph

LangChain 团队开发的多智能体（Multi-Agent）编排框架，使用有向图（DAG）来定义 Agent 之间的控制流和数据流，支持循环、分支和条件路由。

## 核心特征

- **图基编排**：将 Agent 和工作流建模为有向图（节点 = Agent/工具/函数，边 = 数据/控制流），比线性链式调用更灵活
- **状态管理**：图中有持久化的共享状态，各 Agent 节点可读写，支持复杂推理流程
- **循环支持**：内置循环（cycle）能力，适合需要迭代推理的 Agent 场景
- **人机协同**：支持 Human-in-the-loop 节点，在关键决策点暂停等待人工确认

## 主要应用场景

- **多 Agent 协作**：搜索 Agent、总结 Agent、校验 Agent 通过图结构协作完成复杂任务
- **任务自动化 Agent**：定义「抓取→过滤→总结→发送」的自动化流程管道
- **复杂推理工作流**：需要多轮迭代、条件分支、错误重试的 Agent 系统

## 与其他实体的关系

- **vs [[entities/AutoGen]]**：LangGraph 用图结构显式定义流程，AutoGen 用对话式编排
- **配合 [[entities/MCP]]**：LangGraph 图中的工具节点可通过 MCP 协议调用外部工具
- **继承 [[entities/LangChain]]**：LangGraph 是 LangChain 生态的一部分，共享工具链

## 来源

- [[summaries/Agent项目的三个落地方向]] — LangGraph 作为多 Agent 框架被推荐
- [[summaries/面试官视角的AI时代筛选逻辑]] — 面试中提及作为常见框架标签

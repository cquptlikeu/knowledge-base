---
title: "想入行AI Agent？2026最全技术学习清单（从入门到offer）_牛客网"
source: "https://www.nowcoder.com/discuss/874028064714285056?sourceSSR=search"
author:
published:
created: 2026-07-16
description: "一、基础打底（所有人必学） 1. 编程基础（核心：Python） Python语法、函数、类、文件IO、异常处理 常用库：requests、json、pydantic、asyncio 数据结构：列表、字典、队列、栈、图（基础） Git基础：代码管理、分支、提交 2. AI与大模型基础 LLM原理：T_牛客网_牛客在手,offer不愁"
tags:
  - "clippings"
---
一、基础打底（所有人必学）

1\. 编程基础（核心：Python）

Python语法、函数、类、文件IO、异常处理

常用库：requests、json、pydantic、asyncio

数据结构：列表、字典、队列、栈、图（基础）

Git基础：代码管理、分支、提交

2\. AI与大模型基础

LLM原理：Transformer、上下文、token、幻觉、温度

主流模型：GPT4o、Claude 3、Qwen、Llama 3、DeepSeek

模型调用：API密钥、请求格式、流式输出、错误处理

基础NLP：意图识别、实体抽取、文本分类、摘要

3\. 提示工程（Agent灵魂）

基础：角色设定、清晰指令、格式约束（JSON/Markdown）

高级：CoT思维链、ReAct（推理+行动）、FewShot

自我反思、工具调用提示、长上下文管理

二、核心技术（Agent四大模块）

1\. 记忆系统（让AI“记得住”）

短期记忆：上下文窗口、状态管理

长期记忆：向量数据库（Pinecone、Chroma、FAISS、Milvus）

嵌入（Embedding）：textembedding、bge、m3e

RAG（检索增强生成）：文档切分、向量化、检索、重排

2\. 工具调用（让AI“能做事”）

函数调用（Function Calling）：定义、参数、返回、校验

外部API：搜索（SerpAPI）、天气、地图、邮件、数据库

代码执行：Python REPL、沙箱环境

工具封装、权限控制、白名单、异常熔断

3\. 规划与推理（让AI“会思考”）

ReAct、ToT（思维树）、PlanandExecute

任务拆解、子任务调度、依赖管理

自我修正、反思循环、失败重试

状态机、工作流（Workflow）

4\. 多智能体协作（2026重点）

架构：ManagerWorker、专家分工、辩论机制

框架：AutoGen、CrewAI、LangGraph、MetaGPT

通信协议、消息队列、结果聚合

三、主流框架（必学23个）

LangChain/LangGraph：工作流、状态管理、生态最全

AutoGen/CrewAI：多Agent、角色化、企业级流程

LlamaIndex：RAG、知识库、文档理解

Dify/Coze：低代码、快速上线、非技术友好

OpenAI Agent SDK、Semantic Kernel

四、工程化与部署（能上线才值钱）

1\. 后端与服务

FastAPI/Flask：接口开发、路由、中间件

数据库：SQLite、PostgreSQL、Redis

异步、并发、限流、重试、日志

2\. 部署与运维

Docker容器、K8s基础

云服务：AWS/GCP/Azure/阿里云/腾讯云

Serverless、API网关、域名、HTTPS

监控、告警、性能优化、成本控制

3\. 评估与安全

评测：任务完成率、准确率、响应时间、幻觉率

工具：Ragas、Phoenix、自定义测试集

安全：输入过滤、输出审核、权限、隐私、合规

四、学习路线（3个月版）

第1个月：入门

Python基础 + LLM API调用

提示工程（ReAct/CoT）

用Dify/Coze做简单Agent（问答/日程）

第2个月：进阶

LangChain + RAG + 向量库

工具调用、函数封装

项目：文档问答、数据分析助手

第3个月：高级

LangGraph / AutoGen / CrewAI

多Agent、工作流、复杂任务

项目：智能客服、自动化流程、研究助手

五、面试常问（直接背）

解释ReAct的推理行动循环

RAG如何解决幻觉？有哪些优化？

如何设计一个能订机票的Agent？

多Agent架构有哪些模式？

Agent常见问题：卡顿、死循环、幻觉怎么解决？

六、避坑提醒

不用先训模型：重点是调用、编排、工程化

不用全学：先掌握Python + LLM + LangChain + RAG

重实战：每学一个技术就做小Demo，再串成大项目
---
type: summary
created: 2026-07-16
updated: 2026-07-16
tags: [AI Agent, 学习清单, 技术栈, 面试, 从入门到offer]
source: "[[raw/definitely/2026-07-16-AI-Agent技术学习清单从入门到offer]]"
---

# AI Agent 技术学习清单（从入门到 offer）

**核心论点**：一份面向求职的全栈 AI Agent 技术学习清单，从基础打底到工程化部署到面试常见问题，覆盖 3 个月学习路线。

## 六层结构

### 一、基础打底（所有人必学）

1. **编程基础（核心 Python）**：语法、函数、类、文件 IO、异常处理、requests/json/pydantic/asyncio、数据结构、Git
2. **AI 与大模型基础**：LLM 原理（Transformer/上下文/token/幻觉/温度）、主流模型（GPT-4o/Claude/千问/Llama/DeepSeek）、API 调用、基础 NLP（意图识别/实体抽取/文本分类/摘要）
3. **提示工程（Agent 灵魂）**：角色设定、清晰指令、格式约束、CoT、ReAct、Few-Shot、工具调用提示、长上下文管理

### 二、核心技术（Agent 四大模块）

| 模块 | 核心内容 | 关键工具 |
|------|---------|---------|
| **记忆系统** | 短期记忆（上下文窗口+状态管理）、长期记忆（向量数据库）、Embedding、RAG（文档切分→向量化→检索→重排） | Pinecone / Chroma / FAISS / Milvus, bge / m3e / text-embedding |
| **工具调用** | Function Calling（定义/参数/返回/校验）、外部 API（搜索/天气/邮件/数据库）、代码执行（Python REPL 沙箱）、权限控制/白名单/异常熔断 | SerpAPI, Python REPL |
| **规划与推理** | ReAct、ToT（思维树）、Plan & Execute、任务拆解+子任务调度+依赖管理、自我修正+反思循环+失败重试、状态机+工作流 | — |
| **多智能体协作** | Manager-Worker 架构、专家分工、辩论机制 | AutoGen / CrewAI / LangGraph / MetaGPT |

### 三、主流框架

- **LangChain / LangGraph**：工作流、状态管理、生态最全
- **AutoGen / CrewAI**：多 Agent、角色化、企业级流程
- **LlamaIndex**：RAG、知识库、文档理解
- **Dify / Coze**：低代码、快速上线
- **OpenAI Agent SDK / Semantic Kernel**

### 四、工程化与部署

1. **后端与服务**：FastAPI/Flask、SQLite/PostgreSQL/Redis、异步/并发/限流/重试/日志
2. **部署与运维**：Docker + K8s 基础、云服务（AWS/GCP/Azure/阿里云/腾讯云）、Serverless + API 网关 + HTTPS、监控/告警/性能优化/成本控制
3. **评估与安全**：评测指标（任务完成率/准确率/响应时间/幻觉率）、Ragas / Phoenix / 自定义测试集、安全（输入过滤/输出审核/权限/隐私/合规）

### 五、3 个月学习路线

| 月份 | 阶段 | 内容 |
|:---:|------|------|
| 1 | 入门 | Python 基础 + LLM API 调用 + 提示工程（ReAct/CoT）+ Dify/Coze 做简单 Agent |
| 2 | 进阶 | LangChain + RAG + 向量库 + 工具调用 + 项目：文档问答/数据分析助手 |
| 3 | 高级 | LangGraph/AutoGen/CrewAI + 多 Agent + 工作流 + 项目：智能客服/自动化流程/研究助手 |

### 六、常考面试题

- 解释 ReAct 的推理-行动循环
- RAG 如何解决幻觉？有哪些优化手段？
- 如何设计一个能订机票的 Agent？
- 多 Agent 架构有哪些模式？
- Agent 常见问题：卡顿、死循环、幻觉怎么解决？

### 避坑提醒

> 不用先训模型——重点是调用、编排、工程化。不用全学——先掌握 Python + LLM + LangChain + RAG。重实战——每学一个技术就做小 Demo，再串成大项目。

## 与知识库其他内容的连接

这篇文章是一份「便携清单」——适合对照检查自己还缺什么。与 [[summaries/AI-Agent工程师学习路线2026]]（底层机制优先）和 [[summaries/Agent赛道四大岗位精准对标]]（按岗位倒推）形成三种不同的学习路线组织视角。

## 相关实体与概念

- [[entities/LangChain]]、[[entities/LangGraph]] — 核心框架
- [[entities/AutoGen]] — 多 Agent 框架
- [[entities/MCP]] — 工具调用标准协议
- [[concepts/Agent-Memory]] — 记忆系统三大层
- [[concepts/Multi-Agent-Collaboration]] — 多智能体协作模式
- [[concepts/Agent-Execution-Environment]] — 部署/监控/安全

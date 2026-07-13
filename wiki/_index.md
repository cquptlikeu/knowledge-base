# 知识库索引

## 主题：NAS 智能存储平台架构

**核心架构模式**：[[concepts/统一身份源]]（Single Source of Truth）、[[concepts/统一权限源]]（Single Permission Source）、[[concepts/多协议融合]]（跨终端统一接入）、[[concepts/容器化部署]]（四容器架构）

**AI 能力**：[[concepts/Agent-Loop]]（智能体循环）、[[concepts/RAG-三层混合检索]]（成本-质量平衡）、[[entities/MCP]]（工具调用协议）、[[entities/RAG]]（检索增强生成）

**安全体系**：[[concepts/纵深防御]]（四层安全）、[[concepts/哈希链可信存证]]（不可篡改审计）、[[concepts/国产化演进]]（SM2/SM3/SM4）

**移动端**：[[concepts/三级连接回退]]（P2P→mDNS→缓存IP）、[[entities/NFC]]（碰一碰登录）

**核心自研**：[[entities/authd]]（统一业务入口）、[[entities/Docker]]（四容器编排）

**协议对比**：[[comparisons/LDAP-vs-关系数据库]]、[[comparisons/四种文件协议对比]]、[[comparisons/POSIX-ACL-vs-Unix权限]]

**关键实体**：[[entities/OpenLDAP]]、[[entities/POSIX-ACL]]、[[entities/Samba]]、[[entities/NFS]]、[[entities/WebDAV]]、[[entities/Go]]、[[entities/Gin]]、[[entities/JWT]]、[[entities/SQLite]]、[[entities/SHA-256]]、[[entities/PUF]]、[[entities/Nginx]]、[[entities/mDNS]]、[[entities/WiFi-P2P]]、[[entities/Next.js]]、[[entities/React-Native]]

**相关文章**：[[summaries/NAS智能存储平台技术架构]]

## 主题：AI 知识管理

**核心方法论**：[[concepts/LLM-Wiki]]（Karpathy 知识库方法）、[[concepts/Personal-Knowledge-Asset]]（本地化私有知识系统）、[[concepts/Progressive-Disclosure]]（按需加载上下文）

**方法论**：[[concepts/CLAUDE-MD-Two-Layer-Navigation]]（CLAUDE.md + 目录 instructions）、[[concepts/Folder-as-an-APP]]（文件夹即应用）

**自动化**：[[concepts/Automated-Input-Pipeline]]（信息自动流入）、[[concepts/Fleeting-Capture]]（闪念胶囊碎片捕捉）

**范式对比**：[[concepts/RAG-vs-LLM-Wiki]] — RAG 还是 LLM Wiki？、[[comparisons/Obsidian-vs-Milanote]] — AI 时代应该选哪个笔记工具

**关键实体**：[[entities/Andrej-Karpathy]]（思想来源）、[[entities/Zhurudong]]（开源实现者）、[[entities/Obsidian]]（笔记工具）、[[entities/Claude-Code]]（AI 引擎）、[[entities/Milanote]]（被替代的方案）、[[entities/Serena-Xinxin]]（教程作者）、[[entities/Paula-Baola]]（教程作者）

**相关文章**：[[summaries/Obsidian-Claude-Code-Second-Brain]]、[[summaries/Karpathy-knowledge-base-tutorial]]、[[summaries/Karpathy-llm-wiki-template]]

## 主题：AI 求职与项目策略

**核心洞察**：[[concepts/AI-Project-Differentiation]]（差异化 = 垂直场景 + 工程化 + 真实数据）、[[concepts/Agent-Execution-Environment]]（执行环境的隔离与兜底——面试中最深的追问）、[[concepts/Multi-Agent-Collaboration]]（多 Agent 编排——图结构 vs 对话式）、[[concepts/Agent-Memory]]（长期记忆的三难：存储、检索、上下文压缩）

**落地方向**：MCP 垂直 Agent、多模态 RAG、本地代码审计 Agent、端侧日程 Agent

**面试逻辑**：AI 把实现能力拉平 → 筛选从「会不会做」变成「为什么这么做、边界在哪、失败怎么处理」

**关键实体**：[[entities/LangGraph]]（图结构多 Agent 编排）、[[entities/AutoGen]]（对话式多 Agent 编排）、[[entities/LangChain]]（LLM 应用框架，同质化陷阱）、[[entities/Chroma]]（向量数据库，教程标配）、[[entities/Llama]]（本地化部署大模型）、[[entities/Qwen2]]（端侧推理模型）

**相关文章**：[[summaries/面试官视角的AI时代筛选逻辑]]、[[summaries/AI项目避坑与加分项指南]]、[[summaries/AI项目差异化方法论]]、[[summaries/Agent项目的三个落地方向]]

## 主题：Rust

**关键实体**：[[entities/Rust]] — 系统编程语言，所有权系统 + 零成本抽象

**概念**：[[concepts/ABI-Compatibility]]（二进制接口兼容性）、[[concepts/type-name-of-val]]（类型名反射）

**相关文章**：[[summaries/Rust-1.76.0]]

---

## 全部页面（按类型）

### Summaries
- [[summaries/NAS智能存储平台技术架构]]
- [[summaries/Rust-1.76.0]]
- [[summaries/面试官视角的AI时代筛选逻辑]] — 面试官角度的 Agent 项目筛选逻辑
- [[summaries/AI项目避坑与加分项指南]] — 三个巨坑 + 四个加分项目
- [[summaries/AI项目差异化方法论]] — 找到属于你的差异化方向
- [[summaries/Agent项目的三个落地方向]] — 自动化/多Agent协作/记忆助手
- [[summaries/Obsidian-Claude-Code-Second-Brain]]
- [[summaries/Karpathy-knowledge-base-tutorial]]
- [[summaries/Karpathy-llm-wiki-template]]

### Entities
- [[entities/Andrej-Karpathy]]
- [[entities/AutoGen]] — 微软对话式多 Agent 编排框架
- [[entities/authd]]
- [[entities/Chroma]] — 轻量向量数据库，教程标配
- [[entities/Claude-Code]]
- [[entities/Docker]]
- [[entities/Gin]]
- [[entities/Go]]
- [[entities/JWT]]
- [[entities/LangChain]] — LLM 应用框架，同质化陷阱
- [[entities/LangGraph]] — 图结构多 Agent 编排
- [[entities/Llama]] — Meta 开源大模型
- [[entities/MCP]]
- [[entities/mDNS]]
- [[entities/Milanote]]
- [[entities/Next.js]]
- [[entities/NFC]]
- [[entities/NFS]]
- [[entities/Nginx]]
- [[entities/Obsidian]]
- [[entities/OpenLDAP]]
- [[entities/Paula-Baola]]
- [[entities/POSIX-ACL]]
- [[entities/PUF]]
- [[entities/Qwen2]] — 阿里开源端侧推理模型
- [[entities/RAG]]
- [[entities/React-Native]]
- [[entities/Rust]]
- [[entities/Samba]]
- [[entities/Serena-Xinxin]]
- [[entities/SHA-256]]
- [[entities/SQLite]]
- [[entities/WebDAV]]
- [[entities/WiFi-P2P]]
- [[entities/Zhurudong]]

### Concepts
- [[concepts/ABI-Compatibility]]
- [[concepts/Agent-Execution-Environment]] — Agent 执行层的隔离/资源/兜底
- [[concepts/Agent-Loop]]
- [[concepts/Agent-Memory]] — 长期记忆的存储/检索/压缩
- [[concepts/AI-Project-Differentiation]] — AI 项目差异化的策略与方法
- [[concepts/Automated-Input-Pipeline]]
- [[concepts/CLAUDE-MD-Two-Layer-Navigation]]
- [[concepts/Fleeting-Capture]]
- [[concepts/Folder-as-an-APP]]
- [[concepts/LLM-Wiki]]
- [[concepts/Multi-Agent-Collaboration]] — 多 Agent 协作的两种编排范式
- [[concepts/Personal-Knowledge-Asset]]
- [[concepts/Progressive-Disclosure]]
- [[concepts/RAG-vs-LLM-Wiki]]
- [[concepts/RAG-三层混合检索]]
- [[concepts/type-name-of-val]]
- [[concepts/三级连接回退]]
- [[concepts/哈希链可信存证]]
- [[concepts/国产化演进]]
- [[concepts/多协议融合]]
- [[concepts/容器化部署]]
- [[concepts/纵深防御]]
- [[concepts/统一身份源]]
- [[concepts/统一权限源]]

### Comparisons
- [[comparisons/LDAP-vs-关系数据库]]
- [[comparisons/Obsidian-vs-Milanote]]
- [[comparisons/POSIX-ACL-vs-Unix权限]]
- [[comparisons/四种文件协议对比]]

### Synthesis
- [[synthesis/Two-Knowledge-Base-Approaches-Comparison]]

# 操作日志

## 2026-07-13 — 采集 4 篇牛客网 AI 求职文章

**重命名**：`raw/casually/` 中 4 篇命名不规范的文件：
  - `找工作神器笔试题库面试经验实习招聘内推，求职就业一站解决_牛客网.md` → `2026-07-13-面试官视角的AI时代筛选逻辑.md`
  - `Agent相关的项目怎么做才值得写进简历？说几个真实可落地的方向。_牛客网.md` → `2026-07-13-Agent项目的三个落地方向.md`
  - `🚨你的AI项目，为什么总跟别人"撞车"？_牛客网.md` → `2026-07-13-AI项目差异化方法论.md`
  - `ai项目要有差异化_牛客网.md` → `2026-07-13-AI项目避坑与加分项指南.md`

**新增摘要（4 篇）**：
  - `wiki/summaries/面试官视角的AI时代筛选逻辑.md` — 面试官视角：AI 把实现能力拉平后，筛选转向判断力（为什么/边界/失败三层追问）
  - `wiki/summaries/AI项目避坑与加分项指南.md` — 春招亲测：3 个巨坑 + 4 个面试加分项目（MCP 电商 Agent、多模态 RAG 质检、本地代码审计、端侧日程）
  - `wiki/summaries/AI项目差异化方法论.md` — 找差异化方向的三条路径 + 四步落地法（痛点出发/AI 改版/垂直跨界）
  - `wiki/summaries/Agent项目的三个落地方向.md` — 任务自动化 Agent / 多 Agent 协作 / 带记忆个人助手

**新增实体（6 个）**：
  - `entities/LangGraph.md` — 图结构多 Agent 编排框架
  - `entities/AutoGen.md` — 微软对话式多 Agent 编排框架
  - `entities/LangChain.md` — LLM 应用框架（附同质化陷阱警示）
  - `entities/Chroma.md` — 轻量向量数据库（附同质化警示）
  - `entities/Llama.md` — Meta 开源大模型
  - `entities/Qwen2.md` — 阿里开源端侧推理模型

**新增概念（4 个）**：
  - `concepts/Agent-Execution-Environment.md` — Agent 执行环境：隔离/资源/并发/兜底的工程层设计
  - `concepts/AI-Project-Differentiation.md` — 差异化策略：垂直场景 + 工程化 + 真实数据的求职竞争力
  - `concepts/Multi-Agent-Collaboration.md` — 多 Agent 协作的两种编排范式（图 vs 对话）
  - `concepts/Agent-Memory.md` — 长期记忆系统的三大技术挑战

**更新已有页面**：
  - `entities/MCP.md`、`entities/RAG.md`、`concepts/Agent-Loop.md` — 补入新来源引用
  - `wiki/_index.md` — 新增「AI 求职与项目策略」主题，更新全部页面列表

## 2026-07-07 — 采集 NAS 智能存储平台技术架构

**采集**：`raw/definitely/NAS智能存储平台技术架构设计说明书.pdf`（56 页，V1.1）
  - PDF 通过 pdfplumber 提取文字，转为 `raw/definitely/NAS智能存储平台技术架构设计说明书.md`
  - 新增 `wiki/summaries/NAS智能存储平台技术架构.md`

**新增实体（20 个）**：
  - `entities/OpenLDAP.md`、`entities/POSIX-ACL.md`、`entities/authd.md`
  - `entities/MCP.md`、`entities/RAG.md`、`entities/Docker.md`
  - `entities/Go.md`、`entities/Gin.md`、`entities/Samba.md`、`entities/NFS.md`
  - `entities/WebDAV.md`、`entities/JWT.md`、`entities/SQLite.md`
  - `entities/PUF.md`、`entities/SHA-256.md`、`entities/Nginx.md`
  - `entities/mDNS.md`、`entities/WiFi-P2P.md`、`entities/Next.js.md`、`entities/React-Native.md`、`entities/NFC.md`

**新增概念（10 个）**：
  - `concepts/统一身份源.md`、`concepts/统一权限源.md`、`concepts/哈希链可信存证.md`
  - `concepts/Agent-Loop.md`、`concepts/多协议融合.md`、`concepts/纵深防御.md`
  - `concepts/RAG-三层混合检索.md`、`concepts/三级连接回退.md`
  - `concepts/国产化演进.md`、`concepts/容器化部署.md`

**新增对比（3 个）**：
  - `comparisons/LDAP-vs-关系数据库.md`、`comparisons/四种文件协议对比.md`、`comparisons/POSIX-ACL-vs-Unix权限.md`

**更新**：`wiki/_index.md`（新增 NAS 智能存储平台架构主题，更新全部页面列表）

## 2026-07-07 — 补充采集 Karpathy 文章

**采集**：[Paula 寶拉：Karpathy 筆記術教程](https://www.youtube.com/watch?v=FdSO1Yhr76I)
  - raw 文件已存在 → 重命名为 `raw/2026-04-14-Karpathy-knowledge-base-tutorial.md`
  - 新增 `wiki/summaries/Karpathy-knowledge-base-tutorial.md`
  - 新增 `wiki/entities/Paula-Baola.md`
  - 更新 `wiki/entities/Andrej-Karpathy.md`（增量）

**采集**：[zhurudong/andrej-karpathy-llm-wiki](https://github.com/zhurudong/andrej-karpathy-llm-wiki)
  - raw 文件已存在 → 重命名为 `raw/2026-02-12-karpathy-llm-wiki-template.md`
  - 新增 `wiki/summaries/Karpathy-llm-wiki-template.md`
  - 新增 `wiki/entities/Zhurudong.md`
  - 新增 `wiki/concepts/LLM-Wiki.md`
  - 新增 `wiki/concepts/RAG-vs-LLM-Wiki.md`
  - 更新 `wiki/entities/Andrej-Karpathy.md`（增量）

## 2026-07-07 — 知识库架构改进

**改进内容**：
- 新增 `context/about.md` 和 `context/preferences.md`（用户画像）
- 新增各目录 `instructions.md`：`raw/`、`wiki/summaries/`、`wiki/entities/`、`wiki/concepts/`、`wiki/comparisons/`、`projects/`
- 更新 `CLAUDE.md`：会话启动规则（先读 context）、深化编译标准、两层导航
- 升级 `wiki/_index.md`：按主题聚合 + 按类型罗列双结构

**重写（新深度标准）**：
- `wiki/summaries/Rust-1.76.0.md`（15行 → 70行）
- `wiki/entities/Rust.md`（6行 → 45行）
- `wiki/concepts/ABI-Compatibility.md`（14行 → 55行）
- `wiki/concepts/type-name-of-val.md`（25行 → 63行）

## 2026-07-06
- **采集**：[Rust 1.76.0 Release Blog](https://blog.rust-lang.org/2024/02/08/Rust-1.76.0/)
  - 新增 `raw/2024-02-08-Rust-1.76.0.md`
  - 新增 `wiki/summaries/Rust-1.76.0.md`
  - 新增 `wiki/entities/Rust.md`
  - 新增 `wiki/concepts/ABI-Compatibility.md`
  - 新增 `wiki/concepts/type-name-of-val.md`
  - 创建 `wiki/_index.md`

- **采集**：[你为什么立即要用Obsidian+AI搭建第二大脑？保姆级教程｜Claude Code+Obsidian](https://www.youtube.com/watch?v=RZEb6FLZSHE)
  - raw 文件已存在（用户预先放置）
  - 新增 `wiki/summaries/Obsidian-Claude-Code-Second-Brain.md`
  - 新增 `wiki/entities/Obsidian.md`
  - 新增 `wiki/entities/Claude-Code.md`
  - 新增 `wiki/entities/Milanote.md`
  - 新增 `wiki/entities/Andrej-Karpathy.md`
  - 新增 `wiki/entities/Serena-Xinxin.md`
  - 新增 `wiki/concepts/CLAUDE-MD-Two-Layer-Navigation.md`
  - 新增 `wiki/concepts/Progressive-Disclosure.md`
  - 新增 `wiki/concepts/Personal-Knowledge-Asset.md`
  - 新增 `wiki/concepts/Fleeting-Capture.md`
  - 新增 `wiki/concepts/Automated-Input-Pipeline.md`
  - 新增 `wiki/concepts/Folder-as-an-APP.md`
  - 新增 `wiki/comparisons/Obsidian-vs-Milanote.md`

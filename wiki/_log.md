# 操作日志

## 2026-07-19 — 深度拆解儿童留存机制与飞书文档上传

**活动**：深度拆解让儿童主动使用产品的核心机制（小天才/步步高/讯飞/多邻国/可汗/Tamagotchi/Minecraft）
- 确立了 NAS 「三层留存架构」（首日钩子、每日连载循环、长期成长资产）
- 利用本地 `lark-cli` 工具，成功在飞书文档 `7.23` (Ye3xw7Z3Ai1POIkPvHacCDsRnju) 下创建子文档，并上传约 9000 字的深度调研报告：`如何让儿童主动使用产品：竞品留存机制与游戏化设计深度调研报告.md`。

## 2026-07-18 — 黄老师四次问答：NAS 家庭教育智能体产品逻辑梳理

**来源**：`D:\Users\likeu\Desktop\7.16\黄老师.md`（不进入 raw/，非公开素材）
**新增 synthesis**：`wiki/synthesis/NAS家庭教育智能体-黄老师四次问答梳理.md`
  - 四次问答的思想脉络：定位（心理学归因理论）→ 工程落地（五层开源架构）→ 载体与隐私（后台画像前台游戏）→ 冷启动（普遍规律过渡到个体画像）
  - 与现有 NAS 项目映射：可直接复用的技术底座（OpenLDAP、POSIX ACL、authd、SQLite、哈希链），需新增的能力（拾音终端、语音处理层、声纹过滤引擎、隐私盾、儿童交互界面）
  - 四个待讨论的矛盾与选择：终端形态、MVP 范围、开源策略、数据归属
**更新索引**：`_index.md` synthesis 区新增条目

## 2026-07-13 — 补充采集 2 篇 Agent 学习路线文章

**采集**：[如何成为一个AI Agent工程师？2026版学习路线](https://www.nowcoder.com/discuss/879367411529506816?sourceSSR=search)
  - raw → `raw/casually/2026-04-30-AI-Agent工程师学习路线.md`
  - 新增 `wiki/summaries/AI-Agent工程师学习路线2026.md`
  - 核心贡献：先搞懂 Agent 在哪会坏（FC 底层机制、ReAct 四大失败模式、Context 限制、Prompt Caching），再学框架。2026 必学 MCP + BFCL + 流式工具调用。Memory 三层、五个大坑、简历金标准模板。

**采集**：[26年全网最全Agent学习路线，拿走不谢！](https://www.nowcoder.com/discuss/864821937527128064?sourceSSR=users)
  - raw → `raw/casually/2026-03-21-Agent学习路线七层递进.md`
  - 新增 `wiki/summaries/Agent学习路线七层递进.md`
  - 核心贡献：从 Java 后端转 Agent 的实操指南，重点论证 RAG 为何是后端转 Agent 的关键切入点——RAG 五步与后端技术栈一一对应。企业级 RAG > Demo 级 RAG 的四个工程维度（数据/性能/质量/架构）。

**更新已有**：MCP、RAG、LangGraph、LangChain、Agent-Loop、Agent-Memory 页面补入新来源
**更新索引**：`_index.md` 新增两篇摘要

## 2026-07-13 — 补充采集 2 篇 Agent 学习路线文章

## 2026-07-16 — 审计 + 修复链接 + 补充采集 2 篇

**审计发现与修复**：
  - 🔴 死链 3 处 → 已修复：删除 `[[entities/Ollama]]`（改为纯文本）、删除 `[[concepts/Minimum Viable AI Product]]`（未创建）、删除 `[[concepts/MCP Protocol Integration]]`（改为 `[[entities/MCP]]`）
  - 🔴 命名不一致 19 处 → 已全部修复：`[[concepts/Multi-Agent Collaboration]]` → `Multi-Agent-Collaboration`（6 处）、`Agent Execution Environment` → `Agent-Execution-Environment`（6 处）、`AI Project Differentiation` → `AI-Project-Differentiation`（5 处）、`Agent Memory` → `Agent-Memory`（2 处）
  - ✅ 索引一致性：`_index.md` 链接全部正确
  - ✅ 内容矛盾：无
  - ⚠️ 会话启动扫描遗漏：raw/definitely/ 中的新文件未被自动检测——CLAUDE.md 规定了扫 casually 和 definitely，但实际执行时只扫了 casually（已记录为流程缺陷）

**采集（遗漏补采）**：
  - `raw/definitely/2026-07-16-Agent赛道四大岗位精准对标.md`：Agent 赛道两大方向 × 四大岗位（应用开发/核心研发/解决方案/Infra），按岗位倒推技术栈
    - 新增 `wiki/summaries/Agent赛道四大岗位精准对标.md`
  - `raw/definitely/2026-07-16-AI-Agent技术学习清单从入门到offer.md`：6 层学习清单 + 3 月路线 + 面试题总结
    - 新增 `wiki/summaries/AI-Agent技术学习清单从入门到offer.md`
  - 更新 `_index.md`、`_log.md`

## 2026-07-16 — 修复审计死链 + 新增 Agent 学习路线 2 篇

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

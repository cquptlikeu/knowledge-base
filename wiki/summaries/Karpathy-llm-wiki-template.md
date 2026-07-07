---
type: summary
created: 2026-07-07
updated: 2026-07-07
tags: [Karpathy, 知识库, CLAUDE.md, LLM Wiki, 开源]
source: "[[raw/2026-02-12-karpathy-llm-wiki-template]]"
---

# zhurudong/andrej-karpathy-llm-wiki：一个 CLAUDE.md 就是整个知识库

**作者**：[[entities/Zhurudong]]
**来源**：GitHub 开源仓库
**最后更新**：2026-02 前后

## 核心观点

**一个 `CLAUDE.md` 文件 = 一个自维护的本地知识库程序。** 不需要后端、不需要向量数据库、不需要 RAG 框架。这个开源仓库是我们当前知识库的直接实现参考——[[entities/Andrej-Karpathy]] 提出概念，zhurudong 把它做成了一个可安装的模板。

> 原文金句：*"One `CLAUDE.md` = a self-maintaining local knowledge base. No backend, no vector DB, no RAG framework."*
> 
> *"Everything is plain markdown — works with any editor, Git, grep. The knowledge graph emerges naturally from `[[wiki-link]]` — no graph DB."*
> 
> *"Switching LLM tools requires zero data migration — the rules live in `CLAUDE.md`."*

## 为什么走第三条路

当前「个人知识库」方案只走两条路：

| 路径 | 缺点 |
|------|------|
| 笔记 App（Notion/Obsidian/Logseq） | 标记、链接、整理全靠手动 |
| RAG/向量搜索 | 需要 embedding 服务、向量数据库、ingestion pipeline——重、脆弱、不透明 |

这个项目走第三条路：**让 LLM 负责组织，用 Markdown 文件做载体，用 `[[wiki-link]]` 做图谱，用 LLM CLI 做运行时。**

## 设计优势

- **raw 不可变，wiki 可重建**：LLM 的编译产物可随时从 raw 重新生成
- **纯 Markdown**：任何编辑器、Git、grep 都能用
- **知识图谱自然涌现**：`[[wiki-link]]` 就是边，不需要图数据库
- **零迁移成本**：规则全在 `CLAUDE.md` 里，换 LLM 工具只需 swap 规则文件

## 目录结构

与我们的知识库几乎相同：

```
my-knowledge-base/
├── CLAUDE.md                # 规则文件（LLM 读它来运行）
├── raw/                     # 不可变的原始文章
│   └── YYYY-MM-DD-title.md
└── wiki/                    # LLM 生成的理解层
    ├── summaries/           # 文章摘要
    ├── entities/            # 人物、组织、产品、技术
    ├── concepts/            # 方法论、架构、理论
    ├── comparisons/         # A vs B 对比
    ├── overviews/           # 主题综述
    ├── synthesis/           # 问答存档
    ├── _index.md            # 内容索引
    └── _log.md              # 操作日志
```

## 三大工作流

1. **Ingest**：说 `ingest <URL>` → LLM 自动抓取 → 存 raw → 生成摘要 → 提取/更新实体和概念 → 判断是否生成对比或综述 → 更新索引 → 写日志
2. **Query**：自然语言提问 → LLM 先读 `_index.md` 定位 → 综合相关页面回答 → 跨多源的答案建议存档到 `synthesis/`
3. **Lint**：说 `lint wiki` → LLM 扫描死链、孤立页面、矛盾、过时信息、缺失交叉引用

## 跨 CLI 兼容

| CLI | 配置文件 |
|-----|---------|
| Claude Code | `CLAUDE.md` |
| Codex CLI | `AGENTS.md`（symlink 到 CLAUDE.md）|
| OpenCode | `AGENTS.md` |

## 与我们知识库的关系

我们的知识库 + CLAUDE.md 基本上是这个模板的增强版——在原始设计上额外加了：
- `context/` 用户画像
- `daily/` 会话日志
- per-directory `instructions.md` 两层导航
- 深化的编译深度标准（论证逻辑链、金句、误区、边界）

## 相关实体与概念

- [[entities/Zhurudong]] — 项目作者
- [[entities/Andrej-Karpathy]] — 原始思想来源
- [[concepts/LLM-Wiki]] — 核心方法论
- [[entities/Claude-Code]] — LLM CLI 运行时

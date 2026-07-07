---
type: comparison
created: 2026-07-06
updated: 2026-07-06
tags: [obsidian, milanote, note-taking, knowledge-management, ai]
---

# [[entities/Obsidian]] vs [[entities/Milanote]]

## 对比结论

从 [[entities/Milanote]] 迁移到 [[entities/Obsidian]] 不是因为功能更多，而是因为 **Obsidian 的本地 Markdown 文件可以直接被 [[entities/Claude-Code]] 读取和写入**——这是 AI 时代知识管理的关键分水岭。

## 详细对比

| 维度 | Obsidian | Milanote |
|------|----------|----------|
| 存储方式 | 本地 Markdown + JSON 文件 | 云端（封闭格式） |
| AI 可读性 | ✅ 直接读写 | ❌ AI 难以系统读取 |
| 双向链接 | ✅ `[[wikilink]]` + 知识图谱 | ❌ 不支持 |
| 思维导图 | Canvas（JSON 格式，AI 可操作） | 原生画板（核心优势） |
| 插件生态 | 丰富（Web Clipper、Books Highlights 等） | 有限 |
| 同步 | iCloud（免费）/ Obsidian Sync（付费） | 云端内置 |
| 结构化导航 | 支持 CLAUDE.md + instructions.md 两层导航 | 层层嵌套，AI 导航困难 |
| 数据所有权 | 完全本地、完全私有 | 存在云端 |
| 任何 AI 可用 | ✅ 任何能读 Markdown 的 AI 都能用 | ❌ 依赖平台 API |

## 迁移策略

用 Claude Code 辅助迁移：截屏 Milanote 的思维导图 → 让 Claude Code 直接在 Obsidian Canvas（JSON）中复刻。

## 参考

- [[summaries/Obsidian-Claude-Code-Second-Brain]] — 迁移的完整背景和方法
- [[concepts/Personal-Knowledge-Asset]] — 为什么要本地化

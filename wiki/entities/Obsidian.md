---
type: entity
created: 2026-07-06
updated: 2026-07-06
tags: [obsidian, note-taking, markdown, knowledge-management]
aliases: [Obsidian 笔记, 黑曜石笔记]
---

# Obsidian

基于本地 Markdown 文件的知识管理/笔记工具。核心优势：本地文件、纯 Markdown、丰富插件生态、支持 [[wikilink]] 和知识图谱。

## 核心特性

- **本地优先**：所有笔记以 `.md` 文件存储在本地文件夹，可被任何文本编辑器或 AI 工具直接读写
- **Wiki 链接**：`[[page]]` 语法实现笔记之间的双向链接
- **Canvas**：基于 JSON 的思维导图/白板功能，支持 AI 操作
- **插件生态**：Web Clipper（网页剪藏）、Apple Books Highlights（电子书划线导入）等
- **CLI 工具**：官方提供命令行工具，可用于自动化操作

## 与 AI 工具的集成

[[entities/Claude-Code]] 可以直接读取和写入 Obsidian vault 中的 Markdown 文件，这是 Obsidian 在 AI 时代最重要的优势——详见 [[summaries/Obsidian-Claude-Code-Second-Brain]]。

对比 [[entities/Milanote]]：Milanote 存在云端且结构层层嵌套，AI 难以系统读取。Obsidian 的本地文件结构更适合 AI 操作。

## 参考

- [[summaries/Obsidian-Claude-Code-Second-Brain]]

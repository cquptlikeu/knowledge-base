---
type: entity
created: 2026-07-06
updated: 2026-07-06
tags: [claude-code, ai, cli, anthropic]
aliases: [Claude Code CLI]
---

# Claude Code

Anthropic 推出的 AI 编程命令行工具，可以直接读取和写入本地文件系统中的 Markdown 文件。

## 在知识管理中的应用

Claude Code 可以配合 [[entities/Obsidian]] 构建 AI 第二大脑：
- 直接读写 Obsidian vault 中的 Markdown 文件
- 通过 `CLAUDE.md` 作为入口了解用户和项目结构
- 支持 Skills 系统执行特定任务
- 支持 YOLO 模式（自动批准操作）

## 核心机制

- **CLAUDE.md**：项目/知识库的入口文件，每次启动时读取
- **渐进式披露**：按需读取相关内容，不一次性加载整个目录
- **Daily Notes**：通过每日日志实现跨会话连续性

## 参考

- [[summaries/Obsidian-Claude-Code-Second-Brain]]
- [[concepts/CLAUDE-MD-Two-Layer-Navigation]]
- [[concepts/Progressive-Disclosure]]

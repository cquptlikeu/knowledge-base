---
type: concept
created: 2026-07-06
updated: 2026-07-06
tags: [token-optimization, claude-code, design-pattern, anthropic]
aliases: [渐进式披露, 按需加载]
---

# 渐进式披露（Progressive Disclosure）

Anthropic 设计 [[entities/Claude-Code]] 的核心设计原则：AI 不需要一次性读取所有内容，只需按需给它当前所需的上下文。

## 在知识管理中的应用

当笔记库越来越大时，让 AI 每次扫描整个库既不现实也不必要。正确做法：

1. 提供顶层索引（总目录）
2. AI 根据任务按需深入子目录
3. 每次只加载必要的最小上下文

这个概念在 [[concepts/CLAUDE-MD-Two-Layer-Navigation]] 中得到了具体实现。

## 参考

- [[summaries/Obsidian-Claude-Code-Second-Brain]]
- [[concepts/CLAUDE-MD-Two-Layer-Navigation]]

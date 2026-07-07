---
type: concept
created: 2026-07-06
updated: 2026-07-06
tags: [claude-code, token-optimization, navigation, architecture]
aliases: [两层导航, CLAUDE.md 导航系统]
---

# CLAUDE.md 两层导航

在 [[entities/Obsidian]] + [[entities/Claude-Code]] 的知识库系统中，通过两层导航结构控制 [[entities/Claude-Code]] 的 Token 消耗。

## 结构

| 层级 | 位置 | 内容 |
|------|------|------|
| 第一层 | 根目录 `CLAUDE.md` | 介绍用户 + 文件夹地图（什么时候读哪个文件夹） |
| 第二层 | 每个文件夹内的 `instructions.md` | 该文件夹的具体结构、命名规则、操作说明 |

## 工作流程

1. Claude 启动时读取根目录 `CLAUDE.md` → 了解用户和文件夹地图
2. 根据任务类型，按 `CLAUDE.md` 的指引进入目标文件夹
3. 读取目标文件夹的 `instructions.md` → 了解局部结构和操作规则
4. 执行任务 → 只读了两个文件，而非整个 vault

## 为什么有效

这是 [[concepts/Progressive-Disclosure]] 在本地文件系统中的实践——AI 永远只读当下需要的那一层，不会扫描整个笔记库。

## 参考

- [[summaries/Obsidian-Claude-Code-Second-Brain]]
- [[concepts/Progressive-Disclosure]]

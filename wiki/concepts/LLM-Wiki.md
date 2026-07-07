---
type: concept
created: 2026-07-07
updated: 2026-07-07
tags: [knowledge-base, llm, karpathy, methodology]
aliases: [LLM Wiki, Karpathy Wiki 方法]
---

# LLM Wiki（Karpathy 知识库方法）

由 [[entities/Andrej-Karpathy]] 提出并实践的个人知识库构建方法。核心公式：**一个 `CLAUDE.md` + 两个文件夹（raw + wiki）+ 一个 LLM CLI = 自维护的本地知识库。**

## 核心思想

传统的个人知识管理走两条路：笔记 App（整理全靠手动）或 RAG（重基础设施）。LLM Wiki 走第三条路：**让 LLM 担任图书管理员**——负责拆解、分类、链接、索引、健康检查。

## 为什么不需要 RAG

> 原文引用：*"He originally thought he'd need RAG, but letting the LLM maintain the index itself was enough."* — Paula 视频中对 Karpathy 观点的转述

Karpathy 组织了约 100 篇文章后发现：LLM 读索引定位 + 按 wikilink 跳转的效果已经足够好。核心差异见 [[concepts/RAG-vs-LLM-Wiki]]。

## 什么时候用

- 个人知识积累，几十到几百篇文章级
- 需要 AI 自动发现跨文章关联
- 想要完全本地化、私有的知识系统
- 数据格式希望是纯 Markdown（任何工具都能读）

## 什么时候不要用

- **万级以上的文档量**：Karpathy 自己也说这个规模还是需要真正的 RAG。个人使用很难达到这个量
- **需要实时搜索的企业应用**：没有 embedding 的语义搜索，纯靠索引定位
- **多人高频协作**：LLM Wiki 本质是个人工具，多人同时编辑会有冲突

## 常见误区

> 「LLM Wiki 就是 RAG 的简化版」

不完全对。LLM Wiki 的查询机制和 RAG 有根本区别——它不是靠向量相似度匹配，而是像人翻目录一样读索引→按链接跳转。这带来零基础设施成本的巨大优势，但也有精度上限。

> 「可以替代所有笔记 App」

LLM Wiki 擅长的是**编译和检索**，不是**随手记**。它不替代 obsidian 的手动笔记功能——它是笔记库上的 AI 层。

## 我们的实践

本知识库是 LLM Wiki 的增强实现——在 Karpathy/zhurudong 原始设计上增加了 `context/`（用户画像）、`daily/`（会话日志）、per-directory `instructions.md`（两层导航）、深化编译标准。

## 参考

- [[summaries/Karpathy-knowledge-base-tutorial]]
- [[summaries/Karpathy-llm-wiki-template]]
- [[summaries/Obsidian-Claude-Code-Second-Brain]]
- [[entities/Andrej-Karpathy]]
- [[entities/Zhurudong]]
- [[concepts/RAG-vs-LLM-Wiki]]

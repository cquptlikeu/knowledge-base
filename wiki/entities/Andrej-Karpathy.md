---
type: entity
created: 2026-07-06
updated: 2026-07-07
tags: [ai, researcher, tesla, openai]
aliases: [Karpathy, Andrej Karpathy]
---

# Andrej Karpathy

前 Tesla AI 总监、OpenAI 联合创始人，AI 时代最具影响力的工程师之一。

## 核心贡献

### LLM Wiki 模式

提出用 LLM 对本地原始信息进行结构化编译，构建个人知识系统。核心理念：每天接触大量原始信息（推文、文章、会议记录、读书笔记），用 LLM 本地处理 → 结构化知识 → 用 AI 工具查看和操作 → 随时间积累越来越强。

该模式的关键特征：
- **不要 RAG**：Karpathy 原以为自己需要 RAG，后来发现让 LLM 自己维护索引就够了。大约组织了 100 篇文章后发现索引方案完全够用
- **AI 负责维护**：几乎不需要手动编辑 Wiki——编译和维护全是 LLM 的工作
- **健康检查**：AI 可以定期扫描知识库，发现矛盾、空白，主动建议补充
- **归档问答**：每次向 AI 提问后，答案存回 Wiki，知识库越用越丰富

### 原始 Gist

Karpathy 的原始 prompt 发布在：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

zhurudong 在此基础上做了可安装的开源实现：[[entities/Zhurudong]]

## 参考

- [[summaries/Obsidian-Claude-Code-Second-Brain]]
- [[summaries/Karpathy-knowledge-base-tutorial]]
- [[summaries/Karpathy-llm-wiki-template]]
- [[concepts/Personal-Knowledge-Asset]]
- [[concepts/LLM-Wiki]]

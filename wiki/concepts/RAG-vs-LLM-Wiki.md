---
type: concept
created: 2026-07-07
updated: 2026-07-07
tags: [rag, llm-wiki, comparison, knowledge-management]
aliases: [RAG vs LLM Wiki, 向量检索 vs 索引定位]
---

# RAG vs LLM Wiki

两种用 AI 管理大型文本集合的方法论对比。RAG 是 embedding + 向量数据库的工程方案，LLM Wiki 是纯 Markdown + 索引的极简路线。

## 核心思想

两者解决同一个问题——「如何让 AI 在大批文档中找到相关内容」——但走完全相反的路。RAG 走**语义近似**路线（「这段文字和问题在语义空间里近不近」），LLM Wiki 走**结构化索引**路线（「这个话题在哪个目录里」）。

## 详细对比

| 维度 | RAG | LLM Wiki |
|------|-----|----------|
| **核心技术** | embedding + 向量数据库 | Markdown + `[[wikilink]]` + 索引 |
| **查询方式** | 语义向量相似度搜索 | 读索引→按链接定位相关页面 |
| **基础设施** | embedding 服务、向量数据库、ingestion pipeline | 无。只需要文件和 LLM CLI |
| **查准率** | 高（向量搜索可以找到你没预料到的相关） | 中（依赖索引和 wikilink 的覆盖度） |
| **查全率** | 中（可能漏掉相关但不相似的） | 高（通过索引 + 链接的网络可以遍历） |
| **搭建门槛** | 高 | 低——几分钟 |
| **维护成本** | 高——管线脆弱、不透明 | 低——纯文件，Git 可管理 |
| **规模上限** | 万级+ | ~100-500 篇（个人实践上限） |
| **语义发现** | 强——embedding 可以发现「看似无关但语义相关」 | 弱——只能靠已有的 wikilink 网络 |
| **可解释性** | 弱——「为什么返回这篇」难以解释 | 强——可以追溯「索引→链接→页面」的路径 |
| **数据迁移** | 难——依赖特定向量数据库 | 零——纯文件，复制粘贴即可 |

## 什么时候选 RAG

- 企业应用，文档量万级以上
- 需要语义搜索——用户问的问题用词和文档完全不同
- 有团队维护基础设施

## 什么时候选 LLM Wiki

- 个人知识库，几十到几百篇
- 想要零依赖、零维护
- 希望数据完全本地化、私有化
- 需要跨工具兼容（任何 LLM CLI 都能用）

## Karpathy 的实践结论

Karpathy 本来以为自己需要 RAG，用 LLM Wiki 方法组织约 100 篇文章后发现：**让 LLM 读索引就够了，不需要向量搜索。** 这是最关键的经验数据——100 篇的规模，索引方案完全可行。

## 参考

- [[summaries/Karpathy-knowledge-base-tutorial]]
- [[summaries/Karpathy-llm-wiki-template]]
- [[concepts/LLM-Wiki]]
- [[entities/Andrej-Karpathy]]

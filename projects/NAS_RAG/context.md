---
project: NAS_RAG
stack: [Python, LlamaIndex, ChromaDB, sentence-transformers, jieba, RapidOCR]
status: active
---

## 项目概述
个人 NAS 多模态文件检索 —— 检索质量与评估(一期)。评估驱动的多模态检索质量工程切片，核心命题：混合检索(元数据过滤+BM25+向量+重排)优于纯语义检索。

## 当前状态
- 已完成：S0(环境+骨架+评估核心 TDD)+ S1.1(数据合同与不变量)
- 正在进行：S1 语料构建与多模态摄取
- 已知阻塞：无

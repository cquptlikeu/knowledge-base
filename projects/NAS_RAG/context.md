---
project: NAS_RAG
stack:
  - Python 3.12
  - LlamaIndex
  - Chroma
  - bge-m3
  - BM25
  - RapidOCR
  - sentence-transformers
status: active
tags:
  - project/nas-rag
---
## 项目概述
个人 NAS 多模态文件检索 —— 检索质量与评估（一期）。一个**评估驱动的多模态检索质量工程切片 / 简历项目**，不是上线产品。

核心命题：**真实"找文件"的需求大量是非语义的 → 混合检索（元数据过滤 + BM25 + 向量 + 重排）优于纯语义检索**，优幅由实测决定。

- 仓库：`F:\develop\code\vsCode\agent-learning\NAS_RAG`
- 远程：`https://github.com/cquptlikeu/Nas_Rag.git`
- 技术栈：Python 3.12 (conda) · LlamaIndex（原语库）· Chroma（向量库）· bge-m3（embedding）· bge-reranker-v2-m3（重排）· BM25（词法）· RapidOCR
- 方法论：评估优先（尺子先于一切）· TDD · 不可变领域模型 · 单一真源

## 当前状态

### 已完成
- **S0** 环境 + 骨架 + 评估核心 TDD 落地（match / capability / metrics / ground_truth / attribution），pytest 70 passed
- **S0.2** OCR 引擎选定 RapidOCR（numpy-2 兼容，弃 FlagEmbedding 单后端）
- **S0.3** 评估核心纯函数 + 黄金 fixtures（跨年、半开、NFC、2307、归因四分支）
- **S0.4** 依赖锁版（environment.lock.yml / requirements.lock.txt）+ verify_repro 骨架
- **S1.1** manifest/errors 数据合同 + 不变量测试落地（text=null、epoch 成对、synthetic_fields 披露、video/media 能力边界），pytest 85 passed

### 正在进行
- **S1.2** 10–20 文件 dry-run（即将开始）

### 已知阻塞
- 无。S1 ready_with_caveats，阶段真源文档 docs/stages/S1.md 已冻结。

## 关键架构决策
见 [[decisions|decisions.md]]

## 最近会话
见 [[sessions|sessions.md]]

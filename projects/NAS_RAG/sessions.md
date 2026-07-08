## 最近会话（最近 5 条，完整保留）

### 2026-07-08 深夜 — S1.1 数据合同与不变量落地
- 做了什么：在 `src/nas_rag/corpus/` 下建立 manifest/errors 正式数据合同模型（models.py / errors.py / validators.py），写契约测试 15 passed；补 tests 包 `__init__.py` 消除同名模块收集冲突
- 什么决定：合同层锁死 text=null（photo/video/media）、epoch 成对、坏文件保留、synthetic 披露、video 不得带 location、media 不得有 text
- 什么还没做完：S1.2 10–20 文件 dry-run 还没开始

### 2026-07-08 晚间 — S1 启动前多 Agent 建议
- 做了什么：用 4 视角工作流（产品边界 / 架构风险 / 评估诚信 / 执行顺序）产出 S1 readiness council，共识为 ready_with_caveats
- 什么决定：S1 必须先锁合同再 dry-run 再全量；S1 只交付 manifest/errors，不交付检索效果结论
- 什么还没做完：转为起草并冻结 docs/stages/S1.md

### 2026-06-28 下午 — S0.4 锁版收尾 + S0.3 提交
- 做了什么：导出 environment.lock.yml / requirements.lock.txt；搭 verify_repro 骨架；README 复现说明；S0.3 提交（评估核心 TDD 落地）
- 什么决定：S0 整体 DoD 闭合，进入 S1；git 边界已更正为"嵌套独立仓库"（CLAUDE.md §0/§12 + S0.md）
- 什么还没做完：S1 阶段文档 + 实现

### 2026-06-28 上午/中午 — S0.3 评估核心 TDD
- 做了什么：TDD 写出 domain/models + match + eval/metrics + capability + ground_truth + attribution；67 passed
- 什么决定：拍板四条口径——semantic=子串包含 AND、time=created_epoch、precision 分母=min(k,len)、文件名粘连保留整体 q3
- 什么还没做完：锁版 + verify_repro 骨架

### 2026-06-27 下午 — S0.1/S0.2 骨架 + 冒烟门禁
- 做了什么：conda env 建立 + 目录骨架 + config 单一真源；核心依赖冒烟门禁；OCR 选定 RapidOCR
- 什么决定：跳过 PaddleOCR（numpy-2 降级风险）、RapidOCR(onnxruntime) 装包最稳；environment.yml 去 defaults 只留 conda-forge
- 什么还没做完：S0.3 评估核心 TDD

---

## 历史摘要（按月压缩）

### 2026-06 月汇总
- 关键决策：semantic GT 匹配=子串包含（非分词）、time=created_epoch 单字段、precision 分母=min(k,len)、文件名字母数字粘连保留整体 q3
- 重要里程碑：S0 完整闭合（环境→骨架→冒烟门禁→评估核心 TDD→锁版）+ S1.1 数据合同落地
- 架构决策：RapidOCR 当选（弃 PaddleOCR 因 numpy 降级风险）、git 边界更正（NAS_RAG 为嵌套独立仓库）、manifest/errors 合同与不变量锁死
- 踩坑：清华镜像 `pkgs/free` 已弃用导致 conda env create 超时（修复：去 defaults + 只用 conda-forge）；tests/corpus 与 tests/domain 同名 test_models.py 冲突（修复：clean __pycache__ + 补 __init__.py）

# 会话记录

## 最近会话（最近 5 条，完整保留）

### 2026-07-08 晚间 — S0 全阶段完成(S0.1~S0.4)+ S1.1 数据合同落地
- **做了什么**
  - S0.1：conda 环境(修 environment.yml 去 defaults 只留 conda-forge)+ 仓库骨架 + config 单一真源(settings/type_labels/capability_matrix,矩阵对齐 AD-5)+ pytest 骨架冒烟 → 4 passed
  - S0.2：核心依赖冒烟门禁(tests/test_smoke_imports.py,22 passed)+ OCR 回退链选定 rapidocr-onnxruntime(跳过 Paddle 以避 numpy-2 降级)→ 26 passed
  - S0.3：评估核心 TDD 落地——不可变领域模型 + match(epoch 半开/NFC/分词/q3保留整体)/capability(子集判定)/metrics(recall-precision-ndcg-mrr)/ground_truth(created_epoch 统一)/attribution(归因四分支),pytest 67 passed → 补 review 后修补 ground_truth 契约收窄至 FileRecord + 补 modified_epoch 反例 + NFC 集成测试
  - S0.4：锁版(environment.lock.yml + requirements.lock.txt)+ verify_repro 骨架 + README 复现说明 + run_snapshot schema 占位 → 70 passed
  - S0 阶段全部提交并推送
  - 多 Agent S1 readiness council：结论 ready_with_caveats,先锁合同再 dry-run
  - 起草并冻结 docs/stages/S1.md(5 个子阶段、S1 只交付 manifest/errors,不交付检索效果)
  - S1.1：新增 corpus/models.py(manifest 合同)/errors.py(errors 合同)/validators.py(不变量校验),tests/corpus 15 passed,全量 85 passed
  - 修正 CLAUDE.md git 边界表述(NAS_RAG 是嵌套独立仓库,非 agent-learning 子目录/submodule)
  - 修正 README status("待建"→"S0.1 已建")
  - 修 environment.yml 去 defaults 防清华镜像超时
  - 新增 rapidocr-onnxruntime 到 environment.yml
- **什么决定**
  - semantic GT 匹配=子串包含(NFC+casefold, AND)
  - time 统一 created_epoch,photo 的 captured_epoch 在 S1 物化期对齐
  - precision@k 分母=min(k, len(ranked))
  - 文件名字母数字粘连保留整体 q3,剥离扩展名再分词
  - attribution 不保留 matrix 形参(YAGNI)
  - environment.yml 加 rapidocr-onnxruntime 而非留到 lock 文件(遵循 S1 边界)
  - S1 必须先做 dry-run(10-20 小样本)再扩全量
- **什么还没做完**
  - S1.1 已提交;S1.2(10-20 文件 dry-run)待开展

---

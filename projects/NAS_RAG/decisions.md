## 2026-06-28: RRF(k=60) 融合策略

- **背景**：PRD/ARCHITECTURE 已锁 hybrid retrieval 用 RRF 融合向量与 BM25 结果
- **选项**：加权求和（需调参 + 归一化 + 对量纲敏感）vs RRF（免归一化、对量纲不敏感、可解释）
- **选择**：RRF(k=60)，config/settings.py `FUSION` 字段单一真源
- **代价**：k=60 是经验值，CPU 下效果足够；若未来有 GPU 大规模调参可 A/B

## 2026-06-28: 语义 GT 匹配 = 子串包含（非分词）

- **背景**：GT 派生时判定 `text` 文件是否算某 query 的 semantic 正例，需固定口径
- **选项**：A) jieba 分词后 term 命中 → 把 jieba 版本脆性引入 GT；B) 子串包含 NFC+casefold → 确定性好、可手算
- **选择**：子串包含 AND（所有 semantic_terms 全部命中），在 match.py 作为 `semantic_match` 唯一真源
- **代价**：长文本中短词子串可能泛匹配（如来信 信中 → 命中"信任"）。由 `text` 内容+语义 terms 设计缓解

## 2026-06-28: time 分量统一 created_epoch

- **背景**：FileRecord 有三个 epoch（created/modified/exif.captured），GT 派生与检索 FilterSpec 必须同字段防漂移
- **选项**：A) 统一 created_epoch → 最简单零漂移；B) photo 优先 captured_epoch → 跨字段复杂化 AD-9
- **选择**：A 统一 created_epoch，photo 的拍摄时间在 S1 物化阶段令 created_epoch=captured_epoch
- **代价**：非 photo 类的 created 语义是文件创建时间、非内容时间，但已是最干净的口径锚点

## 2026-06-28: OCR 选定 RapidOCR（弃 PaddleOCR）

- **背景**：扫描件 OCR 回退链 PaddleOCR → RapidOCR → Tesseract，需选第一个装得上的
- **选项**：PaddleOCR → 拉 paddlepaddle 会降级 numpy 2→1.x 破坏整栈；RapidOCR(onnxruntime) → 自带小模型、装包最稳
- **选择**：RapidOCR，跳过 Paddle（numpy 降级风险不装），Tesseract 为后备
- **代价**：RapidOCR 中英文识别精度略低于 Paddle，但一期语料大部分直带 text，不强依赖 OCR

## 2026-06-28: precision@k 分母 = min(k, len(ranked))

- **背景**：标准 IR 分母恒为 k，但短结果时这道题有歧义
- **选项**：A) min(k, len) → 没检索到的位置不算判错；B) 恒 k → 短结果受惩罚
- **选择**：min(k, len)，配合 ranked≥K_MAX 硬约束生产路径等价
- **代价**：语义上与某些论文有微妙差异，但报告诚实标注口径即可

## 2026-06-28: 文件名字母数字粘连保留整体 q3

- **背景**：`Q3Report_v2.xlsx` 这类文件名在 BM25/分词时是否拆 `q3` → `q` + `3`
- **选项**：A) 保留整体 q3 → 与 substr_match 口径一致；B) 强拆 → 信号稀释
- **选择**：保留整体，剥离扩展名再分词，用 digit_run 保留纯数字串（如 2307）
- **代价**：`Q3Report` 整体保留时作为 BM25 token 低频但精准，后续可按实测调整

## 2026-06-28: git 边界更正

- **背景**：实测证实 NAS_RAG 是拥有独立 .git 与远程的嵌套独立仓库，非 agent-learning 的 submodule
- **选择**：更正 CLAUDE.md §0/§12 + S0.md S0.4 步骤 4 的 git 边界表述
- **代价**：父 agent-learning 也可 git add . 吸入本仓库（已在 §12 加防），后续操作注意嵌套边界即可

## 2026-07-08: manifest/errors 合同与不变量

- **背景**：S1.1 要求先锁数据合同再写实现，不能沿用 S0 的轻量评估视图
- **选择**：在 `src/nas_rag/corpus/` 下建立独立的 manifest/errors 合同模型与不变量校验函数，不从 `domain/models.py` 复用 FileRecord
- **代价**：corpus 层与 domain 层的 `FileRecord` 语义不同，需在后续 build pipeline 中做一次转换

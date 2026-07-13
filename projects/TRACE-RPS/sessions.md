# 会话记录

## 最近会话（最近 5 条，完整保留）

### 2026-07-10 深夜 — P1 闭合指南审计修复 + 验证完毕
- 多 Agent 审计 P1 闭合指南 v2，发现 8 处确认问题（F2 prompt 混淆、F4 无闭合标准、F7 可选停止、F9 B 行歧义、F10 新循环偏倚、M14 断链、A2 歧义），全部修复
- 验证所有 h2/h3 编号连续、4 个锚点链接有效
- 报告回用户 "验证通过"，列明 8 处改动

### 2026-07-09~10 — P1 闭合实验指南写作 + 多轮迭代
- 写 report/P1-closure-guide.md：7 章（当前状态 → 核心架构 → L2 A-vs-B 框架 → 操作手册 → 待做优先级 → 版本控制 → 附录）
- 多轮用户追问：A/A1/A2/A3 臂含义、P6/P7 功能、gen_model vs llm_model_path、各臂模型配置表
- 在工作指南中加 1.3 模型配置表、1.5 执行策略与 P1-clean 列、3.1 终端标准、A2=B 命名映射
- 用户指令 "开一个工作流，用多个 Agent 审查当前指南"，8 个 Agent 并行审计 → 发现 13 处问题 → 确认 7 处 → 修复

### 2026-06-24~25 — P7 重测 + P1 闭合统计验证
- P7 覆盖率新测：46.7%→88.8%（+42.1ppt）
- P7 隐私效果验证：deepseek-pro 评估 A2≈A1（所有 Δ≤4.1pt，n=124 不显著）
- P1 跨家族验证：road_A vs vanilla TRACE，Llama-3 攻击 + Qwen 裁判，124 样本
  - McNemar p=0.043/0.016/0.043 跨三个指标，3-way 整体 p=0.012
  - road_A 显著优于 vanilla
- 验证结论写入 memory/p7-coverage-vs-privacy.md、memory/p1-closure-roadA-vs-vanilla.md

### 2026-06-23~24 — P7 实现完毕 + P6 0.15 gate 验证
- P7 证据覆盖率提升——6 项改动：fuzzy filter + attention fallback + interleave merge + attacker evidence + max_anonymization_targets + 评估改进
- 241+72 tests passed
- P6 验证：0.15 语义门处于 dormant 状态（min seen 0.219 > 0.15），安全网就位但从未触发
- 模型部署：Qwen2.5-7B + Llama-3.1-8B → autodl，新建 conda env `road_A_eval`（transformers 4.44.2）
- 发现并修复 inference.py 入口误导——关键发现：inference.py 不运行 TRACE，正确入口是 `PYTHONPATH=. python anonymization/trace.py`

### 2026-06-22~23 — P6 语义效用门 + 实验框架搭建
- 实现 P6：all-MiniLM-L6-v2 cosine similarity gate（阈值 0.15），处决匿名化后语义差异过大的替代文本
- 修正 project-env-and-run memory——正确三阶段入口：defense → attack → evaluation
- 修正 trace_concurrent.py 忽略 trace_config 的文档
- 补充 A1/A3 消融臂定义到 memory

---

## 历史摘要（按月压缩，10-20 行/月）

### 2026-06 月汇总
- 关键决策：
  - road_A 分支采用 Attack-Verified 封闭回路：防御生成 → holdout 攻击验证 → 裁判评估
  - 选 cross-family holdout attacker + judge 作为 P1 闭合方向（Llama-3.1-8B + Qwen2.5-7B）
  - P6 语义门 0.15 为安全网（dormant），不调整
  - P7 证据改进虽大幅提升覆盖率但对 deepseek-pro 隐私无影响——需要在跨家族评估下重新验证
- 重要里程碑：
  - P6 实现完毕：语义效用门 at 0.15
  - P7 实现完毕：证据覆盖率 46.7%→88.8%
  - 模型部署：Qwen2.5-7B + Llama-3.1-8B on autodl
  - P1 闭合实验指南 v2 完成
- 踩坑：
  - inference.py 不运行 TRACE——三个阶段的实验全无效，正确入口是 trace.py
  - transformers 4.31 无法加载 Qwen2.5/Llama-3.1——新建 road_A_eval env
  - transformers 过新（>4.46）破坏 torch 2.0.1——pin 4.44.2
  - Llama-3.1 下载 32GB 含冗余 original/*.pth——加 --exclude
  - hf-mirror 偶尔限速 3.92MB/s——换 ModelScope 或等

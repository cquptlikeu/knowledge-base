# 架构决策记录

## 2026-06-22: road_A 采用 Attack-Verified 封闭回路

- **背景**：vanilla TRACE 防御无攻击反馈回路，无法验证防御对 holdout 攻击的实际效果
- **选项**：
  1. 保持 vanilla TRACE（单次防御，无攻击验证）
  2. Attack-Verified 封闭回路：防御 → holdout 攻击 → 裁判评估
- **选择**：选项 2，新建 road_A 分支
- **代价**：增加攻击阶段（多 ~2 分钟/样本），且当前读取 oracle target_label（P4 待解决）

## 2026-06-23: P1 跨家族评估 — Llama-3.1 attacker + Qwen2.5 judge

- **背景**：当前 ③holdout attacker 和 ②internal LLM 同属 deepseek 家族，存在循环自我评估风险
- **选项**：
  1. 保持 deepseek 家族全链路（快速但偏倚）
  2. 跨家族：Llama-3.1-8B attack + Qwen2.5-7B judge
  3. 三模型交叉验证矩阵
- **选择**：选项 2 作为 P1 闭合的最小可行方案
- **代价**：需下载部署两个新模型（~15GB each），需新建 conda env（transformers 4.44.2 vs road_A 的 4.31）

## 2026-06-23: P6 语义效用门 0.15 为安全网而非优化目标

- **背景**：median orig↔anon cosine 仅 0.337，匿名化过于激进。0.15 gate 保护语义最低底线
- **选项**：
  1. 调高门限到 0.3+ 强制改善语义保留
  2. 0.15 作为只拦截极端退化的安全网
- **选择**：选项 2。验证显示 min seen 0.219 > 0.15，门处于 dormant 状态
- **代价**：语义效用未主动优化，road_A 匿名化质量可能偏低

## 2026-06-25: P7 验证采用 deepseek-pro 评估（已知偏差）

- **背景**：P7 证据覆盖率 46.7%→88.8%，需评估对隐私的实际影响
- **选项**：用 deepseek-pro 先快速验证方向 vs 等跨家族评估
- **选择**：先 deepseek-pro 快速验证（A2≈A1，Δ≤4.1pt），再在跨家族框架复测
- **代价**：deepseek-pro 与 defender 同家族，可能低估 P7 效果——需跨家族重测确认

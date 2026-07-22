# 会话记录

## 最近会话（最近 5 条，完整保留）

### 2026-07-22 下午 — TRACE 内部机制改进建议分层分析
- 做了什么：对照当前 `anonymization/trace.py`、`anonymization/evidence.py` 与 P1 配置，核实现有方法实际是“最后一层、平均所有头、问题末 token 对评论 token 的 raw attention”；结合 Contrastive Attribution、AttnLRP、Activation Patching、Probe/Concept Erasure 与 Privacy Neuron 文献，将建议拆成目标对齐、机制定位、因果验证、威胁模型、系统角色和实验设计六个角度
- 什么决定：将建议理解为一条递进证据链，而非并列替代算法——目标 logit 定义解释对象，AttnLRP 筛选候选路径，Top-K patching 验证局部因果；同模型白盒解释保证内部归属，跨家族 attacker/judge 保证外部有效性
- 什么还没做完：未修改代码或启动实验；若继续实施，需先确定目标属性的多 token 序列分数、反事实 donor 构造和 A0-A3 单变量消融协议

### 2026-07-22 下午 — TRACE 论文笔记整理与事实校正
- 做了什么：读取飞书原文“论文笔记”，在同级知识空间创建“TRACE-RPS 论文与代码笔记（整理版）”；对照上游 TRACE-RPS 实现、当前 `road_A` 代码与 P1 配置，将内容重组为 9 章、5 张表，并保留原画板导出图和两张截图
- 什么决定：把“原作者模型搭配错误”收敛为“角色耦合的泛化风险”；明确 Qwen2.5 独立改写器尚未实现；把 P7 结论限定为“覆盖率提升但单组 DeepSeek-v4-pro 实验未见显著隐私收益”；澄清前 6 条截断不等于证据全局丢失
- 什么还没做完：证据反事实验证、改写器角色解耦与 P7 跨家族复测仍待后续实验

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

---
project: TRACE-RPS
stack: [Python, PyTorch, Llama-2-7B, DeepSeek-Flash, Qwen2.5-7B, Llama-3.1-8B]
status: active
---

## 项目概述

TRACE-RPS — 安全导向的 AI 评估与迭代微调项目。核心目标：评估模型安全弱点 → 通过受控微调改善安全性 → 保持通用能力的同时减少有害行为。

当前在 `road_A` 分支上推 Attack-Verified TRACE（封闭回路防御 + 迭代攻击验证）。

## 当前状态

- **已完成**：P6（语义效用门 0.15）、P7（证据覆盖率 46.7%→88.8%，隐私中性）
- **已整理**：飞书“TRACE-RPS 论文与代码笔记（整理版）”已完成事实校正与结构重排，原文保持不变
- **已写作完毕**：P1 闭合实验指南 v2（位于report\P1-closure-guide.md）
- **正在进行**：P1 闭合实验（跨家族 holdout attacker + judge 替换 deepseek 家族评估）
  - 模型已部署：Qwen2.5-7B + Llama-3.1-8B 在 autodl（conda env `road_A_eval`，transformers 4.44.2）
  - 第二步待跑：A(vanilla) 防御 → A/B 跨家族重评 → A1/A3 消融
- **已知阻塞**：P4（无标签可部署停止条件）未开始，仍读 oracle target_label
- **待重测**：P7 在新跨家族评估框架下的覆盖率和隐私效果

## 最近会话

见 sessions.md（最近 5 条）

---
type: summary
created: 2026-07-06
updated: 2026-07-06
tags: [Obsidian, Claude Code, 第二大脑, 知识管理, AI]
source: "[[raw/casually/2026-04-26-obsidian-claude-code-second-brain]]"
---

# Obsidian + Claude Code 搭建 AI 第二大脑（保姆级教程）

**作者**：[[entities/Serena-Xinxin]]（Serena 心心加州）
**来源**：YouTube 视频
**发布日期**：2026-04-26

## 核心观点

从 [[entities/Milanote]] 迁移到 [[entities/Obsidian]] 的核心原因：Obsidian 的本地 Markdown 文件可以被 [[entities/Claude-Code]] 直接读取和写入，这是云笔记无法做到的。

## 系统架构

### 文件夹结构设计

设计原则：文件夹不只是给自己导航用的，更重要的是让 AI 知道去哪里找什么。

- **context/**：个人信息（我是谁、目标、表达风格），AI 每次先读这里
- **reading/**：读书笔记
- **clippings/**：网页剪藏
- **daily/**：每日笔记
- **skills/**：Claude Code Skills 存放处
- **根目录 CLAUDE.md**：第二大脑入口，只做两件事——介绍用户 + 给出文件夹地图

### 两层导航（Token 控制核心）

| 层级 | 文件 | 作用 |
|------|------|------|
| 第一层 | 根目录 `CLAUDE.md` | 总目录，指向正确的文件夹 |
| 第二层 | 每个文件夹的 `instructions.md` | 局部地图，告诉 Claude 该文件夹的结构和操作规则 |

→ 详见 [[concepts/CLAUDE-MD-Two-Layer-Navigation]]

AI 永远只读当前需要的那一层，不会扫描整个笔记库——这就是 **渐进式披露**（[[concepts/Progressive-Disclosure]]）的核心思想。

## 自动化输入管道

1. **Obsidian Web Clipper**：一键保存网页/推文/视频字幕为 Markdown
2. **Apple Books Highlights 插件**：自动导入电子书划线内容
3. **iPhone Action Button + Shortcuts**：一键录音 → 自动转文字 → 保存到 Daily Notes（闪念胶囊）

## 关键技巧

### 跨会话连续性
每天结束时让 Claude 把当天做了什么、需要跟进的事项写入 Daily Notes。下次新 Session 只需读最近几天的 Daily Notes，就能立即知道进展和阻塞。

### 节省 Token 策略
- CLAUDE.md 两层导航，按需读取
- 渐进式披露：不一次性加载整个笔记库
- 使用 Obsidian 官方 CLI 操作笔记，减少 Claude token 消耗

### Skills 与笔记库联动
Skills 的 reference 文档直接放在 Obsidian vault 里的 `skills/` 文件夹，Claude 指向本地的 skills。好处是 skills 可以随着笔记内容不断迭代优化。

## Karpathy 的愿景

[[entities/Andrej-Karpathy]] 提出：每天接触大量原始信息（推文、文章、会议记录、读书笔记），用 LLM 将这些信息本地结构化编译，再用 Obsidian + AI 查看和操作，就能拥有一个随着时间积累越来越强的**个人知识系统**（[[concepts/Personal-Knowledge-Asset]]）。这完全本地化、完全私有、任何 AI 都可以使用。

# 知识库联动指令

> 知识库根路径：`D:\knowledge-base`（以下简称 `$KB`）
>
> 本文件是项目联动的唯一入口。无论从 KB 目录启动还是从项目目录启动，项目相关的上下文读取、会话记录、决策和踩坑都按本文规则执行。

## 项目文件结构

每个项目在 `$KB/projects/<project-name>/` 下有四个文件：

```
$KB/projects/<project-name>/
├── context.md       ← 项目元信息（技术栈、目标、当前阻塞，始终短小）
├── sessions.md      ← 会话记录（最近 5 条完整，旧记录按月压缩）
├── decisions.md     ← 架构决策记录
└── roadblocks.md    ← 踩坑记录
```

## 会话启动

1. 读 `$KB/context/about.md` 和 `$KB/context/preferences.md` 了解用户
2. 读 `$KB/projects/<project-name>/context.md`（完整读取，始终短小）
3. 读 `$KB/projects/<project-name>/sessions.md`，只读「最近会话」区域（`## 最近会话` 到 `---` 分割线之间，最近 5 条完整记录）
4. 如有需要，读 `$KB/projects/<project-name>/decisions.md` 和 `roadblocks.md` 了解历史决策和踩坑

## 开发中

- 技术选型或概念查询 → 先搜索 `$KB/wiki/`（先读 `_index.md` 定位，再定向读取）。如果搜不到或结果不够好，就去联网搜索，务必保证搜索质量。
- 遇到值得保存的文章/文档 → 保存到 `$KB/raw/definitely/`（明确有价值）或 `casually/`（随手存），询问用户确认具体位置。会话结束时告知用户可采集。

---

## 文件模板

### context.md

```yaml
---
project: <项目名>
stack: [Next.js, Prisma, PostgreSQL]
status: active | paused | completed
---
## 项目概述
一句话描述项目是做什么的

## 当前状态
- 已完成的功能
- 正在进行的功能
- 已知阻塞

## 最近会话
见 sessions.md（最近 5 条）
```

### sessions.md

```markdown
# 会话记录

## 最近会话（最近 5 条，完整保留）

### 2026-07-08 晚间 — 商品列表分页 + 用户认证
- 做了什么
- 什么决定
- 什么还没做完

### 2026-07-07 下午 — 数据库 Schema 设计
- ...

---

## 历史摘要（按月压缩，10-20 行/月）

### 2026-06 月汇总
- 关键决策：选 cursor-based 分页而非 offset（理由：大表性能）
- 重要里程碑：完成了数据库 schema 设计和基础 CRUD
- 踩坑：Prisma migration 在 CI 中重复执行（已修复，见 roadblocks.md）
```

**读取规则**：每次启动只读「最近会话」区域（5 条完整记录）。「历史摘要」仅在需要回溯时用 Grep 搜索。

### decisions.md

```markdown
## YYYY-MM-DD: <决策标题>

- **背景**：为什么需要做这个决策
- **选项**：考虑过哪几个方案
- **选择**：选了哪个，为什么
- **代价**：这个选择有什么代价/风险
```

### roadblocks.md

```markdown
## YYYY-MM-DD: <问题描述>

- **现象**：报错信息 / 异常行为
- **原因**：根因是什么
- **修复**：怎么解决的
- **预防**：以后怎么避免
```

---

## 会话结束

### 1. 写项目会话记录

写入 `$KB/projects/<project-name>/sessions.md` 的「最近会话」区域：

**核心原则：一个会话只写一条记录**——不管会话里做了多少件事、讨论了多少个话题，全部合并到一条记录中。不要按主题或任务阶段拆分成多条。

0. **去重**：写入前先读 sessions.md 的最后一条记录（「最近会话」区域的第一条），确认上次会话结束时已经记录了哪些内容。本次只写新产生的内容，不重复已记录的部分。

1. 在 `## 最近会话` 标题下方插入新记录（最新的在最上面）
2. 标题格式：`### YYYY-MM-DD 时段 — 简短主题描述`，时段用 `上午` / `下午` / `晚间` / `深夜`（Claude 拿不到精确时间，用自然语言时段即可）
3. 标题下方列出：
   - **做了什么**：具体完成的事项（文件路径、数量、关键操作）
   - **什么决定**：当前会话做的选择，为什么这么选
   - **什么还没做完**：还在进行中的事项、下一步要做什么
   - 尽可能会话里做了多少件事、讨论了多少个话题，全部合并
4. 保持「最近会话」区域只有 **5 条**完整记录——超过 5 条时，将最旧的那条移到「历史摘要」顶部
5. **月压缩**：当「历史摘要」区域出现上一个月（非本月）的多条记录时，将其合并为一段 `### YYYY-MM 月汇总`（10-20 行），只保留关键决策 + 重要里程碑 + 值得记录的踩坑。压缩后删除原始记录

### 2. 更新项目状态

更新 `$KB/projects/<project-name>/context.md` 的「当前状态」部分（已完成、正在进行、已知阻塞）。

### 3. 记录决策和踩坑

- 架构决策 → 追加到 `$KB/projects/<project-name>/decisions.md`
- 踩坑记录 → 追加到 `$KB/projects/<project-name>/roadblocks.md`

### 4. 写 Daily Notes

如有实质进展，追加到 `$KB/daily/YYYY-MM-DD.md`。格式：

```markdown
## 时段 会话 — 简短主题描述
### 做了什么
- ...
### 决策
- ...
### 还未完成
- ...
```

文件已存在则追加（用 `---` 分割线隔开多场会话），不存在则新建。不需要严格每天写——有实质进展才写。**注意**：这里和 sessions.md 是两份独立的记录，不要混为一谈——Daily Notes 是 KB 全局日志，sessions.md 是单项目日志。

### 5. Git 同步

KB 仓库和项目仓库都要提交和推送：

```bash
# KB 仓库
cd $KB
git add -A
git commit -m "chore: <项目名> 会话记录更新"
git push

# 项目仓库（在项目目录下）
git add -A
git commit -m "<type>: <简要描述本次改动>"
git push
```

- commit message 用约定式提交：`feat:` `fix:` `refactor:` `docs:` `test:` `chore:` `perf:` `ci:`
- KB 尚未初始化 git 时，提醒用户先 `git init && git remote add origin <私有仓库地址>`

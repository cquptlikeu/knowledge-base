# 个人知识库

一个由 Claude Code 维护的两层 Markdown 知识库。所有内容均为纯 Markdown，可用任何编辑器打开。推荐用 Obsidian 浏览（支持 `[[wikilink]]` 和知识图谱），但 Obsidian 不是必需的。

**会话启动**：每次新会话开始时，按以下顺序初始化：
1. 先读取 `context/about.md` 和 `context/preferences.md` 了解用户——这是最优先的，确保 AI 知道在和谁对话
2. 读取 `wiki/_log.md` + 最近 1~3 天的 `daily/` 文件，了解最近操作和进展，维持跨会话的连续性
3. 如果用户有活跃项目：
   - 读取 `projects/<name>/context.md`（完整读取，始终短小）
   - 读取 `projects/<name>/sessions.md`，只读「最近会话」区域（`## 最近会话` 到 `---` 分割线之间，最近 5 条完整记录）
   - 「历史摘要」区域仅在需要回溯旧决策时按需搜索，不每次加载
4. **自动检测 raw/**：扫描 `raw/casually/` 和 `raw/definitely/` 中是否有命名不规范或未编译的新文件
   - 符合 `YYYY-MM-DD-title.md` 规范 → 检查是否已编译（是否有对应的 `wiki/summaries/` 文件）
   - 不符合命名规范 → 读 frontmatter 推断日期和标题，自动重命名为 `YYYY-MM-DD-title.md`
   - 发现未编译的 raw 文件 → 主动告知用户：「raw/ 中有 N 篇待处理：xxx，要我采集吗？」（注明来自 casually 还是 definitely）

## 架构

```
.
├── context/                  ← 用户画像（AI 每次启动先读这里）
│   ├── about.md              ← 你是谁、技术栈、关注方向
│   └── preferences.md        ← 学习方式、决策风格、AI 使用习惯
├── raw/                     ← 原始素材（只追加，不可修改）
│   ├── casually/            ← 随手收集的文档
│   │   └── YYYY-MM-DD-title.md
│   └── definitely/          ← 明确学习目标的文档
│       └── YYYY-MM-DD-title.md
├── wiki/                    ← LLM 编译维护的知识层
│   ├── summaries/           ← 每篇素材的摘要（1:1 对应 raw）
│   ├── entities/            ← 实体：技术、工具、库、产品
│   ├── concepts/            ← 概念：方法论、架构、模式、理论
│   ├── comparisons/         ← A vs B 对比
│   ├── overviews/           ← 主题综述（≥3 篇相关文章时生成）
│   ├── synthesis/           ← 问答存档
│   ├── _index.md            ← 自动维护的索引（按主题分组）
│   └── _log.md              ← 操作日志（追加，按时间线）
├── projects/                ← 项目相关
│   ├── kb-link.md           ← 外部项目接入指令（从项目目录联动 KB）
│   └── <project-name>/
│       ├── context.md       ← 项目元信息（技术栈、目标、当前阻塞，始终短小）
│       ├── sessions.md      ← 会话记录（最近 5 条完整，旧记录按月压缩）
│       ├── decisions.md     ← 架构决策记录
│       └── roadblocks.md    ← 踩坑记录
│   ├── scripts/                 ← 工具脚本
│   │   └── convert-to-markdown.py  ← PDF/DOCX/DOC → Markdown 转换
├── daily/                   ← 会话记录（每次会话结束后自动写入）
```

### 为什么两层

- `raw/` 是不可变的「事实层」——你收集的原始素材。不修改、不删除。
- `wiki/` 是 LLM 对事实的「理解层」——可以随时从 raw 重新生成。
- 分离的好处：理解层可以不断优化、修正、重建，而事实层永远不变。

### 两个特殊文件

- `wiki/_index.md`：按类型分组的目录。查询时**先读索引**定位相关页面，避免盲目扫描整个 wiki。
- `wiki/_log.md`：按时间线的操作记录，只追加。新会话通过日志追赶上一次的操作。

## 核心原则

1. **raw 不可变**：raw/ 中的文件一旦写入就不能被修改或删除——没有例外
2. **wiki 可重新生成**：summaries → entities → concepts → comparisons → overviews 都可以从 raw 重新生成（synthesis 除外，它由查询触发）
3. **创建前先搜索**：创建 entity/concept 页面前，先搜索 `wiki/` 和 `_index.md` 避免重复
4. **增量更新，不丢信息**：更新已有 entity/concept 时，保留所有已有内容，追加新信息
5. **链接格式**：使用 `[[folder/name]]` 格式，带文件夹前缀（如 `[[entities/Kubernetes]]`）
6. **语言**：wiki 内容使用中文；专业术语和技术名词保持原文

## 约定

### 文件命名

- raw 文件：`YYYY-MM-DD-<title>.md`，特殊字符替换为 `-`，标题截断到 80 字符
- wiki 页面：以主题命名（如 `Kubernetes.md`, `Server Actions.md`）
- comparisons：`A vs B.md`
- synthesis：以回答主题命名，不是以问题命名

### Frontmatter

每个 wiki 页面都需要 frontmatter：

```yaml
---
type: summary | entity | concept | comparison | overview | synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
source: "[[raw/YYYY-MM-DD-title]]"   # summary 类型必填
aliases: [alias1, alias2]            # entity/concept 类型
---
```

### 页面之间的交叉链接关系

```
raw/article  ←──  summaries（唯一直接引用 raw 的页面）
                     │
                     ▼
             entities  ↔  concepts
                 │            │
                 ▼            ▼
             comparisons  comparisons
                     \      /
                      ▼    ▼
                   overviews

synthesis ──→ 所有页面（仅出向链接，叶节点）
```

## 三大工作流

### 1. Ingest（采集）

当你说「采集」「保存」「clip」「收藏」，或粘贴 URL 时执行。

**阶段 A：获取并保存 raw**

采集方式有三种，无论哪种入口，最终都走同一个编译流程：

1. **URL 采集**：用户提供 URL
   - 使用可用工具（WebFetch / curl / 浏览器 MCP 等）获取 URL 内容，保留正文、作者、发布日期
   - 默认保存为 `raw/definitely/YYYY-MM-DD-<title>.md`（按规范命名）
   - 如用户说「随手存」「随便看看」→ 保存为 `raw/casually/YYYY-MM-DD-<title>.md`
   
2. **手动放入 + 说「采集」**：用户手动把文件放进了 raw/ 或通过 Web Clipper 保存
   - 说「采集」时先扫描 `raw/casually/` 和 `raw/definitely/` → 找出所有未编译的 raw 文件
   - 如果文件名不符合 `YYYY-MM-DD-title.md` 格式 → 读 frontmatter 推断日期和标题 → 自动重命名
   - **非 Markdown 文件自动转换**：发现 `.pdf` / `.docx` / `.doc` 文件 → 自动运行 `scripts/convert-to-markdown.py` 转为 `.md`，转换后的 .md 文件原地存放，原始文件不移除（raw 不可变原则）
   
3. **仅手动放入（还没说采集）**：会话启动第 4 步已自动检测，不需要额外操作

4. 采集前检查 `wiki/_log.md` 或已有 raw 文件的 frontmatter，确认 URL/内容是否已被采集过——如已采集则跳过

5. **支持的文件格式**：
   | 格式 | 文字 | 图片/图表 | 处理方式 |
   |------|:---:|:---:|---------|
   | `.md` | ✅ | ❌ | 直接使用。内嵌 `![](path)` 图片无法被 Read 读取 |
   | `.pdf` | ✅ | ✅ | **不转换**——Read 工具渲染 PDF 页面画面，图表/公式/截图所见即所得 |
   | `.docx` | ✅ | ❌ | `convert-to-markdown.py` 提取文字+表格。嵌入图片可提取到 assets/ 供你在 Obsidian 查看，但 AI 无法读取 |
   | `.doc` | ✅ | ❌ | LibreOffice 转 .docx 后同上 |
   | `.png/.jpg` | — | ❌ | Read 工具无法读取独立图片文件。如需采集，改为截图贴进 PDF 或直接描述图片内容 |

**阶段 B：编译 wiki**

编译目标：**知识库不是文章存档，而是理解网络**。每个页面不仅要记录「是什么」，更要记录「为什么重要」「什么时候用/不用」「和其他东西的关系」。

**两层导航**：进入某个目录编译前，先读该目录的 `instructions.md` 了解局部规则——不需要一次性记住所有标准，按需读取。

1. **摘要**：先读 `wiki/summaries/instructions.md`，然后在 `wiki/summaries/` 创建 1:1 摘要，链接回 `[[raw/...]]`
   - 不是简单复述，要保留**论证逻辑链**（作者为什么得出这个结论）
   - 保留**关键案例/代码片段**（不只是说「有代码」，要保留最核心的示例）
   - 引用 2-3 个**原文金句**（用 `>` 块引用，让读者感受原文的语气和精确表述）
   - 目标长度 30-60 行——一篇 2000 字的文章，摘要不应少于 30 行
   - 末尾列出「相关实体与概念」的链接

2. **实体提取**：识别文中提到的人物、组织、产品、技术、工具
   - 已有页面 → 增量更新（保留旧内容，追加新来源和发现）
   - 不存在 → 创建 `wiki/entities/<Name>.md`
   - 实体页面应包含：**核心特征**（有什么独特之处）、**主要应用场景**（什么情况下选它）、**与其他实体的关系**（vs X 对比、配合 Y 使用）、**来源列表**（每篇提及的文章都加进来）

3. **概念提取**：识别方法论、架构、模式、理论
   - 同上，已有更新，没有则创建 `wiki/concepts/<Name>.md`
   - 概念页面应包含：**核心思想**（用一句话说清这个概念的独特洞察）、**什么时候用**（适用场景）、**什么时候不要用**（反面边界——这比适用场景更能定义概念）、**常见误区**（人们常犯的错误理解）、**相关概念对比**（和相近但不同的概念区分开）

4. **对比判断**：如果文章显式对比了两个已有实体/概念 → 生成 `wiki/comparisons/A vs B.md`

5. **综述判断**：如果某个主题已关联 ≥3 篇摘要 → 生成或更新 `wiki/overviews/<Topic>.md`

**阶段 C：索引和日志**
1. 更新 `wiki/_index.md`（按类型分组，为新/更新的页面添加一句话描述）
2. 追加 `wiki/_log.md`：时间戳、URL、生成了/更新了哪些页面

### 2. Query（查询）

1. **先读索引**：读取 `wiki/_index.md`，定位与问题相关的页面
2. **定向阅读**：读取索引定位到的相关页面
3. **补充搜索**：如果索引不够，用 Grep 在 `wiki/` 搜索关键词
4. **综合回答**：在回答中使用 `[[folder/name]]` 内链
5. 如果知识库中没有相关内容，直说——不要编造
6. 保持批判性思维，提供有深度的观点，不要只会迎合

**存档判断**——回答后评估是否存档到 `wiki/synthesis/`：

- 综合了 ≥2 个 wiki 页面 → 建议存档
- 产生了跨领域的洞察或连接 → 建议存档
- 用户明确标记为有价值 → 存档
- 简单事实查询、单页面检索 → 不存档

建议话术：「这个回答综合了多个来源，要存档到知识库吗？」

### 3. Audit（审计）

当你说「审查」「检查知识库」「健康检查」时执行。

**第一步：结构扫描**
1. **死链**：grep 所有 `[[...]]` 链接，检查目标文件是否存在
2. **孤立页面**：检查每个 wiki 页面是否被至少一个其他页面引用
3. **缺失交叉引用**：同源文章中共现但未链接的实体/概念

**第二步：内容审查**
4. **矛盾检测**：对比不同来源对同一实体/概念的描述，标出矛盾
5. **过时信息**：新摘要是否使旧结论失效？
6. **缺失页面**：多篇文章中反复出现但缺少独立页面的主题

**第三步：建议**
7. **知识空白**：基于当前知识图谱，建议可以通过搜索填补的空白
8. **新问题**：基于现有内容，建议值得探索的新问题

**输出**：问题列表 + 建议修复方案；等待用户确认后再执行。追加审计记录到 `_log.md`。

## 两种工作模式

这个知识库可以在两种场景下使用：

### 模式 A：在 KB 目录启动终端

终端路径在 `D:\knowledge-base\`，Claude 自动读取本文件。适用于：
- 知识库维护（采集、审计）
- 在 KB 内部管理项目文档（创建 context / sessions / decisions）

会话启动步骤见顶部「会话启动」，项目文件格式见下方「项目工作流」。

### 模式 B：在项目目录启动终端

终端路径在项目目录（如 `D:\my-ecommerce\`），Claude 读的是项目的 CLAUDE.md。

在项目的 CLAUDE.md 中加一行即可接入：

```markdown
## 知识库联动
读取 D:\knowledge-base\projects\kb-link.md，按其中规则联动。
```

`kb-link.md` 是自包含的——Claude 读这一份文件就知道如何从外部项目读写 KB 中的上下文、会话记录、决策和踩坑。

**两种模式的关系**：
- CLAUDE.md 定义「项目文件长什么样」（模板、格式、压缩规则）
- kb-link.md 是「适配器」——告诉外部项目如何找到 KB、按什么规则读写
- 改 CLAUDE.md 的模板时，检查 kb-link.md 是否需要同步更新

## 项目工作流（写项目专用）

### 项目上下文

每个项目的 `projects/<name>/context.md` 记录：
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

### 会话记录

`projects/<name>/sessions.md` 的结构：

```markdown
# 会话记录

## 最近会话（最近 5 条，完整保留）

### 2026-07-08 21:15 — 商品列表分页
- 做了什么
- 什么决定
- 什么还没做完

### 2026-07-08 14:30 — 用户认证模块
- ...

---

## 历史摘要（按月压缩，10-20 行/月）

### 2026-06 月汇总
- 关键决策：选 cursor-based 分页而非 offset（理由：大表性能）
- 重要里程碑：完成了数据库 schema 设计和基础 CRUD
- 踩坑：Prisma migration 在 CI 中重复执行（已修复，见 roadblocks.md）

### 2026-05 月汇总
- ...
```

**读取规则**：
- 每次启动只读「最近会话」区域（`## 最近会话` 到 `---` 分割线之间的 5 条完整记录）
- 「历史摘要」仅在需要回溯旧决策时用 Grep 按关键词搜索
- 会话结束时追加到「最近会话」顶部（最新的在最上面）

### 架构决策

`projects/<name>/decisions.md` 中记录每条决策：
```markdown
## YYYY-MM-DD: <决策标题>

- **背景**：为什么需要做这个决策
- **选项**：考虑过哪几个方案
- **选择**：选了哪个，为什么
- **代价**：这个选择有什么代价/风险
```

### 踩坑记录

`projects/<name>/roadblocks.md` 中记录每个坑：
```markdown
## YYYY-MM-DD: <问题描述>

- **现象**：报错信息 / 异常行为
- **原因**：根因是什么
- **修复**：怎么解决的
- **预防**：以后怎么避免
```

## 会话结束规则

**每次会话结束前**（用户表示要结束、或任务自然告一段落），执行以下步骤：

### 1. 写 Daily Notes

写入 `daily/YYYY-MM-DD.md`。如果文件已存在（同一天有多场会话），**追加**而非覆盖，在末尾追加新段落：

```markdown
# YYYY-MM-DD 会话记录

## 14:30 会话 — 采集 PostgreSQL 文章 + 电商后台认证
### 做了什么
- 采集了一篇 PostgreSQL 查询优化的文章
- 项目中实现了用户认证

### 决策
- 选 next-auth 做 session 管理

### 还未完成
- refresh token 轮换

---

## 21:15 会话 — 项目商品列表继续开发
### 做了什么
- 实现了商品分页和搜索

### 决策
- 分页用 cursor-based 方案

### 还未完成
- 商品图片上传
```

不需要严格每天写——有实质进展才写。内容简洁即可，几十行。

### 2. 写项目会话记录

如果本次会话涉及项目开发，写入 `projects/<name>/sessions.md` 的「最近会话」区域：

1. 在 `## 最近会话` 标题下方插入新记录（最新的在最上面）
2. 格式：`### YYYY-MM-DD HH:MM — 简短主题描述`，下方列出做了什么、什么决定、什么还没做完
3. 保持「最近会话」区域只有 **5 条**完整记录——超过 5 条时，将最旧的那条移到「历史摘要」顶部
4. **月压缩**：当「历史摘要」区域出现上一个月（非本月）的多条记录时，将其合并为一段 `### YYYY-MM 月汇总`（10-20 行），只保留关键决策 + 重要里程碑 + 值得记录的踩坑。压缩后删除原始记录

### 3. Git 同步

将本次变更推送到远程私有仓库，实现多设备同步：

```bash
git add -A
git commit -m "<type>: <简要描述本次改动>"
git push
```

- 不是每次单个操作都 push——会话结束时统一提交
- commit message 用约定式提交：`ingest: <文章名>` 采集、`improve: <改动描述>` 改进、`audit: <审查结果>` 审计
- 如果用户还没初始化 Git 仓库，提醒用户先执行：
  ```bash
  cd D:\knowledge-base
  git init
  git remote add origin <私有仓库地址>
  ```

### 4. 换设备时拉取

用户换另一台设备前，执行 `git pull` 即可同步最新状态。如果是新设备：

```bash
git clone <私有仓库地址> D:\knowledge-base
```

## 其他约定

- 操作前先读规则：所有工作流操作前先读本文件
- raw 中的附件：如果要引用 raw 中的图片，用相对路径 `../raw/assets/...`
- 索引维护：每次修改 wiki 后都要更新 `_index.md`
- 不删除 raw：永远不要删除 raw/ 中的文件
- 改写而非覆盖：更新 wiki 页面时，整合新旧内容而非直接覆盖

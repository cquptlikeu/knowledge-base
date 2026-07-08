# 知识库联动指令

> 知识库根路径：`D:\knowledge-base`（以下简称 `$KB`）
>
> 本文件是自包含的——从外部项目目录启动 Claude 时，读这一份文件就知道如何联动 KB。

## 会话启动

1. 读 `$KB/context/about.md` 和 `$KB/context/preferences.md` 了解用户
2. 读 `$KB/projects/<project-name>/context.md`（完整读取，始终短小）
3. 读 `$KB/projects/<project-name>/sessions.md`，只读「最近会话」区域（`## 最近会话` 到 `---` 分割线之间，最近 5 条完整记录）
4. 如有需要，读 `$KB/projects/<project-name>/decisions.md` 和 `roadblocks.md` 了解历史决策和踩坑

## 开发中

- 技术选型或概念查询 → 搜索 `$KB/wiki/`（先读 `_index.md` 定位，再定向读取）
- 遇到值得保存的文章/文档 → 保存到 `$KB/raw/definitely/`（明确有价值）或 `casually/`（随手存），会话结束时告知用户可采集

## 会话结束

### 1. 写项目会话记录

写入 `$KB/projects/<project-name>/sessions.md` 的「最近会话」区域：

1. 在 `## 最近会话` 标题下方插入新记录（最新的在最上面）
2. 格式：`### YYYY-MM-DD HH:MM — 简短主题描述`，下方列出做了什么、什么决定、什么还没做完
3. 保持「最近会话」区域只有 **5 条**完整记录——超过 5 条时，将最旧的那条移到「历史摘要」顶部
4. **月压缩**：当「历史摘要」区域出现上一个月（非本月）的多条记录时，将其合并为一段 `### YYYY-MM 月汇总`（10-20 行），只保留关键决策 + 重要里程碑 + 值得记录的踩坑。压缩后删除原始记录

### 2. 更新项目状态

更新 `$KB/projects/<project-name>/context.md` 的「当前状态」部分（已完成、正在进行、已知阻塞）。

### 3. 记录决策和踩坑

- 架构决策 → 追加到 `$KB/projects/<project-name>/decisions.md`
- 踩坑记录 → 追加到 `$KB/projects/<project-name>/roadblocks.md`

### 4. 写 Daily Notes

如有实质进展，追加到 `$KB/daily/YYYY-MM-DD.md`（文件已存在则追加，用 `---` 分割线隔开多场会话，时间戳 + 主题命名）。

### 5. Git 同步

```bash
cd $KB
git add -A
git commit -m "chore: <项目名> 会话记录更新"
git push
```

别忘了项目本身的 repo 也要 git 提交和推送。

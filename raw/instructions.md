# raw/ 目录说明

## 原则

**raw/ 中的文件是不可变的。** 一旦写入就不能被修改或删除——没有例外。这是事实层。

## 文件命名

- 格式：`YYYY-MM-DD-<title>.md`
- 特殊字符替换为 `-`
- 标题截断到 80 字符

## 内容格式

每个 raw 文件建议包含 frontmatter：

```yaml
---
type: article
title: "原文标题"
author: 作者
date: 原始发布日期
source: 原始 URL
language: zh | en
---
```

正文保留原文内容，不要篡改、不要删减、不要添加评论。

## 什么时候使用 Web Clipper

如果用 Obsidian Web Clipper 保存内容到 raw/，文件名可能不符合 `YYYY-MM-DD-title.md` 格式。这种情况可以在 wiki 编译时由 Claude 重命名，但原始文件保留不动。

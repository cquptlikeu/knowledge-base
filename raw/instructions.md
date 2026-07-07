# raw/ 目录说明

## 原则

**raw/ 中的文件是不可变的。** 一旦写入就不能被修改或删除——没有例外。这是事实层。

## 子文件夹

```
raw/
├── instructions.md
├── casually/                    ← 随手收集的文档
└── definitely/                  ← 明确学习目标的文档
```

- **casually/**：浏览器刷到的好东西、随手收藏、还没确定要不要深读
- **definitely/**：明确知道需要学习、研究、引用的重要文档

两个子文件夹的编译流程完全一致，区别只是你的分类意图——不影响 wiki 编译深度。

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

## Web Clipper

Obsidian Web Clipper 可分别配置两个模板，保存路径分别指向 `raw/casually/` 和 `raw/definitely/`。

如果文件名不符合 `YYYY-MM-DD-title.md` 格式，wiki 编译时 Claude 会自动重命名。

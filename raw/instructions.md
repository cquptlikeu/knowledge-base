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

## 支持的文件格式

| 格式 | 说明 |
|------|------|
| `.md` | 原生格式，直接使用。内嵌图片无法被 AI 读取 |
| `.pdf` | **不转换**——Read 工具渲染 PDF 页面画面，图表/公式/截图所见即所得 |
| `.docx` | `convert-to-markdown.py` 提取文字+表格。嵌入图片可提取到 assets/ 供 Obsidian 查看 |
| `.doc` | LibreOffice 转 .docx 后同上 |
| `.png` / `.jpg` | **AI 无法读取**。如需采集，用截图工具把图片粘进 PDF，或直接文字描述图片内容 |

`.docx` / `.doc` 转换时嵌入图片提取到 `assets/` 目录（供你浏览，非 AI 消费）。原始文件保留不删（raw 不可变原则）。

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

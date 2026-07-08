# scripts/ 目录说明

## 用途

存放知识库辅助脚本，每个脚本专注一件事。

## 脚本清单

### convert-to-markdown.py

将 DOCX/DOC 文件转换为 Markdown，同时提取嵌入图片。

- **依赖**：python-docx、LibreOffice（仅 .doc 需要）
- **安装**：`pip install python-docx`
- **用法**：`python scripts/convert-to-markdown.py input.docx -o output.md`
- **输出**：`.md` 文件 + `assets/` 目录（提取的图片，供 Obsidian 查看，AI 无法读取）
- **注意**：PDF **不需要**转换——Read 工具渲染 PDF 页面画面，效果优于提取文字

## 原则

- 单一职责：一个脚本只做一件事
- 无副作用：不修改 raw/ 中的原始文件
- 幂等：同一输入多次运行结果一致

# 踩坑记录

## 2026-07-08: conda env create 清华镜像超时

- **现象**：`conda env create -f environment.yml` 在 `pkgs/free` 频道超时，SSL EOF
- **原因**：`environment.yml` 里的 `defaults` 频道展开到了已弃用的清华 `pkgs/free` 镜像
- **修复**：去掉 `defaults` 只留 `conda-forge`，加 `pyyaml` 到 conda 依赖
- **预防**：只用 conda-forge，pip 段承担所有 Python 包

## 2026-07-08: PaddleOCR 与 numpy 2.x 不兼容

- **现象**：PaddleOCR 要求降级 numpy 到 1.x，会破坏已装好的 torch/chromadb/整栈
- **原因**：paddlepaddle 对 numpy 2 的兼容滞后
- **修复**：跳过 PaddleOCR，顺位选 rapidocr-onnxruntime
- **预防**：装 OCR 后立即复跑冒烟探针确认 numpy 版本未被篡改

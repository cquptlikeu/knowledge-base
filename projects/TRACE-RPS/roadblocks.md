# 踩坑记录

## 2026-06-22: inference.py 不运行 TRACE——三个实验阶段全无效

- **现象**：`anonymized_text=None`、空 `anonymization_history`、无 `response` 字段
- **原因**：`inference.py` 没有调用 `adversarial_anonymization`，全代码搜索 `src/` 无任何调用。正确入口是 `PYTHONPATH=. python anonymization/trace.py`
- **修复**：改用 trace.py 入口，更新 memory/project-env-and-run.md
- **预防**：新入口先验证产物结构——检查 response/trace_metadata/anonymization_history 是否填充

## 2026-06-23: transformers 4.31 无法加载 Qwen2.5/Llama-3.1

- **现象**：`AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-7B-Instruct")` 报模型类型不识别
- **原因**：road_A conda env 的 transformers 4.31（2023 年中）太老，不认识 2024 年发布的模型架构
- **修复**：新建 `road_A_eval` conda env，`pip install "transformers==4.44.2"`
- **预防**：检查模型发布时间 vs 库版本；跨家族模型优先新建 env

## 2026-06-23: transformers 过新破坏 torch 2.0.1

- **现象**：`pip install -U transformers` 安装 latest（>4.46），torch 2.0.1 被后续依赖禁用
- **原因**：最新 transformers 要求 torch >= 2.1
- **修复**：指定版本 `pip install "transformers==4.44.2"`
- **预防**：永远不要 `pip install -U transformers` 不带版本号

## 2026-06-23: Llama-3.1 下载 32GB 含冗余 original/

- **现象**：`huggingface-cli download meta-llama/Llama-3.1-8B-Instruct` 下载 32GB，含 `original/consolidated.00.pth`（~15GB 冗余）
- **原因**：HF repo 同时包含 safetensors（~15GB）和 original PyTorch checkpoint（~15GB）
- **修复**：`--exclude "original/*" "*.pth"`
- **预防**：下载大模型前先检查 repo 文件列表，或统一加 `--exclude "original/*" "*.pth"`

## 2026-06-23: hf-mirror 限速 3.92MB/s

- **现象**：`huggingface-cli download` 速度仅 3.92MB/s，15GB 模型需 1 小时+
- **原因**：日本 autodl 节点到 hf-mirror 的带宽不稳定
- **修复**：先用 `export HF_ENDPOINT=https://hf-mirror.com`，如仍慢则试 ModelScope
- **预防**：模型下载安排在不阻塞主实验的时间

## 2026-06-23: trace_concurrent.py 忽略 trace_config

- **现象**：`trace_concurrent.py` 不接收 trace_config 参数，多 GPU 并行时无法指定 P6/P7 配置
- **原因**：并行入口与单 GPU 入口代码路径不同
- **修复**：临时绕过用单 GPU trace.py；长期需修改 trace_concurrent.py
- **预防**：同一功能的单 GPU / 多 GPU 路径应走同一 config 解析函数

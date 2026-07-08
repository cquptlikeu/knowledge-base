## 2026-06-27: conda env create 清华镜像超时 / SSL 失败

- **现象**：`conda env create -f environment.yml` 卡在 `mirrors.tuna.tsinghua.edu.cn` 的 `pkgs/free` 频道，报 `ReadTimeoutError` / `SSLEOFError`
- **原因**：`environment.yml` 原来写 `channels: [conda-forge, defaults]`，而用户的 `.condarc` 将 `defaults` 展开到了清华已弃用的 `pkgs/free` 镜像
- **修复**：去掉 `defaults`、只保留 `conda-forge`；补 `pyyaml` 进 conda 依赖；后续用 `--override-channels -c conda-forge` 兜底
- **预防**：`environment.yml` channels 最简即可——conda 只管 python/pip/pyyaml，其余全走 pip

## 2026-06-28: tests 同名模块收集冲突

- **现象**：`pytest` 全量跑时 `tests/domain/test_models.py` 与 `tests/corpus/test_models.py` 收集失败，报 `import file mismatch`
- **原因**：两个 `test_models.py` 在不同包下，但 pytest 默认会把它们当成同一模块名冲突（`__pycache__` 缓存交叉污染）
- **修复**：清理 `tests/**/__pycache__`；给 `tests/corpus/`、`tests/domain/`、`tests/eval/` 补上 `__init__.py`
- **预防**：新建 tests 子包时一并创建 `__init__.py`；不同子包避免同名测试模块，或用 `test_corpus_models.py` 等唯一命名

## 2026-06-28: code-reviewer 在看 isolated worktree 快照

- **现象**：多次 `code-reviewer` agent 报告"文件不存在"，但主工作树中文件确实存在且测试通过
- **原因**：`Agent(isolation: "worktree")` 创建的是 git worktree 快照，而主工作树未提交的改动不在快照中
- **修复**：对未提交改动做 review 时，应在 Workflow 里直接用 agent 读主工作树路径（不设 isolation），或用 `git diff`/`git stash` 后再跑 worktree
- **预防**：重要 review 先提交或至少 `git add`，再开 worktree agent；或 review 前写明 `只读主工作树 F:\develop\...`

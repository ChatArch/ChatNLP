# ChatNLP

`ChatNLP` 是 ChatArch NLP 方向的 Python CLI 包壳。当前公开 CLI 只提供包信息与真实命令树；后续新增 NLP 能力时，应先落到可复用 Python API，再扩展 CLI、文档和测试。

<div class="grid cards" markdown>

-   :material-console-line: **CLI 树**

    ---

    查看当前真实命令面：[`chatnlp --tree`](cli-tree.md)；使用 `chatnlp --tree-brief` 获取省略参数签名的简洁视图。

-   :material-package-variant: **包边界**

    ---

    当前版本是轻量入口，不执行网络 NLP 服务调用。

-   :material-shield-check: **验证契约**

    ---

    `--tree`、`--tree-brief`、README、MkDocs 和测试必须同步更新。

</div>

## 快速开始

```bash
pip install ChatNLP
chatnlp --version
chatnlp --tree
chatnlp --tree-brief
```

## 开发验证

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

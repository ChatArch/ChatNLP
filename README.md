<div align="center">
    <a href="https://pypi.python.org/pypi/ChatNLP">
        <img src="https://img.shields.io/pypi/v/ChatNLP.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatNLP/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatNLP/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatNLP/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[英文版](README.en.md) | 简体中文
</div>

# ChatNLP

`ChatNLP` 是 ChatArch NLP 方向的 Python CLI 包壳。当前公开 CLI 只提供真实 root-only 包信息入口；后续新增 NLP 能力时，必须同步 Python API、CLI 树、文档和测试。

## 快速开始

```bash
pip install ChatNLP
chatnlp --version
chatnlp --tree
chatnlp --tree-brief
```

开发环境：

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI 树

`chatnlp --tree` 与 `chatnlp --tree-brief` 由共享的 ChatStyle runtime 从真实 Click 注册面生成。完整视图保留命令参数签名，简洁视图省略参数签名；当前 CLI 是 root-only，因此两者显示相同节点。

```text
chatnlp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatnlp hello` 不是公开 CLI；它属于脚手架示例残留，必须失败。

## 文档

- 文档首页：https://arch.gh.wzhecnu.cn/ChatNLP/
- CLI 树：https://arch.gh.wzhecnu.cn/ChatNLP/cli-tree/
- 英文文档：https://arch.gh.wzhecnu.cn/ChatNLP/en/

## 开发说明

扩展命令前先阅读 `DEVELOP.md` 和 `AGENTS.md`，并保持 `--tree`、`--tree-brief`、README、MkDocs、测试与 changelog 同步。

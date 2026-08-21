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

English | [简体中文](README.md)
</div>

# ChatNLP

`ChatNLP` is the ChatArch Python CLI package shell for NLP-oriented workflows. The public CLI currently exposes truthful root-level package information entries only. Future NLP capabilities must update Python APIs, the CLI tree, docs, and tests together.

## Quick Start

```bash
pip install ChatNLP
chatnlp --version
chatnlp --tree
chatnlp --tree-brief
```

Development environment:

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI Tree

Shared ChatStyle runtime generates `chatnlp --tree` and `chatnlp --tree-brief` from the registered Click surface. The full view preserves command signatures, while the brief view omits them. Both show the same nodes while the CLI remains root-only.

```text
chatnlp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`chatnlp hello` is not public CLI; it is a scaffold example leftover and must fail.

## Documentation

- Documentation home: https://arch.gh.wzhecnu.cn/ChatNLP/
- CLI tree: https://arch.gh.wzhecnu.cn/ChatNLP/cli-tree/
- English docs: https://arch.gh.wzhecnu.cn/ChatNLP/en/

## Development Notes

Read `DEVELOP.md` and `AGENTS.md` before expanding commands, and keep `--tree`, `--tree-brief`, README, MkDocs, tests, and changelog synchronized.

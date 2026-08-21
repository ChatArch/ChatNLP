# ChatNLP

`ChatNLP` is the ChatArch Python CLI package shell for NLP-oriented workflows. The public CLI currently exposes package metadata and the real command tree only; future NLP capabilities should start with reusable Python APIs before extending CLI commands, docs, and tests.

<div class="grid cards" markdown>

-   :material-console-line: **CLI Tree**

    ---

    Inspect the current real command surface with [`chatnlp --tree`](cli-tree.md), or use `chatnlp --tree-brief` for the signature-free view.

-   :material-package-variant: **Package Boundary**

    ---

    The current version is a lightweight entrypoint and does not call network NLP services.

-   :material-shield-check: **Verification Contract**

    ---

    `--tree`, `--tree-brief`, README, MkDocs, and tests must stay synchronized.

</div>

## Quick Start

```bash
pip install ChatNLP
chatnlp --version
chatnlp --tree
chatnlp --tree-brief
```

## Development Verification

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

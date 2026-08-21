# Development Guide

## CLI Rules

- The real `chatnlp` console script requires `chatstyle>=0.2.0,<0.3.0` and uses `add_tree_option()` for both `--tree` and `--tree-brief`; do not add a package-local tree renderer.
- Keep the explicit public Click root name `chatnlp`.
- The typed ChatEnv provider requires `chatenv>=0.2.10,<0.3.0`; register fields in `chatnlp.config` and use ChatEnv profile/storage paths rather than package-local dotenv paths.
- Prefer reusable Python APIs before CLI wiring for new NLP capabilities.
- Missing required args should auto-enter interactive mode only when recoverable and explicitly designed.
- `-i` forces interactive mode; `-I` disables prompting and must fail fast.
- Prompt defaults must match actual execution defaults.
- Sensitive values must stay masked in prompts and summaries.
- Prefer lazy imports in CLI wiring and keep implementation imports local when possible.

## Docs and Tests

- Use doc-first CLI testing.
- Put real CLI coverage under `tests/cli-tests/`.
- Put mock/fake CLI coverage under `tests/mock-cli-tests/`.
- Keep `README.md`, `docs/`, and `CHANGELOG.md` in sync with user-facing changes.
- Regenerate or verify both registered views with `chatnlp --tree` and `chatnlp --tree-brief`.

## Automation

- Keep automation small and reviewable.
- Prefer commands that can run in CI without interactive prompts.
- Ensure generated defaults are safe for local development.
- Before release, run `python -m pytest -q`, `mkdocs build --strict`, `python -m build`, `python -m twine check dist/*`, and the source CLI version/tree readbacks.

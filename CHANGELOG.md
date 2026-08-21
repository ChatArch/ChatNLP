# Changelog

## 0.1.2 - 2026-08-22

### Changed

- Replaced the package-local CLI tree renderer with ChatStyle `add_tree_option()` and added registered `--tree-brief` output.
- Aligned runtime bounds to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0` while preserving the typed ChatEnv provider and storage paths.
- Expanded tests, bilingual docs, and CI to verify version/full-tree/brief-tree behavior, built distributions, wheel installs, and ChatEnv provider discovery.

## 0.1.1 - 2026-08-12

### Changed

- Added generated root-only `chatnlp --tree` from the Click command surface.
- Added bilingual MkDocs docs, CLI tree pages, Preview Docs, Deploy Docs, CI docs gate, and workflow/docs contract tests.
- Removed unused direct ChatStyle runtime dependency while preserving the ChatEnv provider entry point.

## 0.1.0 - 2026-07-08

### Added
- Publish the first ChatArch workflow-verified ChatNLP release after the 0.0.1 PyPI placeholder.

## 0.0.1 - 2026-07-08

### Added
- Register the initial PyPI placeholder package.

# CLI Tree

ChatNLP uses shared `chatstyle.add_tree_option()` to generate its tree from the registered Click command surface:

- `chatnlp --tree` includes parameter signatures for interface review.
- `chatnlp --tree-brief` preserves the same nodes and descriptions while omitting parameter signatures.

The CLI is currently root-only and has no business-command parameters, so its full and brief views are identical. The template `hello` command is not public.

## Full command tree

```text
chatnlp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Brief command tree

```text
chatnlp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Current status

| Entry | Status | Contract |
| --- | --- | --- |
| `chatnlp --help` | Implemented | Shows root command help. |
| `chatnlp --version` | Implemented | Shows the installed package version. |
| `chatnlp --tree` | Implemented | Shows the registered tree with parameter signatures. |
| `chatnlp --tree-brief` | Implemented | Shows the same registered tree without parameter signatures. |
| `chatnlp hello` | Removed | Template scaffold command, not a compatibility surface. |
| NLP business commands | Not implemented | Add only when real NLP capabilities exist. |

## Update rule

When adding an NLP capability, add its reusable Python API first, register its CLI command, and then run `chatnlp --tree` and `chatnlp --tree-brief` to update the README and this page.

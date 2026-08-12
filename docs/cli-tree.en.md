# CLI Tree

`chatnlp --tree` is generated from the real registered Click command surface. `ChatNLP` currently exposes root-level package information entries only and no business subcommands; a template `hello` command is not part of the public interface.

## Top-level command

```text
chatnlp  # ChatNLP placeholder package for NLP workflows
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Status Contract

- `chatnlp --help` must expose `--tree`.
- `chatnlp --tree` must exit 0 and list only real registered commands/options.
- `chatnlp hello` must fail; `hello` is not a business command.
- Future NLP capabilities must add reusable Python APIs first, then CLI commands, and then update this page.

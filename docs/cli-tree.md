# CLI 树

ChatNLP 使用共享的 `chatstyle.add_tree_option()` 从真实注册的 Click command surface 生成命令树：

- `chatnlp --tree` 显示参数签名，适合接口审查。
- `chatnlp --tree-brief` 保留同一组节点和说明，但省略参数签名。

当前 CLI 是 root-only，没有业务命令参数，因此完整和简洁视图相同。模板 `hello` 命令不属于公开接口。

## 完整命令树

```text
chatnlp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## 简洁命令树

```text
chatnlp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## 当前状态

| 入口 | 状态 | 说明 |
| --- | --- | --- |
| `chatnlp --help` | 已实现 | 显示根命令帮助。 |
| `chatnlp --version` | 已实现 | 显示已安装包版本。 |
| `chatnlp --tree` | 已实现 | 显示包含参数签名的真实注册树。 |
| `chatnlp --tree-brief` | 已实现 | 显示省略参数签名的同一注册树。 |
| `chatnlp hello` | 已移除 | 模板 scaffold 命令，不作为公开兼容面保留。 |
| NLP 业务子命令 | 尚未实现 | 未来有真实 NLP 能力后再加入 CLI。 |

## 更新规则

新增 NLP 能力时，先增加可复用 Python API，再注册 CLI command，并运行 `chatnlp --tree` 与 `chatnlp --tree-brief` 回填 README 与本页。

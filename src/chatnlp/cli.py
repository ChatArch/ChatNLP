"""CLI entrypoint for chatnlp."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatnlp import __version__


@click.group(
    name="chatnlp",
    invoke_without_command=True,
)
@click.version_option(__version__, prog_name="chatnlp")
@add_tree_option(renderer_options={"root_name": "chatnlp"})
@click.pass_context
def main(ctx: click.Context) -> None:
    """ChatNLP placeholder package for NLP workflows."""

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    main()

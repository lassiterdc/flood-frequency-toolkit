"""Console script for flood_frequency_toolkit."""

import typer
from rich.console import Console

from flood_frequency_toolkit import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for flood_frequency_toolkit."""
    console.print("Replace this message by putting your code into "
               "flood_frequency_toolkit.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()

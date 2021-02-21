from rich import print
from rich import pretty
pretty.install()
from rich.console import Console

console = Console()

# print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())
console.print("Hello", "World!", style="bold red")
console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")
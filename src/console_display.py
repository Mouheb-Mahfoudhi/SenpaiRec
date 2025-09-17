from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from recommender import recommender
import sys
import utils

def print_table(anime_title):

    table = Table(title=anime_title)

    table.add_column("option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", justify="center", style="cyan", no_wrap=True)
    table.add_column("score", justify="center", style="cyan", no_wrap=True)

    animes = recommender(anime_title)

    for anime in animes:
        table.add_row(str(anime['option']), anime['title'], str(anime['score']))
  
    console = Console()
    console.print(table)


def print_synopsis(anime_title):
    animes = recommender(anime_title)
    choice = int(input("choose an option number to view the corresponding anime's synopsis"))
    if choice==0 or choice not in [anime["option"] for anime in animes]:
        sys.exit()
    else:
        synopsis = utils.get_synopsis(choice,animes)
    
    synopsis_panel = Panel(
        synopsis,
        expand=False,
        border_style="magenta"
    )
    console = Console()
    console.print(synopsis_panel)




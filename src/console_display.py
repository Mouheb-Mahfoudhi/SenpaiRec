from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import recommender

def print_table_anime(anime_title,animes):

    table = Table(title=f"Animes like {anime_title.capitalize()}")

    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", justify="center", style="cyan", no_wrap=True)
    table.add_column("Rating", justify="center", style="cyan", no_wrap=True)
    table.add_column("Ranking", justify="center", style="cyan", no_wrap=True)
    table.add_column("Status", justify="center", style="cyan", no_wrap=True)
    table.add_column("Episodes", justify="center", style="cyan", no_wrap=True)
    table.add_column("Genres", justify="center", style="cyan", no_wrap=True)
    table.add_column("Demographic", justify="center", style="cyan", no_wrap=True)


    option = 1
    for anime in animes:
        max_genres = ", ".join(anime.genre[:4])
        if anime.demographic == None:
            anime.demographic = "unknown"
        table.add_row(str(option), anime.title, str(anime.rating), str(anime.ranking), str(anime.status), str(anime.episodes), max_genres,
                       anime.demographic)
        option +=1

    console = Console()
    console.print(table)
#######################################################################################################################33

def print_synopsis(animes):
    choice = int(input("choose an option number to view the corresponding anime's synopsis\n"))
    while choice not in range (1,11):
        print("Invalid, please choose a correct option number\n")
    else:
        synopsis = animes[choice-1].synopsis
    
    synopsis_panel = Panel(
        synopsis,
        expand=False,
        border_style="magenta"
    )
    console = Console()
    console.print(synopsis_panel)



def start_console():
    anime_title = input ("what anime are you looking for recommendaton for?\n")
    animes = recommender.recommendation_list_anime(anime_title)
    print_table_anime(anime_title,animes)
    print_synopsis(animes)

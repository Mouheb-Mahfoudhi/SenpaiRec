import requests

def return_anime_id(anime_title):
    
    r = requests.get(f"https://api.jikan.moe/v4/anime?q={anime_title.replace(' ', '%20')}")
    data = r.json()
    first_result = data["data"][0]
    return first_result["mal_id"]

def return_manga_id(manga_title):
    
    r = requests.get(f"https://api.jikan.moe/v4/manga?q={manga_title.replace(' ', '%20')}")
    data = r.json()
    first_result = data["data"][0]
    return first_result["mal_id"]

def selection_choice():
    choice = input("are you looking for a (M)anga or an (A)nime? \n")
    return choice.upper()

    
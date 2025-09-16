import requests

def return_anime_id(anime_title):
    r = requests.get(f"https://api.jikan.moe/v4/anime?q={anime_title}")
    data = r.json()
    first_result = data["data"][0]
    return first_result["mal_id"]

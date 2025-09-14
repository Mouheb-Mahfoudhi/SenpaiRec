import requests
import utils

def return_anime_id():
    anime_name = utils.name_converter(input("Which anime are you looking for recommendations for? "))
    r = requests.get(f"https://api.jikan.moe/v4/anime?q={anime_name}")
    data = r.json()
    first_result = data["data"][0]
    return first_result["mal_id"]


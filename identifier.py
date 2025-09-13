import requests
import utils

anime_name = utils.name_converter(input("Which anime are you looking for recommendations for? "))

r = requests.get(f"https://api.jikan.moe/v4/anime?q={anime_name}")

data = r.json()





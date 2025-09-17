import requests
import utils

def get_info_anime(title):
    r = requests.get(f"https://myanimelist.net/anime/{utils.return_anime_id(title)}")

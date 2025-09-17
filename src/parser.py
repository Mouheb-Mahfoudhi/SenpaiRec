import requests
from bs4 import BeautifulSoup
import utils

def get_info(title):

    if(utils.selection_choice() in ["A","ANIME"]):
        r = requests.get(f"https://myanimelist.net/anime/{utils.return_anime_id(title)}")

        soup = BeautifulSoup(r.text,'lxml')
        
        episodes_label = soup.find("span", string="Episodes:")
        episodes = episodes_label.next_sibling.strip()

        status_label = soup.find("span", string="Status:")
        status = status_label.next_sibling.strip()

        ratingValue_label = soup.find("span", string="ratingValue:")
        ratingValue = ratingValue_label.next_sibling.strip()
        
        print("Episodes:", episodes)
        print("Status:", status)
        
get_info('monster')
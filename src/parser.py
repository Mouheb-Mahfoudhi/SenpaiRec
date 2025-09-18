import requests
from bs4 import BeautifulSoup
import utils

def get_info(title):

    if(utils.selection_choice() in ["A","ANIME"]):

        r = requests.get(f"https://myanimelist.net/anime/{utils.return_anime_id(title)}").text
        soup = BeautifulSoup(r,'lxml')
        
        episodes = soup.find("span", string="Episodes:").next_sibling.strip()
        status = soup.find("span", string="Status:").next_sibling.strip()
        rating = soup.find("span", itemprop="ratingValue").text
        ranking = soup.find("span", string="Ranked:").next_sibling.strip()[1::]
        demographic = soup.find("span", string="Demographic:").next_sibling.next_sibling.text
        synopsis = soup.find("span", itemprop="description").text

        return {"episodes":episodes,"status":status, "rating":rating, "ranking":ranking, "demographic":demographic, "synopsis":synopsis}

    else:

        r = requests.get(f"https://myanimelist.net/manga/{utils.return_manga_id(title)}").text
        soup = BeautifulSoup(r,'lxml')

        volumes = soup.find("span", string="Volumes:").next_sibling.strip()
        chapters = soup.find("span", string="Chapters:").next_sibling.strip()
        status = soup.find("span", string="Status:").next_sibling.strip()
        rating = soup.find("span", itemprop="ratingValue").text
        ranking = soup.find("span", string="Ranked:").next_sibling.strip()[1::]
        demographic = soup.find("span", string="Demographic:").next_sibling.next_sibling.text
        synopsis = soup.find("span", itemprop="description").text

        return {"volumes":volumes, "chapters": chapters, "status":status, "rating":rating, "ranking":ranking, "demographic":demographic, "synopsis":synopsis}
    

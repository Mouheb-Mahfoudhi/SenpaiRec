import requests
from bs4 import BeautifulSoup
import utils


def get_info_anime(title):

        r = requests.get(f"https://myanimelist.net/anime/{utils.return_anime_id(title)}").text
        soup = BeautifulSoup(r,'lxml')
        
        episodes = soup.find("span", string="Episodes:").next_sibling.strip()
        status = soup.find("span", string="Status:").next_sibling.strip()
        rating = soup.find("span", itemprop="ratingValue").text
        ranking = soup.find("span", string="Ranked:").next_sibling.strip()[1::]
        synopsis = soup.find("p", itemprop="description").text

        genres = soup.find_all("span", itemprop="genre")
        genre_list = [g.text for g in genres]

        demographic_tag = soup.find("span", string="Demographic:")
        if demographic_tag:
                next_sibling = demographic_tag.next_sibling
                if next_sibling and next_sibling.next_sibling:
                        demographic = next_sibling.next_sibling.text
                else:
                        demographic = None
        else:
                demographic = None

        return {"episodes":episodes,"status":status, "rating":rating, "ranking":ranking, "genres":genre_list, "demographic": demographic, "synopsis":synopsis}

def get_info_manga(title):

        r = requests.get(f"https://myanimelist.net/manga/{utils.return_manga_id(title)}").text
        soup = BeautifulSoup(r,'lxml')

        volumes = soup.find("span", string="Volumes:").next_sibling.strip()
        chapters = soup.find("span", string="Chapters:").next_sibling.strip()
        status = soup.find("span", string="Status:").next_sibling.strip()
        rating = soup.find("span", itemprop="ratingValue").text
        ranking = soup.find("span", string="Ranked:").next_sibling.strip()[1::]
        synopsis = soup.find("span", itemprop="description").text

        genres = soup.find_all("span", itemprop="genre")
        genre_list = [g.text for g in genres]

        demographic_tag = soup.find("span", string="Demographic:")
        if demographic_tag:
                next_sibling = demographic_tag.next_sibling
                if next_sibling and next_sibling.next_sibling:
                        demographic = next_sibling.next_sibling.text
                else:
                        demographic = None
        else:
                demographic = None
        

        
        return {"volumes":volumes, "chapters": chapters, "status":status, "rating":rating, "ranking":ranking, 'genres':genre_list, "demographic":demographic, "synopsis":synopsis}
    
def get_recommendation_anime(id, title):
    r = requests.get(f"https://myanimelist.net/anime/{id}/{title}/userrecs").text
    soup = BeautifulSoup(r, "lxml")
    recommendations = [s.text for s in soup.find_all("strong")[1:20] if not s.text.isdigit()]
    return recommendations



def get_recommendation_manga(id, title):
    recommendations_list = []
    r = requests.get(f"https://myanimelist.net/manga/{id}/{title}/userrecs").text
    soup = BeautifulSoup(r, "lxml")
    recommendations = [s.text for s in soup.find_all("strong")[1:20] if not s.text.isdigit()]
    return recommendations


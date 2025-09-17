import utils
import requests

#function that returns a list containing the id of +-10 recommended animes based on the user requested anime
def recommended_animes(anime_id):
    recommended_list = []
    r = requests.get(f"https://api.jikan.moe/v4/anime/{anime_id}/recommendations")
    recommended = r.json()
    for entry in recommended['data'][:10]:
        recommended_list.append(entry['entry']['mal_id'])

    return recommended_list 


# function that return a list of dictionaries each containing the title, mal rating and synopsis of the each recommended anime
def recommender(anime_title):
    recommendations=[]
    option = 1
    anime_id = utils.return_anime_id(anime_title)
    id_list = recommended_animes(anime_id)
    for id in id_list:
        r = requests.get(f"https://api.jikan.moe/v4/anime/{id}")
        anime = r.json()
        if "data" in anime:
            tmp_dict = {"option" : option, "title": anime['data']['titles'][0]['title'], "score": anime['data']['score'], "synopsis" : anime['data']['synopsis'] }
            recommendations.append(tmp_dict)
            option +=1
        else:
            pass
    return recommendations


#list = recommender()
#for item in list:
#   print(item["option"], item["title"], item["score"])

import identifier
import requests

def recommended_animes(anime_id):
    recommended_list = []
    r = requests.get(f"https://api.jikan.moe/v4/anime/{anime_id}/recommendations")
    recommended = r.json()
    for entry in recommended['data'][:10]:
        recommended_list.append(entry['entry']['mal_id'])

    return recommended_list


def recommender():
    recommendations=[]
    anime_id = identifier.return_anime_id()
    id_list = recommended_animes(anime_id)
    for id in id_list:
        r = requests.get(f"https://api.jikan.moe/v4/anime/{id}")
        anime = r.json()
        if "data" in anime:
            tmp_dict = {"title": anime['data']['titles'][0]['title'], "score": anime['data']['score'], "synopsis" : anime['data']['synopsis'] }
            print(tmp_dict)
            recommendations.append(tmp_dict)
        else:
            pass
    return recommendations



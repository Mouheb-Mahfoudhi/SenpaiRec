import identifier
import requests

def recommender():
    recommendation_limit = 0
    recommendations=[]
    anime_id = identifier.return_anime_id()
    r = requests.get(f"https://api.jikan.moe/v4/anime/{anime_id}/recommendations")
    recommended = r.json()
    for entry in recommended['data'][:10]:
        recommendations.append(entry['entry']['title'])
    return recommendations

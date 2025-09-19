import show
import parser

def recommendation_list_anime(title):
    recommendation_list=[]
    anime_requested = show.Anime(title)
    recommendation_titles = parser.get_recommendation_anime(anime_requested.id,title)
    for recommendation in recommendation_titles:
        recommendation_list.append(show.Anime(recommendation))
    

    return recommendation_list



def recommendation_list_manga(title):
    recommendation_list=[]
    anime_requested = show.Manga(title)
    recommendation_titles = parser.get_recommendation_manga(anime_requested.id,title)
    for recommendation in recommendation_titles:
        recommendation_list.append(show.Manga(recommendation))
    

    return recommendation_list
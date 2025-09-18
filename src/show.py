import utils
import parser

class Show:
    def __init__(self, title):
        self.title = title
    

class Anime(Show):
    def __init__(self, title):
        super().__init__(title)
        self.id = utils.return_anime_id(title)
        anime = parser.get_info_anime(title)
        self.episodes = anime["episodes"]
        self.status = anime["status"]
        self.rating = anime["rating"]
        self.ranking = anime["ranking"]
        self.demographic = anime["demographic"]
        self.synopsis = anime["synopsis"]


class Manga(Show):
    def __init__(self, title):
        super().__init__(title)
        self.id = utils.return_manga_id(title)
        manga = parser.get_info_manga(title)
        self.chapters = manga["chapters"]
        self.volumes = manga["volumes"]
        self.status = manga["status"]
        self.rating = manga["rating"]
        self.ranking = manga["ranking"]
        self.demographic = manga["demographic"]
        self.synopsis = manga["synopsis"]


anime1 = Anime('monster')
manga1 = Manga('berserk')


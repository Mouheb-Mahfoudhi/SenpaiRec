import utils

class Show:
    def __init__(self, title, rating, ranking, status, demographic):
        self.id = utils.return_anime_id(utils.name_converter(title))
        self.title = title
        self.rating = rating
        self.ranking = ranking
        self.status = status
        self.demographic = demographic
    

class Anime(Show):
    def __init__(self, title, rating, ranking, status, demographic, episodes, synopsis):
        super().__init__(title, rating, ranking, status, demographic)
        self.episodes = episodes
        self.synopsis = synopsis


class Manga(Show):
    def __init__(self, title, rating, status, demographic, volumes, chapters, synopsis):
        super().__init__(title, rating, status, demographic)
        self.volumes = volumes
        self.chapters = chapters
        self.synopsis = synopsis





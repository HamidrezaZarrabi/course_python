from actor import Actor
import pytube

class Media():
    def __init__(self, id, type, name, director, IMDB_score, url, duration, casts):
        self.id = id
        self.type = type
        self.name = name
        self.director = director
        self.IMDB_score = IMDB_score
        self.url = url
        self.duration = duration
        casts = casts.split(',')
        self.casts = []
        for cast in casts:
            self.casts.append(Actor(cast))    

    def download(self):
        link = self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename='video.mp4')








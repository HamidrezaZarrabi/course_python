from media import Media

class Clip(Media):
    def __init__(self, id, name, director, IMDB_score, url, duration, casts):
        Media.__init__(self, id, 'Clip', name, director, IMDB_score, url, duration, casts)
    def show_info(self):
        casts = '['
        for indx, cast in enumerate(self.casts):
            if indx == len(self.casts) - 1:
                casts = casts + cast.show_info() + ']'
            else:
                casts = casts + cast.show_info() + ','
        print('id: ' + self.id + ', ' + 'type: ' + self.type + ', ' + "name: " + self.name + ', ' + "director: ", self.director 
        + ', ' + "IMDB_score: " + self.IMDB_score + ', ' + "url: " + self.url + ', ' + "duration: " + self.duration + ', ' + "casts: " + str(casts))        
        
    def write_info(self, f):
        casts = '['
        for indx, cast in enumerate(self.casts):
            if indx == len(self.casts) - 1:
                casts = casts + cast.show_info() + ']'
            else:
                casts = casts + cast.show_info() + ','
        f.write(self.id + ',' + self.type + ',' + self.name + ',' + self.director + ',' + self.IMDB_score 
        + ',' + self.url + ',' + self.duration + ',' + str(casts) + '\n')
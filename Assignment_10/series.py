from media import Media

class Series(Media):
    def __init__(self, id, name, director, IMDB_score, url, duration, season, part, casts):
        Media.__init__(self, id, 'Series', name, director, IMDB_score, url, duration, casts)
        self.season = season
        self.part = part
    def show_info(self):
        casts = '['
        for indx, cast in enumerate(self.casts):
            if indx == len(self.casts) - 1:
                casts = casts + cast.show_info() + ']'
            else:
                casts = casts + cast.show_info() + ','
        print('id: ' + self.id + ', ' + 'type: ' + self.type + ', ' + "name: " + self.name + ', ' + "director: ", self.director 
        + ', ' + "IMDB_score: " + self.IMDB_score + ', ' + "url: " + self.url + ', ' + "duration: " + self.duration + ', ' + 
        ', ' + "season: " + self.season, ', ' + "part: " + self.part + ', ' + "casts: " + str(casts))
    def write_info(self, f):
        casts = '['
        for indx, cast in enumerate(self.casts):
            if indx == len(self.casts) - 1:
                casts = casts + cast.show_info() + ']'
            else:
                casts = casts + cast.show_info() + ','
        f.write(self.id + ',' + self.type + ',' + self.name + ',' + self.director + ',' + self.IMDB_score 
        + ',' + self.url + ',' + self.duration + ',' + self.season + ',' + self.part + ',' + str(casts) + '\n')
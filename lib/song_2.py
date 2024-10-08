class Song:
    all = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.all.append(self)
        
    @classmethod
    def get_song_count(cls):
        return len(cls.all)
    
    @classmethod
    def get_artists(cls):
        artists = set()
        for song in cls.all:
            artists.add(song.artist)
        return artists
    
    @classmethod
    def get_artist_counts(cls):
        result = {}
        for song in cls.all:
            if song.artist not in result:
                result[song.artist] = 1
            else:
                result[song.artist] += 1
        return result
    
    @classmethod
    def get_genres(cls):
        genres = set()
        for song in cls.all:
            genres.add(song.genre)
        return genres
    
    @classmethod
    def get_genre_counts(cls):
        result = {}
        for song in cls.all:
            if song.genre not in result:
                result[song.genre] = 1
            else:
                result[song.genre] += 1
        return result


s1 = Song('ironic', 'alanis morrisette', 'pop')
s1 = Song('ironic', 'alanis morrisette', 'pop')
s2 = Song('sk8r boi', 'avril lavigne', 'pop')

print(Song.get_song_count())
print(Song.get_artists())
print(Song.get_artist_counts())
print(Song.get_genres())
print(Song.get_genre_counts())
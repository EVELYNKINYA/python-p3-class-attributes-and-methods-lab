class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
toxic = Song("Toxic", "Britney Spears", "Pop")
rolling_in_the_deep = Song("Rolling in the Deep", "Adele", "Pop")

print(Song.count)  # Output: 3
print(Song.genres)  # Output: ['Rap', 'Pop']
print(Song.artists)  # Output: ['Jay-Z', 'Britney Spears', 'Adele']
print(Song.genre_count)  # Output: {'Rap': 1, 'Pop': 2}
print(Song.artist_count)  # Output: {'Jay-Z': 1, 'Britney Spears': 1, 'Adele': 1}


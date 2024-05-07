""" Briefly describe a possible collection of classes that can be used to represent a music
collection (for example, inside a music player), focusing on how they would be related using
aggregation only or combination between aggregation and weak association. You should
include classes for songs, artists and playlists.
Hint: write down the three class names, draw a line between each pair of classes which you
think should have a relationship, and decide what kind of relationship would be the most
appropriate.
For simplicity, you can assume that any song has a single “artist”, and the “playlists” can
contain multiple songs. Before you start your coding, you need to identify the attributes and
methods needed for each class. For example, the song class will need to store information
about the artist name, song title and time duration of the song. The Playlist class should
contain a method that prints the song titles of all songs it contains. Once you defined the
necessary classes, you need to initialise the necessary objects to test the functionalities of
your code.
"""

class song:
    def __init__(self, artist_name, artist_song_title, song_duration):
        self.artist_name = artist_name
        self.song_title = artist_song_title
        self.duration = song_duration

    def display_song_info(self):
        for item in self.song_title:
            print("The Song Title is =",item)
        print(" ")

class artist:
    def __init__(self, artist_name):
        self.artist_name = artist_name

class artist_playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs = []

    def set_song(self, s):
        self.songs.append(s)

    def display_playlist(self):
        print(f"Playlist: {self.playlist_name}")
        for i in self.songs:
            i.display_song_info()
            #print(song.song_title)

# Create songs and artists
artist_name = []
songs_details = []
playlist_details = []
song_title = []
# Take student details as input
while True:
    artistn = input("Enter the name of Artist = ")
    songtitle = input("Enter the song title = ")
    song_duration = input("Enter the song duration =: ")
    artist_name.append(artistn)
    song_title.append(songtitle) 
    songs_details.append(song_duration)
    nxt = input("Do you want to add more songs in playlist[Yes/No]=")
    if nxt == "no":
        break
    else:
        pass


playlist_name = input("Enter the Playlist name = ")
print(" ")
playlist_details = playlist_name

artist1 = artist(artist_name)


obj_song = song(artist1.artist_name, song_title, songs_details)

# Create a playlist and add songs
playlist = artist_playlist(playlist_details)
playlist.set_song(obj_song)
playlist.display_playlist()







        
        
        
        
        
        









        
class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []
    def add_song(self,song):
        self.songs.append(song)
    def remove_song(self,title):
        if title in self.songs:
            self.songs.remove(title)
    def show_songs(self):
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f'-{song}')
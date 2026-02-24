class Song:
    def __init__(self,title,artist,duration,year,genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.year = year
        self.genre = genre
    def __str__(self):
        return f"{self.title} by {self.artist} ({self.year}) - {self.genre}, {self.duration} minutes"
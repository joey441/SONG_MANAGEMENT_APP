import json
def save_playlist(playlist, filename='playlists.json'):
    data=[]
    for song in playlist.songs:
        data.append({
            'title': song.title,
            'artist': song.artist,
            'duration': song.duration,
            'year': song.year,
            'genre': song.genre
        })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Playlist '{playlist.name}' saved to {filename} successfully!")
def load_playlist(playlist, filename='playlists.json'):
   
        with open(filename, 'r') as f:
            data = json.load(f) 
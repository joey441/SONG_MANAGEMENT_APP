from playlist import Playlist
from file_manager import save_playlist, load_playlist
from song import Song
import utils

def main():
    # Create a playlist
    my_playlist = Playlist("My Favorite Songs")
    
    while True:
        # Use the helper function to show menu
        utils.display_menu()
        
        # Use the helper function to get valid choice
        choice = utils.get_valid_choice()
        
        if choice == '1':
            # Add Song - main.py handles the actual work
            print("\n--- Add New Song ---")
            title = input("Song title: ")
            artist = input("Artist: ")
            duration = input("Duration (MM:SS): ")
            genre = input("Genre: ")
            year = input("Year: ")
            
            new_song = Song(title, artist, duration, genre, year)
            my_playlist.add_song(new_song)
            print(f" Added: {title}")
            
        elif choice == '2':
            # View All Songs - main.py handles the logic
            print("\n--- Your Playlist ---")
            if not my_playlist.songs:
                print(" No songs in playlist")
            else:
                for i, song in enumerate(my_playlist.songs, 1):
                    # Use helper function to format song
                    print(utils.print_song(song, i))
                    
        elif choice == '3':
            # Update Song
            print("\n--- Update Song ---")
            if not my_playlist.songs:
                print(" No songs to update")
                continue
                
            # Show songs with numbers
            for i, song in enumerate(my_playlist.songs, 1):
                print(utils.print_song(song, i))
            
            # Get song to update
            try:
                song_num = int(input("\nEnter song number to update: ")) - 1
                if 0 <= song_num < len(my_playlist.songs):
                    song = my_playlist.songs[song_num]
                    
                    # Get new details
                    print("(Press Enter to keep current value)")
                    
                    new_title = input(f"Title [{song.title}]: ") or song.title
                    new_artist = input(f"Artist [{song.artist}]: ") or song.artist
                    new_duration = input(f"Duration [{song.duration}]: ") or song.duration
                    new_genre = input(f"Genre [{song.genre}]: ") or song.genre
                    new_year = input(f"Year [{song.year}]: ") or song.year
                    
                    # Update song
                    song.title = new_title
                    song.artist = new_artist
                    song.duration = new_duration
                    song.genre = new_genre
                    song.year = new_year
                    
                    print(" Song updated!")
                else:
                    print(" Invalid song number")
            except ValueError:
                print(" Please enter a valid number")
                
        elif choice == '4':
            # Delete Song
            print("\n--- Delete Song ---")
            if not my_playlist.songs:
                print(" No songs to delete")
                continue
                
            # Show songs with numbers
            for i, song in enumerate(my_playlist.songs, 1):
                print(utils.print_song(song, i))
            
            # Get song to delete
            try:
                song_num = int(input("\nEnter song number to delete: ")) - 1
                if 0 <= song_num < len(my_playlist.songs):
                    song = my_playlist.songs[song_num]
                    
                    # Use helper to confirm
                    if utils.confirm_action(f"delete '{song.title}'"):
                        my_playlist.remove_song(song)
                        print(" Song deleted!")
                else:
                    print(" Invalid song number")
            except ValueError:
                print(" Please enter a valid number")
                
        elif choice == '5':
            # Save to File
            if utils.confirm_action("save playlist"):
                save_playlist(my_playlist)
                
        elif choice == '6':
            # Load from File
            if utils.confirm_action("load playlist (this will replace current songs)"):
                load_playlist(my_playlist)
                
        elif choice == '7':
            # Exit
            if utils.confirm_action("exit"):
                print(" Goodbye!")
                break

if __name__ == "__main__":
    main()



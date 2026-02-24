# utils.py - Small, reusable helper functions

def display_menu():
    """Just shows the menu - that's all it does!"""
    print("\n" + "="*40)
    print(" SONG MANAGEMENT APP")
    print("="*40)
    print("1. Add Song")
    print("2. View All Songs")
    print("3. Update Song")
    print("4. Delete Song")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")
    print("="*40)

def get_valid_choice():
    """Gets user input and makes sure it's valid"""
    while True:
        choice = input("Choose (1-7): ")
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            return choice
        print(" Invalid choice! Please enter 1-7")

def print_song(song, number):
    """Formats a single song nicely for display"""
    return f"{number}. {song.title} - {song.artist} ({song.duration}) [{song.genre}, {song.year}]"

def confirm_action(action):
    """Asks user 'Are you sure?' before doing something"""
    response = input(f"Are you sure you want to {action}? (yes/no): ")
    return response.lower() == 'yes'
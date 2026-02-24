# SONG MANAGEMENT BACKEND APP

A professional console-based Song Management System built with Python, demonstrating Object-Oriented Programming (OOP) principles. This app allows users to Create, Read, Update, and Delete songs in a playlist with full data persistence.
## video showcasing the app working
https://app.clipchamp.com/consumer/editor?driveId=BAB00C4DA077C08D&folderId=BAB00C4DA077C08D!s56734f931a23409da7335e935bc7f690&itemId=BAB00C4DA077C08D!s16932009f56e4be389ba0ac9c636550c

## ✨ Features

### Core Features ✅
- **Create** - Add new songs with title, artist, duration, genre, and year
- **Read** - View all songs in your playlist with detailed information
- **Update** - Edit any song's information
- **Delete** - Remove songs from your playlist
- **Data Validation** - Prevents duplicate songs and validates user input

### Professional Features ✅
- **Multiple Playlists** - Create and manage different playlists
- **Search Functionality** - Find songs by title, artist, or genre
- **Sort Options** - Sort songs by artist, duration, or year
- **File Persistence** - Save/load playlists from JSON files
- **Error Handling** - Robust try-except blocks for all user inputs

### Bonus Features ✅
- **Export/Import** - Export playlists to CSV format
- **Statistics** - View total songs, total duration, and artist statistics
- **Colorful Output** - Enhanced console interface with colors

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **JSON** - Data persistence and storage


## 📋 Prerequisites

Before you begin, ensure you have installed:
- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/song-management-app.git
cd song-management-app
### 2. Create and activate virtual environment
 Windows:
      python -m venv venv
      venv\Scripts\activate
Mac/Linux:
      python -m venv venv
      source venv\Scripts\activate
📁 Project Structure
song-management-app/
│
├── main.py                 # Main application entry point
├── song.py                 # Song class definition
├── playlist.py             # Playlist class definition
├── file_manager.py         # File operations (save/load)
├── utils.py                # Helper functions

│---playlists.json      # Default playlist storage
│


│

├── README.md               # Project documentation

import random

"""Using a QUEUE structure for this assignment"""
class Song():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    #equal to
    # def __eq__(self, other):
    #     return ((self.title, self.artist) == (other.title, other.artist))
    
    #not equal
    # def __ne__(self, other):
    #     return not (self == other)
    
    #less than
    # def __lt__(self, other):
    #     return ((self.title, self.artist) < (other.title, other.artist))
        
    #greater than
    # def __gt__(self, other):
    #     return ((self.title, self.artist) < (other.title, other.artist))


class SongQue:
    def __init__(self, data = 0, current = False):
        self.playList = []
        self.data(data)
        self.currentlyPlaying(current)

    def data(self, index):
        self.data = index

    """ 1. Add songs to a playlist """
    def add(self, song):

        if self.size() > 0:
            # If true, insert song at index of listSize + 1. 
            self.playList.insert(self.size() + 1, song)
        else:
            # If not, insert at 0
            self.playList.insert(0, song)

    """ 2. Remove songs from a playlist """
    def remove(self, title):
            # Remove songs from a playlist
            song_index = 0
            
            # For each item in the song store
            for item in self.playList:
                # If the title is equal to the song title, we've found the index
                if item.title == title:
                    break   
                # If the above if statement didnt break this loop, keep looking and add +1 to keep track of the song index to be popped
                song_index += 1

            # Pop Song Index from the song store because we've found the index of the title the user specified in the input
            self.playList.pop(song_index)
            
    """ 3. Play the current selected song, default is the first song on the playlist"""
    def play(self, song_index):
        self.data = song_index
        self.currentlyPlaying(True)
        
    """ 4. Skip to the next song on the playlist. If at end of list, restart from the beginning"""
    def next(self):
        if self.curently_playing:
            playlistLen = len(self.playList) - 1
            
            # If song is last index, next song will be index 0 making circular queue
            if self.data == playlistLen:
                next_song = 0
            else:
                next_song = self.data + 1

            print("\nSkipping....")
            self.play(next_song)
        else:
            print('\nNothing is Playing!')
        
    """ 5. Go back to the previous song on the playlist.  If at the start, go back to the end of the list."""
    
    def prev(self):
        if self.curently_playing:

            # Set playlist length for 1 less than the length of the store
            playlistLen = len(self.playList) - 1
            
            # If the song index is 0, prev song is playlist len index (1 song)
            if self.data == 0:
                prev_song = playlistLen
            else:
                # else play the prev song (song at the index of the current song - 1)
                prev_song = self.data - 1

            print("\nReplaying....")
            self.play(prev_song)
        else:
            print('\nNothing is Playing!')
             
    """ 6. Randomly shuffle the song list. Create your own algorithm to randomly sort the data structure you have chosen to use.  
        This algorithm does not need to be efficient. """
    def shuffle(self):
        listLen = self.size()
        
        for i in range(listLen // 2):
            # remove first element and append to end of list
            songPop = self.playList.pop(0)
            self.playList.append(songPop)
        
        for i in range(listLen):
            # Generate random number based on size of list
            random_num = random.randint(0, listLen - 1)

            # Pop off random element append to end of list
            list_element = self.playList.pop(random_num)
            self.playList.append(list_element)
            
            
    """ 7. Show Currently Playing Song """
    def currentlyPlaying(self, current):
        self.curently_playing = current
    
    def currentSong(self):
        if self.curently_playing:
            print("\nCurrently Playing:")
            print(self.playList[self.data])
        else:
            print('\nPlease Play a Song to Display Currently Playing')
    
    """ 8. Show Current Playlist Order"""
    def size(self):
        return len(self.playList)

    def myPlaylist(self):
        x = 1
        print("\nSong List:\n")
        for item in self.playList:
            print(str(x) + '. ' + str(item))
            x += 1

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")
    print('\n')
    
""" Preload your playlist with at least six songs of your choice """
currentQue = SongQue()
currentQue.add(Song('Bossa Uh', 'Potsu'))
currentQue.add(Song('Gazebo', 'Potsu'))
currentQue.add(Song('Goodbye Autumn', 'Tomppabeats'))
currentQue.add(Song('Hillside', 'Chromonicci'))
currentQue.add(Song('Telecaster Luv', 'Slipfunc'))
currentQue.add(Song('Violet', 'A Boy With A Balloon'))


while True:
    menu()
    choice = int(input())
    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        title = input('Enter Song Title: ')
        artist = input('Enter Song Artist: ')
        # Add song to playlist
        newSong = Song(title, artist)
        currentQue.add(newSong)
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        title = input('Enter the Song Title to be Removed: ')
        # remove song from playlist
        currentQue.remove(title)
        print("Song Removed from Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        currentQue.play(0)
        # Display song name that is currently playing
        currentQue.currentSong()
        print("Playing....")        
    elif choice == 4:
        # Skip to the next song on the playlist
        currentQue.next()
        # Display song name that is now playing
        currentQue.currentSong()
        print("Skipping....")                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        currentQue.prev()
        # Display song name that is now playing
        currentQue.currentSong()
        print("Replaying....")  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        currentQue.shuffle()
        currentQue.play(0)
        # Display song name that is now playing
        currentQue.currentSong()
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        currentQue.currentSong()
        print("Currently playing: ", end=" ")    
    elif choice == 8:
        # Show the current song list order
        currentQue.myPlaylist()
        print("\nSong list:\n")
    elif choice == 0:
        print("Goodbye.")
        break
    

    
    
    
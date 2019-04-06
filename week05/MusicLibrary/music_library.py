import datetime
import random
import json

class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist 
        self.album = album
        self._length = length
    
    def __str__(self):
        return '{} -  {} from {} - {}'.format(self.artist, self.title, self.album, self._length)

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and self.album == other.album and self.length() == other.length()

    def __hash__(self):
        return hash(self.title. self.artist, self.album, self.length())

    def length(self, seconds = False, minutes = False, hours = False):
        
        timelst = self._length.split(':')
        if len(timelst) < 3:
            timelst.insert(0, '00')
        
        if seconds:
            return str((int(timelst[0]) * 3600) + (int(timelst[1]) * 60) + int(timelst[2]))
        if minutes:
            #in order to remove the 0 if the number of minutes is less than 9
            return str(int(timelst[1]))
        if hours:
            #in order to remove the 0 if the number of hours is less than 9
            return str(int(timelst[0]))

        return self._length

class Playlist:
    def __init__(self, name, repeat = False, shuffle = False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist_songs = []
        self.already_played_songs_indexes = []
    
    def add_song(self, song):
        self.playlist_songs.append(song)
    
    def remove_song(self, song):
        self.playlist_songs.remove(song)
    
    def add_songs(self, songs):
        for song in songs:
            self.playlist_songs.append(song)
    
    def total_length(self):
        total_seconds = 0

        for song in self.playlist_songs:
            total_seconds += int(song.length(seconds = True))
        
        return str(datetime.timedelta(seconds = total_seconds))
    
    def artists(self):
        artist_dic = {}
        for song in self.playlist_songs:
            if song.artist in artist_dic:
                artist_dic[song.artist] += 1
            else:
                artist_dic.update({song.artist : 1})

        return artist_dic

    def curr_song_index(self, current_song):
        return self.playlist_songs.index(current_song)

    def next_song(self, current_song): 
        if self.shuffle:
            if self.repeat:
                if len(self.already_played_songs_indexes) == len(self.playlist_songs):
                    self.already_played_songs_indexes = []
            
            x = [i for i in range(len(self.playlist_songs)) if i not in self.already_played_songs_indexes]
            rnd_song_index = random.choice(x)
            self.already_played_songs_indexes.append(rnd_song_index)
            return self.playlist_songs[rnd_song_index]

        if self.repeat:
            if self.curr_song_index(current_song) + 1 == len(self.playlist_songs):
                return self.playlist_songs[0]

        if self.curr_song_index(current_song) + 1 == len(self.playlist_songs):
            return "End of the playlist"
        return self.playlist_songs[self.curr_song_index(current_song) + 1]
    
    def all_songs(self):
        return self.playlist_songs

    def pprint_playlist(self):
        pass

    def save(self):
        song_dic = {}
        for playlist_order, song in enumerate(self.playlist_songs):
            song_dic.update({str(playlist_order) : song.__dict__}) 
        
        d = {self.name : song_dic}

        with open("data.json", "w") as f:
            f.write(json.dumps(d, indent = 4))

    @staticmethod
    def load(path):
        with open(path, 'r') as f:
            data = json.load(f)
        
        song_list = []
        for info in list(data.values()):
            for song_args in list(info.values()):
                song_list.append(Song(*song_args.values()))
        
        new_playlist = Playlist(next(iter(data)))
        new_playlist.add_songs(song_list)
        
        return new_playlist

def main():
    song = Song(title="Odin", artist="Manowar1", album="The Sons of Odin", length="3:44")
    song2 = Song(title="Odin", artist="Manowar2", album="The Sons of Odin", length="3:44")
    song3 = Song(title="Odin", artist="Manowar3", album="The Sons of Odin", length="3:44")
    song4 = Song(title="Odin", artist="Manowar4", album="The Sons of Odin", length="3:44")
    song5 = Song(title="Odin", artist="Manowar5", album="The Sons of Odin", length="3:44")
    song6 = Song(title="Odin", artist="Manowar6", album="The Sons of Odin", length="3:44")
    playlist = Playlist(name="Code", repeat=True, shuffle=True)
    songs = [song, song2, song3, song4, song5, song6]
    playlist.add_songs(songs)
     
    playlist.save()
    pls = Playlist.load('data.json')
    print(pls.artists())

if __name__ == '__main__':
    main()
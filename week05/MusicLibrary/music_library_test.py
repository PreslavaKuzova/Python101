import unittest
from music_library import Song, Playlist

class TestPolynomials(unittest.TestCase):
    def test_length_of_the_song_and_return_it_in_seconds(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:59")
        expected_result = '239'
        self.assertEqual(song.length(seconds = True), expected_result)
    
    def test_length_of_the_song_and_return_the_minutes(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="03:44")
        expected_result = '3'
        self.assertEqual(song.length(minutes = True), expected_result)

    def test_length_of_the_song_and_return_the_hours(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="03:44")
        expected_result = '0'
        self.assertEqual(song.length(hours = True), expected_result)

    def test_length_of_the_song_and_return_the_length_itself(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="03:44")
        expected_result = '03:44'
        self.assertEqual(song.length(), expected_result)

    def test_add_list_of_songs_to_an_empty_playlist_then_return_the_total_length_of_the_songs(self):
        song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        song2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        song3 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        playlist = Playlist(name="Code", repeat=True, shuffle=True)
        playlist.add_songs([song, song2, song3])
        expected_result = '0:11:12'
        self.assertEqual(playlist.total_length(), expected_result)

    def test_the_function_artists_of_a_playlist_then_return_dictionary_where_keys_are_the_artists_and_values_are_the_numbers_of_the_songs(self):
        song = Song(title="Odin", artist="Manowar1", album="The Sons of Odin", length="3:44")
        song2 = Song(title="Odin", artist="Manowar2", album="The Sons of Odin", length="3:44")
        song3 = Song(title="Odin", artist="Manowar3", album="The Sons of Odin", length="3:44")
        playlist = Playlist(name="Code", repeat=True, shuffle=True)
        playlist.add_songs([song, song2, song3])
        expected_result = {'Manowar1': 1, 'Manowar2': 1, 'Manowar3': 1}
        self.assertEqual(playlist.artists(), expected_result)

    def test_returning_playlist_next_song_when_reach_the_last_song_and_no_shuffle_and_no_repeat(self):
        song = Song(title="Odin", artist="Manowar1", album="The Sons of Odin", length="3:44")
        song2 = Song(title="Odin", artist="Manowar2", album="The Sons of Odin", length="3:44")
        song3 = Song(title="Odin", artist="Manowar3", album="The Sons of Odin", length="3:44")
        playlist = Playlist(name="Code", repeat=False, shuffle=False)
        playlist.add_songs([song, song2, song3])
        expected_result = "End of the playlist"
        self.assertEqual(playlist.next_song(song3), expected_result)

    def test_returning_playlist_next_song_when_reach_the_last_song_and_repeat_and_no_shuffle_then_return_the_first_song(self):
        song = Song(title="Odin", artist="Manowar1", album="The Sons of Odin", length="3:44")
        song2 = Song(title="Odin", artist="Manowar2", album="The Sons of Odin", length="3:44")
        song3 = Song(title="Odin", artist="Manowar3", album="The Sons of Odin", length="3:44")
        playlist = Playlist(name="Code", repeat=True, shuffle=False)
        playlist.add_songs([song, song2, song3])
        expected_result = song
        self.assertEqual(playlist.next_song(song3), expected_result)

    def test_returning_playlist_next_song_when_reach_the_last_song_and_shuffle_and_no_repeat_then_return_a_song(self):
        song = Song(title="Odin", artist="Manowar1", album="The Sons of Odin", length="3:44")
        song2 = Song(title="Odin", artist="Manowar2", album="The Sons of Odin", length="3:44")
        song3 = Song(title="Odin", artist="Manowar3", album="The Sons of Odin", length="3:44")
        playlist = Playlist(name="Code", repeat=False, shuffle=True)
        playlist.add_songs([song, song2, song3])
        expected_result = song
        self.assertEqual(type(playlist.next_song(song3)), type(expected_result))

if __name__ == '__main__':
    unittest.main()
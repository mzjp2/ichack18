import spotipy
import jsonreader
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=jsonreader.spotify_client_id, client_secret=jsonreader.spotify_client_key)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


uri = ''
anal = sp.audio_features('5CtI0qwDJkDQGwXD1H1cLb')
print(anal)
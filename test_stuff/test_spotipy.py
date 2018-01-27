import spotipy
import jsonreader
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=jsonreader.spotify_client_id, client_secret=jsonreader.spotify_client_key)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


data = sp.recommendations(seed_genres=['piano'], limit = 20)
data_list = data['tracks']



for d_point in data_list:
	print(d_point['id'], i)
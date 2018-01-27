import spotipy
import jsonreader
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=jsonreader.spotify_client_id, client_secret=jsonreader.spotify_client_key)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

despacito = '5CtI0qwDJkDQGwXD1H1cLb'


uri = ''
anal = sp.audio_features('5CtI0qwDJkDQGwXD1H1cLb')

"""
f = open('spotify_tags.txt', 'w')

for key in anal[0].keys():
	f.write(key + "\n")

f.close()


print(sp.recommendation_genre_seeds())

f = open('recommendation_genre_seeds.txt', 'w')

for genre in sp.recommendation_genre_seeds()['genres']:
	f.write(genre + "\n")

f.close()
"""




print(len(sp.recommendations(seed_tracks=['5CtI0qwDJkDQGwXD1H1cLb'])))

print(type(sp.recommendations(seed_tracks=['5CtI0qwDJkDQGwXD1H1cLb'])))


print(sp.recommendations(seed_tracks=['5CtI0qwDJkDQGwXD1H1cLb']).keys())
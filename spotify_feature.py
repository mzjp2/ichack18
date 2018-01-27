import spotipy, jsonreader, json
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=jsonreader.spotify_client_id, client_secret=jsonreader.spotify_client_key)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def dumpFeatures(track_list):

	for track_id in track_list:

		features = sp.audio_features(track_id)
		track_name = sp.track(track_id)['name']
		with open('features/' + track_name + '_features.json', 'w') as outfile:
			json.dump(features, outfile, indent=4)

	return None

dumpFeatures(['5CtI0qwDJkDQGwXD1H1cLb'])

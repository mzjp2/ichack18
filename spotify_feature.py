import spotipy, jsonreader, json
from spotipy.oauth2 import SpotifyClientCredentials

# authentication stuff

client_credentials_manager = SpotifyClientCredentials(client_id=jsonreader.spotify_client_id, client_secret=jsonreader.spotify_client_key)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

spot_tags = []

# generate genre

def generateGenre(spot_tags):
	return 'piano'

# generate recommended list based on genre

def recommendedList(genre):
	recommendations_dict = sp.recommendations(seed_genres = [genre], limit = 100)
	data_list = recommendations_dict['tracks']
	track_list = [0] * 100
	i=0
	for d_point in data_list:
		track_list[i] = d_point['id']
		i += 1


	return track_list
# takes in track_list (list of tracks) and outputs json features of the track

def dumpFeatures(track_list):

	features = [0] * 100
	i = 0
	for track_id in track_list:
		features[i] = sp.audio_features(track_id)
		i += 1
	#	track_name = sp.track(track_id)['name']
	return features

genre = generateGenre(spot_tags)
track_list = recommendedList(genre)
feature = dumpFeatures(track_list)
print(feature)


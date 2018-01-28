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

def recommendedList(genre, limit=10):
	recommendations_dict = sp.recommendations(seed_genres = [genre], limit = limit)
	data_list = recommendations_dict['tracks']
	track_list = [0] * limit
	i=0
	for d_point in data_list:
		track_list[i] = d_point['id']
		i += 1


	return track_list
	
# takes in track_list (list of tracks) and outputs json features of the track

def dumpFeatures(track_list, limit=10):

	features = [0] * limit
	i = 0
	for track_id in track_list:
		features[i] = sp.audio_features(track_id)
		i += 1
	#	track_name = sp.track(track_id)['name']
	return features

def averageTags(tracks_features_list):
	"""
	Getting list from sp.recommendations()
	Returning average value of the wanted tags
	"""


	tag_values = {"danceability": 0,"energy": 0, "acousticness": 0,"instrumentalness": 0,"liveness": 0,"valence": 0,"tempo": 0,}
	for track in tracks_features_list:
		for key in tag_values.keys():
			tag_values[key] += track[0][key]

	l = float(len(tracks_features_list))

	for key in tag_values.keys():
		tag_values[key] = tag_values[key] / l

	return tag_values

if __name__ == '__main__':
	genre = generateGenre(spot_tags)
	track_list = recommendedList(genre)
	feature = dumpFeatures(track_list)
	averaged_tag = averageTags(feature)
	print(averaged_tag)

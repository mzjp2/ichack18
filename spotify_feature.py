import spotipy, jsonreader, json
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
from tagtospot import tag_to_mood
from analyse_image import get_image_tags

# authentication stuff

client_credentials_manager = SpotifyClientCredentials(client_id=jsonreader.spotify_client_id, client_secret=jsonreader.spotify_client_key)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

spot_tags = []

# generate genre

def generateGenre(spot_tags, list_len=2):
	infile = open('proper_avg_gen.json', 'r')
	f = json.load(infile)


	genres_nparrays = {}
	for genre in f.keys():
		spot_tags_arr = []
		genre_values_list = []
		for i in enumerate(f[genre]):
			if i[1] == 'tempo':
				genre_values_list.append(f[genre][i[1]])
				spot_tags_arr.append(spot_tags[i[1]]/float(250))
			else:
				genre_values_list.append(f[genre][i[1]])
				spot_tags_arr.append(spot_tags[i[1]])

		genres_nparrays[genre] = np.array(genre_values_list)

	spot_tags_arr = np.array(spot_tags_arr)

	dist = {}
	sugg_list = []

	for genre in genres_nparrays.keys():
		dist[genre] = np.linalg.norm(genres_nparrays[genre]-spot_tags_arr)


	for _ in range(list_len):
		max1 = min(dist, key=dist.get)
		sugg_list.append(max1)
		del dist[max1]

	return sugg_list



# generate recommended list based on genre

def recommendedList(genre_list, limit=10):
	recommendations_dict = sp.recommendations(seed_genres = genre_list, limit = limit)
	data_list = recommendations_dict['tracks']
	track_list = [0] * limit
	i=0
	for d_point in data_list:
		track_list[i] = d_point['id']
		i += 1


	return track_list

# takes in track_list (list of tracks) and outputs json features of the track

def dumpFeatures(track_list, limit = 10):

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

if __name__ == '__main_':
	genre = generateGenre(spot_tags)
	track_list = recommendedList(genre)
	feature = dumpFeatures(track_list)
	averaged_tag = averageTags(feature)
	print(averaged_tag)

if __name__ == '__main_':
	genres_txt = open('genre.txt', 'r')
	genre_list = []

	for genre in genres_txt.readlines():
		s = genre.split("\n")[0]
		genre_list.append(s)

	genres_avg_dict = {}

	for genre in genre_list:
		print(genre)
		track_list = recommendedList(genre, 50)
		feature = dumpFeatures(track_list, 50)
		averaged_tag = averageTags(feature)
		genres_avg_dict[genre] = averaged_tag

	with open('averaged_genres.json', 'w') as outfile:
		json.dump(genres_avg_dict, outfile, indent=4)

	joes_tags = {"danceability":0.5035, "energy": 0.3688, "acousticness":0.61967, "instrumentalness": 0.015, "liveness": 0.189796, "valence": 0.36, "tempo":117.2}
	print(generateGenre(joes_tags))
	
	image = 'room.jpg'
	curr_img_tags = get_image_tags(image)
	spot_tags = tag_to_mood(curr_img_tags)
	genre = generateGenre(spot_tags)
	print(genre)
	track_list = recommendedList(genre, 5)
	print(track_list)

	joes_tags = {"danceability":0.5035, "energy": 0.3688, "acousticness":0.61967, "instrumentalness": 0.015, "liveness": 0.189796, "valence": 0.36, "tempo":117.2}
	x = generateGenre(joes_tags, 3)
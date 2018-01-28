import spotipy, jsonreader, json, sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from analyse_image import get_image_tags
import time

# Dummy ID for Spotify API bad return workaround
dummy_id = "0aWMVrwxPNYkKmFthzmpRi"

# Set up API credentials
client_credentials_manager = SpotifyClientCredentials(client_id=jsonreader.spotify_client_id, 
	client_secret=jsonreader.spotify_client_key)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load image - song pairing json
with open("song_examples.json", "r") as f:
	song_examples = json.load(f)

# Get audio analysis for each song
# Make list of song ids to request
"""id_list = []
for image_file in song_examples:
	for song_id in song_examples[image_file]:
		id_list.append(song_id)

print(sp.audio_features(id_list))"""

# Get audio analysis for each song
for image_file in song_examples:
	for song_id in song_examples[image_file]["song_ids"]:
		song_examples[image_file]["song_ids"][song_id] = sp.audio_features(song_id)[0]
		print(song_examples[image_file]["song_ids"][song_id])
		#time.sleep(0.5) # Wait to avoid Spotify API rate limiting
		"""if song_examples[image_file]["song_ids"][song_id] == None:
			# Dumb workaround
			print("Replace with dummy id that gives stupid weights but idk how to fix this")
			time.sleep(0.5)
			song_examples[image_file]["song_ids"][song_id] = sp.audio_features(dummy_id)[0]
			print(song_examples[image_file]["song_ids"][song_id])
			time.sleep(0.5)"""


# Get Microsoft CV API data for each image
for image_file in song_examples:
	song_examples[image_file]["image_data"] = get_image_tags("/home/joe/"+image_file)

# Get list of all unique tags
tags_nonunique = []
for image_file in song_examples:
	for tag in song_examples[image_file]["image_data"]["tags"]:
		tags_nonunique.append(tag)
unique_tags = list(set(tags_nonunique))

# Define initial dict of relevant audio analysis features
relevant_features = {
	"danceability": 0.0,
	"energy": 0.0,
	"loudness": 0.0,
	"acousticness": 0.0,
	"instrumentalness": 0.0,
	"liveness": 0.0,
	"valence": 0.0,
	"tempo": 0.0
	}

# Define initial dict of tags to weights
tag_weights = {tag:{
	"danceability": 0.0,
	"energy": 0.0,
	"loudness": 0.0,
	"acousticness": 0.0,
	"instrumentalness": 0.0,
	"liveness": 0.0,
	"valence": 0.0,
	"tempo": 0.0
	} for tag in unique_tags}

# Iterate through all unique CV tags and calculate running average for each Spotify 
# audio analysis feature
for tag in unique_tags:
	n = 0 # Running total of instances of the tag

	for image_file in song_examples:
		if tag in song_examples[image_file]["image_data"]["tags"]:
			print(tag + " in " + image_file)
			# Update running averages with data from sound analyses
			for song_id in song_examples[image_file]["song_ids"]:
				for song_feature, value in relevant_features.items():
					tag_weights[tag][song_feature] = (n*tag_weights[tag][song_feature] + 
						song_examples[image_file]["song_ids"][song_id][song_feature])/(n+1)
				n = n + 1

with open('tag_weights.json', 'w') as f:
	json.dump(tag_weights, f, sort_keys=True, indent=4)

print(tag_weights)

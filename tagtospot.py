import json

def tag_to_mood(curr_img_tags):
	file = open('tag_weights.json', 'r+')
	input_1 = json.load(file)
	input_2 = curr_img_tags
	m = len(list(input_2['tags']))
	output = {'danceability': 0, 'loudness': 0, 'liveness': 0, 'energy': 0, 'valence': 0, 'tempo': 0, 'instrumentalness': 0, 'acousticness': 0}
	for tag in input_2['tags']:
		if tag in input_1.keys():
			weights = input_1[tag]
			for mood in list(weights.keys()):
				output[mood] += weights[mood]/m

	return output
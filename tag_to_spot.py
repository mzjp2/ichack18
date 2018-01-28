import json, codecs, csv

def tag_to_spot(data):
	CON_1 = 1 # tags weight
	CON_2 = 1 # categories weight
	CON_3 = 1 # colors weight
	tot_1 = {'danceability': 0, 'loudness': 0, 'liveness': 0, 'energy': 0, 'valence': 0, 'tempo': 0, 'instrumentalness': 0, 'acousticness': 0}
	with open('tag_weights.csv', newline= '') as csvfile:
		reader = csv.DictReader(csvfile)
		new_reader = {}
		for row in reader:
			curr = row.pop('tag')
			new_reader[curr] = row
	input_1 = data['tags']
	for tag in input_1:
		try:
			for feature in new_reader[tag].keys():
				tot_1[feature] += float(new_reader[tag][feature])
		except:
			continue
	m = len(input_1)
	for tag in tot_1.keys():
		tot_1[tag] = CON_1*tot_1[tag]/m

	tot_2 = {'danceability': 0, 'loudness': 0, 'liveness': 0, 'energy': 0, 'valence': 0, 'tempo': 0, 'instrumentalness': 0, 'acousticness': 0}
	with open('category_weights.csv', newline= '') as csvfile:
		reader = csv.DictReader(csvfile)
		new_reader = {}
		for row in reader:
			curr = row.pop('category')
			new_reader[curr] = row
	input_1 = data['categories']
	for tag in input_1:
		try:
			for feature in new_reader[tag].keys():
				tot_2[feature] += float(new_reader[tag][feature])
		except:
			continue
	m = len(input_1)
	for tag in tot_2.keys():
		tot_2[tag] = CON_2*tot_2[tag]/m

	tot_3 = {'danceability': 0, 'loudness': 0, 'liveness': 0, 'energy': 0, 'valence': 0, 'tempo': 0, 'instrumentalness': 0, 'acousticness': 0}
	with open('color_weights.csv', newline= '') as csvfile:
		reader = csv.DictReader(csvfile)
		new_reader = {}
		for row in reader:
			curr = row.pop('color')
			new_reader[curr] = row
	input_1 = data['colors']
	for tag in input_1:
		try:
			for feature in new_reader[tag].keys():
				tot_3[feature] += float(new_reader[tag][feature])
		except:
			continue
	m = len(input_1)
	for tag in tot_3.keys():
		tot_3[tag] = CON_3*tot_3[tag]/m

	tot = {'danceability': 0, 'loudness': 0, 'liveness': 0, 'energy': 0, 'valence': 0, 'tempo': 0, 'instrumentalness': 0, 'acousticness': 0}
	for feature in tot.keys():
		tot[feature] = tot_1[feature] + tot_2[feature] + tot_3[feature]

	return tot
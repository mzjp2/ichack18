#!/bin/env python3
import http.client, urllib.request, urllib.parse, urllib.error, base64
import jsonreader
import requests

CONF_THRESHOLD = 0.2 # Confidence threshold for accepting a tag
SCORE_THRESHOLD = 0.0 # Score threshold for accepting a category

def get_image_tags(image_path):
	headers = {
	"Content-Type": "application/octet-stream",
	"Ocp-Apim-Subscription-Key": jsonreader.mscv_key,
	}

	params = {
		'visualFeatures': 'Categories, Tags, Color',
		'language': 'en',
	}

	image = open(image_path, 'rb').read()

	try:
		response = requests.post(url = 'https://westeurope.api.cognitive.microsoft.com/vision/v1.0/analyze',
			headers = headers,
			params = params,
			data = image)
		data = response.json()
		#print(data)
		#return data;
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))
		return ""

	# If the API does not detect any tags/categories/colours it does not create
	# the key, leading to an error when we try to read it.
	# We make sure the key exists otherwise we get an error when processing the data.
	for key in ['tags', 'categories', 'color']:
		if key not in data: data[key] = {'dominantColors':[]}

	# Make data nice and easily readable :)
	# Because I am a nice person :)
	
	nice_data = {'tags': [], 'categories': [], 'color': []}
	try: 
		nice_data['tags'] = [img_object['name'] for img_object in data['tags'] 
						  if img_object['confidence'] >= CONF_THRESHOLD]
	except TypeError as e:
		print("No tags given by API.")
		nice_data['tags'] = []

	try: 
		nice_data['categories'] = [img_category['name'] for img_category in 
			data['categories'] if img_category['score'] >= SCORE_THRESHOLD]
	except TypeError as e:
		print("No categories given by API.")
		nice_data['categories'] = []

	try:
		nice_data['color'] = data['color']['dominantColors']
	except TypeError as e:
		print("No colors given by API.")
		nice_data['color'] = []

	print(nice_data['tags'])
	return nice_data

if __name__ == "__main__":
	images = ['sea_test.jpg', 'beach.jpg', 'bedroom.jpeg', 'city_street.jpg',
	'gym.jpg', 'kids_party.jpg', 'library.jpg', 'office.jpg', 'park.jpg', 'party.jpg',
	'fancy_cafe.jpg', 'cafe.jpg', 'train_interior.jpg', 'queens_college.jpg', 'funeral.jpg',
	'bar.jpg', 'living_room.jpeg', 'kitchen.jpg', 'field.jpg', 'lake.jpg', 'museum.jpg',
	'gallery.jpg', 'forest.jpg', 'beach2.jpg', 'gathering.jpg', 'hackathon.jpg',
	'skatepark.jpeg']
	tags_nonunique = [get_image_tags('/home/joe/' + image_name)['tags']
					  for image_name in images]
	tags_flattened = []
	for sublist in tags_nonunique:
		for tag in sublist:
			tags_flattened.append(tag)
	tags = list(set(tags_flattened))
	print(tags)
	print(len(tags))





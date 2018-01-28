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

	# Make data nice and easily readable :)
	# Because I am a nice person :)
	nice_data = {"tags": [img_object['name'] for img_object in data['tags'] 
						  if img_object['confidence'] >= CONF_THRESHOLD],
				 "categories": [img_category['name'] for img_category in data['categories']
				 			    if img_category['score'] >= SCORE_THRESHOLD],
				 "colors": data['color']['dominantColors']}

	return nice_data

if __name__ == "__main__":
	print(get_image_tags("/home/joe/sea_test.jpg")["tags"])



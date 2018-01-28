import http.client, urllib.request, urllib.parse, urllib.error, base64
import jsonreader
import requests
import analyse_image
from tagtospot import tag_to_mood as t2m

print(t2m(analyse_image.get_image_tags('./test_stuff/testimg.jpg')))
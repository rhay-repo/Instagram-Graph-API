'''
Author: Reagan Hay
tools: requests, pprint, json, re, PIL, NASA API

'''

import requests
import json
import re
from pprint import pprint
from PIL import Image

## url
url = 'https://api.nasa.gov/planetary/apod?api_key='

## key
key = '9TgPZfReTnC88xmszgy6WvHnLTxa0arXFFOn6czP'

## retrieve all APOD data
r = requests.get(url + key)

## save json data
json_data = r.json()

## retrieve JUST the image

## parse through the headers for the url
for header in json_data:
	if header == 'url':
		# save the url of the image
		image_url = json_data[header]

## save the image
image = requests.get(image_url)

## get the name of the image via regular expression
regex_match = re.search('([^\/]*(.jpg))', image_url)
file_name = regex_match.group(0)

print(file_name)

## open the file and write the image to it
file = open(file_name, 'wb')
file.write(image.content)
file.close()

view_image = input('Would you like to view the image now? (y/n)\n')
if view_image == 'y':
	image = Image.open(file_name)
	image.show()

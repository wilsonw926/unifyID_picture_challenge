#Random Bitmap Image Coding Challenge for UnifyID
#Author: Wilson Wang (github.com/wilsonw926)

import requests
import numpy as np
from PIL import Image

#Constants
RANDOM_ORG_URL = "https://www.random.org/integers/"

IMG_ROW = 128
IMG_COL = 128
TOTAL_PIXELS = IMG_ROW * IMG_COL

#Grabs the random integers from the random.org url with the given params
def grab_random_ints(num):

	#Sample URL: https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new
	#Params for the random.org url
	params = {
		'num': str(num),
	    'min': '0',
	    'max': '255',
	    'col': '3',
	    'base': '10',
	    'format': 'plain',
	    'rnd': 'new'
	}

	r = requests.get(RANDOM_ORG_URL, params=params)
	#Makes sure response is 200
	if r.status_code != 200:
		print(str(r.status_code) + " Error")
		exit()
	else:
		parsed_data = [int(x) for x in r.text.split()]
		return parsed_data

#Compiles list of RGB Pixels, taking note of the 10000 random number limit
def list_pixels():
	returned_pixels = []
	#Total pixels x 3 (Red, Green, and Blue)
	RGB_PIXELS = TOTAL_PIXELS * 3
		
	#Note that the limit is 10000 random numbers
	while RGB_PIXELS > 0:
		if (RGB_PIXELS > 10000):
			returned_pixels.extend(grab_random_ints(10000))
			RGB_PIXELS -= 10000
		else:
			returned_pixels.extend(grab_random_ints(RGB_PIXELS))
			RGB_PIXELS -= 10000

	#print len(returned_pixels)
	return returned_pixels

def create_image(random_pixels):
	img = Image.new( 'RGB', (128,128)) # new image
	RGB_CONFIG = np.array(random_pixels).reshape((IMG_ROW * IMG_COL, 3))
	img.putdata([tuple(pixel) for pixel in RGB_CONFIG])
	img.save("results.bmp")
	print("fin")

def main():
	random_pixels = list_pixels()
	create_image(random_pixels)

#execute
main()
#Test file just to make sure generated pic is valid
from PIL import Image

def num_pixels_test(filepath):
    width, height = Image.open(open(filepath)).size
    print("Expected image size: " + str(128 * 128))
    print("Actual image size: " + str(width * height))
    if (128 * 128) == (width * height):
    	print("Success!")
    else:
    	comparison = ""
    	if (128 * 128) > (width * height):
    		comparison += "small"
    	if (128 * 128) < (width * height):
    		comparison += "large"
    	print("Image size is too " + comparison)
    

num_pixels_test("results.bmp")
	
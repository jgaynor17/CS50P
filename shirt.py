import sys
from PIL import Image, ImageOps
from os.path import splitext

if len(sys.argv) > 3: # Check for valid cmd #
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

_, ext1 = splitext(sys.argv[1]) # get input image extension by splitting text
_, ext2 = splitext(sys.argv[2]) # get input image extension by splitting text

if ext2 not in [".jpg", ".jpeg", ".png"]: #Verify input/output ext
    sys.exit("Invalid output")
if ext1 != ext2: #if exts do not match
    sys.exit("Input and output have different extensions")

try:
    input = Image.open(sys.argv[1]) # open input image
except FileNotFoundError:
    sys.exit("Input does not exist")

im = Image.open("shirt.png") #creates variable of the shirt png file
input = ImageOps.fit(input, im.size) #resize and fit the image

input.paste(im, im) #paste (image, coords, mask)
input.save(sys.argv[2]) #save to second CLA
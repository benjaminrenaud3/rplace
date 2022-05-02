from PIL import Image, ImageColor
from getinfo import getPixels
import webbrowser
import os


pixels = getPixels()


# creating a image object
if os.path.exists('../image/rplace.png'):
    os.remove('../image/rplace.png')
    im = Image.new('1', (2000,2000)) # create the Image of size 1 pixel
    im.save('../image/rplace.png')
image = Image.open("../image/rplace.png") 
width, height = image.size
image = image.convert('RGBA')

  
for pixel in pixels:
    # print(pixel.color)
    image.putpixel( (pixel.X, pixel.Y), ImageColor.getrgb(pixel.color) )

image.save('../image/rplace.png')
# webbrowser.open("../image/rplace.png")
image.show()




# im = Image.new('1', (2000,2000)) # create the Image of size 1 pixel

# im.save('../image/rplace.png')

# webbrowser.open("../image/rplace.png")


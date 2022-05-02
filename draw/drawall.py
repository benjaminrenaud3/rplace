from PIL import Image, ImageColor
from getinfo import getPixels
from pixel import pixel
import webbrowser
import os
import time, datetime


# end = "2022-04-01 23:26:51.728"


def drawall():

    if os.path.exists('../image/rplace.png'):
        os.remove('../image/rplace.png')
        im = Image.new('1', (2000,2000)) # create the Image of size 1 pixel
        im.save('../image/rplace.png')
    image = Image.open("../image/rplace.png") 
    width, height = image.size
    image = image.convert('RGBA')


    for filename in os.listdir("rplace"):
        with open(os.path.join("rplace", filename), 'r') as f:
            file = f.read().splitlines()
            for i, line in enumerate(file, 1):
                if i == 1:
                    continue
                line = line.replace('"', '')
                line = line.replace('UTC', '')
                x = line.split(',')

                if x[0] < "2022-04-04 22:00:00.000":
                    image.putpixel( (int(x[3]), int(x[4])), ImageColor.getrgb(x[2]) )

    image.save('../image/rplace.png')
    webbrowser.open("../image/rplace.png")
    return ""



tps1 = time.clock()
drawall()
tps2 = time.clock()
print(tps2 - tps1)


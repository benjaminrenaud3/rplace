import sys
import webbrowser
import os

from PIL import Image, ImageColor


def draw_all():
    """
    If picture exist, delete it.
    Check all files and draw each pixel before the date to avoid all end white pixel.
    Draw and save it.
    """

    if os.path.exists('image/rplace.png'):
        os.remove('image/rplace.png')
        im = Image.new('1', (2000,2000)) # create the Image of size 1 pixel
        im.save('image/rplace.png')
    image = Image.open("image/rplace.png") 
    image = image.convert('RGBA')

    for inc, filename in enumerate(os.listdir("rplace")):
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

    image.save('image/rplace.png')
    webbrowser.open("image/rplace.png")
    return ""

if __name__ == '__main__':
    draw_all()
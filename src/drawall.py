import sys
import os
import json
sys.path.append('../')

from customClass.createfile import create_file
from PIL import Image, ImageColor


def get_last_pixel():
    """
    Create a dict with all last pixel before date to avoid all end white pixel
    """

    last_pixels = {}

    for inc, filename in enumerate(os.listdir("rplace")):
        with open(os.path.join("rplace", filename), 'r') as f:
            file = f.read().splitlines()
            for i, line in enumerate(file, 1):
                if i == 1:
                    continue

                line = line.replace('"', '')
                line = line.replace('UTC', '')
                infos = line.split(',')

                if infos[0] > "2022-04-04 22:47:40.185": #last time before end white pixels wave
                    continue

                pixel_coord = infos[3]+","+infos[4]
                pixel_value = {"date": infos[0], "color": infos[2]}

                if pixel_coord in last_pixels:
                    if infos[0] > last_pixels[pixel_coord]["date"]:
                        last_pixels[pixel_coord] = pixel_value
                else:
                        last_pixels[pixel_coord] = pixel_value

    create_file("src/users/last.json", last_pixels)

def draw_all():
    """
    If picture exist, reset it
    Draw final rplace
    """

    if os.path.exists('image/rplace.png'):
        os.remove('image/rplace.png')
        im = Image.new('1', (2000,2000))
        im.save('image/rplace.png')
    image = Image.open("image/rplace.png") 
    image = image.convert('RGBA')

    last_pixels = json.load(open("last.json"))

    for pixel in last_pixels:
        coord = pixel.split(',')
        image.putpixel( (int(coord[0]), int(coord[1])), ImageColor.getrgb(last_pixels[pixel]["color"]) )

    image.save('image/rplace.png')
    image.show()

if __name__ == '__main__':
    get_last_pixel()
    draw_all()
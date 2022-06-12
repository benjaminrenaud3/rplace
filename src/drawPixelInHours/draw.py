import os

from PIL import Image, ImageColor
from getinfo import get_pixel


def draw_and_save():
    """
    Get a list of pixel.
    If picture exist, delete it.
    Creating a full black picture object and, foreach pixel, draw it in picture.
    Save and show it.
    """

    pixels = get_pixel()

    if os.path.exists('rplace.png'):
        os.remove('rplace.png')
        im = Image.new('1', (2000,2000))
        im.save('rplace.png')
    image = Image.open("rplace.png") 
    image = image.convert('RGBA')

    for pixel in pixels:
        image.putpixel((pixel.X, pixel.Y), ImageColor.getrgb(pixel.color))

    image.save('rplace.png')
    image.show()


if __name__ == '__main__':
    draw_and_save()
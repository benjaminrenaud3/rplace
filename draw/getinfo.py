from pixel import pixel
import time, datetime
import os


def getPixels():
    f = open("final", "r")
    file = f.read().splitlines()

    pixels = []

    for i, line in enumerate(file, 1):
        if i == 1:
            continue
        pixel1 = pixel()
        line = line.replace('"', '')
        line = line.replace('UTC', '')
        x = line.split(',')

        pixel1.time, pixel1.user, pixel1.color = x[0], x[1], x[2]
        pixel1.X = int(x[3])
        pixel1.Y = int(x[4])
        pixels.append(pixel1)
    return pixels

#check
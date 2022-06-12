import os
import json
import sys
sys.path.append('../')

from customClass.createfile import create_file


def get_number_of_colors():
    """
    Check all file.
    Create and set a dictionnary for each color.
    Increment value each time color is set.
    """

    colors = {}

    for inc, filename in enumerate(os.listdir("../rplace")):
        with open(os.path.join("../rplace", filename), 'r') as f:
            file = f.read().splitlines()
            for i, line in enumerate(file, 1):
                if i == 1:
                    continue
                split = line.split(',')

                if split[0] > "2022-04-04 22:47:40.185":
                    continue
                if split[2] in colors:
                    colors[split[2]] += 1
                else:
                    colors[split[2]] = 1
    create_file("src/colors/colors.json", colors)

    return()

if __name__ == '__main__':
    get_number_of_colors()
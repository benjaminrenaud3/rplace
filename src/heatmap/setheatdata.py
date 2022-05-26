import os
import json
from collections import OrderedDict


def set_unique_map():
    """
    Check all file.
    Create and set a dictionnary for each pixel with its coordinate.
    Increment value each time it modified.
    """

    unique = {}

    for filename in os.listdir("../rplace"):
        with open(os.path.join("../rplace", filename), 'r') as f:
            file = f.read().splitlines()
            for i, line in enumerate(file, 1):
                if i == 1:
                    continue
                line = line.replace('"', '')
                split = line.split(',')

                if split[4]+','+split[3] in unique:
                    unique[split[4]+','+split[3]] += 1
                else:
                    unique[split[4]+','+split[3]] = 1

    return(unique)

def set_heat_map():
    """
    Get a list with each pixel and how much was modified.
    Sort this to have all first pixel order to correspond x axis.
    Create a 2D-array.
    Fill and write file.
    """

    dic = set_unique_map()
    dic = OrderedDict(sorted(dic.items(), key=lambda t: t[0]))
    row, col = 2000, 2000
    heatmap = [[0]*row for _ in range(col)]

    for item in dic.keys():
        split = item.split(',')
        heatmap[int(split[0])][int(split[1])] = dic[item]

    if os.path.exists('heatmap.json'):
        os.remove('heatmap.json')

    with open('heatmap.json', 'w') as fp:
        json.dump(heatmap, fp)

    return ""


if __name__ == '__main__':
    set_heat_map()
import os
import json
from collections import OrderedDict

    
    
def setUniqueMap():
    unique = {}
    for n, filename in enumerate(os.listdir("../rplace")):
        print(n)
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

def setHeatMap():
    dic = setUniqueMap()
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

setHeatMap()
# def setHeatMap():
#     dic = setUniqueMap()
#     dic = OrderedDict(sorted(dic.items(), key=lambda t: t[0]))
#     print(len(dic))
#     return [[1]]


# def setHeatMap():
#     my_rows, my_cols = 2000, 2000
#     heatmap = [[0]*my_cols]*my_rows
#     f = open("../rplace/header.txt", "r")
#     file = f.read().splitlines()
#     for i, line in enumerate(file, 1):
#         if i == 1:
#             continue
#         line = line.replace('"', '')
#         line = line.replace('UTC', '')
#         split = line.split(',')
#         print(int(split[3]), int(split[4]))
#         # heatmap[int(split[3])][int(split[4])] += 1

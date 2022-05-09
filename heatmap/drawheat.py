import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import pandas as pd
import json

data = json.load(open("heatmap.json"))

# for x, ligne in enumerate(data):
#     for y, case in enumerate(ligne):
#         if case > 1000:
#             data[x][y] = 1000

heat_map = sb.heatmap(data, robust=True, cmap="Spectral")

plt.show()
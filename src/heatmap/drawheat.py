import matplotlib
import matplotlib.pyplot as plt
import seaborn as sb
import json


def draw_heat():
    """
    Draw heatmap with heatmap file
    """
    data = json.load(open("heatmap.json"))
    heat_map = sb.heatmap(data, robust=True, cmap="Spectral")
    plt.show()

if __name__ == '__main__':
    draw_heat()
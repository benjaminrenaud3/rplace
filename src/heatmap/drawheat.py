import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import seaborn as sb
import json


def draw_heat():
    """
    Draw heatmap with heatmap file
    """

    data = json.load(open("heatmap.json"))
    heat_map = sb.heatmap(data, robust=True, norm=LogNorm())
    plt.show()

if __name__ == '__main__':
    draw_heat()
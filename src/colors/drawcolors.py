import matplotlib.pyplot as plt
import json

from collections import OrderedDict


def draw_color():
    """
    Draw color pie with colormap file
    """

    colors = json.load(open("colors.json"))
    colors = OrderedDict(sorted(colors.items(), key=lambda t: t[1], reverse=True))
    colors = dict(list(colors.items())[:15])

    labels = colors.keys()
    items = colors.values()

    plt.figure(figsize = (15,15))
    plt.pie(items, labels = labels, colors=labels, autopct = lambda x: str(round(x, 2)) + '%')
    plt.show()

if __name__ == '__main__':
    draw_color()
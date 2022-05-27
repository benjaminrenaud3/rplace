import json
import os
import matplotlib.pyplot as plt
import numpy as np


def user_bar_graph():
    """
    Draw a bar graph with the userstat file
    """

    user_stat = json.load(open("userstat.json"))

    data = []
    values = []
    for y in range(len(user_stat[0])):
        for u, i in enumerate(user_stat):
            values.append(i[y])
        data.append(values)
        values = []

    dim = len(data[0])
    w = 0.80
    dimw = w / dim

    fig, ax = plt.subplots()
    x = np.arange(len(data))
    labels = ["files 0-20", "files 21-40", "files 41-60", "files 61-80"]
    for i in range(len(data[0])):
        y = [d[i] for d in data]
        b = ax.bar(x + i * dimw, y, dimw, label=labels[i])

    ax.set_xticks(x + dimw*1.5, labels=("1-4", "5-8", "9-12", "13-16", "> 16"))

    ax.set_xlabel('number of pixel was changed')
    ax.set_ylabel('number of users')
    ax.set_title('how many users change how many pixels')
    ax.legend()

    plt.show()

if __name__ == '__main__':
    user_bar_graph()
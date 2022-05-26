from pstats import Stats
import matplotlib.pyplot as plt
import numpy as np
import json
import time
import os

from collections import OrderedDict
from statistics import mean, median, quantiles


def group_person():
    """
    Create a file with the sum of user sort by how many he change pixels
    In all_users
    """

    start_time = time.time()

    all_users = json.load(open("person.json"))

    user_stat = [[], [], [], []]

    for i, user in enumerate(all_users):
        user_stat[i].append(sum(0 < i < 3 for i in user.values()))
        user_stat[i].append(sum(3 <= i <= 6  for i in user.values()))
        user_stat[i].append(sum(7 <= i <= 10 for i in user.values()))
        user_stat[i].append(sum(11 <= i <= 15 for i in user.values()))
        user_stat[i].append(sum(15 < i for i in user.values()))

    if os.path.exists('userstat.json'):
        os.remove('userstat.json')
    with open('userstat.json', 'w') as fp:
        json.dump(userstat, fp)

    print("--- %s seconds ---" % (time.time() - start_time))

def user_bar_graph():
    """
    Draw a bar graph with the userstat file
    """
    start_time = time.time()

    user_stat = json.load(open("userstat.json"))
    X = np.arange(5)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(X + 0.00, user_stat[0], color = '#FF0000', width = 0.20)
    ax.bar(X + 0.20, user_stat[1], color = '#0800FF', width = 0.20)
    ax.bar(X + 0.40, user_stat[2], color = '#00CA19', width = 0.20)
    ax.bar(X + 0.60, user_stat[3], color = '#DFDB00', width = 0.20)

    # data = [[30, 25, 50, 20, 17],
    # [40, 23, 51, 17, 14],
    # [35, 22, 45, 19, 18],
    # [35, 22, 45, 19, 23]]
    # X = np.arange(5)
    # fig = plt.figure()
    # ax = fig.add_axes([0,0,1,1])
    # ax.bar(X + 0.00, data[0], color = 'b', width = 0.20)
    # ax.bar(X + 0.20, data[1], color = 'g', width = 0.20)
    # ax.bar(X + 0.40, data[2], color = 'r', width = 0.20)
    # ax.bar(X + 0.60, data[3], color = 'b', width = 0.20)
    plt.show()

    print("--- %s seconds ---" % (time.time() - start_time))

def write_pixels(min: int, max: int, users: dict, stat_file):
    """
    Get number of pixel between 2 numbers and write in file
    """
    pixels = sum(min <= i <= max for i in users.values())
    stat_file.write(f"{min} to {max} pixels changed: {'{:,}'.format(pixels).replace(',', ' ')}\n")
    return (pixels)

def user_basic_stat():
    """
    Stat with user dictionnary
    """
    start_time = time.time()
    all_users = json.load(open("person.json"))

    if os.path.exists('stats.txt'):
        os.remove('stats.txt')
    stat_file = open('stats.txt', 'w')

    stats = [0, 0, 0, 0, 0, 0]

    for i, users in enumerate(all_users):
        stat_file.write(f"for files {i*20} to {(i+1)*20}: \n")
        stat_file.write(f"total user: {'{:,}'.format(len(users)).replace(',', ' ')}\n")

        mean_value = mean(users.values())
        stats[0] += mean_value
        stat_file.write(f"moyenne: {round(mean_value, 2)}\n")
        stat_file.write(f"mediane: {median(users.values())}\n")
        stat_file.write(f"quantiles: {quantiles(users.values())}\n\n")


        stats[1] += write_pixels(1, 4, users, stat_file)
        stats[2] += write_pixels(5, 8, users, stat_file)
        stats[3] += write_pixels(9, 12, users, stat_file)
        stats[4] += write_pixels(13, 16, users, stat_file)
        stats[5] += write_pixels(17, 10000, users, stat_file)
        
        stat_file.write('\n\n\n')
    
    stat_file.write(f"total mean: {'{:,}'.format(round(stats[0]/4, 2)).replace(',', ' ')}\n")
    stat_file.write(f"total 1 to 4: {'{:,}'.format(stats[1]).replace(',', ' ')}\n")
    stat_file.write(f"total 5 to 8: {'{:,}'.format(stats[2]).replace(',', ' ')}\n")
    stat_file.write(f"total 9 to 12: {'{:,}'.format(stats[3]).replace(',', ' ')}\n")
    stat_file.write(f"total 13 to 15: {'{:,}'.format(stats[4]).replace(',', ' ')}\n")
    stat_file.write(f"total over 15: {'{:,}'.format(stats[5]).replace(',', ' ')}\n")

    print("--- %s seconds ---" % round(time.time() - start_time))


if __name__ == '__main__':
    # group_person()
    user_basic_stat()
    # user_bar_graph()
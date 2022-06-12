from pstats import Stats
import json
import time
import os
import sys
sys.path.append('../')

from customClass.createfile import create_file
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
        user_stat[i].append(sum(1 <= i <= 4 for i in user.values()))
        user_stat[i].append(sum(5 <= i <= 8  for i in user.values()))
        user_stat[i].append(sum(9 <= i <= 12 for i in user.values()))
        user_stat[i].append(sum(13 <= i <= 16 for i in user.values()))
        user_stat[i].append(sum(16 < i for i in user.values()))

    create_file("src/users/userstat.json", user_stat)

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

import os
import json
import math


def get_each_person():
    """
    Check all file.
    Create and set an array of 4 dictionnary for each user.
    Its necessary because compare id in one dictionnary its too long
    Increment value each user change pixel.
    """

    person = [{}, {}, {}, {}]

    for inc, filename in enumerate(os.listdir("../rplace")):
        print(inc)
        with open(os.path.join("../rplace", filename), 'r') as f:
            file = f.read().splitlines()
            for i, line in enumerate(file, 1):
                if i == 1:
                    continue
                split = line.split(',')

                if split[1] in person[math.floor((inc)/20)]:
                    person[math.floor((inc)/20)][split[1]] += 1
                else:
                    person[math.floor((inc)/20)][split[1]] = 1
    # print(len(person[0]), len(person[1]), len(person[2]), len(person[3]))
    if os.path.exists('person.json'):
        os.remove('person.json')
    with open('person.json', 'w') as fp:
        json.dump(person, fp)

    return()

if __name__ == '__main__':
    get_each_person()
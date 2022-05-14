import os


def set_selection():
    """
    Check all files and copy each between 2 hours in array. 
    """

    pixels = []
    for filename in os.listdir("../rplace"):
        with open(os.path.join("../rplace", filename), 'r') as f:
            file = f.read().splitlines()
            for i, line in enumerate(file, 1):
                if i == 1:
                    continue
                line = line.replace('"', '')
                line = line.replace('UTC', '')
                x = line.split(',')

                if "2022-04-04 12:00:00.000" < x[0] < "2022-04-04 12:10:00.000":
                    pixels.append(line)
    return pixels

def write_selection():
    """
    Get an array of selected pixel and write them on file. 
    """

    if os.path.exists('selectedPixels.txt'):
        os.remove('selectedPixels.txt')
    file = open("selectedPixels.txt", "a")
    pixels = set_selection()

    print(len(pixels))
    for pixel in pixels:
        file.write(pixel + "\n")
    file.close()

if __name__ == '__main__':
    write_selection()
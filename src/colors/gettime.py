import os


def get_last_time_with_color():
    """
    Check all file.
    get last hours with colored pixel
    """

    end_date_with_color = "2022-04-03 08:00:00.000"

    for inc, filename in enumerate(os.listdir("../rplace")):
        with open(os.path.join("../rplace", filename), 'r') as f:
            file = f.read().splitlines()
            for i, line in enumerate(file, 1):
                if i == 1:
                    continue
                split = line.split(',')

                if split[0] > end_date_with_color and split[2] != "#FFFFFF":
                    end_date_with_color = split[0]
    return(end_date_with_color)


if __name__ == '__main__':
    print(get_last_time_with_color())


import os
import json

def create_file(path: str, data):
    """
    Reset File in path with data
    Args:
        path (String) : the path to create file
        data : data to write in file in json format
    """

    if os.path.exists(path):
        os.remove(path)
    with open(path, 'w') as fp:
        json.dump(data, fp)


if __name__ == '__main__':
    create_file()
import os
import argparse
from typing import Text
from alive_progress import alive_it

def init_parser():
    parser = argparse.ArgumentParser(description="This application takes in a path and outputs the sub direcotry with the longest name")
    parser.add_argument('-s', '--starting-point', type=Text, help="A valid path as the starting point", required=True)
    return parser.parse_args()

def get_all_directories(starting_point):
    directories = []
    for root, dirs, files in alive_it(os.walk(starting_point), title="Gathering sub directories", unknown="dots_waves"):
        for dir in dirs:
            directories.append({"root": root, "name": dir})
    return directories

def get_longest_dir(directories):
    longest_dir = {"root": "", "name": ""}
    
    for directory in directories:
        if len(directory["name"]) > len(longest_dir["name"]):
            longest_dir = directory
    return longest_dir

if __name__ == "__main__":
    args = init_parser()
    starting_point = args.starting_point

    if not os.path.exists(starting_point):
        raise Exception("Provided starting point is not a directory")
    
    directories = get_all_directories(starting_point)
    longest_dir = get_longest_dir(directories)

    if(longest_dir["name"] == ""):
        print(f'No sub dirs found :(')
    else:
        print(f'Found { longest_dir["name"] }')
        print(f'In directory { longest_dir["root"] }')
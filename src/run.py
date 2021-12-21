import os
import argparse
from typing import Text

def init_parser():
    parser = argparse.ArgumentParser(description="This application takes in a path and outputs the sub direcotry with the longest name")
    parser.add_argument('-s', '--starting-point', type=Text, help="A valid path as the starting point", required=True)
    return parser.parse_args()    

if __name__ == "__main__":
    args = init_parser()
    directory = args.starting_point

    if not os.path.exists(directory):
        raise Exception("Provided starting point is not a directory")

    print("Recursively checking: " + directory)

    directories = []

    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            directories.append({"root": root, "name": dir})
    
    longest_dir_name = {"root": "", "name": ""}

    for directory in directories:
        if len(directory["name"]) > len(longest_dir_name["name"]):
            longest_dir_name = directory

    name = 'World'
    program = 'Python'
    
    print(f'Found { longest_dir_name["name"] } in directory { longest_dir_name["root"] } to be the longest available directory name')
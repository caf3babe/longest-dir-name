#!/usr/bin/env bash

echo "Enter the desired starting starting point"
read STARTING_POINT

if [[ ! -d "$STARTING_POINT" ]];then
    echo "Input was not valid, please start over and enter a valid directory"
    exit 1
fi

echo "Starting docker container"
docker run \
--rm --tty --read-only --mount type=bind,src=$STARTING_POINT,dst=$STARTING_POINT \
longest-dir-name python3 /src/run.py --starting-point=$STARTING_POINT
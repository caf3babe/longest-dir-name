> This application traverse a given directory and outputs the longest directory name

How to use:
```bash
# build the image
docker build -t dedalus-longest-dir-name .

# start container from that image
docker run dedalus-longest-dir-name python3 /src/run.py --starting-point=/
```

FROM python:3.10.1-slim-buster
COPY src /src
RUN pip3 install -r /src/requirements.txt
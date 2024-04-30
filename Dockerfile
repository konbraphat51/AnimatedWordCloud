FROM nvidia/cuda:11.8.0-base-ubuntu20.04

# install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# set working directory
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

# install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

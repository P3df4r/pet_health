#!/bin/bash

apt install docker.io
docker pull mongo:latest
docker run -d -p 27017:27017 -v ~/data/db --name pet_health_mongodb mongo:latest


#!/bin/bash

docker build -t ph_image .
docker run -p 8888:5000 -p 27017:27017 -v ~/data/db --name pet_health_mongodb ph_image
#docker run -d -p 27017:27017 -v ~/data/db --name pet_health_mongodb mongo:latest


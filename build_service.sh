#!/bin/bash

# Run the Python script to generate the docker-compose.yml file
python3 generate_compose.py

# Then, build and start the Docker Compose environment
docker-compose --env-file ./keys.env up -d --build

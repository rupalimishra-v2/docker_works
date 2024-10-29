# Docker Works

## Overview
This project demonstrates a customizable plugin architecture for Docker services using FastAPI.

## Project Structure
1. **Add Services**: Create new service folders under the `plugins` directory, including a `Dockerfile`, `app.py`, and `requirements.txt` etc.
2. **Generate the Docker Compose File**: The script is present called generate_compose.py to generate `docker-compose.yml`.

## How to use
1. Run the command: ./build_service.sh to spin the containers.

## Customizing the Environment Variables
Make sure to include a `.env` or `keys.env` file at the root of your project if your services depend on specific environment variables. An example `keys.env` could look like this:
SERVICE_API_KEY=your_api_key_here
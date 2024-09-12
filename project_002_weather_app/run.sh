#/bin/bash
docker build -t django-weather-app .  && \
    docker run -p 8000:8000 django-weather-app

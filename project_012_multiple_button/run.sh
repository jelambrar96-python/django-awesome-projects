#/bin/bash
docker build -t django-multiple-button-app .  && \
    docker run -p 8000:8000 django-multiple-button-app

#/bin/bash
docker build -t django-url-shorter-app .  && \
    docker run -p 8000:8000 django-url-shorter-app

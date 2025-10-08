#/bin/bash
docker build -t django-wikipedia-app .  && \
    docker run -p 8000:8000 django-wikipedia-app

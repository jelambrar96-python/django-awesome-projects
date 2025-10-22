#/bin/bash
docker build -t django-netest-serializer-app .  && \
    docker run -p 8000:8000 django-netest-serializer-app

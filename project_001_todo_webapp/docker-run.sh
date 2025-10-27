#/bin/bash
docker build -t django-todo-app .  && \
    docker run -p 8000:8000 django-todo-app

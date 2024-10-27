#/bin/bash
docker build -t blogging-platform .  && \
    docker run -p 8000:8000 blogging-platform

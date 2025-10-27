#/bin/bash
docker build -t dap001-todo-app .  && \
    docker run -p 8000:8000 dap001-todo-app

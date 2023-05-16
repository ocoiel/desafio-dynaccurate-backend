ARG APP_NAME=dynaccurate
ARG APP_PATH=/opt/$APP_NAME
ARG PYTHON_VERSION=3.11.0
ARG POETRY_VERSION=1.4.2

# Stage: staging
FROM nikolaik/python-nodejs:latest as staging
ARG APP_NAME
ARG APP_PATH
ARG POETRY_VERSION

# Update/upgrade libraries and install helper tools
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y wget curl && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

# PYTHONDONTWRITEBYTECODE=1: Prevents python from writing .pyc (compiled byte) codes to disk
# PYTHONUNBUFFERED=1: Forces python outputs to be sent straight to terminal -- without buffering
ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1
ENV \
    POETRY_VERSION=$POETRY_VERSION \
    POETRY_HOME="/opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
ENV \
    DOCKERIZE_VERSION="v0.6.1"

# Install dockerize to ensure availability of container dependencies
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz


# Install poetry (OLD)
# RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - \
#     && cd /usr/local/bin \
#     && ln -s /opt/poetry/bin/poetry

# Install poetry (NEW from chatgpt)
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -
RUN cd /usr/local/bin && rm -f poetry && ln -s /opt/poetry/bin/poetry poetry


# Stage: development
FROM staging as development
ARG APP_NAME
ARG APP_PATH
WORKDIR $APP_PATH
COPY ./ ./
RUN poetry install --no-root
RUN poetry export \
    --without dev \
    --without hashes \
    -f requirements.txt \
    --output requirements.txt
ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "src.infrastructure.http.server:app", "--host=0.0.0.0", "--port=3333"]

# Stage: production
FROM python:${PYTHON_VERSION}-slim-bullseye as production
ARG APP_NAME
ARG APP_PATH

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

ENV \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

ENV PORT=3333

# Install only production dependencies and run ASGI web server
WORKDIR $APP_PATH
COPY --from=development ${APP_PATH}/src ./src
COPY --from=development ${APP_PATH}/.env ./
COPY --from=development ${APP_PATH}/requirements.txt ./
# COPY --from=development ${APP_PATH}/src/infrastructure/database/prisma/schema.prisma ./primsa
COPY ./.docker/entrypoint.sh ./
RUN chmod +x ./entrypoint.sh
COPY ./.docker/wait-for-it.sh ./
RUN chmod +x ./entrypoint.sh ./wait-for-it.sh

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

RUN pip install -r requirements.txt
RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate

# Install Node.js and npm (i dont need more to install since the image already come with node)
# RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
# RUN apt-get install -y nodejs

# ENTRYPOINT ["dockerize", "-wait", "tcp://db:5432", "-timeout", "30s"]
ENTRYPOINT ["./entrypoint.sh"]

RUN npm install -g prisma
# RUN prisma generate --schema src/infrastructure/database/prisma/schema.prisma
RUN npx prisma db push --schema src/infrastructure/database/prisma/schema.prisma

COPY --from=staging /usr/local/bin/dockerize /usr/local/bin

CMD ["python", "-m", "uvicorn", "src.infrastructure.http.server:app", "--host=0.0.0.0", "--port=3333"]

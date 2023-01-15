FROM python:3.10-slim as builder
ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=false

WORKDIR /src
COPY pyproject.toml /src/

RUN python -m pip install poetry && \
    python -m poetry config virtualenvs.create false && \
    python -m poetry export --without-hashes --output requirements.txt
# RUN apt-get update && apt-get -y install
# apt-get clean  &&\
# rm -rf /var/lib/apt/lists/*

CMD ["bash"]

FROM python:3.10-slim as pycontainer
ENV PYTHONUNBUFFERED=1

ARG UID=123
ARG GID=123

WORKDIR /src
COPY --from=builder /src/requirements.txt /src
COPY pyproject.toml README.md /src/

RUN groupadd -g $GID user  &&  \
    useradd -m -u $UID -g $GID user && \
    pip install -r requirements.txt

USER user
CMD ["bash"]
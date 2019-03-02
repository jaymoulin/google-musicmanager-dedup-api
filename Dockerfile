FROM python:alpine3.6 as builder

COPY qemu-*-static /usr/bin/

FROM builder

ARG VERSION=1.0.0

LABEL maintainer="Jay MOULIN <jaymoulin@gmail.com> <https://twitter.com/MoulinJay>"
LABEL version=${VERSION}

WORKDIR /app
COPY . /app/
RUN pip3 install --upgrade pip && \
    pip3 install -e .

VOLUME /root/db

ENV PORT=80\
    DB_PATH=/app/db/googlemusicmanager.db
CMD ["python", "-u", "-m", "api"]

FROM python:alpine

ARG VERSION=1.0.0
ARG TARGETPLATFORM

LABEL maintainer="Jay MOULIN <https://jaymoulin.me>"
LABEL version="${VERSION}-${TARGETPLATFORM}"

WORKDIR /app
COPY . /app/
RUN pip3 install -e .

VOLUME /root/db

ENV PORT=80\
    DB_PATH=/app/db/googlemusicmanager.db
CMD ["python", "-u", "-m", "api"]

FROM alpine:3.10.1
LABEL version="0.1a"
LABEL maintainer="Paal Pedersen"
RUN apk update \
    && apk add --virtual build-dependencies \
        build-base \
        gcc \
        wget \
        git \
    # && apk add \
        bash \
	# && apk add --no-cache --virtual .build-deps \
        autoconf \
        automake \
        g++ \
		c \
		c++ \
        json-c-dev \
        libtool \
        libxml2-dev \
        make \
        perl \
    # && apk add --no-cache --virtual .build-deps-edge \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \    
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        gdal-dev \
        geos-dev \
        proj4-dev \
        protobuf-c-dev \
RUN git clone https://github.com/postgis/postgis.git

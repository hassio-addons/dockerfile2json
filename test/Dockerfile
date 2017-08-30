FROM alpine:3.6

# Internal arguments
ARG MAINTAINER="Franck Nijhof <frenck@geekchimp.com>"

# Environment variables
ENV \
    HOME="/root" \
    LANG="C.UTF-8" \
    PS1="$(whoami)@$(hostname):$(pwd)$ " \
    TERM="xterm"

# Entrypoint & CMD
ENTRYPOINT [ "/init" ]

# Install base system
RUN \
# Install build dependencies
    apk add --no-cache --virtual .build-dependencies \
        curl \
        tar \
    \
    && apk add --no-cache \
        ca-certificates \
        eudev \
        jq \
        tzdata \
    \
    && apk del --purge .build-dependencies \
    \
    && mkdir -p \
        /etc/cont-finish.d \
        /etc/cont-init.d \
        /etc/fix-attrs.d \
        /etc/services.d

# Copy root filesystem
COPY rootfs /

# Labels
LABEL \
    maintainer=${MAINTAINER} \
    org.label-schame.description="Docker Test Description" \
    org.label-schema.name="Docker Test" \
    org.label-schema.schema-version="1.0"
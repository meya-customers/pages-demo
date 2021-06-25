#!/bin/sh
set -e
echo "Installing custom requirements"
apk add --no-cache --virtual .build-deps \
  gcc \
  python3-dev \
&& pip install --disable-pip-version-check --no-cache-dir -r requirements.txt
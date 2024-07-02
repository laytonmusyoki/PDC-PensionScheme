#!/usr/bin/env bash

# Update package list and install dependencies
apt-get update
apt-get install -y \
  libpango-1.0-0 \
  libpango1.0-dev \
  libcairo2 \
  libcairo2-dev \
  libgdk-pixbuf2.0-0 \
  libgdk-pixbuf2.0-dev \
  libffi-dev \
  libxml2-dev \
  libxslt1-dev \
  libjpeg-dev \
  zlib1g-dev \
  libpangoft2-1.0-0 \
  libpangocairo-1.0-0

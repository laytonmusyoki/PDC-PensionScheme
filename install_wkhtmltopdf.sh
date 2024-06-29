#!/bin/bash
set -e

# Install dependencies
apt-get update
apt-get install -y software-properties-common wget

# Download and install wkhtmltopdf
wget -q -O /tmp/wkhtmltopdf.deb https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
apt-get install -y /tmp/wkhtmltopdf.deb

# Verify the installation
if ! command -v wkhtmltopdf &> /dev/null; then
    echo "wkhtmltopdf could not be found"
    exit 1
else
    echo "wkhtmltopdf installed successfully"
    wkhtmltopdf --version
fi

# Clean up
rm -rf /var/lib/apt/lists/* /tmp/*

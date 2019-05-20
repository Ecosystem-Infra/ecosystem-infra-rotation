#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

# Install webapp dependencies.
cd webapp
rm -rf bower_components
# This will call `bower install`. `--unsafe-perm` is needed for GitHub Actions where
# this script will be run as root.
npm install --unsafe-perm

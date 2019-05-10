#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

# Install webapp dependencies.
cd webapp
rm -rf bower_components
bower install

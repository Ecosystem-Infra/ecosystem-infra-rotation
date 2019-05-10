#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

dev_appserver.py app.yaml

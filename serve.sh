#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

set +u
source env/bin/activate
set -u

python main.py

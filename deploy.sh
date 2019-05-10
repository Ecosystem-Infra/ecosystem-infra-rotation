#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

MONORAIL_KEY="monorail-key.json"
if [[ ! -f "$MONORAIL_KEY" ]]; then
    echo "$MONORAIL_KEY needed to deploy"
    exit 1
fi

VERSION="$(git describe --always --dirty --long)"
gcloud app deploy --project=ecosystem-infra-rotation --version="$VERSION"

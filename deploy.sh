#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

VERSION="$(git describe --always --dirty --long)"
gcloud app deploy --project=ecosystem-infra-rotation --version="$VERSION"

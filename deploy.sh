#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

VERSION="$(git describe --always --dirty --long)"
gcloud app deploy --no-promote --project=ecosystem-infra-rotation --version="$VERSION"

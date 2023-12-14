#!/bin/bash

set -e

cd $(dirname $0)

mkdir -p ./build/auto_build
PYDEVD_DISABLE_FILE_VALIDATION=1 sphinx-autobuild ./source ./build/auto_build --host 0 --port 3821

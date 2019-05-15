#!/usr/bin/env bash

set -o errexit
set -o nounset

if (( "$#" != 1 )); then
  echo "Usage: ./error_handling <greetee>" >&2
  exit 1
fi

echo "Hello, ${1}"

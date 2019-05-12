#!/usr/bin/env bash

year=$1

if [[ "$#" != 1 ]] || ! [[ $year =~ ^[0-9]{4}$ ]]; then
  { echo "Usage: $0 <year>" >&2; exit 1; }
fi

if [[ $((year % 4)) == 0 ]] \
  && [[ $((year % 100)) != 0 ]] \
  || [[ $((year % 400)) == 0 ]]; then
  echo "true"
else
  echo "false"
fi

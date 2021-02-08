#!/usr/bin/env bash

number=$1

if (( number % 3 == 0 )); then
  result+="Pling"
fi

if (( number % 5 == 0 )); then
  result+="Plang"
fi

if (( number % 7 == 0 )); then
  result+="Plong"
fi

echo ${result:-$number}

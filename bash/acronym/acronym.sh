#!/usr/bin/env bash
#
# Converts a long name like Portable Network Graphics to its acronym (PNG).

# Set input as variable
input=$1

# Set space as delimiter
IFS=' '

# Read the split words into an array based on space delimiter
read -ra acronym <<< "$input"

# Print the acronym
for word in "${acronym[@]}"; do
  echo -n "${word:0:1}"
done

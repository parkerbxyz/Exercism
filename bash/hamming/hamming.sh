#!/usr/bin/env bash
#
# Calculate the Hamming Distance between two DNA strands

strand_1=$1
strand_2=$2

# Exit if the number of input parameters is not 2
[[ "$#" != 2 ]] && {
  echo "Usage: hamming.sh <string1> <string2>"
  exit 1
}

# Exit if the strands are not of equal length
[[ "${#strand_1}" != "${#strand_2}" ]] && {
  echo "left and right strands must be of equal length"
  exit 1
}

hamming_distance=0
strand_length="${#strand_1}"
for ((i = 0; i < strand_length; i++)); do
  # Compare the two strands of DNA and count the differences between them
  [[ "${strand_1:$i:1}" != "${strand_2:$i:1}" ]] && ((hamming_distance++))
done

echo "$hamming_distance"

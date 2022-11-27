#!/usr/bin/env bash

# Global variables
declare -ra COLORS=(
    black brown red orange yellow
    green blue violet grey white
)
declare -ra PREFIXES=('' kilo mega giga)

# Validate input
for color in "$@"; do
    if ! [[ "${COLORS[*]}" =~ $color ]]; then
        echo "Invalid color: $color"
        exit 1
    fi
done

for color in "$1" "$2"; do
    case "$color" in
    black) resistance+=0 ;;
    brown) resistance+=1 ;;
    red) resistance+=2 ;;
    orange) resistance+=3 ;;
    yellow) resistance+=4 ;;
    green) resistance+=5 ;;
    blue) resistance+=6 ;;
    violet) resistance+=7 ;;
    grey) resistance+=8 ;;
    white) resistance+=9 ;;
    esac
done

for color in $3; do
    case "$color" in
    brown) resistance+=0 ;;
    red) resistance+=00 ;;
    orange) resistance+=000 ;;
    yellow) resistance+=0000 ;;
    green) resistance+=00000 ;;
    blue) resistance+=000000 ;;
    violet) resistance+=0000000 ;;
    grey) resistance+=00000000 ;;
    white) resistance+=000000000 ;;
    esac
done

# Force base-10 interpretation
((resistance = 10#$resistance))

# Convert ohms to kiloohms, megaohms, gigaohms
for ((i = 0; i < ${#PREFIXES[@]}; i++)); do
    prefix=${PREFIXES[$i]}
    # If the resistance is less than 1000, we're done
    ((resistance < 1000)) && break
    # Use the nearest untit that results in a whole number
    ((resistance % 1000 != 0)) && break
    ((resistance /= 1000))
done

echo "${resistance} ${prefix}ohms"

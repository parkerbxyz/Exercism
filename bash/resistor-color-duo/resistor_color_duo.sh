#!/usr/bin/env bash
#
# Takes color names as input and outputs a two digit resistance value.

colors=("$@")

# Iterate through the first two elements of $color
for color in "${colors[@]:0:2}"; do
    case "$color" in
    black)
        resistance_value+=0
        ;;
    brown)
        resistance_value+=1
        ;;
    red)
        resistance_value+=2
        ;;
    orange)
        resistance_value+=3
        ;;
    yellow)
        resistance_value+=4
        ;;
    green)
        resistance_value+=5
        ;;
    blue)
        resistance_value+=6
        ;;
    violet)
        resistance_value+=7
        ;;
    grey)
        resistance_value+=8
        ;;
    white)
        resistance_value+=9
        ;;
    *)
        resistance_value="invalid color: $color"
        break
        ;;
    esac
done

echo "$resistance_value"

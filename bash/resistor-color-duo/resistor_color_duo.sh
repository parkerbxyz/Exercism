#!/usr/bin/env bash
#
# Take two color names as input and output a two digit resistance value.

for color in "$1" "$2"; do
    case "$color" in
    black)  resistance+=0 ;;
    brown)  resistance+=1 ;;
    red)    resistance+=2 ;;
    orange) resistance+=3 ;;
    yellow) resistance+=4 ;;
    green)  resistance+=5 ;;
    blue)   resistance+=6 ;;
    violet) resistance+=7 ;;
    grey)   resistance+=8 ;;
    white)  resistance+=9 ;;
    *)
        echo "invalid color: $color"
        exit 1
        ;;
    esac
done

echo "$resistance"

#!/bin/zsh

# $ zsh my_script.sh README.md README.pdf
A1=$(cd $(dirname $1) && pwd)
B1=$(basename $1)
C1="$A1/$B1"

A2=$(cd $(dirname $2) && pwd)
B2=$(basename $2)
C2="$A2/$B2"

echo -e "$A1\n$B1\n$C1\n\n$A2\n$B2\n$C2\n"

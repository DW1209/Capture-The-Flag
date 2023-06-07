#!/usr/bin/bash

info="$(xxd -p meow.jpg | tr -d '\n' | grep -o '504b0304.*')"
echo "$info" | xxd -r -p > compressed.bin
unzip compressed.bin > /dev/null
cat flag.txt | grep -o 'FLAG{[^}]*}'
rm *.txt *.bin

#!/usr/bin/bash

echo "$(strings -n 12 ./string)" | while IFS= read -r line; do
    decoded="$(echo "$line" | base64 -d 2> /dev/null)"
    if [ $? -eq 0 ]; then
        if [[ $decoded == FLAG\{*\} ]]; then
            echo "$decoded"; break
        fi
    fi
done
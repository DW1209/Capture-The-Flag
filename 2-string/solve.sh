#!/usr/bin/bash

echo -e "$(strings -n 16 --data ./string | head -n 1 | base64 -d)"
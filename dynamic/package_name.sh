#!/bin/bash
aapt dump badging $1 | grep package | sed -r "s/package: name='([a-z0-9.]*)'.*/\1/" > package_name.txt
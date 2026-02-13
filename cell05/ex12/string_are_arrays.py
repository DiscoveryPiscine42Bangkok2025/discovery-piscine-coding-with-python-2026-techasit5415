#!/usr/bin/env python3
import sys

params = sys.argv[1:]

if len(params) != 1:
    print("none")
else:
    text = params[0]
    z_count = text.count("z")

    if z_count > 0:
        print("z" * z_count)
    else:
        print("none")
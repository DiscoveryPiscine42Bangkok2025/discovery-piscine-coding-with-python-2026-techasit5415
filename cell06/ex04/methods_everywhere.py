#!/usr/bin/env python3
import sys

def shrink(s):
    return s[:8]

def enlarge(s):
    return s + "Z" * (8 - len(s))

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    for p in params:
        if len(p) > 8:
            print(shrink(p))
        elif len(p) < 8:
            print(enlarge(p))
        else: 
            print(p)
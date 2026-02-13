#!/usr/bin/env python3
import sys

params = sys.argv[1:]  

if len(params) == 0:
    print("none")
else:
    printed = False
    for p in params:
        if not p.endswith("ism"):
            print(p + "ism")
            printed = True
    if not printed: 
        print("none")
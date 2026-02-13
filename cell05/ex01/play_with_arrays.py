#!/usr/bin/env python3
import array
original = array.array('i', [2, 8, 9, 48, 8, 22, -12, 2])
new = array.array('i', [x + 2 for x in original])
print(f"Original array: {original.tolist()}")
print(f"New array: {new.tolist()}")
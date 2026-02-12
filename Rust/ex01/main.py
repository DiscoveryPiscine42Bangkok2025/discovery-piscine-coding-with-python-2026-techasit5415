#!/usr/bin/env python3
import sys
import os
from checkmate import checkmate

def run_app():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <board_file1> <board_file2> ...")
        return

    # loop
    for filepath in sys.argv[1:]:
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue

        try:
            with open(filepath, 'r') as f:
                content = f.read()
                
            result = checkmate(content)
            print(f"{result}")
            
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    run_app()
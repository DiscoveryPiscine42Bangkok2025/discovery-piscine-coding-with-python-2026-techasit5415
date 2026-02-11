import sys

def downcase(text):
    return text.lower()

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    for p in params:
        print(downcase(p))
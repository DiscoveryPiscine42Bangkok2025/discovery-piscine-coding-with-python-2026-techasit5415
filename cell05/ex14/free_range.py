import sys

params = sys.argv[1:]

if len(params) != 2:
    print("none")
else:
    try:
        start = int(params[0])
        end = int(params[1])
        numbers = list(range(start, end + 1))
        print(numbers)
    except ValueError:
        print("none")
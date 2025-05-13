#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: ./0-fizzbuzz.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Invalid number")
    sys.exit(1)

output = []
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        output.append("FizzBuzz")
    elif i % 3 == 0:
        output.append("Fizz")
    elif i % 5 == 0:
        output.append("Buzz")
    else:
        output.append(str(i))

print(" ".join(output))


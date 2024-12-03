#!/usr/bin/env python3

import re

with open("input.txt", "r") as f:
    memory = f.read()

instructions = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))", memory)

sum = 0
enabled = True

for instruction in instructions:
    if instruction[0] == "do()":
        enabled = True
    elif instruction[0] == "don't()":
        enabled = False
    elif enabled:
        sum += int(instruction[1]) * int(instruction[2])

print(sum)

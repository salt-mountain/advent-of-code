#!/usr/bin/env python3

import re

with open("input.txt", "r") as f:
    memory = f.read()

instructions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)

sum = 0

for instruction in instructions:
    sum += int(instruction[0]) * int(instruction[1])

print(sum)
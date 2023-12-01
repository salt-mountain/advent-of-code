#!/usr/bin/env python3

import re

with open("input.txt", "r") as file:
    lines = file.readlines()

# Part 1
calibration_values = []

for line in lines:
    number = ""
    for character in line:
        if character.isnumeric():
            number += character
    calibration_values.append(int(number[0] + number[-1]))
    
print(sum(calibration_values))

# Part 2
real_calibration_values = []

for line in lines:
    real_number = ""
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")

    for character in line:
        if character.isnumeric():
            real_number += character
    real_calibration_values.append(int(real_number[0] + real_number[-1]))

print(sum(real_calibration_values))
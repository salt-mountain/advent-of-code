#!/usr/bin/env python3

# Part 1
x_position, y_position = 0, 0

with open("input.txt", "r") as file:
    movement = [line.strip() for line in file]

for move in movement:
    direction, value = move.split()
    value = int(value)
    if direction == "forward":
        x_position += value
    elif direction == "up":
        y_position -= value
    elif direction == "down":
        y_position += value
    else:
        print("We should never be here")

print(x_position*y_position)

# Part 2
x_position, y_position, aim = 0, 0, 0

for move in movement:
    direction, value = move.split()
    value = int(value)
    if direction == "forward":
        x_position += value
        y_position += aim * value
    elif direction == "up":
        aim -= value
    elif direction == "down":
        aim += value
    else:
        print("We should never be here")

print(x_position*y_position)
#!/usr/bin/env python3

# Part 1

with open("input.txt", "r") as file:
    rows = [row.rstrip() for row in file]
    lines = [[[int(num) for num in coord.split(",")] for coord in row.split(" -> ")] for row in rows]

def count_overlapping_points(vent_positions):
    overlapping_points = 0
    for number_of_points in vent_positions.values():
        if number_of_points > 1:
            overlapping_points += 1
    return overlapping_points

vent_positions = {}

for line in lines:
    [x1, y1], [x2,y2] = line
    smaller_horizontal = min(x1, x2)
    larger_horizontal = max(x1, x2)
    smaller_vertical = min(y1, y2)
    larger_vertical = max(y1, y2)
    if x1 == x2:
        for y in range(smaller_vertical, larger_vertical + 1):
            coordinate = (x1, y)
            if coordinate in vent_positions:
                vent_positions[coordinate] += 1
            else:
                vent_positions[coordinate] = 1
    elif y1 == y2:
        for x in range(smaller_horizontal, larger_horizontal + 1):
            coordinate = (x, y1)
            if coordinate in vent_positions:
                vent_positions[coordinate] += 1
            else:
                vent_positions[coordinate] = 1

print(count_overlapping_points(vent_positions))

# Part 2
vent_positions = {}

for line in lines:
    [x1, y1], [x2,y2] = line
    smaller_horizontal = min(x1, x2)
    larger_horizontal = max(x1, x2)
    smaller_vertical = min(y1, y2)
    larger_vertical = max(y1, y2)
    x_delta = larger_horizontal - smaller_horizontal
    y_delta = larger_vertical - smaller_vertical
    if x1 == x2:
        for y in range(smaller_vertical, larger_vertical + 1):
            coordinate = (x1, y)
            if coordinate in vent_positions:
                vent_positions[coordinate] += 1
            else:
                vent_positions[coordinate] = 1
    elif y1 == y2:
        for x in range(smaller_horizontal, larger_horizontal + 1):
            coordinate = (x, y1)
            if coordinate in vent_positions:
                vent_positions[coordinate] += 1
            else:
                vent_positions[coordinate] = 1
    elif x_delta == y_delta:
        horizontal_direction_value = 1 if x2 > x1 else -1
        vertical_direction_value = 1 if y2 > y1 else -1
        for i in range(x_delta + 1):
            coordinate = (x1 + i * horizontal_direction_value, y1 + i * vertical_direction_value)
            if coordinate in vent_positions:
                vent_positions[coordinate] += 1
            else:
                vent_positions[coordinate] = 1

print(count_overlapping_points(vent_positions))
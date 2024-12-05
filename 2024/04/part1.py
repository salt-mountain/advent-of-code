#!/usr/bin/env python3

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]

def in_grid(p, grid):
    """
    Check whether a given point is in a 2D Grid.
    The length of one row represents the value an x-coordinate can have.
    The number of rows (length) represents the value the y-coordinate can have. 
    """
    return 0 <= p[0] < len(grid[0]) and 0 <= p[1] < len(grid)

MAGIC_STRING = "XMAS"

with open('input.txt', 'r') as f:
    grid = [line.rstrip() for line in f.readlines()]

sum = 0

for r, row in enumerate(grid):
    for c, _ in enumerate(row):
        for p in DIRECTIONS:
            found = True
            current_point = (r, c)
            for letter in MAGIC_STRING:
                if not in_grid(current_point, grid) or grid[current_point[0]][current_point[1]] != letter:
                    found = False
                    break
                
                current_point = (current_point[0] + p[0], current_point[1] + p[1])

            if found:
                sum += 1

print(sum)



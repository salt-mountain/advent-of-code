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

MAGIC_STRING = "MS"

def is_diagonal(letter1, letter2):
    """
    If we find an 'A', then we can just check the diagonal corners for `MS` or `SM`
    Diagonals spell `MAS` or `SAM`
    """
    return letter1 in MAGIC_STRING and letter2 in MAGIC_STRING and letter1 != letter2

with open('input.txt', 'r') as f:
    grid = [line.rstrip() for line in f.readlines()]

sum = 0

for r, row in enumerate(grid):
    for c, _ in enumerate(row):
        if row[c] == "A":
            # top left, top right, bottom left, bottom right
            corners = [(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]

            if all(in_grid(p, grid) for p in corners):
                # get the letters of the corner points and check if they're right
                corner_letters = [grid[a][b] for a, b in corners]
                if is_diagonal(corner_letters[0], corner_letters[3]) and is_diagonal(corner_letters[1], corner_letters[2]):
                    sum += 1
print(sum)

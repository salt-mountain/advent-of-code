#!/usr/bin/env python3

from itertools import combinations

grid = []
antennas = {}
antinodes = set()
EMPTY = '.'
ANTINODE = '#'

def in_grid(p, grid):
    return 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])

def add_antinode(p):
    if in_grid(p, grid):
        antinodes.add(p)

with open('input.txt', 'r') as f:
    for line in f:
        grid.append(line.strip())

for r, row in enumerate(grid):
    for c, _ in enumerate(row):
        if row[c] != EMPTY:
            antennas.setdefault(row[c], []).append((r, c))

for antenna in antennas.keys():
    points = antennas[antenna]
    point_combinations = list(combinations(points, 2))
    for p1, p2 in point_combinations:
        vector_x = p2[0] - p1[0]
        vector_y = p2[1] - p1[1]

        n = 1
        # extend towards the second point
        p3 = (p2[0] + n * vector_x, p2[1] + n * vector_y)
        # extend towards the first point
        p4 = (p1[0] - n * vector_x, p1[1] - n * vector_y)

        for p in [p3, p4]:
            add_antinode(p)
    
print(len(antinodes))

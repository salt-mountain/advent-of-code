#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    grid = [line.rstrip() for line in f.readlines()]

guard_directions = {
    "^":(">", (-1,0)), 
    ">":("v", (0,1)), 
    "v":("<", (1,0)), 
    "<":("^", (0,-1))
}

position = (0,0)
direction = ">"

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in guard_directions:
            position = (i,j)
            direction = grid[i][j]

while (position[0] >= 0 and position[0] < len(grid)) and (position[1] >= 0 and position[1] < len(grid[position[0]])):
    line = grid[position[0]]
    line = line[:position[1]] + "X" + line[position[1] + 1:]
    grid[position[0]] = line
    (next_direction, delta) = guard_directions[direction]
    next_row = position[0] + delta[0]
    next_column = position[1] + delta[1]

    if next_row < 0 or next_row >= len(grid) or next_column < 0 or next_column >= len(grid[next_row]):
        position = (next_row, next_column)
        continue

    if grid[next_row][next_column] == "#":
        direction = next_direction
        continue

    position = (next_row, next_column)

visited = 0

for i in grid:
    for j in i:
        if j == "X":
            visited += 1

print(visited)
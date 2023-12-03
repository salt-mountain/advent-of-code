#!/usr/bin/env python3

from collections import defaultdict
from functools import reduce
from operator import mul
from pathlib import Path
import string
import re

symbols = set(string.punctuation)
symbols.remove(".")

def has_adjacent_symbol(lines, row, starting_column, ending_column):
    # 00 01 02 03
    # 10 11 12 13
    # 20 21 22 23

    # Say we're at 11 12  row 1, starting_column = 1, ending_column = 2
    # We have to check
    #   00 to 03    -> row -1, all columns from starting_column -1 to ending_column +1
    #   20 to 23    -> row +1, all columns from starting_column -1 to ending_column +1
    #   10 & 13     -> they're adjacent, so starting_column -1 and ending_column + 1

    # Adjacent check is easy
    if starting_column - 1 >= 0 and lines[row][starting_column - 1] in symbols:
        return True
    if ending_column + 1 < len(lines[0]) and lines[row][ending_column + 1] in symbols:
        return True
    for column in range(starting_column -1, ending_column +2):
        # Dont escape the bounds
        if column < 0 or column >= len(lines[0]):
            continue
        if row - 1 > 0 and lines[row - 1][column] in symbols:
            return True
        if row + 1 < len(lines[0]) and lines[row + 1][column] in symbols:
            return True
        
    return False

def get_gear_coordinates(lines, row, starting_column, ending_column):
    # It should be the same algorithm as has_adjacent_symbol
    #    but now we need to keep a track of the coordinates 
    #    we find the gears/asterisks in.

    coordinates = set()

    if starting_column - 1 >= 0 and lines[row][starting_column - 1] == "*":
        coordinates.add((row, starting_column - 1))
    if ending_column + 1 < len(lines[0]) and lines[row][ending_column + 1] == "*":
        coordinates.add((row, ending_column + 1))
    for column in range(starting_column - 1, ending_column + 2):
        if column < 0 or column >= len(lines[0]):
            continue
        if row - 1 > 0 and lines[row -1][column] == "*":
            coordinates.add((row - 1, column))
        if row + 1 < len(lines[0]) and lines[row + 1][column] == "*":
            coordinates.add((row + 1, column))

    return coordinates

def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().split()

    part_numbers = []
    
    for row, line in enumerate(lines):
        for number in re.finditer(r"\d+", line):
            if has_adjacent_symbol(lines, row, number.start(), number.end() - 1):
                part_numbers.append(int(number.group()))
    
    # Part 1
    print(sum(part_numbers))

    # Part 2
    gear_coordinate_numbers = defaultdict(list)

    for row, line in enumerate(lines):
        for number in re.finditer(r"\d+", line):
            if gear_coordinates := get_gear_coordinates(lines, row, number.start(), number.end() - 1):
                for gear_coordinate in gear_coordinates:
                    gear_coordinate_numbers[gear_coordinate].append(int(number.group()))

    gear_ratios = []

    # coordinate, part_numbers but we dont actually need the coordinate now
    for _, part_numbers in gear_coordinate_numbers.items():
        if len(part_numbers) == 2:
            gear_ratios.append(reduce(mul, part_numbers))
    
    print(sum(gear_ratios))


if __name__ == "__main__":
    main()

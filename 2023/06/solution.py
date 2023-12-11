#!/usr/bin/env python3

import numpy as np

def find_winners(time_and_distance):
    record_breakers = []

    for race in time_and_distance:
        working_numbers = set()
        for i in range(1, race[0]):
            distance = (race[0] - i) * i
            if distance > race[1]:
                working_numbers.add(i)
        race_and_distance = race + (list(working_numbers), len(working_numbers))
        record_breakers.append(race_and_distance)
    return np.prod([i[3] for i in record_breakers])

def main():

    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    
    time_values = list(map(int, lines[0].split()[1:]))
    distance_values = list(map(int, lines[1].split()[1:]))
    time_and_distance = list(zip(time_values, distance_values))

    # Part 1
    print(find_winners(time_and_distance))

    # Part 2
    time_values = ''.join(lines[0].split()[1:])
    distance_values = ''.join(lines[1].split()[1:])
    time_and_distance = [(int(time_values), int(distance_values))]
    print(find_winners(time_and_distance))

if __name__ == "__main__":

    main()

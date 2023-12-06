#!/usr/bin/env python3

import sys

class SeedMap:
    def __init__(self, from_map_type, target_map_type):
        self.from_map_type = from_map_type
        self.target_map_type = target_map_type
        # tuple is (source, max_source, target)
        # source is inclusive, max_source is exclusive
        self.map_values: list[tuple[int, int, int]] = []

    def add(self, target, source, offset):
        self.map_values.append((source, source + offset, target))

    def get_destination(self, seed_value):
        # for each mapping range
        for source, max_source, target in self.map_values:
            # if seed_value is between range
            if source <= seed_value < max_source:
                # map it
                return target + (seed_value - source)
        # if no range was found return values unchanged
        return seed_value
    
    def __str__(self):
        return f"{self.from_map_type} => {self.target_map_type}"
    def __repr__(self):
        return self.__str__()

def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    # Seeds Line
    seeds = [int (seed) for seed in lines[0].split(": ")[1].split(" ")]

    # Create Seed Maps
    seed_maps: list[SeedMap] = []

    # for each line after the first
    for line in lines[1:]:
        # skip any empty lines
        if line == "":
            continue
        
        # if new map declaration
        if line.endswith("map:"):
            # get the map type we're going from and
            # the map type we're going to
            from_map_type, to_map_type = line.split(" ")[0].split("-to-", 1)
            # create the map and add it to the list
            current_map = SeedMap(from_map_type, to_map_type)
            seed_maps.append(current_map)
        else:
            # if not a map declaration, add the mapping
            # the * unpacks the list into 3 arguments
            current_map.add(*[int(s) for s in line.split(" ")])
    
    # Start high, the input values are huge
    minimum_location = sys.maxsize

    for seed in seeds:
        # map it through all the seed maps
        for seed_map in seed_maps:
            seed = seed_map.get_destination(seed)
        # update the minimum location
        minimum_location = min(minimum_location, seed)

    # Part 1
    print(minimum_location)

if __name__ == "__main__":
    main()

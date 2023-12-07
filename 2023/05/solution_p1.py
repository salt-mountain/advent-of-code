#!/usr/bin/env python3

import sys

class SeedMap:
    def __init__(self, from_map_type, target_map_type):
        self.from_map_type = from_map_type
        self.target_map_type = target_map_type
        self.map_values: list[tuple[int, int, int]] = []

    def add(self, target, source, offset):
        self.map_values.append((source, source + offset, target))

    def get_destination(self, seed_value):
        # For a given seed
        # For each mapping range
        for source, max_source, target in self.map_values:
            # if seed_value is between range
            if source <= seed_value < max_source:
                # Return the location value
                return target + (seed_value - source)
        # Any source numbers that aren't mapped correspond to the same destination number.
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

    # For each line after the first
    for line in lines[1:]:
        # skip any empty lines
        if line == "":
            continue
        
        # New Map
        if line.endswith("map:"):
            # get the map type we're going from and
            from_map_type, to_map_type = line.split(" ")[0].split("-to-", 1)
            # Create the map and add it to the list
            current_map = SeedMap(from_map_type, to_map_type)
            seed_maps.append(current_map)
        else:
            # if it's not a new map, add the map values
            current_map.add(*[int(s) for s in line.split(" ")])
    
    # Start high, the input values are huge
    minimum_location = sys.maxsize
    
    for seed in seeds:
        # For each seed
        # Map it through all the seed maps
        # Get the location number
        for seed_map in seed_maps:
            seed = seed_map.get_destination(seed)
        # update the minimum location
        minimum_location = min(minimum_location, seed)

    # Part 1
    print(minimum_location)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

class SeedMap:
    def __init__(self, from_map_type, target_map_type):
        self.from_map_type = from_map_type
        self.target_map_type = target_map_type
        self.map_values: list[tuple[int, int, int]] = []

    def add(self, target, source, offset):
        self.map_values.append((source, source + offset, target))

    def sort(self):
        self.map_values.sort(key=lambda x: x[0])

    def get_destination(self, ranges):
        new_ranges = SeedRangeList()

        for start, end in ranges:
            found_mapping = False

            for source, max_source, target in self.map_values:
                if start < source:
                    if end < source:
                        new_ranges.add(start, end)
                        found_mapping = True
                        break

                    if end <= max_source:
                        new_ranges.add(start, source)
                        new_ranges.add(target, target + (end - source))
                        found_mapping = True
                        break

                    new_ranges.add(start, source)
                    new_ranges.add(target, target + (max_source - source))
                    start = max_source

                elif source <= start < max_source:
                    if end <= max_source:
                        new_ranges.add(target + (start - source), target + (end - source))
                        found_mapping = True
                        break

                    new_ranges.add(target + (start - source) , target + (max_source - source))
                    start = max_source

            if not found_mapping:
                new_ranges.add(start, end)

        return new_ranges

    def __str__(self):
        return f"{self.from_map_type} to {self.target_map_type}"

    def __repr__(self):
        return self.__str__()

class SeedRangeList:
    def __init__(self):
        self.ranges: list[tuple[int, int]] = []

    def add(self, start_range, end_range):
        # for each range thats already been added
        for i, (start, end) in enumerate(self.ranges):
            # if start is before the range
            if start_range < start:
                # if end is before the range
                if end_range < start:
                    self.ranges.insert(i, (start_range, end_range))
                    return
                # if the end is in-between the range
                if end_range <= end:
                    # only add until start
                    self.ranges.insert(i, (start_range, start))
                    return
                # else if end is after the range
                # add until start
                self.ranges.insert(i, (start_range, start))
                # then continue with the rest of the range
                start_range = end
            # else if start is in between the range
            elif start_range <= start <= end_range:
                # if end is in between the range
                if end_range <= end:
                    # we should already have this range
                    return
                # else if end is after this range we continue
                start_range = end
        # First time seeing this range, add it
        self.ranges.append((start_range, end_range))

    def __iter__(self):
        return iter(self.ranges)

    def __str__(self):
        return str(self.ranges)

    def __repr__(self):
        return self.__str__()

def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    # split the seeds
    seed_range = lines[0].split(": ")[1].split(" ")
    seeds = SeedRangeList()

    # for each pair of seed inputs
    for i in range(0, len(seed_range), 2):
        # add the range to the list
        seeds.add(int(seed_range[i]), int(seed_range[i]) + int(seed_range[i+1]))
    # create the list of seed maps
    seed_maps: list[SeedMap] = []
    current_map = None

    for line in lines[1:]:
        if line == "":
            continue

        if line.endswith("map:"):
            from_map_type, to_map_type = line.split(" ")[0].split("-to-", 1)
            current_map = SeedMap(from_map_type, to_map_type)
            seed_maps.append(current_map)
        else:
            current_map.add(*[int(s) for s in line.split(" ")])

    # sort the seed map ranges so that they're ascending
    for seed_map in seed_maps:
        seed_map.sort()

    # for each map
    for seed_map in seed_maps:
        # Map all the seed ranges through the map
        seeds = seed_map.get_destination(seeds)

    # print the minimum location
    print(min(start for start, _ in seeds))

if __name__ == "__main__":
    main()

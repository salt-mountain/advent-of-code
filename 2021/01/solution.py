#!/usr/bin/env python3

# Part 1
depths = [int(line.strip()) for line in open("input.txt", "r")]
print(sum([1 for i in range(1, len(depths)) if depths[i] > depths[i-1]]))

# Part 2
windows = [depths[i: i + 3] for i in range(len(depths) - 3 + 1)]
print(sum([1 for i in range(1, len(windows)) if sum(windows[i]) > sum(windows[i-1])]))
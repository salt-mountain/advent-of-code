#!/usr/bin/env python3

lines = []

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lines.append(line)

values = [int(value) for value in list(lines[0])]
checksum = 0
strip = []
id = 0
is_block = True

for i in range(len(values)):
    if is_block:
        # Add a block of values[i] size represented by the blocks ID
        strip.extend([id] * values[i])
        id += 1
    else:
        # Add a gap of values[i] size represented just by 'None'
        strip.extend([None] * values[i])
    # Alternate between blocks and gaps
    is_block = not is_block

# Find the index of the first free space in the strip
free_space = strip.index(None)

for i in reversed(range(0, len(strip))):
    # Compact by moving blocks left into the gaps
    if strip[i] is not None:
        # If we have a block, move it into the free space.
        strip[free_space] = strip[i]
        strip[i] = None
        # Update the free_space to the next gap
        while strip[free_space] is not None:
            free_space += 1
        # Stop as we start running out of space
        if i - free_space <= 1:
            break

checksum = sum(value * i if value is not None else 0 for (i, value) in enumerate(strip))
print(checksum)
#!/usr/bin/env python3

lines = []

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lines.append(line)

values = [int(value) for value in list(lines[0])]
checksum = 0
strip = []
blocks = []
gaps = []
id = 0
is_block = True

for i in range(len(values)):
    if is_block:
        # List of every block to include (start_position, id, length)
        blocks.append((len(strip), id, values[i]))
        strip.extend([id] * values[i])
        id += 1
    else:
        # List of gaps to include (length_of_gap, start_position)
        gaps.append((values[i], len(strip)))
        strip.extend([None] * values[i])
    
    is_block = not is_block

for block in reversed(blocks):
    (position, id, length) = block
    for i, (gap_length, gap_position) in enumerate(gaps):
        if gap_position > position:
            break

        if gap_length >= length:
            for l in range(length):
                strip[position + l] = None
                strip[gap_position + l] = id
            
            diff = gap_length - length
            if diff > 0:
                gaps[i] = (diff, gap_position + length)
            else:
                gaps.pop(i)
            break

checksum = sum(value * i if value is not None else 0 for (i, value) in enumerate(strip))
print(checksum)

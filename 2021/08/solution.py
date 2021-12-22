#!/usr/bin/env python3

# Part 1
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    lines = [x.split(" | ")[1].split(' ') for x in lines]
    total = 0
    # 1 = 2 segments
    # 4 = 4 segments
    # 7 = 3 segments
    # 8 = 7 segments
    for line in lines:
        for segment in line:
            if len(segment) == 2 or len(segment) == 3 or len(segment) == 4 or len(segment) == 7:
                total += 1
    print(total)

# Part 2
total = 0
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        signals, output = line.strip().split(" | ")
        decoder = { l: set(signal) for signal in signals.split() if (l := len(signal)) in (2, 4) }
        number = ""
        for segment in output.split():
            length = len(segment)
            if length == 2: 
                number += "1"
            elif length == 4: 
                number += "4"
            elif length == 3: 
                number += "7"
            elif length == 7: 
                number += "8"
            elif length == 5:
                encoded_signal = set(segment)
                # 1 and 3 share two segments
                if len(encoded_signal & decoder[2]) == 2: 
                    number += "3"
                # 4 and 2 share two segments
                elif len(encoded_signal & decoder[4]) == 2: 
                    number += "2"
                # The only other value thats length 5 is 5
                else:
                    number += "5"
            else: #length == 6
                encoded_signal = set(segment)
                # 1 and 6 share one segment
                if len(encoded_signal & decoder[2]) == 1:
                    number += "6"
                # 4 and 9 share four segments
                elif len(encoded_signal & decoder[4]) == 4:
                    number += "9"
                # Only other number left is 0
                else:
                    number += "0"
        total += int(number)
print(total)
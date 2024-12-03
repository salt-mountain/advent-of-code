#!/usr/bin/env python3

left, right = [], []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        left_number, right_number = (int(number) for number in line.split())
        left.append(left_number)
        right.append(right_number)

left.sort()
right.sort()
length = len(left)

print(sum(abs(left[i]-right[i]) for i in range(length)))

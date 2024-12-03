#!/usr/bin/env python3

from collections import Counter

left, right = [], []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        left_number, right_number = (int(number) for number in line.split())
        left.append(left_number)
        right.append(right_number)

left.sort()
right.sort()
length = len(left)
c = Counter(right)

print(sum(left[i]*c[left[i]] for i in range (length)))

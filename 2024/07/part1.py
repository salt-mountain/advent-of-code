#!/usr/bin/env python3

from itertools import product

import operator

equations = []
operators = [
    operator.add,
    operator.mul
]

with open('input.txt', 'r') as f:
    for line in f:
        s = line.split(':')
        operands = (list(map(int, s[1].split())))
        equations.append((int(s[0]), operands))

total_calibration_result = 0

for test_value, operands in equations:
    permutations = list(product(operators, repeat=len(operands)-1))
    for operations in permutations:
        result = operands[0]
        for i, op in enumerate(operations):
            result = op(result, operands[i + 1])
            
            if result > test_value:
                break
        
        if result == test_value:
            total_calibration_result += test_value
            break

print(total_calibration_result)
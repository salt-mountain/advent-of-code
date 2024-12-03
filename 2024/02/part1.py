#!/usr/bin/env python3

def check_same_direction(report):
    direction = None 

    for i in range(1, len(report)):
        difference = report[i] - report[i-1]
        if difference == 0:
            return False # We should never have two adjacent numbers be equal
        if direction is None:
            direction = difference # Set the initial direction
        elif (direction > 0 and difference < 0) or (direction < 0 and difference > 0):
            return False # We changed direction
    
    return True

def check_delta(report):
    for i in range(len(report) - 1):  # Iterate through adjacent pairs
        if abs(report[i] - report[i + 1]) not in [1, 2, 3]:  # Validate the difference
            return False  # Return False if any difference is out of range
    return True  # Return True only if all differences are valid

with open('input.txt', 'r') as f:
    reports = [line.rstrip() for line in f.readlines()]

safe_reports = 0

for row in reports:
    split_row = [int(value) for value in row.split()]
    if check_same_direction(split_row) and check_delta(split_row):
        safe_reports += 1

print(safe_reports)
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

def dampened_check_same_direction(reports):
    checks = len(reports)
    if check_same_direction(reports): # nothing to do here
        return True, reports
    for position in range(checks):
        modified_reports = [
            report for pos, report in enumerate(reports) if pos != position
        ]
        if check_same_direction(modified_reports):
            return True, modified_reports
    return False, reports

def dampened_check_delta(reports):
    checks = len(reports)
    if check_delta(reports): # nothing to do here
        return True, reports
    for position in range(checks):
        modified_numbers = [
            report for pos, report in enumerate(reports) if pos != position
        ]
        if check_delta(modified_numbers):
            return True, modified_numbers
    return False, reports

def dampen(reports):
    (processed, to_process) = dampened_check_same_direction(reports)
    if processed and check_delta(to_process):
        return True
    (processed, to_process) = dampened_check_delta(reports)
    if processed and check_same_direction(to_process):
        return True
    return False

with open('input.txt', 'r') as f:
    reports = [line.rstrip() for line in f.readlines()]

safe_dampened_reports = 0

for row in reports:
    split_row = [int(value) for value in row.split()]
    if dampen(split_row):
        safe_dampened_reports += 1

print(safe_dampened_reports)
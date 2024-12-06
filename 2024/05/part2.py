#!/usr/bin/env python3

from functools import cmp_to_key

def is_rule(left, right, rules):
    return f'{left}|{right}' in rules

def is_ordered(rules, update):
    ordered = True
    for n, page in enumerate(update):
        for i in range (n + 1, len(update)):
            if not is_rule(page, update[i], rules):
                ordered = False
                break
        
        if not ordered:
            return False
    
    return ordered

def compare(left, right):
    return -1 if is_rule(left, right, rules) else 1

def custom_sort(update, rules):
    return sorted(update, key=cmp_to_key(compare))

with open('input.txt', 'r') as f:
    input = f.read().split('\n\n')

rules = set(input[0].split('\n'))
updates = [list(map(int, line.split(','))) for line in input[1].split()]

sum = 0

for update in updates:
    if not is_ordered(rules, update):
        sorted_row = custom_sort(update, rules)
        sum += sorted_row[len(sorted_row) // 2]

print(sum)

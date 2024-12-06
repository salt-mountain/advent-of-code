#!/usr/bin/env python3

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

with open('input.txt', 'r') as f:
    input = f.read().split('\n\n')

rules = set(input[0].split('\n'))
updates = [list(map(int, line.split(','))) for line in input[1].split()]

sum = 0

for update in updates:
    if is_ordered(rules, update):
        sum += update[len(update) // 2]

print(sum)

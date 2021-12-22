#!/usr/bin/env python3

with open('input.txt', 'r') as file:
    position_list = [int(line) for line in file.read().split(',')]
    
position_dict = {}
for position in position_list:
    position_dict[position] = position_list.count(position)

def calculate_fuel_cost_part1(position):
    cost = 0
    for key, value in position_dict.items():
        cost += abs(key - position) * value
    return(cost)

def calculate_fuel_cost_part2(position):
    cost = 0
    for key, value in position_dict.items():
        cost += sum(range(abs(key - position) + 1)) * value
    return(cost)

cost_dict_part1 = {}
cost_dict_part2 = {}
for position in range(max(position_list)):
    cost_dict_part1[position] = calculate_fuel_cost_part1(position)
    cost_dict_part2[position] = calculate_fuel_cost_part2(position)

print(min(cost_dict_part1.values()))
print(min(cost_dict_part2.values()))
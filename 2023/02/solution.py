#!/usr/bin/env python3

import re

game_pieces = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open("input.txt", "r") as file:
    lines = file.readlines()

# Part 1
total_possible_games = 0

for line in lines:
    line = line.split(" ")
    game_id = int(line[1][:len(line[1])-1])

    is_game_possible = True

    for i in range(2, len(line), 2):
        quantity = int(line[i])
        color = re.sub(r'[;,]', '', line[i+1].strip())
        is_game_possible = is_game_possible and quantity <= game_pieces[color]
    
    total_possible_games += is_game_possible * game_id

print(total_possible_games)

# Part 2
total_game_power = 0

for line in lines:
    minimum_pieces = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    line = line.split(" ")
    game_id = int(line[1][:len(line[1])-1])

    for i in range(2, len(line), 2):
        quantity = int(line[i])
        color = re.sub(r'[;,]', '', line[i+1].strip())
        minimum_pieces[color] = max(quantity, minimum_pieces[color])
    
    power = 1
    for color in minimum_pieces:
        power *= minimum_pieces[color]
    
    total_game_power += power

print(total_game_power)
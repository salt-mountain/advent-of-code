#!/usr/bin/env python3

points = {
    'AX': 4,
    'AY': 8,
    'AZ': 3, 
    'BX': 1, 
    'BY': 5, 
    'BZ': 9,
    'CX': 7, 
    'CY': 2,
    'CZ': 6, 
}

rigged_points = {
    'AX': 0 + 3,
    'AY': 3 + 1,
    'AZ': 6 + 2, 
    'BX': 0 + 1, 
    'BY': 3 + 2, 
    'BZ': 6 + 3,
    'CX': 0 + 2, 
    'CY': 3 + 3,
    'CZ': 6 + 1,
}


with open("input.txt", "r") as file:
    lines = file.read().split("\n")
    games = {}
    total_points = 0
    rigged_total = 0
    for line in lines:
        game_round = ''.join(str(line).split())
        if game_round in games.keys():
            games[game_round] += 1
        else:
            games[game_round] = 1
    total = 0
    for game in games:
        total += points[game]*games[game]
        rigged_total += rigged_points[game]*games[game]
    
    # Part 1
    print(total)
    
    # Part 2
    print(rigged_total)
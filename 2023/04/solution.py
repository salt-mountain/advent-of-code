#!/usr/bin/env python3

from collections import Counter
from pathlib import Path

def calculate_winning_points(scratchcard):
    # Get the numbers
    game_numbers = scratchcard.split(":")[1].split("|")[0].strip().split(" ")
    player_numbers =scratchcard.split(":")[1].split("|")[1].strip().split(" ") 

    # Remove empty strings
    game_numbers = list(filter(None, game_numbers))
    player_numbers = list(filter(None, player_numbers))

    # Check if we're a winner
    winning_numbers = list((Counter(game_numbers) & Counter(player_numbers)).elements())
    return winning_numbers

def main():

    with open("input.txt", "r") as file:
        scratchcard = file.read().splitlines()
    
    winning_points = 0

    for i, card in enumerate(scratchcard):
        winning_numbers = calculate_winning_points(card)
        if len(winning_numbers) > 0:
            winning_points += 2 ** (len(winning_numbers)-1)

    # Part 1
    print(winning_points)

if __name__ == "__main__":
    main()

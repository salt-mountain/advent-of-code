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
    # Part 2 Logic
    # Generate a List of 1s for each card, since that's guaranteed.
    # For a given Winning Card, we'll iterate over the number of winning numbers
    # which gives us an easy way to iterate to the next sets of cards to increase
    # how many of each we have.
    # Ex:
    # Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
    # Looping over the amount winning numbers, we can easily increment scratchcard + winning number (e.g 1,2,3,4) to get a
    # new total of original card + new winning card/duplicate.
    total_scratchcards = [1] * len(scratchcard)

    for i, card in enumerate(scratchcard):
        winning_numbers = calculate_winning_points(card)
        if len(winning_numbers) > 0:
            # Part 1
            winning_points += 2 ** (len(winning_numbers)-1)
            # Part 2
            for number in range(1, len(winning_numbers) + 1):
                total_scratchcards[i + number] += total_scratchcards[i]

    # Part 1
    print(winning_points)

    # Part 2
    print(sum(total_scratchcards))

if __name__ == "__main__":
    main()

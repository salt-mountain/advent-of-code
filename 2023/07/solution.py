#!/usr/bin/env python3

from collections import Counter

# A hand is defined by the number of unique cards it has
#   and the number of each of those cards.
# For instance:
#   A 4 of a kind is 4 instances of one card and 1 instance of another. 
#   A 3 of a kind is 3 instances of one card and 2 instances of another.
#   etc.
# For scoring, we dont care what the cards are, just how many we have.
#
# Part 2: Jokers
# The "cheat" here is that we dont actually have to worry about Jokers
# You will always want to just increase whatever card you have the most of (the last value)
# So we can remove the Joker and add their count to the end value
def hand_value(hand, jokers=False):
    hand_values = sorted(Counter(hand).values())

    if jokers and (joker_count := hand.count("J")) and joker_count < 5:
        hand_values.remove(joker_count)
        hand_values[-1] += joker_count
    
    match hand_values:
        # 5 of a kind
        case [5]:
            return 7
        # 4 of a kind
        case [1, 4]:
            return 6
        # Full House
        case [2, 3]:
            return 5
        # 3 of a kind
        case [1, 1, 3]:
            return 4
        # 2 Pair
        case [1, 2, 2]:
            return 3
        # 1 Pair
        case [1, 1, 1, 2]:
            return 2
        # High Card
        case [1, 1, 1, 1, 1]:
            return 1
        # This should never happen
        case _:
            return 0

# Each card needs a numeric value
# We know the ordering, from 2 -> A
# Replace each letter with its corresponding
#   index in the list.
def hand_strength(hand, card_values):
    return tuple(card_values.index(card) for card in hand)

def main():

    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    hand_scores: list[tuple[int, tuple[int, ...], int]] = []
    hand_scores_with_jokers: list[tuple[int, tuple[int, ...], int]] = []
    card_values = "23456789TJQKA"
    joker_card_values = "J23456789TQKA"

    for line in lines:
        hand, bid = line.split()
        hand_scores.append((hand_value(hand), hand_strength(hand, card_values), int(bid)))
        hand_scores_with_jokers.append((hand_value(hand, jokers=True), hand_strength(hand, joker_card_values), int(bid)))

    # Part 1
    total = sum((i + 1) * bid for i, (hand_value, cards, bid) in enumerate(sorted(hand_scores)))
    print(total)

    # Part 2
    total2 = sum((i + 1) * bid for i, (hand_value, cards, bid) in enumerate(sorted(hand_scores_with_jokers)))
    print(total2)

if __name__ == "__main__":

    main()

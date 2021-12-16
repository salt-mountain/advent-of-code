#!/usr/bin/env python3

# Part 1
with open('input.txt', 'r') as f:
    bingo_numbers, *bingo_boards = f.read().split('\n\n')

def create_boards(bingo_numbers, bingo_boards):
    numbers = map(int, bingo_numbers.split(','))
    boards = []
    for board in bingo_boards:
        rows = [[int(i) for i in row.split()] for row in board.split('\n')]
        boards.append([set(row) for row in rows])
        boards.append([set(col) for col in zip(*rows)])
    return numbers, boards

def get_winning_score(number, board):
    return (sum(sum(group) for group in board) - number) * number

def part1():
    numbers, boards = create_boards(bingo_numbers, bingo_boards)
    for number in numbers:
        for i, board in enumerate(boards):
            if {number} in board:                
                return get_winning_score(number, board)
            else:
                boards[i] = [group.difference({number}) for group in board]

print(part1())

# Part 2
def part2():
    numbers, boards = create_boards(bingo_numbers, bingo_boards)
    for number in numbers:
        for i, board in enumerate(boards):
            if board is not None:
                if {number} in board:
                    winner = get_winning_score(number, board)
                    boards[i] = None
                    if i%2:
                        boards[i-1] = None
                    else:
                        boards[i+1] = None
                else:
                    boards[i] = [group.difference({number}) for group in board]
    return winner

print(part2())
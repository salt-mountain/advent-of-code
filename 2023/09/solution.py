#!/usr/bin/env python3

def get_next_value(history):
    
    if all(numbers == 0 for numbers in history):
        return 0
    else:
        # ex:
        #
        # i i+i
        # v v
        # 0 3 6 9 12 15
        #  3 3 3 3  3
        #  ^ - difference
        difference = [history[i + 1] - history[i] for i in range(len(history) - 1)]
        return history[-1] + get_next_value(difference)

def get_previous_value(history):

    if all(numbers == 0 for numbers in history):
        return 0
    else:
        difference = [history[i + 1] - history[i] for i in range(len(history) - 1)]
        return history[0] - get_previous_value(difference)

def main():

    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    extrapolated_values = 0
    previous_values = 0

    for history in lines:
        sequence = [int(number) for number in history.split()]
        extrapolated_values += get_next_value(sequence)
        previous_values += get_previous_value(sequence)

    # Part 1
    print(extrapolated_values)

    # Part 2
    print(previous_values)

if __name__ == "__main__":

    main()

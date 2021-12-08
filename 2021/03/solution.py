#!/usr/bin/env python3

# Part 1
gamma, epsilon = "", ""

with open("input.txt", "r") as file:
    numbers = [line.strip() for line in file]

columns = zip(*numbers)
for column in columns:
    if column.count("1") > column.count("0"):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)

# Part 2
def get_rating(switch=False):
    remaining_numbers = numbers.copy()
    number_of_bits = int(len(numbers[0]))
    for i in range(number_of_bits):
        if len(remaining_numbers) == 1:
            break
        columns = list(zip(*remaining_numbers))
        first_column = columns[i]
        target_number = "0"
        if switch:
            if first_column.count("0") > first_column.count("1"):
                target_number = "1"
        else:
            if first_column.count("1") >= first_column.count("0"):
                target_number = "1"
        new_remaining_numbers = []
        for number in remaining_numbers:
            if number[i] == target_number:
                new_remaining_numbers.append(number)
        remaining_numbers = new_remaining_numbers
    return remaining_numbers[0]

oxygen_rating = int(get_rating(), 2)
co2_rating = int(get_rating(switch=True), 2)
print(oxygen_rating * co2_rating)
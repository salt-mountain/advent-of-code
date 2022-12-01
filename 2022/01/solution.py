#!/usr/bin/env python3

with open("input.txt", "r") as file:
    elves = file.read().split("\n\n")

calorie_totals = list()

for elf in elves:
    calories = 0
    for calorie in elf.split():
        calories += int(calorie)
    calorie_totals.append(calories)

# Part 1
print("The Elf carrying the most calories is carrying {0} calories".format(str(max(calorie_totals))))

# Part 2
calorie_totals.sort(reverse = True)
print("The Top Three Elves are carrying {0} calories".format(sum(calorie_totals[:3])))

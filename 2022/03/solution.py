#!/usr/bin/env python3

with open("input.txt", "r") as file:
    lines = file.read().split("\n")
    
    priorities = 0
    
    # Create a map of letters and values
    lowercase = {chr(i): i - 96 for i in range(ord("a"), ord("a") + 26)}
    uppercase = {chr(i): i - 38 for i in range(ord("A"), ord("A") + 26)}
    values = {**lowercase, **uppercase}
    
    # Part 1
    for line in lines:
        first_half, second_half = line[:len(line)//2], line[len(line)//2:]
        common_letter = ''.join(set(first_half).intersection(second_half))
        priorities += int(values[common_letter])
    
    print(priorities)
    
    # Part 2
    priorities = 0
    for x in range(0,len(lines), 3):
        common_letter = ''.join(set(lines[x]).intersection(lines[x+1], lines[x+2]))
        priorities += int(values[common_letter])
    
    print(priorities)

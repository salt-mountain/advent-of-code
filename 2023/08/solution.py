#!/usr/bin/env python3

import math
import re

def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()

    instructions = list(lines[0].strip())
    nodes = { 
        x[1]: (x[2], x[3])
        for x in (re.match(r"([A-Z]{3})\s*=\s*\(([A-Z]{3}), ([A-Z]{3})\)", line) for line in lines[2:])
    }

    starting_node = "AAA"
    destination_node = "ZZZ"

    i = 0
    steps = 0

    while starting_node != destination_node:
        if i >= len(instructions):
            i = 0
        
        instruction = instructions[i]
        current_node = nodes[starting_node]
        starting_node = current_node[instruction == "R"]

        steps += 1
        i += 1
    
    # Part 1
    print(steps)

    # Part 2
    count = []

    for starting_node in [node for node in nodes if node.endswith("A")]:
        steps = 0
        i = 0

        while not starting_node.endswith("Z"):
            if i >= len(instructions):
                i = 0

            instruction = instructions[i]
            current_node = nodes[starting_node]
            starting_node = current_node[instruction == "R"]

            steps += 1
            i += 1

        count.append(steps)

    print(math.lcm(*count))

if __name__ == "__main__":

    main()

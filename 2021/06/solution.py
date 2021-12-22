#!/usr/bin/env python3

from collections import Counter

def part1(fishes):
    for day in range(80):
        for i, fish in enumerate(fishes):
            if fish == 0:
                fishes[i] = 7
                fishes.append(9)
        fishes = [fish - 1 for fish in fishes]
    print(len(fishes))

def part2(fishes):
    timers = Counter({timer: 0 for timer in range(10)})
    fishes = Counter(fishes)
    fishes.update(timers)

    for day in range(256):
        fishes[7] += fishes.get(0,0)
        fishes[9] += fishes.get(0,0)
        fishes = {fish: fishes.get(fish + 1, 0) for fish in fishes}

    print(sum(fishes.values()))

def main():
    with open("input.txt", "r") as f:
        fishes = f.read().strip().split(',')
        fishes = list(map(int, fishes))
    part1(fishes)
    part2(fishes)

if __name__ == "__main__":
    main()
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func main() {

	elves := make([][]int, 0)
	elf := make([]int, 0)
	calorie_totals := make([]int, 0)

	readFile, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer readFile.Close()

	fileScanner := bufio.NewScanner(readFile)

	// Create a list of lists for each elf and their calorie amounts

	for fileScanner.Scan() {
		s := fileScanner.Text()
		if s == "" {
			elves = append(elves, elf)
			elf = make([]int, 0)
		} else {
			calorie, err := strconv.Atoi(s)
			if err != nil {
				log.Fatal(err)
			}
			elf = append(elf, calorie)
		}
	}
	// Go through the elves and their calories and find the max
	// As well as creating a new list of calorie totals for Part 2
	largest := 0

	for _, elf := range elves {
		sum := 0
		for _, calorie := range elf {
			sum += calorie
		}
		// Keep a list of caloric sums
		calorie_totals = append(calorie_totals, sum)
		if sum > largest {
			largest = sum
		}
	}

	fmt.Println(largest)
	sort.Sort(sort.Reverse(sort.IntSlice(calorie_totals)))
	fmt.Println(calorie_totals[0] + calorie_totals[1] + calorie_totals[2])

}

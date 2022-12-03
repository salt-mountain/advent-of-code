package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {

	total := 0
	rigged_total := 0

	points := map[string]int{
		"AX": 4,
		"AY": 8,
		"AZ": 3,
		"BX": 1,
		"BY": 5,
		"BZ": 9,
		"CX": 7,
		"CY": 2,
		"CZ": 6,
	}

	rigged_points := map[string]int{
		"AX": 0 + 3,
		"AY": 3 + 1,
		"AZ": 6 + 2,
		"BX": 0 + 1,
		"BY": 3 + 2,
		"BZ": 6 + 3,
		"CX": 0 + 2,
		"CY": 3 + 3,
		"CZ": 6 + 1,
	}

	readFile, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	// Get all the Games in a list
	games := strings.Split(strings.ReplaceAll(string(readFile), " ", ""), "\n")

	for _, game := range games {
		total += points[game]
		rigged_total += rigged_points[game]
	}
	// Part 1
	fmt.Println(total)

	// Part 2
	fmt.Println(rigged_total)

}

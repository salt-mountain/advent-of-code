package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

var numberMap = map[string]int{
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
}

func main() {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Fields(string(file))

	// Part 1
	calibration_total := 0
	for _, line := range lines {
		var values []int
		for _, character := range line {
			// Check if the character is a number
			if character >= 48 && character <= 57 {
				// Subtracting the value of rune '0' from any rune '0' through '9' will give
				// you an integer 0 through 9. Resulting type is int32 (base type of runes).
				values = append(values, int(character)-'0')
			}
		}
		calibration_total += values[0]*10 + values[len(values)-1]
	}
	fmt.Println("Part 1:", calibration_total)

	// Part 2
	real_calibration_total := 0
	for _, line := range lines {
		var values []int
		real_number := ""

		for _, character := range line {
			// Using this to construct a word number
			real_number += string(character)

			// Same as in Part 1
			if character >= 48 && character <= 57 {
				values = append(values, int(character)-'0')
			}

			// Handle a word number
			// -- Every loop we're accumulating letters in real_number
			// -- We can determine we're at the end of a word by checking if
			//    the character we're at is the last letter of a word.
			if strings.Contains("eorxnt", string(character)) {
				// Lookup the number based on the word
				for value, number := range numberMap {
					if strings.HasSuffix(real_number, value) {
						values = append(values, number)
					}
				}
			}
		}
		real_calibration_total += values[0]*10 + values[len(values)-1]
		real_number = ""
	}
	fmt.Println("Part 2:", real_calibration_total)
}

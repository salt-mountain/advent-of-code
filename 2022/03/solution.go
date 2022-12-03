package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

// It seems like there's no built in way to compare
// two strings, so we have to write our own function
func commonLetter(str1 string, str2 string) string {
	// Store the first string and every letter we see as a set
	letters := make(map[rune]struct{})
	for _, letter := range str1 {
		letters[letter] = struct{}{}
	}

	// Go through the second string and check if the letters
	// exist in the first string.
	for _, letter := range str2 {
		if _, ok := letters[letter]; ok {
			return string(letter)
		}
	}

	// We should never hit this but return an empty
	// string if no letter was found
	return ""
}

// We need a function that will take a letter and
// find its corresponding "point" value

func characterPointValue(str string) int {
	// Get the letter that's being passed in
	letter := str[0]

	// Check if the character is lowercase or uppercase
	if letter >= 'a' && letter <= 'z' {
		return int(letter - 96)
	} else {
		return int(27 + letter - 65)
	}
}

func main() {

	priorities := 0

	readFile, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	// Get the lines
	lines := strings.Split(string(readFile), "\n")
	for _, line := range lines {
		halfway_point := len(line) / 2
		first_half := line[0:halfway_point]
		second_half := line[halfway_point:len(line)]
		common_letter := commonLetter(first_half, second_half)
		priorities += characterPointValue(common_letter)

	}
	// Part 1
	fmt.Println(priorities)

	// Part 2
	for i := 0; i < len(lines)-3; i += 3 {
		first_string := lines[i]
		second_string := lines[i+1]
		third_string := lines[i+2]
		one_and_two_match := commonLetter(first_string, second_string)
		fmt.Println("one and two match")
		fmt.Println(one_and_two_match)
		two_and_three_match := commonLetter(second_string, third_string)
		fmt.Println("two and three match")
		fmt.Println(two_and_three_match)
		fmt.Println()
	}

}

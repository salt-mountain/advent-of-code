const input = await Bun.file('input.txt').text()

let totalOutputJoltage = 0
let totalLargerOutputJoltage = 0

for (const line of input.split('\n')) {
    if (line.trim() === '') continue

    const joltageRatings: number[] = line.trim().split('').map(Number)
    const sortedRatings = joltageRatings.toSorted((a, b) => b - a)

    // Find where the largest battery is
    // If the battery is at the end of the array, it can't be the first value of the voltage
    // Grab the second highest battery and look at the remaining batteries in the array
    let largestJoltageIndex = joltageRatings.findIndex((rating) => rating === sortedRatings[0])
    if (largestJoltageIndex === joltageRatings.length - 1) {
        largestJoltageIndex = joltageRatings.findIndex((rating) => rating === sortedRatings[1])
    }

    const remainingRatings = joltageRatings.slice(largestJoltageIndex + 1)
    const remainingRatingsSorted = remainingRatings.toSorted((a, b) => b - a)

    totalOutputJoltage += (joltageRatings[largestJoltageIndex] * 10 ) + remainingRatingsSorted[0]

    // For Part 2, traverse the joltage ratings and remove the batteries that are smaller than
    // the next one. Do this until we've created a 12 length digit.
    while(joltageRatings.length > 12) {
        for(let index=0; index < joltageRatings.length; index++) {
            if(index === joltageRatings.length - 1) 
            {
                joltageRatings.splice(index, 1);
            }
            if(joltageRatings[index] <  joltageRatings[index + 1]) {
                joltageRatings.splice(index, 1);
                break;
            }
            if(joltageRatings.length <= 12) break;
        }
    }
    totalLargerOutputJoltage += Number(joltageRatings.join(''));
}

console.log(totalOutputJoltage)
console.log(totalLargerOutputJoltage)

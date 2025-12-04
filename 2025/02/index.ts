const input = await Bun.file('input.txt').text()

const repeatingPattern = /^([1-9]\d*)\1$/;
const repeatsAtLeastTwice = /^([1-9]\d*)\1+$/

let invalidSums = 0
let invalidSumsAtLeastTwice = 0

for (const line of input.split(',')) {
   const [lowerRange, upperRange] = line.split('-').map(Number)

   for (let id = lowerRange; id <= upperRange; id++) {
    const idString = id.toString()
    if (repeatingPattern.test(idString)) {
        invalidSums += id
    }
    if (repeatsAtLeastTwice.test(idString)) {
        invalidSumsAtLeastTwice += id
    }
   }
}

console.log(invalidSums)
console.log(invalidSumsAtLeastTwice)
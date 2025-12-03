import * as fs from 'fs';

// Stuck to TypeScript docs so I read it this way as opposed to
// using a nice Bun built in that I learned about after.
// Leaving this in to show learn progress.
const filePath: string = 'input.txt';
const content: string = fs.readFileSync(filePath, 'utf-8');
const lines: string[] = content.split(/\r?\n/);

let dial = 50;
let zeros = 0;
let clicks = 0;

for (const line of lines) {
    const direction = line.startsWith("R") ? 1 : -1;
    const turn = parseInt(line.slice(1));

    // Count how many times we cross 0 during this turn
    for (let i = 0; i < turn; i++) {
        dial = (dial + direction + 100) % 100;
        if (dial === 0) {
            clicks += 1;
        }
    }

    if (dial === 0) {
        zeros += 1;
    }
}

console.log(zeros);
console.log(clicks);
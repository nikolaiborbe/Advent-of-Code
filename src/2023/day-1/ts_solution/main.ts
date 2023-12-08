import { readFileSync } from 'fs';

let input = readFileSync('src/2023/day-1/ts_solution/input.txt', 'utf-8')
    .split('\r\n')
    .filter(x => !!x);

let sum: number = 0;
const numbers: string = "123456789";
const strNumbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

input.forEach(word => {
    let numbersInString: string[] = [];

    for (let i = 0; i < word.length; i++) {
        if (numbers.includes(word[i])) {
            numbersInString.push(word[i]);
        }

        if ()
    }

    sum += (parseInt(numbersInString[0]) * 10) + parseInt(numbersInString[numbersInString.length - 1])
})

console.log(sum)
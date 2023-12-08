import { readFileSync } from 'fs';
import { Games, gameScores } from './types';

let input = readFileSync('src/2023/day-2/input.txt', 'utf-8')
    .split('\r\n')
    .filter(x => !!x);

let games: Games = [];

// Game 83: 6 blue, 5 green; 2 green, 12 blue; 1 red, 2 green, 6 blue
//
// -> [ (id, [ (blue, green, red) ]) ]

input.forEach(line => {
    let gameIDstring: string = line.split(": ")[0];
    let gameID: number = parseInt(gameIDstring.split(" ")[1]);

    let gameInfo: string = line.split(": ")[1];
    let gameScores: string[] = gameInfo.split("; ");

    let scores: Games[] = [];
    gameScores.forEach(round => {
        let colorScoresStr = round.split(", ");
        console.log(colorScoresStr)
        
        // [ '14 green', '9 red', '9 blue' ]
        // 
        // [ '9 blue', '10 green', '8 red' ]
        colorScoresStr.forEach(color => {
            if (color.includes("blue")) {
                let index = colorScoresStr.indexOf(color);
                if ( index > -1 ) {
                    colorScoresStr.splice(index, 1);
                    colorScoresStr.unshift(color);
                }
            }
            else if (color.includes("green")) {
                let index = colorScoresStr.indexOf(color);
                if ( index > -1 ) {
                    colorScoresStr.splice(index, 1);
                    colorScoresStr.splice(1, 0, color);
                }
            }
            else if (color.includes("red")) {
                let index = colorScoresStr.indexOf(color);
                if ( index > -1 ) {
                    colorScoresStr.splice(index, 1);
                    colorScoresStr.splice(2, 0, color);
                }
            }
        
        
        let colorScores: number[] = [];
        /* colorScoresStr.forEach(color => {
            colorScores.push(parseInt(color.split(" ")[0]));
        }) */
        })
    })
})

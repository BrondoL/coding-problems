'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}


/*
 * Complete the 'isChild' function below.
 *
 * The function is expected to return a BOOLEAN.
 * The function accepts following parameters:
 *  1. STRING parentA
 *  2. STRING parentB
 *  3. STRING child
 */

const rules = {
    "AA": ["A", "O"],
    "AB": ["A", "B", "O", "AB"],
    "AO": ["A", "O"],
    "AAB": ["A", "B", "AB"],
    "BB": ["B", "O"],
    "BO": ["B", "O"],
    "BAB": ["A", "B", "AB"],
    "00": ["O"],
    "0AB": ["A", "B"],
    "ABAB": ["A", "B", "AB"],
}

function isChild(parentA, parentB, child) {
    let prob = rules[parentA.replace(/\s/g, '')+parentB.replace(/\s/g, '')] || rules[parentB.replace(/\s/g, '')+parentA.replace(/\s/g, '')];

    if (!prob || !prob.length) {
        return false
    }

    return prob.includes(child)
}
function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const parentA = readLine();

    const parentB = readLine();

    const child = readLine();

    const result = isChild(parentA, parentB, child);

    ws.write((result ? 1 : 0) + '\n');

    ws.end();
}

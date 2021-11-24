"use strict";

function mostWanted(data) {
    let mwl = {}
    let letter = new Set(data.toLowerCase().match(/[a-z]/gi))
    letter.forEach(x => mwl[x] = data.match(new RegExp(`${x}`, 'gi')).length)
    return Object.entries(mwl).reduce((x,y) => x[1] > y[1] ? x :
        x[1] == y[1] ? (x[0] < y[0] ? x : y) : y, 0)[0]
}

// console.log(mostWanted("Hello World!")) // 'l'
// console.log(mostWanted("How do you do?")) //'o'
// console.log(mostWanted("One")) // 'e'
// console.log(mostWanted("Oops!")) // 'o'
// console.log(mostWanted("AAaooo!!!!")) // 'a'

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(mostWanted("Hello World!"), "l", "1st example");
    assert.equal(mostWanted("How do you do?"), "o", "2nd example");
    assert.equal(mostWanted("One"), "e", "3rd example");
    assert.equal(mostWanted("Oops!"), "o", "4th example");
    assert.equal(mostWanted("AAaooo!!!!"), "a", "Letters");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}

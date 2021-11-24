"use strict";

function longRepeat(line) {
    let len = 0
    let letter = new Set(line.match(/[a-zA-Z]/g))
    letter.forEach( x => {
        let z = line.match(new RegExp('[' + `${x}` + ']+', 'g')).reduce((x, y) => x.length > y.length ? x : y).length
        z > len ? len = z : ''
    })
    return len
}

console.log(longRepeat('ddvvrwwwrggg'))
console.log(longRepeat("abababaab")) // 2


var assert = require('assert');

if (!global.is_checking) {
    assert.equal(longRepeat('sdsffffse'), 4, "First")
    assert.equal(longRepeat('ddvvrwwwrggg'), 3, "Second")
    console.log('"Run" is good. How is "Check"?');
}

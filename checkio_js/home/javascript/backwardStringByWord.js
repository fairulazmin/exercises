import assert from "assert";

function backwardStringByWord(text) {
    return text.split(' ').map(a => a.split('').reverse().join('')).join(' ')
}

console.log('Example:');
console.log(backwardStringByWord(''));

// These "asserts" are used for self-checking
assert.equal(backwardStringByWord(''), '');
assert.equal(backwardStringByWord('world'), 'dlrow');
assert.equal(backwardStringByWord('hello world'), 'olleh dlrow');
assert.equal(backwardStringByWord('hello   world'), 'olleh   dlrow');
assert.equal(backwardStringByWord('welcome to a game'), 'emoclew ot a emag');

console.log("Coding complete? Click 'Check' to earn cool rewards!");

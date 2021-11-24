import assert from "assert";

function wordsOrder(text, words) {
    let text2 = text.split(' ')
    let arr = []
    text2.forEach(a => words.includes(a) ? arr.push(a) : 0)
    return new Set(arr).size === words.length && words.toString() == arr.toString()
}

console.log('Example:');
console.log(wordsOrder('hi world im here', ['world', 'here']));

// These "asserts" are used for self-checking
assert.equal(wordsOrder('hi world im here', ['world', 'here']), true);
assert.equal(wordsOrder('hi world im here', ['here', 'world']), false);
assert.equal(wordsOrder('hi world im here', ['world']), true);
assert.equal(wordsOrder('hi world im here',
 ['world', 'here', 'hi']), false);
assert.equal(wordsOrder('hi world im here',
 ['world', 'im', 'here']), true);
assert.equal(wordsOrder('hi world im here',
 ['world', 'hi', 'here']), false);
assert.equal(wordsOrder('hi world im here', ['world', 'world']), false);
assert.equal(wordsOrder('hi world im here',
 ['country', 'world']), false);
assert.equal(wordsOrder('hi world im here', ['wo', 'rld']), false);
assert.equal(wordsOrder('', ['world', 'here']), false);
assert.equal(wordsOrder('hi world world im here',
 ['world', 'world']), false);

console.log("Coding complete? Click 'Check' to earn cool rewards!");

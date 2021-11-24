function firstWord(a, b) {
    a = a.replace(/^[., ]+/, '')
    a = a.replace(/[., ]+$/, '')
    a = a.replace(/[.,]+/, '')
    return a.split(' ')[0]
}

// return data.match(/[\w']+/)[0]

var assert = require('assert');
if (!global.is_checking) {
    console.log('Example:')
    console.log(firstWord("Hello world"))

    // These "asserts" using for self-checking and not for auto-testing
    assert.equal(firstWord("Hello world"), "Hello")
    assert.equal(firstWord(" a word "), "a")
    assert.equal(firstWord("don't touch it"), "don't")
    assert.equal(firstWord("greetings, friends"), "greetings")
    assert.equal(firstWord("... and so on ..."), "and")
    assert.equal(firstWord("hi"), "hi")
    console.log("Coding complete? Click 'Check' to earn cool rewards!");
}

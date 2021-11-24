import assert from "assert";

function secondIndex(text, symbol) {
    if (text.indexOf(symbol, text.indexOf(symbol) + 1) != -1){
        return text.indexOf(symbol, text.indexOf(symbol) + 1)
    } else {
        return undefined
    }
}


console.log('Example')
console.log(secondIndex("sims", "s"))

// These "asserts" are used for self-checking and not for an auto-testing
assert.equal(secondIndex("sims", "s"), 3)
assert.equal(secondIndex("find the river", "e"), 12)
assert.equal(secondIndex("hi", " "), undefined)
assert.equal(secondIndex("hi mayor", " "), undefined)
assert.equal(secondIndex("hi mr Mayor", " "), 5)
console.log("You are awesome! All tests are done! Go Check it!");

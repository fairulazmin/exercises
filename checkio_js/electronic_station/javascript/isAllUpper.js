import assert from "assert";

function isAllUpper(text) {
    return text.match(/[a-zA-Z]/) ? text === text.toUpperCase() : false
}

console.log('Example:');
console.log(isAllUpper('ALL UPPER'));

// These "asserts" are used for self-checking
assert.equal(isAllUpper('ALL UPPER'), true);
assert.equal(isAllUpper('all lower'), false);
assert.equal(isAllUpper('mixed UPPER and lower'), false);
assert.equal(isAllUpper(''), false);
assert.equal(isAllUpper("     "), false);

console.log("Coding complete? Click 'Check' to earn cool rewards!");

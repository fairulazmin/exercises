import assert from "assert";

function splitPairs(text) {
    let arr = []
    for (let i=0; i<text.length; i+=2){
      if (text.substr(i, 2).length < 2) {
        arr.push(text.substr(i, 2) + '_')
      } else {
        arr.push(text.substr(i, 2))
      }
    }
    return arr;
}

console.log('Example:');
console.log(splitPairs('abcd'));

// These "asserts" are used for self-checking
assert.deepEqual(splitPairs('abcd'), ['ab', 'cd']);
assert.deepEqual(splitPairs('abc'), ['ab', 'c_']);
assert.deepEqual(splitPairs('abcdf'), ['ab', 'cd', 'f_']);
assert.deepEqual(splitPairs('a'), ['a_']);
assert.deepEqual(splitPairs(''), []);

console.log("Coding complete? Click 'Check' to earn cool rewards!");

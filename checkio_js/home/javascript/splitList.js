import assert from "assert";

function splitList(values) {
    let mid = Math.ceil(values.length / 2)
    let end = values.length
    return [values.slice(0, mid), values.slice(mid, end)];
}

console.log('Example:');
console.log(splitList([1, 2, 3, 4, 5, 6]));

// These "asserts" are used for self-checking
assert.deepEqual(splitList([1, 2, 3, 4, 5, 6]), [[1, 2, 3], [4, 5, 6]]);
assert.deepEqual(splitList([1, 2, 3]), [[1, 2], [3]]);
assert.deepEqual(splitList([1, 2, 3, 4, 5]), [[1, 2, 3], [4, 5]]);
assert.deepEqual(splitList([1]), [[1], []]);
assert.deepEqual(splitList([]), [[], []]);

console.log("Coding complete? Click 'Check' to earn cool rewards!");

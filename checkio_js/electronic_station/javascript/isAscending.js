import assert from "assert";

function isAscending(values) {
    for (let i = 0; i<=values.length; i++){
        if (values[i] > values[i+1]){
            return false
        }
    }

    return values.length <= 1 ? true :
        new Set(values).size === 1 ? false :
        true
}

console.log('Example:');
console.log(isAscending([-5, 10, 99, 123456]));

// These "asserts" are used for self-checking
assert.equal(isAscending([-5, 10, 99, 123456]), true);
assert.equal(isAscending([99]), true);
assert.equal(isAscending([4, 5, 6, 7, 3, 7, 9]), false);
assert.equal(isAscending([]), true);
assert.equal(isAscending([1, 1, 1, 1]), false);
assert.equal(isAscending([-1, 0, 1]), true);

console.log("Coding complete? Click 'Check' to earn cool rewards!");

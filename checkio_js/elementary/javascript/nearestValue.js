import assert from "assert";

function nearestValue(values, search) {
    values.push(search)
    values.sort((a,b) => a-b)
    let idx = values.indexOf(search)
    if (idx == 0) {
        return values[1]
    } else if (values.length == idx + 1) {
        return values[values.length - 2]
    } else if ((values[idx + 1] - search) < (search - values[idx - 1])) {
        return values[idx + 1]
    } else {
        return values[idx - 1]
    }
}

console.log('Example:');
console.log(nearestValue([4, 7, 10, 11, 12, 17], 9));

// These "asserts" are used for self-checking
assert.equal(nearestValue([4, 7, 10, 11, 12, 17], 9), 10);
assert.equal(nearestValue([4, 7, 10, 11, 12, 17], 8), 7);
assert.equal(nearestValue([4, 8, 10, 11, 12, 17], 9), 8);
assert.equal(nearestValue([4, 9, 10, 11, 12, 17], 9), 9);
assert.equal(nearestValue([4, 7, 10, 11, 12, 17], 0), 4);
assert.equal(nearestValue([4, 7, 10, 11, 12, 17], 100), 17);
assert.equal(nearestValue([5, 10, 8, 12, 89, 100], 7), 8);
assert.equal(nearestValue([-1, 2, 3], 0), -1);

console.log("Coding complete? Click 'Check' to earn cool rewards!");

import assert from "assert";

function frequencySort(items) {
    let set_arr = []
    items.forEach(a => set_arr.includes(a) ? 0 : set_arr.push(a))
    let arr = []
    set_arr.forEach(a => arr.includes(a) ? 0 : arr.push(Array(items.filter(b => b == a).length).fill(a)))
    arr.sort((a, b) => b.length - a.length)
    let final_arr = []
    arr.forEach(a => final_arr.push(...a))
    return final_arr
    /**
    let arr = []
    items.forEach(a => arr.includes(a)? 0 : arr.push(a))
    let sorted = []
    arr.forEach(a => sorted.push(...items.filter(b => b === a)))
    return sorted
    **/
}

console.log('Example:');
console.log(frequencySort([4, 6, 2, 2, 6, 4, 4, 4]));

// These "asserts" are used for self-checking and not for an auto-testing
assert.deepEqual(frequencySort([4, 6, 2, 2, 6, 4, 4, 4]), [4, 4, 4, 4, 6, 6, 2, 2]);
assert.deepEqual(frequencySort(['bob', 'bob', 'carl', 'alex', 'bob']), ['bob', 'bob', 'bob', 'carl', 'alex']);
assert.deepEqual(frequencySort([17, 99, 42]), [17, 99, 42]);
assert.deepEqual(frequencySort([]), []);
assert.deepEqual(frequencySort([1]), [1]);
assert.deepEqual(frequencySort([4,6,2,2,2,6,4,4,4]), [4,4,4,4,2,2,2,6,6]);

console.log("Coding complete? Click 'Check' to earn cool rewards!");

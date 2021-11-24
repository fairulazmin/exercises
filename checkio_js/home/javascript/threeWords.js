import assert from "assert";

function threeWords(text) {
    let count = 0
    let arr = text.split(' ').map(a => isNaN(a))
    for (let i=0; i<arr.length; i++){
        if (arr[i]){
            count++
            if (count == 3){
                return true
            }
        } else {
            count = 0
        }
    }
    return false
}

console.log('Example:')
console.log(threeWords("Hello World hello"))

assert.equal(threeWords("Hello World hello"), true);
assert.equal(threeWords("He is 123 man"), false);
assert.equal(threeWords("1 2 3 4"), false);
assert.equal(threeWords("bla bla bla bla"), true);
assert.equal(threeWords("Hi"), false);
assert.equal(threeWords("start 5 one two three 7 end"), true);
console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");

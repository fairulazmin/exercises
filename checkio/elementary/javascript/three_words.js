/*
let words = 0
for (let word of data.split(/\s/ig)) {
    words = isNaN(word) ? ++words : 0
    if (words === 3) return true
}
return false
*/


function threeWords(data) {
    var count = 0
    var inspect = data.split(' ').map(a => a.match(/^\d+$/) == null)
    var result = false

    inspect.forEach((item) => {
        if (item == true){
            count++
            if (count == 3){
                result = true
            }
        } else {
            count = 0
        }
    });
    return result
}


var assert = require('assert');

if (!global.is_checking) {
    assert.equal(threeWords("Hello World hello"), true, "1st example");
    assert.equal(threeWords("He is 123 man"), false, "2nd example");
    assert.equal(threeWords("1 2 3 4"), false, "3rd example");
    assert.equal(threeWords("bla bla bla bla"), true, "4th example");
    assert.equal(threeWords("Hi"), false, "Letters");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}

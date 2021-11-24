function easyUnpack(elements) {
    var first = elements[0]
    var third = elements[2]
    var scdLast = elements[elements.length - 2]
    return [first, third, scdLast]
    // return [...elements.slice(0,2)], [...elements[elements.length - 1]];
}

// console.log(easyUnpack([1, 2, 3, 4, 5, 6, 7, 9]))

var assert = require('assert');

if (!global.is_checking) {
    console.log('Examples:')
    console.log(easyUnpack([1, 2, 3, 4, 5, 6, 7, 9]))

    assert.deepEqual(easyUnpack([1, 2, 3, 4, 5, 6, 7, 9]), [1, 3, 7])
    assert.deepEqual(easyUnpack([1, 1, 1, 1]), [1, 1, 1])
    assert.deepEqual(easyUnpack([6, 3, 7]), [6, 7, 3])
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}

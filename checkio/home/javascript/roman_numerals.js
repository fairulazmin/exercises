"use strict";

function romanNumerals(number) {

    let num = ''

    if (number >= 1000){
        num += 'M'.repeat(number / 1000)
        number %= 1000
    }

    if (number >= 900){
        num += 'CM'
        number -= 900
    }

    if (number >= 500){
        num += 'D'.repeat(number / 500)
        number %= 500
    }

    if (number >= 400){
        num += 'CD'
        number -= 400
    }

    if (number >= 100){
        num += 'C'.repeat(number / 100)
        number %= 100
    }

    if (number >= 90){
        num += 'XC'
        number -= 90
    }

    if (number >= 50){
        num += 'L'.repeat(number / 50)
        number %= 50
    }

    if (number >= 40){
        num += 'XL'
        number -= 40
    }

    if (number >= 10){
        num += 'X'.repeat(number / 10)
        number %= 10
    }

    if (number >= 9){
        num += 'IX'
        number -= 9
    }

    if (number >= 5){
        num += 'V'.repeat(number / 5)
        number %= 5
    }

    if (number >= 4){
        num += 'IV'
        number -= 4
    }

    num += 'I'.repeat(number)
    return num
}

// console.log(romanNumerals(9))
// console.log(romanNumerals(6))
console.log(romanNumerals(499))  // CDXCIX
console.log(romanNumerals(1))
console.log(romanNumerals(579))

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(romanNumerals(6), 'VI', "First");
    assert.equal(romanNumerals(76), 'LXXVI', "Second");
    assert.equal(romanNumerals(499), 'CDXCIX', "Third");
    assert.equal(romanNumerals(3888), 'MMMDCCCLXXXVIII', "Forth");
    console.log("Done! Go Check!");
}

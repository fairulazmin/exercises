function numberRadix(str_number, radix){

    if (radix <= 10){
        var re = new RegExp("[^0-" + radix + "]", "i")
    }else {
        var re = new RegExp("[^0-9A-" + String.fromCharCode(54 + radix) + "]", "i")
    }


    if (str_number.match(re) != null){
        return -1
    } else if (parseInt(str_number, radix)){
        return parseInt(str_number, radix)
    } else{
        return -1
    }
}

// var numberRadix = (s, r) => parseInt([...s].sort().pop(), r) ? parseInt(s, r) : -1;

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(numberRadix("AF", 16), 175, "Hex");
    assert.equal(numberRadix("101", 2), 5, "Bin");
    assert.equal(numberRadix("101", 5), 26, "5 base");
    assert.equal(numberRadix("Z", 36), 35, "Z base");
    assert.equal(numberRadix("AB", 10), -1, "B > A > 10");
    assert.equal(numberRadix("ASD", 15), -1, "Exceed E");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}

"use strict";

function weakPoint(matrix){
    let row = []
    matrix.forEach(x => row.push(x.reduce((a,b) => a + b)))
    let idx_row = row.indexOf(Math.min(...row))

    let col = []
    for (let x of matrix){
        for (let y=0; y<x.length; y++){
            col[y] = (col[y] || 0) + x[y]
            // col[y] = (col[y] == undefined ? x[y] : col[y] + x[y])
            }
    }
    let idx_col = col.indexOf(Math.min(...col))
    return [idx_row, idx_col]
}

var assert = require('assert');

if (!global.is_checking) {
    assert.deepEqual(weakPoint([[7, 2, 7, 2, 8],
                                [2, 9, 4, 1, 7],
                                [3, 8, 6, 2, 4],
                                [2, 5, 2, 9, 1],
                                [6, 6, 5, 4, 5]]
                                ), [3, 3], "Example");
    assert.deepEqual(weakPoint([[7, 2, 4, 2, 8],
                                [2, 8, 1, 1, 7],
                                [3, 8, 6, 2, 4],
                                [2, 5, 2, 9, 1],
                                [6, 6, 5, 4, 5]]
                                ), [1, 2], "Two weak point");

    assert.deepEqual(weakPoint([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]]
                                ), [0, 0], "Top left");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}

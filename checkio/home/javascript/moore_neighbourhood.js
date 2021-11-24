
function countNeighbours(data, row, col) {
    let count = 0
    let neighbour = []

    for (let i=-1; i<2; i++){
        for (let j=-1; j<2; j++){
            if (i != 0 || j != 0){
                neighbour.push([i,j])
            }
        }
    }
    let ok = neighbour.filter(coord => data[coord[0] + row] != undefined)
    ok.forEach(coord => data[coord[0] + row][coord[1] + col] == undefined ? '' :
                               data[coord[0] + row][coord[1] + col] == 1 ? count++ : '')
    return count
}

/*
var counter = 0;
for (var i = row - 1; i < row + 2; i++) {
    for (var j = col - 1; j < col + 2; j++) {
        if (data[i] !== undefined && data[i][j] !== undefined) {
            counter += data[i][j];
        }
    }
}
counter -= data[row][col];
return counter;
*/

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(countNeighbours([[1, 0, 0, 1, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 1],
                                  [1, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0]], 1, 2), 3, "1st example");

    assert.equal(countNeighbours([[1, 0, 0, 1, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 1],
                                  [1, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0]], 0, 0), 1, "2nd example");

    assert.equal(countNeighbours([[1, 1, 1],
                                  [1, 1, 1],
                                  [1, 1, 1]], 0, 2), 3, "Dense corner");

    assert.equal(countNeighbours([[0, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, 0]], 1, 1), 0, "Single");

    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}

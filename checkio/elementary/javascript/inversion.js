function isEqual(arr1, arr2){
    for (let i = 0; i < arr1.length; i++){
        if (arr1[i] != arr2[i]){
            return true
        }
    }
    return false
}

function countInversion(sequence){
    var count = 0
    var sortedArr = [...sequence]
    sortedArr.sort((a,b) => a - b)

    while (isEqual(sequence, sortedArr)) {
        for (let i = 0; i<sequence.length - 1; i++){
            if (sequence[i] > sequence[i + 1]){
                var temp = sequence[i]
                sequence[i] = sequence[i + 1]
                sequence[i + 1] = temp
                count++
            }
        }
    }
    return count
}

console.log(countInversion([1, 2, 5, 3, 4, 7, 6]))  // 3, "Example"
console.log(countInversion([0, 1, 2, 3]))           // 0, "Sorted"
console.log(countInversion([99, -99]))              // 1, "Two numbers"
console.log(countInversion([5, 3, 2, 1, 0]))        // 10, "Reversed"

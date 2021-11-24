function median(arr){
    arr = arr.sort(function(a, b){return a - b});
    console.log(arr);
    if (arr.length % 2 == 1){
        return arr[Math.floor(arr.length / 2)]
    }
    else {
        var idx = arr.length / 2;
        console.log(arr[idx - 1] + ' ' + arr[idx]);
        return (arr[idx - 1] + arr[idx]) / 2;
    }
}


// console.log(median([1, 2, 3, 4, 5]))         // == 3
// console.log(median([3, 1, 2, 5, 3]))         // == 3
// console.log(median([1, 300, 2, 200, 1]))     // == 2
console.log(median([3, 6, 20, 99, 10, 15]))  // == 12.5

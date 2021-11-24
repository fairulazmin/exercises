function evenLast(data) {
    var sum = 0
    if (data.length == 0) return 0

    for (let i = 0; i < data.length; i+=2){
        sum += data[i]
    }
    var x = data.pop()
    return sum * x
}

console.log(evenLast([0, 1, 2, 3, 4, 5]))  // 30, "(0+2+4)*5=30");
console.log(evenLast([1, 3, 5]))           // 30, "(1+5)*5=30");
console.log(evenLast([6]))                 // 36, "(6)*6=36");
console.log(evenLast([]))                  // 0, "An empty array = 0");

function digitsMultip(data) {
    var num
    while (data > 0) {
        if (data % 10 != 0){
            if (num == undefined){
                num = data % 10
            } else {
                num *= data % 10
            }
        }
        data = Math.floor(data / 10)
    }
    return num
}


console.log(digitsMultip(123405))   // 120
console.log(digitsMultip(999))      // 729
console.log(digitsMultip(1000))     // 1
console.log(digitsMultip(1111))     // 1

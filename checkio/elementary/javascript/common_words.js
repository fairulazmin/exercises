function commonWords(first, second) {
    first = first.split(',')
    second = second.split(',')
    var third = []
    for (let i=0; i<first.length; i++){
        for (let j=0; j<second.length; j++){
            if (first[i] == second[j]) {
                third.push(first[i])
            }
        }
    }
    return third.sort().toString()
}

// return first.split(',').filter((a) => second.split(',').filter((b) => a === b) == a).sort().toString()

console.log(commonWords("hello,world", "hello,earth"))                  // "hello", "Hello");
console.log(commonWords("one,two,three", "four,five,six"))              // "", "Too different");
console.log(commonWords("one,two,three", "four,five,one,two,six,three"))// "one,three,two", "1 2 3");

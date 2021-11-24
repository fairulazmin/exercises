function secondIndex(text, symbol) {
    var count = 0
    for (let i = 0; i < text.length; i++){
        if (text[i] === symbol){
            count++
            if (count == 2){
                return i
            }
        }
    }
    return undefined
}

console.log(secondIndex("sims", "s"))           // 3
console.log(secondIndex("find the river", "e")) // 12
console.log(secondIndex("hi", " "))             // undefined
console.log(secondIndex("hi mayor", " "))       // undefined
console.log(secondIndex("hi mr Mayor", " "))    // 5

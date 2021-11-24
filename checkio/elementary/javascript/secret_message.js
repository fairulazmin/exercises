
function findMessage(data) {
    var regex = /[A-Z]/g
    var str = ''
    var idx

    while (data.search(regex) != -1){
        idx = data.search(regex)
        str += data[idx]
        data = data.slice(idx + 1)
    }
    return str
}

// var findMessage = data => data.replace(/[^A-Z]/g, '');


console.log(findMessage("How are you? Eh, ok. Low or Lower? Ohhh."))// "HELLO"
console.log(findMessage("hello world!"))                            // ""
console.log(findMessage("HELLO WORLD!!!"))                          // "HELLOWORLD"

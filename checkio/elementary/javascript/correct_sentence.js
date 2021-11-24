function correctSentence(text) {
    text = text[0].toUpperCase() + (text.slice(1))
    // var text = text[0].toUpperCase().concat(text.slice(1))

    if (text.search(/[.]$/g) == -1){
        text += '.'
    }
    return text
}

    // return text[0].toUpperCase() + text.replace(/\.?$/, '.').slice(1);


console.log(correctSentence("greetings, friends"))  // "Greetings, friends."
console.log(correctSentence("Greetings, friends"))  // "Greetings, friends."
console.log(correctSentence("Greetings, friends.")) // "Greetings, friends."
console.log(correctSentence("hi"))                  // "Hi."
console.log(correctSentence("welcome to New York")) // "Welcome to New York."

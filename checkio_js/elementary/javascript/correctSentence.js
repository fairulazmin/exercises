import assert from "assert";

function correctSentence(text) {
    if (text.match(/^[a-z]/) != null){
        text = text[0].toUpperCase() + text.substring(1)
    }
    if (text.match(/[.]$/) == null){
        text += '.'
    }
    return text;
}

console.log('Example:');
console.log(correctSentence('greetings, friends'));

// These "asserts" are used for self-checking
assert.equal(correctSentence('greetings, friends'), 'Greetings, friends.');
assert.equal(correctSentence('Greetings, friends'), 'Greetings, friends.');
assert.equal(correctSentence('Greetings, friends.'), 'Greetings, friends.');

console.log("Coding complete? Click 'Check' to earn cool rewards!");

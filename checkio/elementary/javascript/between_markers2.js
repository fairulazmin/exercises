function betweenMarkers(text, begin, end) {
    return text.slice((text.indexOf(begin) >= 0)? (text.indexOf(begin) + begin.length):0 ,
        (text.indexOf(end) >= 0)? text.indexOf(end): text.length)
}


// console.log(betweenMarkers('No [b]hi', '[b]', '[/b]'))
// console.log(betweenMarkers('What is >apple<', '>', '<'))
// console.log(betweenMarkers("<head><title>My new site</title></head>",
//                             "<title>", "</title>"))
// console.log(betweenMarkers('No[/b] hi', '[b]', '[/b]'))




var assert = require('assert');

if (!global.is_checking) {
    console.log('Example:')
    console.log(betweenMarkers('What is >apple<', '>', '<'), 'apple')

    assert.equal(betweenMarkers('What is >apple<', '>', '<'), 'apple')
    assert.equal(betweenMarkers("<head><title>My new site</title></head>",
                                "<title>", "</title>"), 'My new site')
    assert.equal(betweenMarkers('No[/b] hi', '[b]', '[/b]'), 'No')
    assert.equal(betweenMarkers('No [b]hi', '[b]', '[/b]'), 'hi')
    assert.equal(betweenMarkers('No hi', '[b]', '[/b]'), 'No hi')
    assert.equal(betweenMarkers('No <hi>', '>', '<'), '')
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}

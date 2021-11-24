import assert from "assert";

function betweenMarkers(text, begin, end) {
    let first, last
    text.includes(begin) ? first = text.indexOf(begin) + begin.length : first = 0
    text.includes(end) ? last = text.indexOf(end) : last = text.length
    return text.slice(first, last)
}

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

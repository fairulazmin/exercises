"use strict";

function popularWords(text, words) {
    return words.reduce((k,v) => (k[v] = text.match(RegExp(`(\\b${v}\\b)`, "gi"))?.length || 0, k), {})
    // let popular = {}
    /**
    words.map(a => popular[a] = text.match(RegExp(`\\b${a}\\b`, 'gi')) == null ?
        0 : text.match(new RegExp(`\\b${a}\\b`, 'gi')).length)
    **/
    // words.map(a => popular[a] = text.match(RegExp(`\\b${a}\\b`, 'gi'))?.length || 0)
    // return popular
}
// return words.reduce((k,v) => (k[v] = text.match(RegExp(`(\\b${v}\\b)`, "gi"))?.length || 0, k), {})

console.log('Example:')
console.log(popularWords(`
When I was One
I had just begun
When I was Two
I was nearly new`, ['i', 'was', 'three', 'near']))

import assert from "assert";

function sortByExt(files) {
    return files.sort((a,b) => a.match(/[.](\w+)/i)[1] < b.match(/[.](\w+)/i)[1] ? -1 : a.match(/[.](\w+)/i)[1] > b.match(/[.](\w+)/i)[1] ? 1 : 0)
}

console.log('Example:');
console.log(sortByExt(['1.cad', '1.bat', '1.aa']));

// These "asserts" are used for self-checking
assert.deepEqual(sortByExt(['1.cad', '1.bat', '1.aa']), ['1.aa', '1.bat', '1.cad']);
assert.deepEqual(sortByExt(['1.cad', '1.bat', '1.aa', '2.bat']), ['1.aa', '1.bat', '2.bat', '1.cad']);
assert.deepEqual(sortByExt(['1.cad', '1.bat', '1.aa', '.bat']), ['.bat', '1.aa', '1.bat', '1.cad']);
assert.deepEqual(sortByExt(['1.cad', '1.bat', '.aa', '.bat']), ['.aa', '.bat', '1.bat', '1.cad']);
assert.deepEqual(sortByExt(['1.cad', '1.', '1.aa']), ['1.', '1.aa', '1.cad']);
assert.deepEqual(sortByExt(['1.cad', '1.bat', '1.aa', '1.aa.doc']), ['1.aa', '1.bat', '1.cad', '1.aa.doc']);
assert.deepEqual(sortByExt(['1.cad', '1.bat', '1.aa', '.aa.doc']), ['1.aa', '1.bat', '1.cad', '.aa.doc']);

console.log("Coding complete? Click 'Check' to earn cool rewards!");

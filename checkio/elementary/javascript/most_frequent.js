function mostFrequent(data) {
    var strData = data.toString()
    var setData = new Set(data)
    var count = 0
    var maxLetter
    setData.forEach((item, i) => {
        var re = new RegExp(item, "g")
        if (strData.match(re).length > count){
            maxLetter = item
            count = strData.match(re).length
        }
    });
    return maxLetter
}

// return data.sort((a,b) => data.filter(v => v===a).length - data.filter(v => v===b).length).pop();

    console.log(mostFrequent([
            'a', 'b', 'c', 'a',
            'a', 'b',
            'a'
        ]))

    console.log(mostFrequent(['a', 'a', 'bi', 'bi', 'bi']))

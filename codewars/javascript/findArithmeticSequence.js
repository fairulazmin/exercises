const findArithmeticSequence = (lst) => {
  const len = lst.length;

  for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
      for (let k = j + 1; k < len; k++) {
        const arr = [lst[i], lst[j], lst[k]];
        arr.sort((a, b) => a - b);
        if (arr[1] - arr[0] === arr[2] - arr[1]) return arr;
      }
    }
  }

  return [];
};

console.log(findArithmeticSequence([99, 11, 4, 7, 9, 1])); //[7,9,11]
console.log(findArithmeticSequence([13, 20, 17, 9, 27])); //[7,9,11]
console.log(findArithmeticSequence([])); //[]

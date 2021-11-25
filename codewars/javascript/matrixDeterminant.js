const sum = (arr) => {
  const length = arr.length;
  if (length === 1) {
    return arr[0];
  } else if (length === 4) {
    return arr[0] * arr[3] - arr[1] * arr[2];
  } else {
    let total = 0;
    const len = Math.sqrt(length);
    let temp = arr.slice(len);
    let operation = 1;
    for (let i = 0; i < len; i++) {
      temp = [...arr.slice(len)];
      for (let j = i + len * (len - 2); j >= 0; j = j - len) {
        temp.splice(j, 1);
      }
      total = total + operation * arr[i] * sum(temp);
      operation = operation * -1;
    }
    return total;
  }
};

const determinant = (m) => {
  return sum(m.reduce((a, b) => [...a, ...b]));
};

console.log(determinant([[1]]));
console.log(
  determinant([
    [1, 3],
    [2, 5],
  ])
);
console.log(
  determinant([
    [2, 5, 3],
    [1, -2, -1],
    [1, 3, 4],
  ])
);

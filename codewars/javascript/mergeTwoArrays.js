const mergeArrays = (a, b) => {
  let index = 0;
  const arr = [];

  while (a[index] || b[index]) {
    a[index] && arr.push(a[index]);
    b[index] && arr.push(b[index]);

    index++;
  }
  return arr;
};

console.log(mergeArrays(["a", "b", "c"], [1, 2, 3, 4, 5, 6, 7]));

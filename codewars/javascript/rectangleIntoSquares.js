const getRect = (x, y) => {
  return x === y
    ? [x]
    : x > y
    ? [y, ...getRect(x - y, y)]
    : [x, ...getRect(x, y - x)];
};

const sqInRect = (x, y) => {
  if (x === y) return null;

  return getRect(x, y);
};

const tests = [
  { input: [5, 5], output: null },
  { input: [5, 3], output: [3, 2, 1, 1] },
  { input: [3, 5], output: [3, 2, 1, 1] },
  { input: [20, 14], output: [14, 6, 6, 2, 2, 2] },
];

tests.map((test) => {
  console.log(sqInRect(...test.input));
});

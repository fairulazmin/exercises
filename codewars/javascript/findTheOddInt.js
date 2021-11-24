const findOdd = (A) => {
  const num = {};

  for (let i of A) {
    num[i] = (num[i] || 0) + 1;
  }

  for (const i in num) {
    if (num[i] % 2 === 1) {
      return parseInt(i);
    }
  }
};

tests = [
  { input: [7], output: 7 },
  { input: [0], output: 0 },
  { input: [1, 1, 2], output: 2 },
  { input: [0, 1, 0, 1, 0], output: 0 },
  {
    input: [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5],
    output: 5,
  },
  {
    input: [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5],
    output: 5,
  },
  {
    input: [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5],
    output: 5,
  },
  { input: [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5], output: -1 },
  { input: [20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5], output: 5 },
  { input: [10], output: 10 },
  { input: [1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1], output: 10 },
  { input: [5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10], output: 1 },
];

tests.map((test) => {
  console.assert(
    findOdd(test.input) === test.output,
    `${findOdd(test.input)} should be ${test.output}`
  );
});

const sum = (num) => {
  return num < 1 ? 0 : num + sum(num - 1);
};

const rowSumOddNumbers = (n) => {
  return (sum(n - 1) * 2 + 1) * n + sum(n - 1) * 2;
};

console.assert(
  rowSumOddNumbers(1) === 1,
  `Expected ${rowSumOddNumbers(1)} to equal 1`
);
console.assert(
  rowSumOddNumbers(42) === 74088,
  `Expected ${rowSumOddNumbers(42)} to equal 74088`
);

//best answer = Math.pow(n, 3)

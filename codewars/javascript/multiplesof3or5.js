const factorial = (n) => {
  return n < 2 ? 1 : n + factorial(n - 1);
};

const sum = (ceil, num) => {
  return num * factorial(parseInt(ceil / num));
};

findSum = (n) => {
  return sum(n, 5) + sum(n, 3) - (n > 5 * 3 ? sum(n, 5 * 3) : 0);
};

console.assert(findSum(5) === 8, `expected findSum(5) = 8 not ${findSum(5)}`);
console.assert(
  findSum(10) === 33,
  `expected findSum(10) = 33 not ${findSum(10)}`
);
console.assert(
  findSum(-7) === 8,
  `expected findSum(-7) = 8 not ${findSum(-7)}`
);

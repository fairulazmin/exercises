const zero = (x) => (x ? parseInt(eval(`0${x}`)) : "0");
const one = (x) => (x ? parseInt(eval(`1${x}`)) : "1");
const two = (x) => (x ? parseInt(eval(`2${x}`)) : "2");
const three = (x) => (x ? parseInt(eval(`3${x}`)) : "3");
const four = (x) => (x ? parseInt(eval(`4${x}`)) : "4");
const five = (x) => (x ? parseInt(eval(`5${x}`)) : "5");
const six = (x) => (x ? parseInt(eval(`6${x}`)) : "6");
const seven = (x) => (x ? parseInt(eval(`7${x}`)) : "7");
const eight = (x) => (x ? parseInt(eval(`8${x}`)) : "8");
const nine = (x) => (x ? parseInt(eval(`9${x}`)) : "9");

const times = (x) => `*${x}`;
const plus = (x) => `+${x}`;
const minus = (x) => `-${x}`;
const dividedBy = (x) => `/${x}`;

console.assert(
  seven(times(five())) === 35,
  `Expected: 35, instead got: ${seven(times(five()))}`
);
console.assert(
  four(plus(nine())) === 13,
  `Expected: 13, instead got: ${four(plus(nine()))}`
);
console.assert(
  eight(minus(three())) === 5,
  `Expected: 5, instead got: ${eight(minus(three()))}`
);
console.assert(
  six(dividedBy(two())) === 3,
  `Expected: 3, instead got: ${six(dividedBy(two()))}`
);
console.assert(
  one(dividedBy(nine())) === 0,
  `Expected: 0, instead got: ${one(dividedBy(nine()))}`
);

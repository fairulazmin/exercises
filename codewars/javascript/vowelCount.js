const getCount = (str) => {
  return (str.match(/[aeiou]/g) || []).length;
};

test = [
  { input: "my pyx", output: 0 },
  { input: "abracadabra", output: 5 },
  { input: "", output: 0 },
];

test.map((x) =>
  console.assert(
    getCount(x.input) === x.output,
    `Expected: ${x.output} but got: ${getCount(x.input)}`
  )
);

const validParentheses = (parens) => {
  while (parens.match(/\(\)/g)) {
    parens = parens.replace(/\(\)/g, "");
  }
  return !parens;
};

tests = [
  { input: "()", output: true },
  { input: ")(()))", output: false },
  { input: "(", output: false },
  { input: "(())((()())())", output: true },
];

tests.map((test) => {
  console.assert(
    validParentheses(test.input) === test.output,
    `Expected ${test.output} received ${validParentheses(test.input)}`
  );
});

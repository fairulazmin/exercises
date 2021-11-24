const solution = (str) => {
  return (str + "_").match(/../g) || [];
  /*
  if (str === "") return [];

  const x = str.match(/.?./g);
  const y = x.pop();

  return y.length === 1 ? [...x, y + "_"] : [...x, y];
  */
};

console.log(solution("abc"));
console.log(solution("abcdef"));
console.log(solution(""));

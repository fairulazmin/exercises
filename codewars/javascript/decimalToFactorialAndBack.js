function dec2FactString(nb) {
  const conversionTableD2S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

  let str = "0";
  let idx = 2;

  while (nb) {
    const mod = conversionTableD2S[nb % idx];
    nb = parseInt(nb / idx);
    str = mod + str;
    idx++;
  }
  return str;
}

function factString2Dec(str) {
  const factorial = (num) => {
    return num <= 1 ? 1 : num * factorial(num - 1);
  };

  let sum = 0;

  for (let i = 0; i < str.length; i++) {
    const num = str[i].charCodeAt();
    sum =
      sum + (num < 65 ? num - 48 : num - 55) * factorial(str.length - i - 1);
  }

  return sum;
}

testsD2S = [
  { input: 2982, output: "4041000" },
  { input: 463, output: "341010" },
  { input: 1273928000, output: "27A0533231100" },
];

testsD2S.map((test) => {
  console.assert(
    dec2FactString(test.input) === test.output,
    `Expected ${test.output} but received ${dec2FactString(test.input)}`
  );
});

testsS2D = [
  { input: "4041000", output: 2982 },
  { input: "341010", output: 463 },
  { input: "27A0533231100", output: 1273928000 },
];

testsS2D.map((test) => {
  console.assert(
    factString2Dec(test.input) === test.output,
    `Expected ${test.output} but received ${factString2Dec(test.input)}`
  );
});

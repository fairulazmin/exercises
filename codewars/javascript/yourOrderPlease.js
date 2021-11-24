const order = (words) => {
  const arr = words.split(" ");
  arr.sort((a, b) => a.match(/\d+/)[0] - b.match(/\d+/)[0]);
  return arr.join(" ");
};

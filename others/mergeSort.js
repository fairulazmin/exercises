const merged = (left, right) => {
  let m = [];
  let idxL = 0;
  let idxR = 0;

  while (idxL < left.length && idxR < right.length) {
    if (left[idxL] <= right[idxR]) {
      m.push(left[idxL]);
      idxL++;
    } else if (left[idxL] > right[idxR]) {
      m.push(right[idxR]);
      idxR++;
    }
  }

  if (idxL === left.length) {
    m = [...m, ...right.slice(idxR, right.length)];
  } else if (idxR === right.length) {
    m = [...m, ...left.slice(idxL, left.length)];
  }

  return m;
};

const mergeSort = (m) => {
  const len = m.length;
  return len <= 1
    ? m
    : merged(
        mergeSort(m.slice(0, len / 2)),
        mergeSort(m.slice(len / 2, m.length))
      );
};

console.log(mergeSort([8, 3, 3, 0, 7, 13, 2, 5, 1, 0, 3, 7, 6, 4]));

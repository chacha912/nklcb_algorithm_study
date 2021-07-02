const fs = require('fs');

const input = fs.readFileSync('input.txt').toString().split('\n');
const [N] = input[0].split(' ');
const arr = input[1].split(' ').map(Number);

const obj = {};

for (let i = 0; i < N; i++) {
  const val = arr[i];
  obj[val] = val in obj ? [obj[val][0], obj[val][1] + 1] : [i, 1];
}

const sortArr = Object.entries(obj).sort((x, y) =>
  x[1][1] === y[1][1] ? x[1][0] - y[1][0] : y[1][1] - x[1][1]
);

const answer = [];
for (let i = 0; i < sortArr.length; i++) {
  answer.push(Array.from({ length: sortArr[i][1][1] }, () => +sortArr[i][0]));
}

console.log(answer.flat().join(' '));

const fs = require('fs');

const input = fs.readFileSync('input.txt').toString().split('\n');
const [K, N] = input[0].split(' ').map(Number);

const lan = [];

for (let i = 0; i < K; i++) {
  lan.push(+input[i + 1]);
}

let left = 0;
let right = 2 ** 32;

while (left <= right) {
  const mid = Math.floor((left + right) / 2);

  let num = 0;
  for (let i = 0; i < K; i++) {
    num += Math.floor(lan[i] / mid);
  }

  if (num < N) right = mid - 1;
  else left = mid + 1;
}

console.log(right);

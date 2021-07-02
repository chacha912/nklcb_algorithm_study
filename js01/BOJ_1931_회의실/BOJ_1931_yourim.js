const fs = require('fs');

const input = fs.readFileSync('input.txt').toString().split('\n');
const N = +input[0];
const arr = [];

for (let i = 0; i < N; i++) {
  arr.push(input[i + 1].split(' ').map(Number));
}

const greedy = arr => {
  let answer = 0;
  let start = 0;
  for (let i = 0; i < N; i++) {
    if (arr[i][0] >= start) {
      [, start] = arr[i];
      answer += 1;
    }
  }
  return answer;
};

arr.sort((x, y) => x[0] - y[0]).sort((x, y) => x[1] - y[1]);
console.log(greedy(arr));

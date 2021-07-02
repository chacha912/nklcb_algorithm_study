const fs = require('fs');

const LIS = arr => {
  const dp = Array.from({ length: arr.length }, () => 0);
  dp[0] = 1;

  for (let i = 1; i < arr.length; i++) {
    let max = 0;
    for (let j = i - 1; j >= 0; j--) {
      if (arr[j] < arr[i] && dp[j] > max) {
        max = dp[j];
      }
    }
    dp[i] = max + 1;
  }

  return Math.max(...dp);
};

const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const arr = input[1].split(' ').map(Number);

console.log(LIS(arr));

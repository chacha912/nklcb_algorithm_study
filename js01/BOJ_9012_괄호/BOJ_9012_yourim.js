const fs = require('fs');

const chkVPS = str => {
  if (str.length % 2 !== 0) return false;

  let num = 0;
  for (const letter of str) {
    num = letter === '(' ? num + 1 : num - 1;
    if (num === -1) return false;
  }
  return num === 0;
};

const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = +input[0];

for (let i = 1; i <= N; i++) {
  str = input[i];
  console.log(chkVPS(str) ? 'YES' : 'NO');
}

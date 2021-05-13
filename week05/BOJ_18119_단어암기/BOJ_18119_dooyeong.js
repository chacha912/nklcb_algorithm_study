const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const [N, M] = input
  .shift()
  .split(" ")
  .map((x) => +x);

const words = [],
  a = "a".charCodeAt(0);

const getWordBit = (word) => {
  let tmp = 0;

  for (let i = 0, l = word.length; i < l; i++) {
    tmp |= 1 << (word[i].charCodeAt(0) - a);
  }

  return tmp;
};

const getCharBit = (ch) => {
  return 1 << (ch.charCodeAt(0) - a);
};

for (let i = 0; i < N; i++) {
  words[i] = getWordBit(input[i]);
}

let status = (1 << 27) - 1,
  ans = "";

for (let i = N; i < N + M; i++) {
  const [cmd, ch] = input[i].split(" ");

  if (cmd == "1") status &= ~getCharBit(ch);
  else status |= getCharBit(ch);

  let cnt = 0;
  for (let i = 0; i < N; i++) {
    if ((words[i] & status) == words[i]) cnt += 1;
  }

  ans += cnt.toString() + "\n";
}

console.log(ans);

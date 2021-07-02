const fs = require('fs');

const input = fs.readFileSync('input.txt').toString().split('\n');
const [M, N, K] = input[0].split(' ').map(Number);
const row = Array.from({ length: N }, () => 0);
const board = Array.from({ length: M }, () => [...row]);
const que = [];
const dx = [-1, 0, 1, 0];
const dy = [0, -1, 0, 1];

for (let i = 0; i < K; i++) {
  const [sy, sx, ey, ex] = input[i + 1].split(' ').map(Number);

  // 직사각형 채우기
  for (let x = sx; x < ex; x++) {
    for (let y = sy; y < ey; y++) {
      board[x][y] = 1;
    }
  }

  // 분리될 가능성 있는 영역
  const num = (ex - sx + 2) * (ey - sy + 2) - (ex - sx) * (ey - sy);
  let dir = 0;
  let x = ex;
  let y = ey;
  for (let i = 0; i < num; i++) {
    if (i === 0) {
      if (x >= M || x < 0 || y >= N || y < 0) continue;
      que.push([x, y]);
      continue;
    }

    x += dx[dir];
    y += dy[dir];

    if (x === sx - 1 && y === ey) dir = 1;
    if (x === sx - 1 && y === sy - 1) dir = 2;
    if (x === ex && y === sy - 1) dir = 3;

    if (x >= M || x < 0 || y >= N || y < 0) continue;
    que.push([x, y]);
  }
}

// 분리된 영역 체크
let cnt = 0;
const cntArr = [];

for (let i = 0; i < que.length; i++) {
  const [qx, qy] = que[i];
  if (board[qx][qy] === 2 || board[qx][qy] === 1) continue;

  cnt += 1;

  let sum = 0;
  const stack = [[qx, qy]];

  while (stack.length) {
    const [x, y] = stack.pop();
    if (x >= M || x < 0 || y >= N || y < 0) continue;
    if (board[x][y] === 2 || board[x][y] === 1) continue;

    board[x][y] = 2;
    sum += 1;

    for (let i = 0; i < 4; i++) {
      const x2 = x + dx[i];
      const y2 = y + dy[i];
      stack.push([x2, y2]);
    }
  }
  cntArr.push(sum);
}

console.log(cnt);
console.log(cntArr.sort((x, y) => x - y).join(' '));

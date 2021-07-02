const fs = require('fs');

const input = fs.readFileSync('input.txt').toString().split('\n');

const [r] = input[0].split(' ').map(Number);
const [x0, y0, dir0] = input[1].split(' ').map(Number);

const dx = [-1, 0, 1, 0]; // 북, 동, 남, 서
const dy = [0, 1, 0, -1];

const room = [];
for (let i = 0; i < r; i++) {
  room.push(input[i + 2].split(' ').map(Number));
}

let answer = 0;
const clean = (x, y, dir, goClean) => {
  if (goClean) {
    room[x][y] = 2;
    answer += 1;
  }

  let allClean = true;
  for (let i = 0; i < 4; i++) {
    if (room[x + dx[i]][y + dy[i]] === 0) allClean = false;
  }

  const backDir = dir < 2 ? dir + 2 : dir - 2;
  const bx = x + dx[backDir];
  const by = y + dy[backDir];

  if (allClean) {
    if (room[bx][by] === 1) return;
    clean(bx, by, dir, false);
    return;
  }

  const leftDir = dir === 0 ? 3 : dir - 1;
  const nx = x + dx[leftDir];
  const ny = y + dy[leftDir];

  if (room[nx][ny] === 0) {
    clean(nx, ny, leftDir, true);
  } else {
    clean(x, y, leftDir, false);
  }
};

clean(x0, y0, dir0, true);
console.log(answer);

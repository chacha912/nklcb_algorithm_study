const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const [N, M] = input
		.shift()
		.split(" ")
		.map((x) => +x),
	board = input.map((x) => x.split("")),
	red = [0, 0],
	blue = [0, 0],
	hole = [0, 0],
	dirs = [
		[-1, 0],
		[1, 0],
		[0, -1],
		[0, 1],
	];

const tilt = (board, di, red, blue) => {
	let res = true,
		blueMet = false,
		redMet = false,
		goalIn = false,
		[rr, rc] = [...red],
		[br, bc] = [...blue];

	while (board[rr + di[0]][rc + di[1]] != "#") {
		rr += di[0];
		rc += di[1];

		const cur = board[rr][rc];

		if (cur == "B") {
			blueMet = true;
			break;
		}

		if (cur == "O") {
			goalIn = true;
			break;
		}
	}

	while (board[br + di[0]][bc + di[1]] != "#") {
		br += di[0];
		bc += di[1];

		const cur = board[br][bc];

		if (cur == "R") {
			redMet = true;
			break;
		}

		if (cur == "O") {
			goalIn = true;
			res = false;
			break;
		}
	}

	if (goalIn) {
		if (redMet || blueMet) {
			res = false;
		}
	} else {
		if (redMet) {
			br = rr - di[0];
			bc = rc - di[1];
		} else if (blueMet) {
			rr = br - di[0];
			rc = bc - di[1];
		}
	}

	return [res, rr, rc, br, bc];
};

let goal = false;

const dfs = (board, cnt, red, blue, past) => {
	if (goal || cnt == 10) {
		return;
	}
	// console.log(board);
	const originalR = [...red],
		originalB = [...blue];

	for (let i = 0; i < 4; i++) {
		if (i == past) continue;

		const [res, rr, rc, br, bc] = tilt(board, dirs[i], [...red], [...blue]);

		if (!res) continue;

		if (board[rr][rc] == "O") {
			goal = true;
			return;
		}

		board[originalR[0]][originalR[1]] = ".";
		board[originalB[0]][originalB[1]] = ".";
		board[rr][rc] = "R";
		board[br][bc] = "B";
		dfs(board, cnt + 1, [rr, rc], [br, bc], i);
		board[rr][rc] = ".";
		board[br][bc] = ".";
		board[originalR[0]][originalR[1]] = "R";
		board[originalB[0]][originalB[1]] = "B";
		board[hole[0]][hole[1]] = "O";
	}
};

for (let i = 0; i < N; i++) {
	for (let j = 0; j < M; j++) {
		if (board[i][j] == "R") [red[0], red[1]] = [i, j];
		if (board[i][j] == "B") [blue[0], blue[1]] = [i, j];
		if (board[i][j] == "O") [hole[0], hole[1]] = [i, j];
	}
}

dfs(board, 0, red, blue, -1);
console.log(goal ? 1 : 0);

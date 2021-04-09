## 백준 #15649 N과M(1)

- 알고리즘 스터디 문제 풀이입니다.
- [백준 15649번](https://www.acmicpc.net/problem/15649) 에서 풀어볼 수 있습니다.

### 문제설명

- 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다. 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

### 풀이

```python
from sys import stdin

def solve(cnt):
    if cnt >= m:
        print(' '.join(ans))
        return

    for i in range(1, n+1):
        if i in used:
            continue

        ans.append(str(i))
        used.add(i)
        solve(cnt+1)
        ans.pop()
        used.remove(i)

ans = []
used = set()
n, m = map(int, stdin.readline().split())
solve(0)
```

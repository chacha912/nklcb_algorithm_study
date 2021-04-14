## 백준 #2437 저울

- 알고리즘 스터디 문제 풀이입니다.
- [백준 2437번](https://www.acmicpc.net/problem/2437) 에서 풀어볼 수 있습니다.

### 문제설명

<img src='https://www.acmicpc.net/upload/images/Screen%20Shot%202012-09-07%20at%20%EC%98%A4%ED%9B%84%203_42_35.png' alt='저울'>

하나의 양팔 저울로 물건의 무게를 측정하려고 한다.  
저울 양팔의 길이는 같고, 한쪽에는 저울추만, 다른 쪽에는 물건만 놓을 수 있다.

무게가 양의 정수인 N개의 저울추가 주어질 때, 이 추들을 사용하여 측정할 수 없는  
양의 정수 무게 중 최솟값을 구하는 프로그램을 작성하시오.

예를 들어, 무게가 각각 3, 1, 6, 2, 7, 30, 1인 7개의 저울추가 주어졌을 때,  
이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값은 21이다.

### 풀이

1. 추의 무게를 기준으로 정렬한다.
2. 인덱스 0부터 차례대로 확인. 숫자가 (누적합 + 1) 이하라면 누적합 + 1까지의 숫자들은 기존의 숫자들의 조합으로 모두 표현 가능하다.
3. 숫자가 (누적합 + 2) 이상이라면 기존 숫자들의 조합으로 (누적합 + 1) 표현이 불가능하므로 (누적합 + 1)을 출력한다.

```python
from sys import stdin

def solution(weight):
    weight.sort()
    sum = 0
    for w in weight:
        if w >= sum + 2:
            return sum + 1
        else:
            sum += w
    return sum + 1

n = int(stdin.readline())
weight = list(map(int, stdin.readline().split()))
print(solution(weight))
```

```python
from sys import stdin

n = int(stdin.readline().strip())
a = list(map(int,stdin.readline().split()))
a.sort()
s = 1

for i in range(n):
    if a[i] > s:
        break
    s += a[i]

print(s)
```

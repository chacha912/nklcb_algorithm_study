## 백준 #11653 소인수분해

- 알고리즘 스터디 문제 풀이입니다.
- [백준 11653번](https://www.acmicpc.net/problem/11653) 에서 풀어볼 수 있습니다.

### 문제설명

- 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
- N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

### 풀이1.

index 2부터 index로 값이 나눠지는지 확인하고 더 이상 나눠지지 않으면 index를 1씩 증가하면서 다시 나눠지는지 확인한다.

```python
def factorization(n):
    index = 2
    while n != 1:
        if n % index == 0:
            print(index)
            n /= index
        else:
            index += 1

N = int(input())

factorization(N)
```

### 풀이2.

```python
import math

def factorization(n):
    index = 2
    while n != 1:
        if index > math.sqrt(n):
            print(int(n))
            return

        if n % index == 0:
            print(index)
            n /= index
        else:
            index += 1

N = int(input())

factorization(N)
```

### 💡

두 번째 풀이에서 n /= index 할때 값이 float로 나오기 때문에 print할 때 정수형으로 변환해야한다.

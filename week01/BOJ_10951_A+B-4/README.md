## 백준 #10951 A+B -4

- 알고리즘 스터디 문제 풀이입니다.
- [백준 10951번](https://www.acmicpc.net/problem/10951) 에서 풀어볼 수 있습니다.

### 문제설명

- 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
- 입력은 여러 개의 테스트 케이스로 이루어져 있다.
- 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

### 문제 팁

- [☆★ [필독] A+B - 4 FAQ ★☆](https://www.acmicpc.net/board/view/39199)

  > **이 문제의 목적은 파일의 끝(EOF)을 올바르게 판단하는 법을 연습하는 것입니다.**
  > 총 몇 줄이 주어진다 등의 정보는 절대 입력으로 주지 않습니다.
  > 또한 단순히 키보드로 입력 내용만 적고 프로그램이 종료되지 않은 상태까지만 봐서는 EOF를 제대로 처리했는지 알 수 없습니다. 더 이상 읽을 게 없을 때 프로그램을 종료하는 법을 알아야 합니다.
  > 그 방법은 언어마다 다르고 사용하는 함수마다 다르니, 구글에 "C언어 EOF" 와 같이 검색해서 그 방법을 알아보세요. 주로 파일 입출력으로 설명되어 있겠지만, 입력 스트림도 파일 입력이기 때문에 결국 동일합니다.
  >
  > 1. (C/C++) scanf는 EOF를 반환하지, 변수에 저장해주지 않습니다.
  > 1. (Java) Scanner의 메서드들은 NoSuchElementException을 던집니다.
  > 1. (Java) BufferedReader.readLine()은 null을 반환합니다.
  > 1. (Python) input()은 EOFError를 발생시킵니다.
  > 1. (Python) sys.stdin.readline()은 빈 문자열을 반환합니다.

### 풀이1. input()

```python
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except Exception as e:
        print(e) # EOF when reading a line
        break
```

### 풀이2. sys.stdin.readline()

풀이 1에서는 EOF 에러가 발생하지만, sys.stdin.readline()은 파일 끝에서 빈 문자열을 반환하므로 try-except 문에서 not enough values to unpack 에러가 발생한다.

```python
from sys import stdin

while True:
    try:
        a, b = map(int, stdin.readline().split())
        print(a + b)
    except Exception as e:
        print(e) # not enough values to unpack (expected 2, got 0)
        break
```

### 💡

Python으로 백준 문제를 풀 때 내장 함수 input()으로 입력을 받으면 시간 초과로 오답처리가 되고, sys 모듈의sys.stdin.readline()으로 입력을 받으면 시간 안에 채점이 되는 경우가 자주 발생한다.  
대량의 데이터를 반복적으로 입력받아야 할 때, input()대신 sys.stdin.readline()을 이용하면 성능(속도)이 향상된다.

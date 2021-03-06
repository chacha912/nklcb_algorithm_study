## 백준 #14500 테트로미노

- 알고리즘 스터디 문제 풀이입니다.
- [백준 14500번](https://www.acmicpc.net/problem/14500) 에서 풀어볼 수 있습니다.

### 문제설명

![](https://images.velog.io/images/lky9303/post/0156b393-0217-43b4-9b58-6d14cc7c3444/image.png)

### 풀이

모든 테트로미노 블록에 대해, 회전, 대칭으로 만들어지는 모든 경우의 수를 계산해서, 시작점에 대한 숫자합을 모두 계산해주면 풀 수 있다.

조금 더 효율적인 방법도 가능할 거 같아, 다른 방법도 시도해 볼만할 듯.

특히 배열로, 블록모양을 구현해, 주어진 배열을 순회할 수 있는 방법을 공부하면 더 가독성 높은 코드를 짤 수 있을 거라 생각한다.

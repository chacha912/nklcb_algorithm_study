## 백준 #1976 여행가자

- 알고리즘 스터디 문제 풀이입니다.
- [백준 1976번](https://www.acmicpc.net/problem/1976) 에서 풀어볼 수 있습니다.

### 문제설명
유니온 파인드 문제 

문제에서 주어진 그래프를 따라서 문제에서 주어진 경로 탐색이 가능한지 찾아내는 문제

주어지는 노드들이 한 집합에 있는지 찾아내는 문제 
### 풀이
전형적인 유니온 파인드 문제로 특정 두 노드에 대해 루트 노드를 찾아내는 find 함수와
두 노드를 합치는 유니온 함수를 통해 문제 해결

1. 주어지는 그래프에 대해 발생하는 노드의 루트를 자기 자신으로 초기화
  - 리스트나, 딕셔너리를 사용해도 상관없음.
2. for문을 돌면서 발생하는 경로의 두 노드의 루트값을 각각 찾아줌.
3. union 함수로 (rank로 최적화) 해당 두 노드의 루트값이 다를 경우 합쳐줌
4. 주어지는 spot을 순회하면서 해당 경로의 루트 노드가 무슨 노드인지 모두 찾아줌.
5. 해당 루트 노드가 다른 노드가 있다면 연결될 수 없는 루트 노드가 있는것이므로, 
 set 자료구조로 중복을 없앴 을 때, 길이가 1이 넘으면 NO 반대면 YES


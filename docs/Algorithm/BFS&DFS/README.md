<aside>
💡

아래는 **DFS, BFS 알고리즘** 사용 시 사용되는 **1차원 그래프 탐색**을 기준으로 한 기본 코드에요 !
node나 neighbor 의 변수명은 자유롭게 편한대로 사용하는 것을 추천해요 !!!
예) v, w / now, next / i, j 등등

</aside>

![DFS AND BFS.png](./DFS%20AND%20BFS.png)

### DFS 재귀

- **슈도 코드**
    1. **현재 노드를 방문 표시**한다.
    2. 현재 노드의 모든 **인접 노드를 확인**한다.
    2.1 인접 노드 중 **방문하지 않은 노드**에 대해 **재귀 호출**을 진행한다.
    3. 모든 인접 노드가 방문될 때까지 위 과정을 **반복**한다.

```python
def dfs_recursive(node):
    visited[node] = True
    for neighbor in arr[node]:
        if not visited[neighbor]:
            dfs_recursive(neighbor)
```

### DFS 스택

- **슈도 코드**
    1. 시작 노드를 **스택에 넣는다.**
    visited 배열에 시작 노드를 **방문 표시**한다.
    2. 스택이 비어있지 않은 동안 다음을 **반복**한다:
    3.1 스택에서 **노드를 꺼낸다.**
    3.2 꺼낸 노드의 모든 **인접 노드를 확인**한다.
    3.3 인접 노드 중 방문하지 않은 노드를 **스택에 넣고** **방문 표시**한다. (중요)
    3. 모든 노드를 탐색할 때까지 위 과정을 **반복**한다.

```python
def dfs_stack():
    while stack:
        node = stack.pop()
        for neighbor in arr[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True
```

### BFS 큐

- **슈도 코드**
    1. 시작 노드를 **큐에 넣는다.**
    visited 배열에 시작 노드를 **방문 표시**한다.
    2. 큐가 비어있지 않은 동안 다음을 **반복**한다:
    1.1 큐에서 **노드를 꺼낸다.**
    1.2 꺼낸 노드의 모든 **인접 노드를 확인**한다.
    1.3 인접 노드 중 방문하지 않은 노드를 **큐에 넣고** **방문 표시**한다. (중요)
    3. 모든 노드를 탐색할 때까지 위 과정을 반복한다.

```python
from collections import deque

def bfs():
    while q:
        node = q.popleft()
        for neighbor in arr[node]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
```
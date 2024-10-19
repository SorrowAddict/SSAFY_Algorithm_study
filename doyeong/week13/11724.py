# 11724. 연결 요소의 개수

import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    global cnt
    q = deque([s])
    visited[s] = True

    while q:
        v = q.popleft()
        for i in adjL[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    cnt += 1    # BFS 탐색으로 visited 처리 해주고 cnt값 증가

V, E = map(int, input().split())
adjL = [[] for _ in range(V+1)]
visited = [False] * (V+1)
for _ in range(E):  # 인접 리스트
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

cnt = 0
for i in range(1, V+1): # 모든 노드에 대하여
    if not visited[i]:  # 방문하지 않은 정점에서만 BFS탐색
        bfs(i)
print(cnt)
# 2606. 바이러스

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([1])      # 1번부터 BFS 너비 탐색
    visited = [0] * (N+1)
    visited[1] = 1
    cnt = 0     # 1번 컴퓨터에 연결된 컴퓨터 수
    while q:
        i = q.popleft()
        for j in adj[i]:    # 연결되어 있음
            if not visited[j]:
                q.append(j)
                visited[j] = 1
                cnt += 1    # count값 증가
    return cnt

N = int(input())
E = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(E):      # 인접 리스트 기록
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

print(bfs())
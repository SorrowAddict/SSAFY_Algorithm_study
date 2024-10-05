# 14940. 쉬운 최단거리

import sys
from collections import deque
input = sys.stdin.readline

# 시작점 찾기
def find_start():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return i, j

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
def bfs():
    while q:
        ti, tj = q.popleft()
        for k in range(4):
            ni, nj = ti+di[k], tj+dj[k]
            # 방문하지 않았고, 갈 수 있다면(1이라면)
            if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and arr[ni][nj]:
                q.append((ni, nj))          # 유망한 노드 인큐
                visited[ni][nj] = True      # 방문 처리
                arr[ni][nj] = arr[ti][tj] + 1   # BFS로 퍼지면서 +1씩 값을 증가

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
i, j = find_start()
q = deque([(i, j)])
visited[i][j] = True    # 시작점 인큐
arr[i][j] = 0           # 초기값을 0부터 시작 (퍼지면서 +1씩 증가)
bfs()

for i in range(n):
    for j in range(m):
        # BFS를 돌린 이후에
        if arr[i][j] and not visited[i][j]: # 갈 수 있는 땅인데 방문하지 못했으면
            arr[i][j] = -1      # -1로 처리

for row in arr:     # 전체 arr 출력
    print(*row)
# 21736. 헌내기는 친구가 필요해 - DFS 방식 (stack)

import sys
sys.setrecursionlimit(10**6)

def find_start():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'I':
                return i, j

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

def dfs(ti, tj):
    global cnt

    for k in range(4):
        ni, nj = ti+di[k], tj+dj[k]
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] != 'X':
            if arr[ni][nj] == 'P':
                cnt += 1
            visited[ni][nj] = True
            dfs(ni, nj)

N, M = map(int, sys.stdin.readline().split())
arr = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
i, j = find_start()
visited[i][j] = True
cnt = 0
dfs(i, j)
if cnt == 0:
    print('TT')
else: print(cnt)
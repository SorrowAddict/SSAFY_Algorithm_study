# 21736. 헌내기는 친구가 필요해 - DFS 방식

import sys

def find_start():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'I':
                return i, j

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

def dfs(ti, tj):
    cnt = 0

    stack = [(ti, tj)]
    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] != 'X':
                if arr[ni][nj] == 'P':
                    cnt += 1
                visited[ni][nj] = True
                stack.append((ni, nj))
    return cnt

N, M = map(int, sys.stdin.readline().split())
arr = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
i, j = find_start()
visited[i][j] = True
ans = dfs(i, j)
if ans == 0:
    print('TT')
else: print(ans)
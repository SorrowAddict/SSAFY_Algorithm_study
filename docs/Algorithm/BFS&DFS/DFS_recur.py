# ------------- 재귀를 사용하는 DFS 기본 코드 ------------- #
# 1. 현재 노드를 방문 표시한다.
# 2. 현재 노드의 모든 인접 노드를 확인한다.
#    2.1 인접 노드 중 방문하지 않은 노드에 대해 재귀 호출을 진행한다.
# 3. 모든 인접 노드가 방문될 때까지 위 과정을 반복한다.

# ------------- 아래 함수 부분 다음주 시험! ------------- #
def dfs_recursive(node):
    visited[node] = True
    for neighbor in arr[node]:
        if not visited[neighbor]:
            dfs_recursive(neighbor)
# ------------- 여기까지 (DFS의 경우 재귀, stack 중 편한걸로) ------------- #

# 아래는 입력 예시 (안써도 됨)
V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
visited = [False] * len(V)

stack = [1]
visited[1] = True
dfs_recursive(1)



# ------------- 2차원 배열의 경우 ------------- #
# 2차원 배열의 경우, graph는 n x m 크기의 배열로 설정
# visited 역시 같은 크기의 2차원 배열로 설정

def dfs_recursive(i, j):
    visited[i][j] = True
    
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni, nj = i + di, j + dj
        # 범위 안에 있고, 방문하지 않은 노드만 탐색
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
            dfs_recursive(ni, nj)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _  in range(N)]

dfs_recursive(0, 0)
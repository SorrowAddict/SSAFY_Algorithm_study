# 15654. N과 M (5) (순열)

import sys
input = sys.stdin.readline

def perm_recur(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        if not used[i]: # 중복을 검사
            path.append(arr[i])
            used[i] = True
            perm_recur(level + 1)
            used[i] = False
            path.pop()

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))   # 오름차순으로 정렬
used = [0] * N  # 중복되는 수열 처리를 위한 used 배열
path = []
perm_recur(0)
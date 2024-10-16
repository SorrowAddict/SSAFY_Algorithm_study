# 15650. N과 M (2) (조합)

import sys
input = sys.stdin.readline

# 재귀의 깊이를 결정할 level / 순회 지점을 저장할 start 매개변수 사용
def comb_recur(level, start):
    if level == M:
        print(*path)
        return
    for i in range(start+1, N+1):
        path.append(i)
        comb_recur(level+1, i)
        path.pop()

N, M = map(int, input().split())
path = []
comb_recur(0, 0)
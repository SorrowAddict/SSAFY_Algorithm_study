# 16953. A → B

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([(A, 1)])
    while q:
        v, cnt = q.popleft()
        if v == B:
            return cnt
        # 리스트 안에 [2를 곱한 값, 1을 수의 오른쪽에 추가한 값]을 순회
        lst = [v*2, int(str(v)+'1')]
        for i in lst:
            if i <= B:  # 아직 리스트 안의 값이 목적하는 B값보다 작은 경우에만
                q.append((i, cnt+1))    # 큐에 push
    return -1

A, B = map(int, input().split())
print(bfs())
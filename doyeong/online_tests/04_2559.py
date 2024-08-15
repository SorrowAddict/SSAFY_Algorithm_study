# 2559 - 수열

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 0~K-1 인덱스를 초기값을 import deque를 통해 설정
stack = deque(arr[:K])
stack_sum = sum(stack)
max_v = stack_sum       # 비교해 줄 초기 최댓값 설정

# K~N 만큼 순회 (결국 전체 순회)
for i in range(K, N):
    # 우측값을 추가하면서 왼쪽에서 popleft (큐의 성질을 이용)
    stack_sum += arr[i] - stack.popleft()
    stack.append(arr[i])        # 스택(사실 큐인데 변수명 못 바꿈)에 우측값 추가
    if max_v < stack_sum:       # 스택합 최댓값인지 판별
        max_v = stack_sum

print(max_v)
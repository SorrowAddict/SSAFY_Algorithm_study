# SWEA_1234번, [S/W 문제해결 기본] 10일차 - 비밀번호

import sys
sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, arr = input().split()
    N = int(N)
    my_stack = []
    for str in arr:
        if not my_stack or my_stack[-1] != str:
            my_stack.append(str)
        else:
            my_stack.pop()
    print(f'#{tc}', end=' ')
    for ch in my_stack:
        print(ch, end='')
    print()
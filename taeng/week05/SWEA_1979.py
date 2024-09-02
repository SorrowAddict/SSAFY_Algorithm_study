# SWEA_1979번, 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    # 행마다 체크
    for i in range(N):
        streak = 0
        for j in range(N):
            # 검은색 부분
            if board[i][j] == 0:
                # 연속된 부분이 K 만큼이면
                if streak == K:
                    result += 1
                streak = 0
            # 흰색 부분
            else:
                streak += 1
            # 마지막 열에 도착했을 때
            if j == N - 1 and streak == K:
                result += 1
    # 열마다 체크
    for i in range(N):
        streak = 0
        for j in range(N):
            # 검은색 부분
            if board[j][i] == 0:
                # 연속된 부분이 K 만큼이면
                if streak == K:
                    result += 1
                streak = 0
            # 흰색 부분
            else:
                streak += 1
            # 마지막 행에 도착했을 때
            if j == N - 1 and streak == K:
                result += 1

    print(f'#{tc} {result}')
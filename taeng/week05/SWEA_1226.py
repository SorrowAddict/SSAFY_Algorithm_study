# SWEA_1226번, [S/W 문제해결 기본] 7일차 - 미로1

import sys
sys.stdin = open('input.txt')

def search(x, y):
    global is_find
    # 도착 지점에 도달
    if board[x][y] == '3':
        is_find = True
        return 1
    # 델타 이동
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx = x + dx
        ny = y + dy
        # 해당 칸에 이동할 수 있다면
        if board[nx][ny] != '1':
            # 다시 방문하지 않도록 처리
            board[x][y] = '1'
            # 해당 칸에서 탐색
            search(nx, ny)
    # 도착 지점을 찾은 경우
    if is_find:
        return 1
    # 찾지 못한 경우
    else:
        return 0

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    TC = int(input())

    board = [list(input()) for _ in range(16)]
    board[1][1] = '1'
    is_find = False
    answer = search(1, 1)

    print(f'#{tc} {answer}')
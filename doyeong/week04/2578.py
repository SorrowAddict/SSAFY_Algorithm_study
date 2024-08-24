# 2578 - 빙고

import sys
input = sys.stdin.readline

# 초기 빙고판 입력
arr = [list(map(int, input().split())) for _ in range(5)]

def check_bingo():
    temp = 0
    # 대각선
    for i in range(5):
        if arr[i][i] != 0:
            break
    else: temp += 1
    
    # 대각선
    for i in range(5):
        if arr[i][4-i] != 0:
            break
    else: temp += 1
    
    # 가로
    for i in range(5):
        for j in range(5):
            if arr[i][j] != 0:
                break
        else: temp += 1

    # 세로
    for j in range(5):
        for i in range(5):
            if arr[i][j] != 0:
                break
        else: temp += 1
    return temp

# 빙고 입력 받아오기
lst = []
for _ in range(5):
    lst.extend(map(int, input().split()))

# 빙고 함수 돌리기
cnt = 0
for x in lst:
    cnt += 1
    # 해당 번호를 X표(0으로) 바꿈
    for i in range(5):
        for j in range(5):
            if arr[i][j] == x:
                arr[i][j] = 0
                break
        else:
            continue
        # 바꿨을 때 2중 for문 탈출
        break
    
    # 빙고 3회 이상이면 프린트하고 바로 정지
    if check_bingo() >= 3:
        print(cnt)
        break
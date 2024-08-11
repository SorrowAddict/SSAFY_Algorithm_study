import sys
input=sys.stdin.readline

# 1001 x 1001 칸 격자 배열 생성
arr = [[0] * 1001 for _ in range(1001)]
N = int(input())
cnt_N = [0]*(N+1)   # 1~N 까지 인덱싱으로 카운팅을 세 줄 배열

for i in range(1, N+1):
    row, col, row_l, col_l = map(int, input().split())  # x, j, x길이, y길이 값을 받아온다.
    for x in range(row, row+row_l):         # x, y 사각형 범위만큼 순회하면서
        for y in range(col, col+col_l):
            if arr[x][y] != 0:              # 이미 색칠이 되어있으면
                cnt_N[arr[x][y]] -= 1       # 색칠된 값을 기준 인덱스로 -= 1 카운트를 빼줌
            # if 구문이 실행되고 그려야 할 사각형을 덧붙여 그려주고 카운팅 배열을 더해줌
            arr[x][y] = i
            cnt_N[i] += 1
print('\n'.join(map(str, cnt_N[1:])))       # join()함수와 map(str, iterable)을 사용해 출력
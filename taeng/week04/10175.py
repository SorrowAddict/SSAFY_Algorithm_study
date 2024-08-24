# 10175번, 자리배정
C, R = map(int, input().split())
K = int(input())
if K > C * R:
    print(0)
else:
    matrix = [[0] * R for _ in range(C)]
    x = 0
    y = 0
    matrix[x][y] = -1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    k = 0
    cnt = 1
    while cnt < K:
        k %= 4
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < C and 0 <= ny < R and matrix[nx][ny] != -1:
            # 지나온 길 체크
            matrix[nx][ny] = -1
            x = nx
            y = ny
            cnt += 1
        else:
            k += 1
    print(x+1, y+1)
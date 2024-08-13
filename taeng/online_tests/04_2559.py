# 2559번, 수열
# N: 배열 길이, K: 연속된 배열의 수
N, K = map(int, input().split())
# N개 길이를 가진 수열
arr = list(map(int, input().split()))
# 배열 내 맨 앞 K개의 데이터의 합 구하기
max_v = 0
for i in range(K):
    max_v += arr[i]
# 배열을 순회하며 이전 배열 합 부분의 맨 앞 값을 빼고 현재 값 더하기
temp = max_v
for i in range(K, N):
    temp -= arr[i-K]
    temp += arr[i]
    if max_v < temp:
        max_v = temp
print(max_v)

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


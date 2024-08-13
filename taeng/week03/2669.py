# 2669번, 직사각형 네개의 합집합의 면적 구하기
# 데이터의 최대 개수가 100이므로 시간 복잡도를 고려하지 않아도 된다.

matrix = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if matrix[i][j] == 1:
            cnt += 1
print(cnt)

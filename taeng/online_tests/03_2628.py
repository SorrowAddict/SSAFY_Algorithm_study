# 2628번 종이자르기
# 가로, 세로
a, b = map(int, input().split())
N = int(input())
matrix = [[0] * a for _ in range(b)]

new_dict = {}
for _ in range(N):
    direction, dot = map(int, input().split())
    # 가로로 자르는 경우
    if direction == 0:
        for i in range(dot):
            for j in range(a):
                matrix[i][j] += 100
    # 세로로 자르는 경우
    if direction == 1:
        for i in range(dot):
            for j in range(b):
                matrix[j][i] += 1

for i in range(b):
    for j in range(a):
        # 해당 키가 존재하지 않으면
        if new_dict.get(matrix[i][j]) == None:
            new_dict[matrix[i][j]] = 1
        # 해당 키가 존재하면
        else:
            new_dict[matrix[i][j]] += 1

result = -1
# 딕셔너리 값 중에서 최댓값 구하기
for value in new_dict.values():
    if result < value:
        result = value
print(result)
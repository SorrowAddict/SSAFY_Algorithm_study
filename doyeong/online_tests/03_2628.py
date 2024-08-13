import sys

input = sys.stdin.readline

row, col = map(int, input().split())

n = int(input())

# 잘린 종이 조각들의 인덱스값 (x, y)을 저장할 리스트 생성 / 0, row, col 값 추가
row_list, col_list = [0, row], [0, col]

# 점선방향 rc와 자르는 길이 l을 받는다.
for _ in range(n):
    rc, l = map(int, input().split())
    if rc == 0:     # 세로인덱스 (가로로 자르는 점선)이면 세로리스트에 추가
        col_list.append(l)
    else:           # 가로인덱스 (세로로 자르는 점선)이면 가로리스트에 추가
        row_list.append(l)

# 가로, 세로 리스트를 정렬함
row_list, col_list = sorted(row_list), sorted(col_list)

for i in range(len(row_list)-1, 0, -1): # 가로 리스트를 1~끝 까지의 인덱스를 거꾸로 순회
    row_list[i] -= row_list[i-1]        # 기준값에서 기준값 이전 인덱스값의 차
for i in range(len(col_list)-1, 0, -1): # 세로 리스트를 마찬가지의 방법으로 순회
    col_list[i] -= col_list[i-1]        # 이하동일

# 가로 리스트와 세로 리스트의 최댓값이 가장 큰 종이 조각의 넓이값임
print(max(row_list)*max(col_list))
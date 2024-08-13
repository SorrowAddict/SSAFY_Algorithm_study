import sys
input = sys.stdin.readline

# 1~100 까지의 문제 조건에 해당하는 2차원 배열 생성 (인덱스 넘버로 색칠을 할 것이기에 0~100 까지)
arr = [[0]*101 for _ in range(101)]
result = 0    # 결과 초기값

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
		        # 색칠을 안한 곳일 때만 색칠을 하면서 result 변수 카운팅값 증가
            if arr[i][j] == 0:
                arr[i][j] = 1
                result += 1
print(result)
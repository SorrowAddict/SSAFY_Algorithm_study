# 2805. 나무 자르기 (이분 탐색)

import sys
input = sys.stdin.readline

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2    # 톱의 높이
        height = 0
        # 전체 배열을 순회하면서 x-mid 가 양수이면 누적합 (자를 수 있는 나무면)
        for x in arr:
            height += x-mid if x-mid >= 0 else 0

        # 자른 나무의 누적합 height가 목표 길이 M보다 부족하면 더 짧게 자르기 위해 mid값보다 작은 범위 탐색
        if height < M:
            end = mid - 1
        elif height >= M:   # 반대의 경우 mid값보다 큰 범위 탐색
            start = mid + 1
        # 같을 경우 start를 계속 올려서 최대인 end 값을 찾음
    return end

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

start, end = 1, arr[-1]
print(binary_search(start, end))
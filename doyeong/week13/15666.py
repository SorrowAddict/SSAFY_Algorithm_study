# 15666. N과 M (12) (백트래킹)

import sys
input = sys.stdin.readline

def back_tracking(level):
    if len(path) == M:  # 기저 조건
        print(*path)
        return

    for i in range(level, len(arr)):    # 매개변수로 받은 level(인덱스 번호)부터 시작
        path.append(arr[i])
        back_tracking(i)    # 재귀 들어갈 인덱스 변수 i
        path.pop()

N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))    # set 중복을 제거 / sorted 정렬된 리스트 반환
path = []
back_tracking(0)
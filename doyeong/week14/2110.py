# 2110. 공유기 설치 (이분 탐색)

import sys
input = sys.stdin.readline

def bs(s, e):
    while s <= e:
        mid = (s + e) // 2  # 중간값 즉, 공유기의 거리

        start = arr[0]  # 첫 공유기 위치는 arr[0]
        cnt = 1         # 첫 공유기를 설치
        for i in arr:
            if start + mid < i: # 설치지점 + 공유기 거리에서 i를 벗어나면
                start = i       # 공유기를 설치하고 설치지점 start를 업데이트
                cnt += 1        # 카운팅 + 1
            if cnt >= C:        # 공유기 설치수가 최대 개수 C에 도달하면
                s = mid + 1     # mid 탐색 범위를 늘리기 위해 이분 탐색의 오른쪽 범위를 탐색
                break
        if cnt >= C:
            s = mid + 1
        else:
            e = mid - 1
    print(s)


N, C = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])  # 정렬된 리스트로 받기
start, end = 1, arr[-1] # 시작점과 끝점을 1과 최댓값으로 설정
bs(start, end)
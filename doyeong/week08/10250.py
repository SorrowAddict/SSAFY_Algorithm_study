# 10250. ACM 호텔

import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    # H 층수 / W 각 층의 방 수 / N 몇 번째 손님인지
    H, W, N = map(int, input().split())

    # N을 H로 나눈 나머지가 층
    floor = N % H
    # N을 H로 나눈 몫에서 1번방부터 배치
    room = N // H + 1

    # 예외 케이스 처리
    if floor == 0:
        floor = H
        room -= 1
    
    print(floor*100 + room)
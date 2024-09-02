# SWEA_1859번, 백만 장자 프로젝트

import sys
sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    # 뒤집어서 받기
    arr = list(map(int, input().split()))[::-1]
    total_price = 0
    max_price = 0
    for price in arr:
        if max_price < price:
            max_price = price
        # 차익을 더하기
        else:
            total_price += (max_price - price)
    print(f'#{tc} {total_price}')
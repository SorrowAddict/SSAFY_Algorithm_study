# SWEA_1860번, 진기의 최고급 붕어빵

import sys
sys.stdin = open('input.txt')

TIME = 11112

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer_cnt = [0] * TIME

    t_arr = list(map(int, input().split()))
    # 카운트 배열 활용
    for t in t_arr:
        customer_cnt[t] += 1
    total_customer = 0
    answer = "Possible"
    for t in range(TIME):
        # 총 고객을 누적
        total_customer += customer_cnt[t]
        # 누적된 고객만큼 붕어빵을 만들 수 있다면
        if (t // M * K) < total_customer:
            answer = "Impossible"
            break
    print(f'#{tc} {answer}')
# 1436. 영화감독 숌 (완탐)

# 처음 문제를 풀 때는 어떻게 풀어야 할 지 굉장히 헤맸던 문제.
# 완탐으로 1씩 증가시키면서 숫자 안에 '666'이 들어있으면
# 리스트에 담아서 저장하면서 숫자를 세서 확인하는 방법.

import sys
input = sys.stdin.readline

N = int(input())

lst = []
num = 0
while 1:
    num += 1
    if '666' in str(num):
        lst.append(num)
        if len(lst) == N:
            print(lst[-1])
            break
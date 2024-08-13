# 1676 팩토리얼 0의 개수

"""
N! 을 계산하지 않고 풀기
- 소인수 분해의 원리를 이용한다.
- 소인수 분해 했을 때,
    2의 지수가 3
    5의 지수가 2
    이면, 뒤에서 부터 구한 0의 개수는 2개이다.
"""

N = int(input())

two = 0
five = 0

for num in range(2, N+1):
    while num % 2 == 0:
        two += 1
        num /= 2

    while num % 5 == 0:
        five += 1
        num /= 5

if two > five:
    print(five)
else:
    print(two)

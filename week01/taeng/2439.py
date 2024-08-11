#2439번, 별 찍기 - 2

N = int(input())

for i in range(1, N + 1):
    # 문자열 연산 이용
    line = ' ' * (N - i) + '*' * i
    print(line)
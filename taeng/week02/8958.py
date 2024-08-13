# 8958 OX퀴즈

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    # X를 기준으로 스플릿해서 연속된 O를 가지는 리스트 생성하기
    scores = input().split('X')
    total = 0
    for s in scores:
        N = len(s)
        # 1~N까지의 합은 (1+N)/2*N 이라는 공식 이용하기
        # 나누기 연산 과정에서 float로 형변환 되므로 다시 int로 형변환 해주기
        total += int((N + 1) / 2 * N)
    print(total)

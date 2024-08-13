# 숫자 3개 입력
A = int(input())
B = int(input())
C = int(input())

# 숫자 B를 문자열로 변환
b = str(B)

# 숫자 B를 문자열로 변환했을 때 이 문자열의 길이
b_len = len(b)

# 숫자 B의 자릿수만큼 A에 곱해준뒤 계산 진행
sum = A*(10**(b_len))+B-C
print(A+B-C)
print(sum)
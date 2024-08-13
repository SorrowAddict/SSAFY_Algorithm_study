N = int(input())
numbers = input()

result = 0
# 각 str형 숫자를 int로 변환 후 합산
for n in numbers:
    result += int(n)

print(result)
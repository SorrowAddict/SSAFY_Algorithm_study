a = int(input())
b = int(input())
c = int(input())

# 수로 생각했을 때 결과값
result_1 = a + b - c
# 문자열로 생각했을 때 결과값
result_2 = int(str(a) + str(b)) - c

print(result_1)
print(result_2)
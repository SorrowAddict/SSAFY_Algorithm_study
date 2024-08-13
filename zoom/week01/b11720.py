#Test케이스와 넘버 활용을 위해 문자열 iterable이니까 문자열 한개씩 접근하자
Test = int(input())
N = input() #string type으로 하나씩 접근

total = 0
for number in N:
    total += int(number)

print(total)
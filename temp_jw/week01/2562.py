# 인덱스 크기가 9인 빈 리스트 할당
list_num = []*9 

# 9번 반복해서 숫자를 입력하고 이 숫자를 빈 리스트에 삽입
for i in range(9):
    
    num = int(input())
    list_num.append(num)

#리스트에서 가장 큰 값과 인덱스를 찾고 인덱스에 1을 더해서 리스트에서 순서를 찾음
a = max(list_num)
print(a)
print(list_num.index(a)+1)
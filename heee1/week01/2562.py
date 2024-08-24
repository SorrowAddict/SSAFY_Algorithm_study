# 서로 다른 9개의 자연수 입력
num_lst = []
for i in range(9):
    numbers = int(input())
    num_lst.append(numbers)

# 최댓값
num = max(num_lst)
print(num)

# 최댓값이 몇 번째 수인지
for pos in range(len(num_lst)):# pos가 인덱스(0부터 시작)
    if num == num_lst[pos]:
      pos = pos + 1

      print(pos)
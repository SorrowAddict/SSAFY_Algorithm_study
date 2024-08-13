N = input()
num = input()

num_list = [] # num_list 만들기
for i in num:
  num_list.append(i)

result = 0
for i in num_list:
  result += int(i) # num_lsit 순회하며 result에 더하
print(result)
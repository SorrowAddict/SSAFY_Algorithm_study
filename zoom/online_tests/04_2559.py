#전체 날짜, 연속적 날짜
N, K = map(int, input().split())
num_list = list(map(int, input().split()))

first_sum = 0
for i in range(K):
    first_sum += num_list[i]

#윈도우 슬라이딩 -> 배운거써먹기
max_sum = first_sum

move = first_sum
for i in range(K, len(num_list)):
    move = move + num_list[i] - num_list[i-K]
    if max_sum < move:
        max_sum = move
print(max_sum)




###########초기코드 (시간초과) ###########
N, K = map(int, input().split())
num_list = list(map(int, input().split()))

max_num = 0
for i in range(len(num_list)-K):
    sum = 0
    for j in range(i, i+K): #원하는 범위 만큼 더하기
        sum += num_list[j]
    if max_num < sum :
        max_num = sum
print(max_num)


# 2635번, 수 이어가기
N = int(input())
max_arr = []
max_length = -1
for n in range(N//2, N+1):
    arr = [N, n]
    temp = arr[-2] - arr[-1]
    arr.append(temp)
    while True:
        temp = arr[-2] - arr[-1]
        if temp < 0:
            break
        arr.append(temp)
    if max_length < len(arr):
        max_length = len(arr)
        max_arr = arr
print(max_length)
print(*max_arr)

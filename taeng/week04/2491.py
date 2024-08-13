# 2491번, 수열

N = int(input())
arr = list(map(int, input().split()))
k_1 = 1
k_2 = 1
max_k = 1
for i in range(1, len(arr)):
    if arr[i] >= arr[i - 1]:
        k_1 += 1
    else:
        k_1 = 1
    if arr[i] <= arr[i - 1]:
        k_2 += 1
    else:
        k_2 = 1

    if max_k < k_1:
        max_k = k_1
    if max_k < k_2:
        max_k = k_2
print(max_k)
n = int(input())

arr = list(map(int, input().split()))
arr2 = []
for i in range(1,n+1):
    arr2.append(i)

for i in range(1, n): # 1~n-1 값만큼 반복
    for j in range(arr[i]): # j가 1이면 arr[1]인 1, j가 2이면 arr[2]인 1, j가 3이면 arr[3]인 3, j가 4이면 arr[4]인 2만큼 앞자리와 교환을 하겠다
        arr2[i-j] , arr2[i-1-j] = arr2[i-1-j], arr2[i-j]
print(*arr2)
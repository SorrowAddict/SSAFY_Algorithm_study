N = int(input()) #색종이 개수

arr = [[0]*1002 for _ in range(1002)]
idx = 0
for tc in range(N):
    idx += 1
    col1, row1, plus_col, plus_row = map(int, input().split())
    for row in range(1001-row1, 1001 - row1 - plus_row, -1):
        for col in range(col1, col1+plus_col):
 #가려지는데,,
            arr[row][col] = idx 
for i in range(1,N+1): 
    count = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == i:
                count += 1
    if count == 0:
        print(0)
    else:
        print(count)
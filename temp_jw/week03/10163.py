a = int(input())
matrix = list([0] *1001 for _ in range(1001))
for i in range(1, a+1):
    x, y, width, height = map(int, input().split())
    for k in range(x, x+width):
        for l in range(y, y+height):
            matrix[k][l] = i
                
n = len(matrix)
m = len(matrix[0])
for i in range(1, a+1): 
    count = 0
    for j in range(n):
        for k in range(m):
            if matrix[j][k] == i:
                count += 1
    print(count)
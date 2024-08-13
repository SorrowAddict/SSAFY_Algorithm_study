N = int(input())

max_len = 0
max_result = []
for i in range(1, N):
    temp = [N]
    temp.append(i)
    while temp[-2] - temp[-1] > 0:
        result = temp[-2] - temp[-1]
        temp.append(result)

        if max_len < len(temp):
            max_len = len(temp)
            max_result = temp
print(max_len)
for max in max_result:
    print(max, end = " ")
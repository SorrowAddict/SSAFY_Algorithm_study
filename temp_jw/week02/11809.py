a = list(input())
str_alpha = 'abcdefghijklmnopqrstuvwxyz'
list_num = [-1]*26

for i in range(len(str_alpha)):
    for j in range(len(a)):
        if str_alpha[i] == a[j]:
            if list_num[i] == -1:
                list_num[i] = j

print(*list_num)
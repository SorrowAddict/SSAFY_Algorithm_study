def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input())
list_num = list(str(factorial(num)))
count = 0
list_reverse = list_num[::-1]
for i in range(len(list_reverse)):
    if int(list_reverse[i]) == 0:
        count+=1
    elif int(list_reverse[i]) !=0:
        break
print(count)
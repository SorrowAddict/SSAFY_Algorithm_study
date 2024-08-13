def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
list_height = []
for _ in range(9):
    a = int(input())
    list_height.append(a)
sum = 0

for i in list_height: #입력받은 값들을 다 더한다.
    sum += i
sum = sum -100 # 여기서 100을 빼준다.
a = b = 0
for i in range(len(list_height)): 
    for j in range(i+1, len(list_height)):
        if list_height[i]+list_height[j] == sum: # 총합에서 100을 뺀 값과 합이 동일한 두 값을 찾는다.
            a = (list_height[i]) # 첫 값은 a에
            b = (list_height[j])  # 두번째 값은 b에

list_height.remove(a) # a를 없앤다.
list_height.remove(b)  # b를 없앤다.

bubble_sort(list_height) # 버블 정렬로 오름차순으로 정렬

for i in list_height:
    print(i)
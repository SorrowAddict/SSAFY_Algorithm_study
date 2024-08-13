### 2562번

array = [0] * 9
temp = 0
idx = 0
for i in range(9):
    # 9개의 자연수 한 줄씩 입력 받기
    array[i] = int(input())
    if array[i] > temp:
        # 최댓값 저장
        temp = array[i]
        # 최댓값의 인덱스 저장
        idx = i

print(temp)
print(idx + 1)

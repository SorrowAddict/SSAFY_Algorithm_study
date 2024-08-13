# 멋있다!!!

def bubble_sort(arr): # 버블 정렬 함수 정의
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

n, m = map(int, input().split())
x = int(input())
coly = [] # 세로값을 넣기 위한 리스트 선언
rowx = [] # 가로값을 넣기 위한 리스트 선언
for i in range(x):
    dir, line = map(int, input().split()) 
    if dir == 0: # 가로이면 rowx에 넣는다
        rowx.append(line)
    else: # 세로이면 coly에 넣는다
        coly.append(line)
rowx.append(0) # 각 리스트에 0과
rowx.append(m) # 세로길이 넣기
coly.append(0) # 각 리스트에 0과
coly.append(n) # 가로길이 넣기
area = [] # 넓이를 넣기 위한 리스트 선언
rowx = bubble_sort(rowx) # 버블 정렬을 통해 오름차순으로 정렬 0~n까지
coly = bubble_sort(coly) # 버블 정렬을 통해 오름차순으로 정렬 0~m까지
width = [] # 값들의 차이로 구한 가로값이 들어갈 리스트
height = [] # 값들의 차이로 구한 세로값이 들어갈 리스트
for i in range(1,len(rowx)): # 값을 빼면서 넓이에 들어갈 수 구해주기
    result_row = rowx[i]-rowx[i-1] # 오름차순으로 정렬되어있기 때문에 현재값에서 이전 인덱스 값을 빼주면 된다.
    width.append(result_row) # 가로 리스트에 삽입

for i in range(1,len(coly)): # 값을 빼면서 넓이에 들어갈 수 구해주기
    result_col = coly[i]-coly[i-1] # 오름차순으로 정렬되어있기 때문에 현재값에서 이전 인덱스 값을 빼주면 된다.
    height.append(result_col) #세로 리스트에 삽입

for i in width: # 모든 수에 대해 가로 곱하기 세로
    for j in height:
        result = i*j # 각각의 사각형의 넓이 구하기
        area.append(result) # area에 넓이 삽입
 
print(max(area)) # 사각형의 넓이 중 최대 값 구하기
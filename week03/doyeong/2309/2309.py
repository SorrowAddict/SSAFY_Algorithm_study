import sys

input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]  # 배열로 입력을 받기
arr.sort()      # 미리 정렬해준다

check_num = sum(arr)-100        # 100 = sum(arr) - check_num
for idx_x, x in enumerate(arr): # pop 을 하기 위해 enumerate 사용
    for idx_y, y in enumerate(arr):
        # 9개 중 2개를 뺐을 때 100이 되는 값이고 x와 y가 다를 때
        # 중복된 연산이 안되도록 체크
        if x + y == check_num and x != y and sum(arr)>100:
            arr.pop(idx_y)  # x -> y 순서로 돌리기 때문에 y가 항상 더 높은 인덱스
            arr.pop(idx_x)  # l.pop(idx) 인덱스 번호를 기준으로 pop 하는 것을 이용
            break
# 리스트 컴프리헨션을 사용해 str타입으로 바꿔주고 '\n'.join 을 이용해 줄넘김
print('\n'.join(str(x) for x in arr))
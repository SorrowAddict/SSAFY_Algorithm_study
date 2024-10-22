# 1541. 잃어버린 괄호 (구현)

import sys
S = sys.stdin.readline().strip().split('-')     # -로 split
temp = []
for i in S:     # -로 나뉜 리스트를 순회
    cnt = 0
    for j in i.split('+'):  # 그 속에서 +로 나눈 리스트를 순회
        cnt += int(j)       # cnt 변수에 쌓기
    temp.append(cnt)
result = temp[0]            # 초기값은 + 값이므로 지정
for i in temp[1:]:          # 2번째 값부터 (1번 인덱스부터) 초기값에서 -= 연산
    result -= i
print(result)
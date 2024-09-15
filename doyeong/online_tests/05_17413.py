# 17413. 단어 뒤집기 2

# import sys
from collections import deque
# input = sys.stdin.readline

S = input()
que = deque()
chk = False     # 부등호 안인지를 체크할 변수

result = ''
for x in S:
    if x == '<':        # 부등호가 시작되면
        chk = True      # 체크 시작
        while que:      # 이전까지 있던 값들을 거꾸로 출력
            result += que.pop()
    que.append(x)       # 부등호 que에 push
    if x == '>':        # 부등호가 닫히면
        chk = False     # 체크 풀기
        while que:
            result += que.popleft() # 부등호 안의 que를 정방향으로 출력
    
    # 공백이고 and 부등호 안이 아닐때만
    if x == ' ' and chk == False:
        que.pop()       # 공백을 잠시 뺐다가
        while que:
            result += que.pop() # 이전까지의 값을 거꾸로 출력
        result += ' '   # 뒤에 공백 출력
else:
    while que:          # 순회가 다 끝났을 때 que의 남은 요소들을
        result += que.pop()     # 거꾸로 출력
print(result)
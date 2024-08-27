# 1158. 요세푸스 문제

# ------------------- #
# 1st 풀이 
# (python으로는 실패, pypy3으로 성공)
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = deque(list(range(1, N+1)))    # 1~N 까지의 deque 리스트 생성
lst = []                            # 정답을 저장할 리스트
i = 0                               # try 횟수를 늘려나갈 변수 i
while len(lst) < N:                 # 정답 리스트가 N개 도달하기 전까지 (리스트가 N개가 찰때까지 실행)
    temp = arr.popleft()        # 처음 값부터 뽑아서 temp에 저장
    if (i+1)%K == 0:            # (뽑은 인덱스 +1)를 K로 나누어 떨어지면
        lst.append(temp)        # 정답 리스트에 추가하고 arr에서 버림
    else:
        arr.append(temp)        # 뽑아야할 인덱스가 아니면 arr의 뒤로 push 
    i += 1                      # i값 증가
print('<'+', '.join(map(str, lst))+'>') # 결과 출력

# ------------------- #
# 2nd 풀이 
# (Python으로도 성공, 하지만 여전히 긴 실행 시간)
# l.append()의 실행 시간이 무거운 것 같아 빼낼 변수를 발견했을 때 바로 출력
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = deque(list(range(1, N+1)))
print('<', end='')
i, cnt = 0, 0
while cnt < N:
    temp = arr.popleft()
    if (i+1)%K == 0:
        cnt += 1
        print(temp, end='')         # 그때그때 바로 출력하게 함
        if cnt != N:
            print(', ', end='')     # 마지막 출력의 경우 ', ' 생략
    else:
        arr.append(temp)
    i += 1
print('>')

# ------------------- #
# 3rd 풀이 
# (실패, 규칙성을 찾아서 deque 없이 풀 수 있을 것 같아서 시도)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(range(1, N+1))
cnt, result = 0, ''
while cnt < N:
    cnt += 1
    result += str(arr[(cnt*K -1)%N -(cnt*K)//N])
print('<'+', '.join(result)+'>')

# ------------------- #
# 4th 풀이 
# (i 값을 계속 변화시키면서 pop(i)를 통해서 뽑아내는 방식)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(range(1, N+1))
result = []
i = 0
while arr:
    i = (i + K - 1) % len(arr)      # 하나씩 인덱스를 뽑아갈 것 이므로 -1를 붙임, 이에 따라 len(arr)도 변화
    result.append(arr.pop(i))
print('<' + ', '.join(map(str, result)) + '>')
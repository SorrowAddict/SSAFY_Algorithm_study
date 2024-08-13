# 백준에 첫 코드를 돌렸는데 코드 돌아가는 시간이 너무 길어서 줄여보고자 사용
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 1. 2차원 배열 생성 [[여자, 남자], * 6] # 리스트 안의 리스트는 같은 학년을 의미
lst = [[0, 0] for i in range(6)]
for i in range(N):
    S, Y = map(int, input().split())
    # 2. lst 해당 항목에 +1
    lst[Y-1][S] += 1

cnt = 0
# 3. lst를 순회하면서 1학년부터 6학년까지 case를 순회
for case in lst:
    # 4. case안의 [여자수, 남자수]를 i로 하나씩 돌아가면서
    for i in case:
        # 5. 아래 코드는 7/29 오늘 풀었던 오르락내리락 & 물채우기 문제 관련 코드
        cnt += i//K
        if i % K:
            cnt += 1
print(cnt)
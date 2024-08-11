import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

result = []     # 결과값을 저장할 리스트
# l.insert(idx, value) 함수를 이용하기 위해 enumerate(list)를 사용
for idx, x in enumerate(nums):
    # 문제는 왼쪽으로 줄을 세웠지만 reversed 혹은 [::-1]을 사용할 수 있기 때문에 오른쪽으로 줄을 세움
    result.insert(x, idx+1)

print(*result[::-1])    # 결과 뒤집고 언패킹으로 출력
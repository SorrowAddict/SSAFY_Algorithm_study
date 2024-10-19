# 15663. N과 M (9) (백트래킹)

# 입력값에 중복이 있을 수 있지만 출력값 리스트에는 중복 X
# 단, 같은 수로 된 리스트는 O
# $ 해결 방법을 찾지 못해서 코드 서칭을 통해 이해한 문제

def perm_recur(n):
    if n == M:
        print(*path)
        return

    check = 0   # 중복된 수열을 출력하는 것을 방지
    for i in range(len(arr)):
        # 방문하지 않았고 이전에 썼던 값이 아니면
        if not used[i] and check != arr[i]:
            path.append(arr[i])
            used[i] = True
            check = arr[i]
            perm_recur(n+1)
            used[i] = False
            path.pop()

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
used = [0] * N
path = []
perm_recur(0)
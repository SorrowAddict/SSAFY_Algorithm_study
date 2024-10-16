# 15652. N과 M (4) (중복조합)

def comb_recur(level, start):
    if level == M:
        print(*path)
        return

    # 중복을 허용하므로 start에서 그대로 시작
    for i in range(start, N+1):
        path.append(i)
        comb_recur(level+1, i)
        path.pop()

N, M = map(int, input().split())
path = []
comb_recur(0, 1)
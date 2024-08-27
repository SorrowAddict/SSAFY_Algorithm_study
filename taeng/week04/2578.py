# 2578번, 빙고

bingo_matrix = [list(map(int, input().split())) for _ in range(5)]

# 빙고 개수를 체크
def bingo_check(matrix):
    bingo_cnt = 0
    # 행마다 검사
    for i in range(5):
        is_bingo = True
        for j in range(5):
            if matrix[i][j] != -1:
                is_bingo = False
                break
        if is_bingo:
            bingo_cnt += 1
    # 열마다 검사
    for j in range(5):
        is_bingo = True
        for i in range(5):
            if matrix[i][j] != -1:
                is_bingo = False
                break
        if is_bingo:
            bingo_cnt += 1
    # 대각선 검사 1
    is_bingo = True
    for i in range(5):
        if matrix[i][i] != -1:
            is_bingo = False
            break
    if is_bingo:
        bingo_cnt += 1
    # 대각선 검사 2
    is_bingo = True
    for i in range(5):
        if matrix[5-1-i][i] != -1:
            is_bingo = False
            break
    if is_bingo:
        bingo_cnt += 1

    return bingo_cnt

num = []
for _ in range(5):
    num += list(map(int, input().split()))

for n in range(25):
    for i in range(5):
        for j in range(5):
            if num[n] == bingo_matrix[i][j]:
                bingo_matrix[i][j] = -1 
    # 빙고 개수가 3개 이상이면 몇번째 수인지 출력
    if bingo_check(bingo_matrix) >= 3:
        print(n + 1)
        break
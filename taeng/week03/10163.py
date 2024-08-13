# 10163번, 색종이

def main():
    visited = [[False] * 1001 for _ in range(1001)]

    N = int(input())

    pos = [None] * 101
    pos_top = -1
    cnt = [None] * N
    cnt_top = -1
    # 스택에 색종이 붙일 위치 넣기
    for _ in range(N):
        x, y, dx, dy = map(int, input().split())
        pos_top += 1
        pos[pos_top] = (x, y, dx, dy)
    # 스택에서 꺼내면서 역으로 색종이 붙이기
    while pos_top >= 0:
        x, y, dx, dy = pos[pos_top]
        # 스택 pop()
        pos_top -= 1
        total = 0
        # 해당 색종이 붙이기
        for i in range(x, x + dx):
            for j in range(y, y + dy):
                # 해당 위치에 색종이가 붙여지지 않았다면
                if not visited[i][j]:
                    # 색종이 붙이기
                    visited[i][j] = True
                    total += 1
        # 색종이를 붙인 넓이 카운트
        cnt_top += 1
        cnt[cnt_top] = total
    # 색종이 넓이 출력해주기
    while cnt_top >= 0:
        print(cnt[cnt_top])
        cnt_top -= 1


if __name__ == "__main__":
    main()
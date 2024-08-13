# 10158번, 개미

# 가장 자리 값
w, h = map(int, input().split())
# 시작 위치, pos[0], pos[1]: 현재 위치 x, y
pos = list(map(int, input().split()))
# 이동 횟수
k = int(input())
# 제자리로 돌아오는 부분 고려 X
x = k % (2 * w)
y = k % (2 * h)
# x, y 방향으로 나눠서 움직이기
dx = 1
for i in range(x):
    if pos[0] + dx > w:
        dx = -1
    elif pos[0] + dx < 0:
        dx = 1
    pos[0] += dx
dy = 1
for i in range(y):
    if pos[1] + dy > h:
        dy = -1
    elif pos[1] + dy < 0:
        dy = 1
    pos[1] += dy

print(*pos)

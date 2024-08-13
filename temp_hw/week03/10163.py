# 각 색종이의 보이는 부분의 면적 구하기
# 색종이 장수
N = int(input())

# 1001칸이면 인덱스는 0 ~ 1000
arr = [[0]*1000 for _ in range(1000)]

# 색종이 정보 저장
papers = []

# 색종이 N개가 한 도화지에 표시
for i in range(N):                          # i: 색종이 번호
    x, y, w, h = map(int, input().split())  # x(열), y(행), 너비(width), 높이(height)
    papers.append((x, y, w, h))             # 색종이 정보 튜플로 리스트에 저장
    for r in range(y, y+h):                 # 색종이 범위 칠하기
        for c in range(x, x+w):
            arr[r][c] = i + 1               # 색종이 번호로 칠하기. 1번 색종이면 1, 2번 색종이면 2

# ----------------------------------------------
# 각 색종이 보이는 면적 계산
for j in range(N):
    x, y, w, h = papers[j]                  # 저장해뒀던 색종이 정보 불러오기
    count = 0
    for r in range(y, y+h):
        for c in range(x, x+w):
            if arr[r][c] == j + 1:          # 해당 색종이 번호와 일치하면 보이는 부분
                count += 1

    print(count)                 
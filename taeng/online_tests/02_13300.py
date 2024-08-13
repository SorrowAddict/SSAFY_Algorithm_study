n, k = map(int, input().split())

# 여학생, 남학생 1~6 학년 (0학년 제외)
girl = [0] * 7
boy = [0] * 7

for i in range(n):
    # 성별, 학년 입력 받기
    s, y = map(int, input().split())
    # 여학생의 경우
    if s == 0:
        girl[y] += 1
    # 남학생의 경우
    else:
        boy[y] += 1

room = 0
# 여학생 방 배정
for i in range(1, 7):
    # 방에 일정하게 모두 들어가는 경우
    if girl[i] % k == 0:
        room += girl[i] // k
    # 방에 일정하게 모두 들어가지 못하는 경우
    else:
        room += (girl[i] // k + 1)

# 남학생 방 배정
for i in range(1, 7):
    # 방에 일정하게 모두 들어가는 경우
    if boy[i] % k == 0:
        room += boy[i] // k
    # 방에 일정하게 모두 들어가지 못하는 경우
    else:
        room += (boy[i] // k + 1)

print(room)
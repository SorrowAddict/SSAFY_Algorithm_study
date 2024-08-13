h, m = map(int, input().split())

# 분으로 변환해서 합산
time = h * 60 + m - 45

# 23:59 을 넘어가면
if time >= 24 * 60:
    time -= 24 * 60
# 0:0 을 넘어가면
elif time < 0:
    time += 24 * 60

# 다시 시, 분으로 변환
print(time // 60, time % 60)

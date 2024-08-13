#####################
# max / index 사용  #
#####################

num = []
for _ in range(9):
    num.append(int(input()))
max_num = max(num)
print(max_num)
print(num.index(max_num)+1)

######################
# max / index 미사용 #
######################

H, M = list(map(int, input().split()))


if H >= 24:
    H = H - 24
elif H == 0:
    H = 24 - (H)
if M >= 60:
    H = H + (M // 60)
    M = M - 60 #H에 값이 더해짐


# 15 - 45 = -30
if M < 45:
    M = M - 45 + 60
    H -= 1
else :
    M -= 45

print(H, M)
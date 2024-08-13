# 2309 일곱 난쟁이

# 9명의 난쟁이의 키
height = [0] * 9
# 9명의 난쟁이의 키 총합
total = 0

# 9명의 난쟁이의 키 입력과 총합 합산
for i in range(9):
    height[i] = int(input())
    total += height[i]

is_check = False
# 9명의 난쟁이 중 2명 선택
for i in range(0, 8):
    for j in range(i + 1, 9):
        # 제외할 난쟁이를 찾음
        if total - height[i] - height[j] == 100:
            # 제외할 난쟁이 키 -1로 변경
            height[i] = -1
            height[j] = -1
            is_check = True
            break
    # 제외할 난쟁이 찾은 경우 더 이상 찾지 않음
    if is_check:
        break

# 버블 정렬
for i in range(8, 1, -1):
    for j in range(0, i):
        if height[j] > height[j + 1]:
            height[j], height[j + 1] = height[j + 1], height[j]

# 인덱스 2부터 출력
for i in range(2, 9):
    print(height[i])

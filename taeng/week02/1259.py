# 1259 팰린드롬수

while True:
    # 정수형으로 값 받기
    num = list(map(int, list(input())))

    # 값이 0 이면 실행 끝내기
    if num == [0]:
        break

    is_equal = True

    for i in range(len(num) // 2):
        # 좌우 대칭되는 값이 다르면
        if num[i] != num[len(num)-1-i]:
            is_equal = False
            break
    
    if is_equal:
        print('yes')
    else:
        print('no')

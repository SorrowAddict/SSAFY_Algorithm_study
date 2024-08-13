# 14696번, 딱지놀이

def selection_sort(arr):
    N = len(arr)
    for i in range(N - 1):
        min_idx = i
        for j in range(i, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

N = int(input())

for _ in range(N):
    # 카드 오름차순 정렬하기
    a_card = selection_sort(list(map(int, input().split()))[1:])
    b_card = selection_sort(list(map(int, input().split()))[1:])

    # 경기가 끝났음을 체크
    is_over = False
    # 가장 높은 카드부터 서로 꺼냄
    while a_card and b_card:
        a = a_card.pop()
        b = b_card.pop()
        if a > b:
            result = 'A'
            is_over = True
            break
        elif a == b:
            continue
        else:
            result = 'B'
            is_over = True
            break

    # 결판이 나지 않은 경우
    if not is_over:
        if a_card:
            result = 'A'
        elif b_card:
            result = 'B'
        else:
            result = 'D'

    print(result)

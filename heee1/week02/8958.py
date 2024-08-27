T = int(input())

for tc in range(T): # 테스트 케이스 수 만큼 반복. 테스트 케이스 출력 필요X
    OX = input()
   
    total = 0 # O가 연속적으로 있을 때 누적합
    point = 0 # O일 때의 점수
    for i in range(len(OX)):
        if OX[i] == 'O': # 인덱스로 뽑아올 필요없었지만 매번 헷갈려하는 부분 중 하나라 사용해봄ㅋ
            point += 1
            total += point

        elif OX[i] == 'X': # else로 처리해도 되지만 직관적으로 표현해봄
            point = 0

    print(total)
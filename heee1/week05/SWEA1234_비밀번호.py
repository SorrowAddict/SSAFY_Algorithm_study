# 0 ~ 9 문자열에서 같은 번호로 붙어있는 상들을 소거하고 남은 번호를 비밀번호로 만드는 것

T = 10  # 10개의 테스트 케이스
for tc in range(1, T+1):
    N, pw = input().split()
    N = int(N)
    pw = list(str(pw))  # 문자열 리스트로 변형해줘야 순회, pop 사용 가능

    # i, i+1 비교해서 같으면 pop(인덱스)
    i = 0   # 인덱스 초기 설정
    while i < len(pw) - 1:          # i가 리스트의 마지막 인덱스보다 하나 작을 때까지
        if pw[i] == pw[i+1]:        # 기준위치와 그 다음위치의 값이 같다면
            pw.pop(i)               # 내 위치 pop
            pw.pop(i)               # 그 다음 위치 pop///i+1로 했다가 인덱스 오류남
            i = max(0, i-1)         # 다시 처음부터 순회해야되니까 인덱스 0으로 초기화라고 생각했는데 인덱스 오류남 -> 인공지능 선생님 추천방법...
                                    # 인덱스가 음수 되는 것을 방지
        else:   # 다르다면
            i = i + 1               # 계속 순회해야되니까 다음 인덱스로 만들어주기

    print(f'#{tc}', ''.join(pw))    # pw는 문자


'''
리뷰
1. 처음에 계산기 문제랑 비슷한가? 하면서 스택으로 풀면 되나? 싶었는데 스택이 몇개 필요한지, 언제 어떻게 넣고 꺼내야하는지를 못해서
2. 그냥 순회하면서 기준위치랑 다음 위치랑 비교하고 pop 하면 되지 않나라는 생각을 해봄
3. 별 생각없이 순회하려고 했는데 정수형은 순회 불가 -> 문자로 바꿈
4. pop은 리스트여야 사용가능 -> 리스트로 바꿈
5. 왜 마지막 output값 0 남아있음? -> 5-1 참고해 수정
5-1. 입력받은 비밀번호의 맨 앞에 0이 있는 경우, int() 함수를 사용하면 이 leading zero가 제거됨. 그러나 다시 문자열로 변환할 때 이 0은 포함되지 않음.
예를 들어, 입력이 "0123"이라면 int()로 변환 시 123이 되고, 다시 str()로 변환하면 "123".
'''


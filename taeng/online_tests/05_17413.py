# 17413번, 단어 뒤집기 2

string = input()
# 괄호 스택
stack_1 = [];
# 문자열 뒤집기 스택
stack_2 = [];
for ch in string:
    # 괄호 스택이 비어있지 않으면
    if stack_1:
        # '>'을 만나면 괄호 스택 pop() (정상 출력이 끝남)
        if ch == '>':
            stack_1.pop()
            print(ch, end="")
        # 계속 정상 출력
        else:
            print(ch, end="")
    # 괄호 스택이 비어있는 경우
    else:
        if ch == '<' or ch == " ":
            # 뒤집은 문자열 모두 출력해주기
            while stack_2:
                print(stack_2.pop(), end="")
            print(ch, end="")
            if ch == '<':
                stack_1.append(ch)
        # 스택에 계속 넣어주기
        else:
            stack_2.append(ch)
# 마지막 뒤집은 문자열 출력
while stack_2:
    print(stack_2.pop(), end="")
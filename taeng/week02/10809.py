# 10809 알파벳 찾기

string = list(input())

# 'a': index 0 ~ 'z': index 26
alphabet = [-1] * 26

# string 배열을 인덱스로 순회
for i in range(len(string)):
    # 해당 알파벳이 처음으로 나타났으면
    if alphabet[ord(string[i]) - ord('a')] == -1:
        # alphabet 배열에 인덱스를 저장
        alphabet[ord(string[i]) - ord('a')] = i

print(*alphabet)
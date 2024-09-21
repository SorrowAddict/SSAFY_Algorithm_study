# 1181. 단어 정렬

N = int(input())
lst = []

for i in range(N):
    lst.append(input())

# sorted() 메서드의 key 매개변수 사용, 람다를 이용해 구현
print('\n'.join(sorted(list(set(lst)), key= lambda i: (len(i), i))))
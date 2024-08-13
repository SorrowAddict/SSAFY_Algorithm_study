lst = list(map(str, input().split()))
print(len(lst))

# len() 없이 사용하는 방법
cnt = 0
for i in lst:
	cnt += 1
print(cnt)

# 사용자 지정 함수로 코드 재사용성이 가능하게 구현
def my_len(arr):
  len_cnt = 0
  for i in arr:
    len_cnt += 1
  return len_cnt
print(my_len(lst))   # == print(len(lst)) 와 결과가 같음
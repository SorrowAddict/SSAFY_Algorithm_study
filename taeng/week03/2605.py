# 2605번, 줄 세우기

N = int(input())
student_line = []
idx_arr = map(int, input().split())
# 해당 인덱스에 값 삽입하기
for std, idx in enumerate(idx_arr):
    student_line.insert(idx, std + 1)
print(*student_line[::-1])

# 입력받은 시간보다 45분 빠르게 만들기
H, M = map(int,input().split()) # H(시) M(분)

if M >= 45:# (분)이 45보다 크면
  print(f'{H} {M - 45}') # (분)에서 45분 빼기
elif H == 0 & M < 45 : # (시)가 0시이고 (분)이 45분보다 작다면
  print(f'23 {M + 15}') # (시)는 23시 (분)은 +60 -45 => +15
else: # 그렇지 않다면
  print(f'{H - 1} {M + 15}') # (시)에서 1시간 빼고 (분)에 60분 더하고 45분 빼기
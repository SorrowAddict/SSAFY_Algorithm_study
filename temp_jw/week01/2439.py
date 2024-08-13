a = int(input())

for i in range(1,a+1): #range(1,a+1) 를 통해 입력한 a값에 맞춰 ‘0~4’가 아닌 ‘1~5’로 i값을 설정
    k = a-i # i(별의 개수)가 커질수록 빈칸의 개수는 줄어들도록 설정하였음
    print(' '*k + '*'*i)
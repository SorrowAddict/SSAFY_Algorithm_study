a, b = map(int, input().split())

# 일찍 일어나야 하는 시간 구하기
wake_hour = (a*60 + b - 45) // 60
wake_minute = (a*60 + b - 45) % 60

# 입력받은 시간이 0시이면서 45분보다 작은경우
if (a == 0)&(b<45):

# 입력받은 시간에 24를 더해서 45분을 뺐을 때 0시 이전인 23이 나오도록 설계
    a+=24
    wake_hour = (a*60 + b - 45) // 60
    wake_minute = (a*60 + b - 45) % 60
    print(wake_hour, wake_minute)
    
# 나머지는 그냥 출력
else:
    print(wake_hour, wake_minute)
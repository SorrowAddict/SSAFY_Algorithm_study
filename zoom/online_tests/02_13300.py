N, K = list(map(int, input().split()))
student_list = []
for i in range(1, N+1):
    SY = list(map(int, input().split()))
    student_list.append(SY) #list로 묶어서
print(student_list) #list 내부 출력
#i번째에 2번째 인덱스가 1이라면? -> 그럼 인덱스가 1인것들만 묶음 -> 그룹화 방법.. --> dictionary
grouped_data = {}
for student in student_list:
    key = student[1] #student의 1번쨰 인덱스 값을 키로 두고
    if key not in grouped_data:
        grouped_data[key] = []
    grouped_data[key].append(student[0])
print(grouped_data)
group = list(grouped_data.values())
print(group)
total = 0
for g in group: #첫번째 배열 index -> 1의 내용이 나올 것
    g.sort() #첫번째거 정렬
    if len(g) < 2:
        total += 1
    else : #2보다 크거나 같으면 --> g안에 [1,0,1], 또 값이 다르면 찢어짐
        one = g.count(1)
        zero = g.count(0)



#########################
# --------------------- #

# 참가하는 학생수 N, 최대 인원수 K
# 성별 S(남1,여0), 학년 Y
# 생각한 접근 방법
# list로 성별과 학년을 구분한다
# 학년별로 묶고 -> 묶은 학년에서 성별을 우선적으로 묶는다
# 묶인 것들을 카운트하고, 나머지 값들을 개별적으로 센다
N, K = list(map(int, input().split()))
a_list = []
for _ in range(N):
    S, Y = list(map(int, input().split()))
    a_list.append([S,Y])
print(a_list)

# 똑같은거 있으면

#학년도 같고 성별도 같다면 -> 같이 묶고 그게 아니라면 일단 열외 --> zip쓰면 안될까?
#모두 순회를 해야할 것 같긴 해
#학년도 같고 성별도 같다면 --> 그럼 일단 학년끼리 다시 리스트 화 해야하지 않을까?


# 학년도 같고 성별도 같다면
#for i in range(len(Sex)): #성별과 학년에 index값이 똑같으니가..
#    if Sex[i] and Year[i] :


#result = list(zip(Sex, Year))
#print(result) #성별과 학년을 묶었어 -> tuple로
#같은 학년끼리 묶은 후 같은 성별 카테고리..
#for i in range(1,7): #학년별로 묶기
#    for y in Year: #1학년
#        if i == int(y): #1학년이라면
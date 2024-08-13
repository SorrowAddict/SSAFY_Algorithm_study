def score_sum(a):
    score = 0
    for i in range(1,len(a)+1):
        score += i
    return score
T = int(input())
for test_case in range(1, T+1):
    o_x = input()
    list_o_x = (o_x)
    list_o_x = list_o_x.split('X')
    list_o = []
    for i in range(len(list_o_x)):
        if 'O' in list_o_x[i]:
            list_o.append(list_o_x[i])
    sum = 0
    for i in range(len(list_o)):
        result = score_sum(list_o[i])
        sum += result
    print(sum)
    
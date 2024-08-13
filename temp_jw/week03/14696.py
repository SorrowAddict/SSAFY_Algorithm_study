T  = int(input())
for test_case in range(1,T+1):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr_a = a[1:len(a)]
    arr_b = b[1:len(b)]
    a_shape = [0]*5
    b_shape = [0]*5
    for i in range(len(arr_a)):
        if arr_a[i] == 4:
            a_shape[4] +=1
        elif arr_a[i] == 3:
            a_shape[3] +=1
        elif arr_a[i] == 2:
            a_shape[2] +=1
        elif arr_a[i] == 1:
            a_shape[1] +=1
    
    for i in range(len(arr_b)):
        if arr_b[i] == 4:
            b_shape[4] +=1
        elif arr_b[i] == 3:
            b_shape[3] +=1
        elif arr_b[i] == 2:
            b_shape[2] +=1
        elif arr_b[i] == 1:
            b_shape[1] +=1
    if a_shape[4] > b_shape[4]:
        print('A')
    elif a_shape[4] < b_shape[4]:
        print('B')
    else:
        if a_shape[3] > b_shape[3]:
            print('A')
        elif a_shape[3] < b_shape[3]:
            print('B')
        else:
            if a_shape[2] > b_shape[2]:
                print('A')
            elif a_shape[2] < b_shape[2]:
                print('B')
            else:
                if a_shape[1] > b_shape[1]:
                    print('A')
                elif a_shape[1] < b_shape[1]:
                    print('B')
                else:
                    print('D')
while True:
    pal = input() # 문자열로 입력
    if pal == '0':
        break
    elif pal == pal[::-1]: # 문자열로 받아와야 가능
        result = 'yes'
    else:
        result = 'no'
    print(result)
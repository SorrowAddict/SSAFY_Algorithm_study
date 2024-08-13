while 1:
    word = int(input())
    word_num = str(word)
    word_num = word_num[::-1]
    word_num = int(word_num)
    if word ==0:
        break
    if word_num==word:
        print('yes')
    else:
        print('no')
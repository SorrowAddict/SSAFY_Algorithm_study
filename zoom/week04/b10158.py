w, h = map(int, input().split()) #전체column, row
p, q = map(int, input().split()) #start위치
t = int(input()) #소요시간

#row -> 좌표를 만든상태에서는 -1, 1로 시작하는게 맞지만 지금은 단순 이동에 사용할 것이기 떄문에 굳이..
data_row = [1, -1]
data_col = [1, -1]

col = p
row = q
#대입 내용 잘보기 --> 여기서 문제!!!

time = 1 #애초에 설정할 때 1 move처음도 반영
r = c = 0
while time <= t:
    move_row = row + data_row[r]
    move_col = col + data_col[c]

    if 0 <= move_row <= h and 0 <= move_col <= w: #이건 좌표 기준 -> 지금은 6,4까지 가야하는 상황 부등호 다시!!
        row = move_row
        col = move_col
        time += 1
    else :
        if not 0 <= move_row <= h :
            r = (r+1) % 2
        if not 0 <= move_col <= w:
            c = (c+1) % 2 #c가 안바뀌는 문제..
print(col, row)
# a, b = map(int, input().split())
# list_boy =[0]*6
# list_girl =[0]*6
# list_num = []
# list_gen = []
# for i in range(a):
#     c, d = list(map(int, input().split()))
#     list_num.append(c)
#     list_gen.append(d)
# print(list_num)
# print(list_gen)
# gen_num = list(list(zip(list_num, list_gen)))
# print(gen_num)
# for k in range(a):
#     for j in gen_num:
#         if j[0] == 0:
#             list_girl[k] += 1
#         elif j[0] == 1:
#             list_boy[k] += 1

# print(list_girl)
# print(list_boy)

a, b = map(int, input().split())
list_boy =[0]*6
list_girl =[0]*6
gen_num = [(1, 1), (0, 1), (1, 1), (1, 2)]
list_boy[0,0,0,0,0,0]
for i in gen_num:
    if i[0] == 0:
        list_girl[i[1] - 1] += 1
    elif i[0] == 1:
	    # for 
        list_boy[i[1]-1] += 1

print(list_girl)
print(list_boy)
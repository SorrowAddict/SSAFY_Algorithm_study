# word = input()
# # 인덱스 번호 활용. z는 공백
# alphabet = 'abcdefghijklmnopqrstuvwxyz' # 26개
# result = [-1] * 26
#
# for char in word:
#     for i in range(len(alphabet)):
#         if char == alphabet[i]:
#             if char == 'z':
#                 result[i] = ' '
#             else:
#                 result[i] = i
#
#
# print(result)
"""
如果想生成一个平方列表，比如[1，4，9...] ,使用for循环怎么写，使用列表生成又该怎么写
"""

# list_square=[]
# for i in range(1,4):
#     list_square.append(i**2)
# print(list_square)
#
# list_square2=[i**2 for i in range(1,4)]
#
# print("list_square2",list_square2)
#
#
# list_square3=[i**2 for i in range(1,4) if i !=1 ]
# # list_square3=[]
# # for i in range(1,4):
# #     if i !=1:
# #         list_square3.append(i**2)
# # print(list_square3)

list_square4 = []
for i in range(1,4):
    for j in range(1,4):
        list_square4.append(i*j)
print(list_square4)
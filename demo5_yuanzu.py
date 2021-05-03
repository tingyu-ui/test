# #元组定义
# tuple_hogwarts = (1,2,3)
# tuple_hogwarts2 = 1,2,3
#
# print("tuple_hogwarts",tuple_hogwarts)
# print(type(tuple_hogwarts))
#
# print("tuple_hogwarts2",tuple_hogwarts2)
# print(type(tuple_hogwarts2))
#
# #元组不可表特性
# a = [1,2,3]
# tuple_hogwarts = (1,2,a)
# print(id(tuple_hogwarts[2]))
# tuple_hogwarts[2][0] = "a"
# print(id(tuple_hogwarts[2]))
# print(tuple_hogwarts)

a = (1,2,3,"a","a")
# print(a.count("a"))
print(a.index("a"))
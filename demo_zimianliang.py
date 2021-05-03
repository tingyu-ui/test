name = 'lili'
age = 20
list1 = [1,3,4]
dic1 = {'name':'tom','gender':'male'}

print (f"my name is {name}, age is {age},my list is {list1[1]}")
#大写
print(f"my name is {name.upper()}")

print(f"result is {(lambda x: x+1)(2)}")


#
# print('my list is {},dict is {}'.format(list1,dic1))
# print('my name is {0}, age is {1},{1},{1}'.format(name,age))
#
# namelist = ['lili','tom','jerry']
# print('we name : {}、{} and {} '.format(*namelist))
# print('my name is {name}, gender is {gender}'.format(**dic1))
# # print('my name is {}, gender is {} '.format(dic1))
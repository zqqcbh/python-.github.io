#依次打印（for
magicians = ['alice' , 'david' , 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick')
    print("I can't wait to see your next trick, " + magician + ".\n")
print('Thank you,everyone.that was a great magic show!')
#个人练习
pizis = ['haha' , 'hehe' , 'lala']
for pizi in pizis:
    print('I like ' + pizi + ' pizis')
print('\nI love all pizis!')

animals = ['dog' , 'cat' , 'pig']
for animal in animals:
    print('A' + animal + " would make a great pet.")
print('Any of these animals would make a great pet!')
#创建数值列表
for value in range(1,5):
    print(value)#打印不输出5
numbers = list(range(2,11,2))#设置步长为2
print(numbers)
squares = []
for value1 in range(1,11):
    squares.append(value1**2)
print(squares)
#数字统计
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits),max(digits),sum(digits))#最小最大以及总和
#列表解析强化版
squares0 = [value2**2 for value2 in range(1,11)]
print(squares0)
#个人练习
# for num0 in range(1,1000000):
#     print(num0)
# num2 = list(range(1,1000000))
# print(min(num2),max(num2),sum(num2))
for num3 in range(1,21,2):
    print(num3)
L_num3 = list(range(1,21,2))
print(L_num3)
for ber in range(3,31,3):
    print(ber)
L_ber = list(range(3,31,3))
print(L_ber)
for int1 in range(1,11):
    print(str(int1**3))
Lis = [Li**3 for Li in range(1,11)]
print(Lis)
#切片——使用列表的一部分
players = ['charles' , 'martina' , 'michael' , 'eli' , 'haha']
print(players[0:3])#依旧是左闭右开区间
print(players[:4])#没有指定第一个索引的情况下默认第一个是0
print(players[2:])#没有指定后面的索引时默认后面的索引是最后一个
print(players[-3:])#一个有趣的办法，输出的是后面三个
print(players[:3])#输出前三个
for player in players[:3]:
    print(player.title())
my_food = ['pizza' , 'falafel' , 'carrot cake']
friends_food = my_food[:]# : 表示从最开始到最后面
#错误示例
# friends_food = my_food输出结果是导致同加同减
my_food.append('cannoli')
friends_food.append('ice cream')
print('My favorite foods are: ')
print(my_food)
print('\nMy friends favorite foods are: ')
print(friends_food)
#个人检测
print('"The first three items in list are:"')
print(my_food[:3])
print('"The last three items in list are:"')
print(my_food[-3:])
print('"Three items from the middle of the list are:')
print(players[1:4])
print(pizis)
friends_pizis = pizis[:]
pizis.append('xixi')
friends_pizis.append('lulu')
print('My pizis are:')
for pizis0 in pizis:
    print(pizis0)
print('My friends pizis are:')
for friends_pizis0 in friends_pizis:
    print(friends_pizis0)
#元组不能改变
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 300#错误写法
#遍历元组
for dimension in dimensions:
    print(dimension)
#修改元组只能重新定义一整个元组
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)
foods = ('nood' , 'ice' , 'ceffe')
for food in foods:
    print(food)
# food[0] = 'di'
# print(food)
foods = ('nood' , 'haha' , 'hehe')
for food in foods:
    print(food)


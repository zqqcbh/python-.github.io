motorcycles = ['honda', 'yamaha' , 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducity'#修改元素直接顶替
print(motorcycles)
motorcycles.append('tianjia')#添加到末尾不影响其他元素
print(motorcycles)
#下列是对append的一些实例
motorcycles2 = []#首先创建一个空列表
motorcycles2.append('honda2')
motorcycles2.append('yamaha2')
motorcycles2.append('yamaha3')
print(motorcycles2)
#下列是关于元素的插入（insert
motorcycles2.insert(0,'ducity')#表示在位置0（表头）插入ducity
print(motorcycles2)
#下列是关于元素的删除(del
del motorcycles2[0]#注意书写格式
print(motorcycles2)#这里删除了表头元素，一样可以删除任意位置的，表头具有代表性
# del motorcycles2[2]
# print(motorcycles2)
#下列是关于元素的删除(pop弹出
popped_motorcycles2 = motorcycles2.pop()#相当于将它分为两部分，弹出栈顶元素（最后一个
print(motorcycles2)#原元素保留
print(popped_motorcycles2)#弹出元素弹出（栈顶）但是我们依旧能访问它（del不能访问
#实例
motorcycles3 = ['honda3', 'yamaha3', 'suzuki','haha','hehe']
# last_owned = motorcycles3.pop()
# print('the last motorcycle I owner was a ' + last_owned.title() + '.')
#弹出任意位置（pop（x））
any_owner = motorcycles3.pop(3)
print(motorcycles3)
print(any_owner)
#根据值删除元素(remove)（上面是根据位置删除
motorcycles3.remove('yamaha3')
print(motorcycles3)
#实例
too_expensive = 'suzuki'
motorcycles3.remove(too_expensive)
print(motorcycles3)
print('\nA ' + too_expensive.title() + 'is too expensive for me')#写出来删除的原因
#个人练习
guest_list = ['chares' , 'adam' , 'nola' , 'sola' , 'jel' , 'jack' , 'joshua']
print('\n I would like to invite ' + guest_list[0].title() + ',' + guest_list[-1].title() + ' and ' + guest_list[2].title() +' to my dinner')
print('But ' + guest_list[1].title() + 'have ill,so he cannot join us')
ill = 'chares'
guest_list.remove(ill)
new = 'roha'
guest_list.insert(0,new)
print('so I invite ' + new.title())
message = 'At the end time, I invite as follow:'
print(message)
print(guest_list)
message2 = 'I find a bigger table ,so a plan to invite someone to my dinner'
guest_list.insert(0,'lee')
guest_list.insert(5,'hehe')
guest_list.insert(9,'haha')
message4 = 'So the guest list as follow:'
print(message4)
print(guest_list)
message6 = "\nI'm so sorry to cannot to invite someone,because the table cannot timely delivery, "
message5 = "\nI'm so sorry to cannot to invite you,because the table cannot timely delivery, "
print(message6)
popped_guest1 = guest_list.pop()
print(message5 + popped_guest1.title())
popped_guest2 = guest_list.pop()
print(message5 + popped_guest2.title())
print('For otherone you are still in the guest list')
# del guest_list
#接下来讲排列（sort
cars = ['bmw','audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#下面是反排列（reverse=Ture
cars.sort(reverse=True)
print(cars)
#下列是临时排列(sorted
cars1 = ['bmw','audi', 'toyota', 'subaru']
print('\n Here is the original list:')
print(cars1)
print('\n Here is the sorted list :')
print(sorted(cars1))
print('\n Here is the original list:')
print(cars1)
#反排列同理传参数reverse=Ture即可
#反转列表,不是字母顺序
print(cars)
cars.reverse()
print(cars)
#确定列表长度
m=len(cars)
print(m)#len函数需要打印，是从一开始计数的
#个人练习
mytrip = ['london' , 'tokyo' , 'mogao' , 'summer palace' , 'egypt']
print(mytrip)#打印原来
print(sorted(mytrip))#临时排序
print(mytrip)#确认顺序未变
print(sorted(mytrip,reverse=True))#临时颠倒顺序
print(mytrip)#确认顺序未变
mytrip.reverse()
print(mytrip)
mytrip.reverse()
print(mytrip)
mytrip.sort()
print(mytrip)
mytrip.sort(reverse=True)
print(mytrip)
mun = len(guest_list)
print('一共有' + str(mun)+ "人")


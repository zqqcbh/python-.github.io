cars = ['audi' , 'bmw' , 'subaru' , 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
car = 'bwm'
print(car == 'bwm')#检查是否相等
print(car == 'hha')
print(car == 'BWm')#大小写也在考虑范围以内
print(car.upper() == 'BWM')#可以转换
print(car)#这个比较并不影响变量的值
#下面是判断是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('hold the anchovies!')
age = 18
print(age == 18)
answer = 17
if answer != 42:
    print('That is not the correct answer.Please try again!')
num =[num1 for num1 in range(1,9)]
print(num)
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >=21)
age_1 = 22
print(age_0 >= 21 and age_1 >=21)
print((age_0>=21)and(age_1>=21))
#or的使用
age_0 =22
age_1 = 18
print(age_0>=21 or age_1>=21)
age_0 = 18
print(age_0>=21 or age_1>=21)
requested_toppings = ['mushrooms', 'onions' , 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
bannded_user =['andrew' , 'carolina' , 'david']
user = 'marie'
if user not in bannded_user:
    print(user.title()+',you can post a response if you wish.')
food = 'ceffe'
print("Is food =='sosi'? I predict Ture.")
print(food =='sosi')
print("\nIs food =='ceffe'? I predict Ture")
print(food =='ceffe')
str = ('abcd efg')
str1 = ('ABCD EFg')
print('\n')
print(str == str1)
print(str == str.lower())
num2 = 26
num3 = 19
print('\n')
print(num2 == num3)
print(num2>=22 and num3>=22)
print(num2>=22 or num3>=22)
print('\n')
lin = ['cod' , 'cf' , 'zx' , 'lol']
vx ='qq'
if vx in lin:
    print('yes')
else:
    print('no')
#if 语句
age =17
if age>=18:
    print('you are old enough to votel! ')
    print('Have you vegistered to vote yet?')
else:
    print("Sorry,you are to young to vote.")
    print('Please register to vote as soon as you turn 18.')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission is ",price,".")
age = 63
if age < 4:
    price = 0
elif age<18:
    price =5
elif age<68:
    price =10
elif age >=68:
    price = 5
print("Your admission is ", price, ".")
print('\n')
requestded_topping = ['mushroom' , 'extra cheese']
if 'mushroom' in requestded_topping:
    print('Adding mushroom')
if 'pepperoni' in requestded_topping:
    print("Add pepperoni")
if 'extra cheese' in requestded_topping:
    print("Adding extra cheese")
#个人练习
print('\n')
aline_color = 'Green'
if aline_color.lower() == 'green':
    print("You get 5")
print('\n')
aline_color = 'red'
if aline_color == 'green':
    print('You get 5,because of kill')
if aline_color != 'green':
    print('You get 10')
print('\n')
aline_color = 'green'
if aline_color == 'green':
    print('You get 5,because of killed')
else:
    print('You get 10')
print('\n')
aline_color = 'yellow'
if aline_color == 'green':
    print('You get 5')
elif aline_color == 'red':
    print('You get 10')
elif aline_color == 'yellow':
    print('You get 15')
print('\n')
aline_color = 'yellow'
if aline_color == 'green':
    print('You get 5')
if aline_color == 'red':
    print('You get 10')
if aline_color == 'yellow':
    print('You get 15')
print('\n')
aline_color = 'yellow'
if aline_color == 'green':
    print('You get 5')
elif aline_color == 'red':
    print('You get 10')
else:
    print('You get 15')
age = 21
if age<2:
    print('她正蹒跚学步')
elif age<4:
    print('她是儿童')
elif age<13:
    print("她是青少年")
elif age<20:
    print('她是成年人')
elif age<65:
    print('她是成年人')
elif age>25:
    print('她是老年人')
favorite_fruits = ['apple' , 'orienge' , 'tomamto' , 'bananas']
if 'bananas' in favorite_fruits:
    print('you really like bananas!')
#检查特殊元素
requested_toppings = ['mushroom' , 'green peppers' , 'estra cheese']
for requested_topping1 in requested_toppings:
    if 'green peppers' in requested_topping1:
        print('Sorry,we are out of green peppers right now!')
    else:
        print('Adding ' + requested_topping1 + '.')
print('\nFinished making your pizza!')
requested_toppings = []
if requested_toppings :#确定列表是否为空
    for requested_topping1 in requested_toppings:
        print('Adding ' + requested_topping1 + '.')
else:
    print('Are you sure you want a plain pizza?')
#使用多个列表
available_toppings = ('mushrooms' , 'olives' , 'green pepeers' ,
                      'pepperoni' , 'pineapple' , 'cheese')
requested_toppings = ['mushrooms' , 'green peppers' , 'estra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry,we don't have " + requested_topping + "!")
print("\nFinish making your pizza!")
#自测
print('\n')
users = ['Adam' , 'Sxiwa' , 'chares' , 'Admin' , 'Hezi']
for user in users:
    if 'Admin' in user:
        print("Hello Admin would you like to see a status report?")
    else:
        print('Hello '+ user + ' thank you for logging in again!')
users = []
if users:
    print('Hello ' + 'thank you for logging in again!')
else:
    print('We need to find some users!')
print('\n')
current_users = ['cric' , 'chares' , 'kelala' , 'adam' , 'amo']
new_users =['Lee' , 'Long' , 'Eric' , 'Adam' , 'Joe']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('You need take new name!')
    else:
        print('The name is null!you can use it')
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        number = "1st"
    elif number == 2:
        number = '2rd'
    elif number == 3:
        number = '3rd'
    elif number == 4:
        number = '4th'
    elif number == 5:
        number = '5th'
    elif number == 6:
        number = '6th'
    elif number == 7:
        number = '7th'
    elif number == 8:
        number = '8th'
    elif number == 9:
        number = '9th'
    print(number)

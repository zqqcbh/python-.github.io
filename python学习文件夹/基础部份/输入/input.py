#输入语句（简直是python的灵魂！！
# message = input("Tell me something,and I will repeat it back to you: ")#只接受一个参数
# print(message)
# print('\n')
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")
#多行字符串
# promt = "If you tell us who you are, we can personalize the messages you see."
# promt += "\nWhat is your first name?"
#
# name = input(promt)
# print("Hello, " + name + "!")
# age = input("How old are you?")
# age = int(age)#可以比较数字了
# print(age>=18)
# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")
# #数字比较前务必表示成int
#11求模运算
# print(4 % 3)
# print(5%3)
# print(6%3)
# print(7%3)
# #可以用于判断是奇数还是偶数
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number%2 ==0:
#     print("\nThe number " + str(number) + "is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")
# message = input("What cat would you favorite? please tell me : ")
# message1 = "\nLet me see if I can find you a Subaru"
# print(message,message1)
#排座位
# humnan = input("How many are you in totall?")
# num = int(humnan)
# if num >= 8:
#     print("Sorry,we don't have more order")
# else:
#     print("Please order,it's enough!")
#十的倍数
# number = input("Enter a number, and I'll tell you if it's 10 order:")
# number = int(number)
# if number%10 == 0:
#     print("It's 10 order!")
# else:
#     print("No")
#while 循环数数
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number+=1
#用户选择何时退出
# promt ="\nTell me something, and I will repeat it back to you:"
# promt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(promt)
#     if message != 'quit':
#         print(message)
#使用标志
# promt ="\nTell me something, and I will repeat it back to you:"
# promt += "\nEnter 'quit' to end the program."
# active = True
# while active:
#     message = input(promt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#使用break退出循环
# promt ="\nTell me something, and I will repeat it back to you:"
# promt += "\nEnter 'quit' to end the program."
# while True:
#     city = input(promt)
#     if city == 'quit':
#         break
#     else:
#         print("I don't love to " + city.title() + " !")
#continue语句(直接返回循环的开始相当于忽视剩下的代码
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
#避免无限循环
# x = 1
# while x < 5:
#     print(x)
#     x += 1#如果不小心漏掉了这个语句呢,可以按住Ctrl+c停止输出，有些编译器则需要关闭编译器

# pizza_food = "Please set your pizza table: "
# pizza_food += "\nYou can set quit to stop it!"
# active = True
# while active:
#     pizza = input(pizza_food)
#     if pizza != 'quit':
#         print("We will add the food " + pizza)
#     else:
#         active = False

# price = "Please tell me about your age "
# price += "\nI will cheak your price"
# while True:
#     price = int(input(price))
#     if price < 3:
#         print("Free")
#     elif price <= 12:
#         print("10 doller")
#     else:
#         print("15 doller")

# uncomfirmed_users = ['alice' , 'brian' , 'candace']
# confirmed_users = []
# while uncomfirmed_users:
#     current_users = uncomfirmed_users.pop()
#     print("Verifying user: " + current_users.title())
#     confirmed_users.append(current_users)
#     print("\nThe following users have been confirmed: ")
#     for confirmed_user in confirmed_users:
#         print(confirmed_user)
# pets = ['dog' , 'cat' , 'dog' , 'goldfish' , 'cat' , 'rabbit' , 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nPlease tell me what's your name: ")
#     response = input("Which mountain would like to climb someday: ")
#     responses[name] = response
#     repeat = input("Would you like to let anther person respond?(yes / no) ")
#     if repeat == 'no':
#         polling_active = False
# print("\n-- Poll Results ---")
# for name,response in responses.items():
#     print(name + " would like to climb " + ".")

# sandwich_orders = ['haha' , 'lala' , 'hehe']
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print("I made your " + sandwich + " sandwich!")
#     finished_sandwiches.append(sandwich)
# for sand in finished_sandwiches:
#     print("Your " + sand + " have benn finished!")

# sandwich_orders = ['haha' , 'pastrami' , 'lala' , 'pastrami' , 'hehe' , 'pastrami']
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)

vitor = {}
message = "Please tell me what you are wanting"
message += "\nIf you could visit one please in the world,where would you go?"
active = True
while active:
    name = input("Tell me your name. ")
    print("Hello " + name.title())
    question = input(message)
    vitor[name.title()] = question.title()
    over = input("\nCould you like to join our cheack?(yes/ no)")
    if over == 'no':
        break
print("The following table is about the cheack")
print(vitor)












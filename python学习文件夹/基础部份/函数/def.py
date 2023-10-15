# def greet_user():
#     print("hello")
# greet_user()
# def greet_user(usersname):
#     print("hello " + usersname.title())
# greet_user("prin")
# def display_message():
#     print("python")
# display_message()
# def favorite_book(book):
#     print("My favorite book is " + book.title() + ".")
# favorite_book("alie")
# def describle_pet(animal_type,pet_name):
#     print("\nI have a " + animal_type + '.')
#     print("My " + animal_type + "'s name is " + pet_name.title() + '.')
# describle_pet('hamster' , 'harry')#注意不要写错位置
# describle_pet('dog', 'wille')#调用多次
# #关键字实参
# describle_pet(pet_name='harry' , animal_type='hamster')#准确,必须要函数中的形参名
#默认值
# def describle_pet(pet_name,animal_type='dog'):#默认的处于后面，否则报错！
#     print("\nI have a " + animal_type + '.')
#     print("My " + animal_type + "'s name is " + pet_name.title() + '.')
# describle_pet(pet_name='Willie')
# describle_pet('harry')
# describle_pet(pet_name='harry',animal_type='hamster')
# describle_pet()#错误写法
# def make_shirt(size,zi = "I love Python"):
#     print("\nyour size: " + size)
#     print("Your zi: " + zi)
# make_shirt("XL")
# make_shirt("L")
# make_shirt("XXL","JAVA")
# def describle_city(City_name,City_country = "Eytin"):
#     print(City_name.title() + "is in " + City_country )
# describle_city("Naty")
# describle_city("Xiwa")
# describle_city("Hongkong","China")
#简单返回值
#让参数变为可选的
# def get_formatted_name(first_name,last_name,middle_name=" "):#给middle设置默认空白值
#     if middle_name:#如果存在middle
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:#不存在就动用默认值置空
#         full_name = first_name + ' ' + last_name
#     return full_name.title()#将full返回为title格式
# musician = get_formatted_name('jimi' , 'hendrix')
# print(musician)
# musician = get_formatted_name('john' , 'hooker' , 'lee')
# print(musician)
#返回字典
# def build_person(first_name,last_name,age = " "):#这里age是可选的默认置空，同上面的算法一致
#     person = {"first": first_name, "last": last_name}
#     if age:
#         person = {'first': first_name, "last":last_name, 'age': age}
#     return person  # 返回person，不设置返回值他会输出none
# musician = build_person("jimi",'hendirix' ,18)
# print(musician)
#结合函数和while循环
#设置退出值
# def get_formatted_name(first_name, last_name):
#     full_name = first_name + " " + last_name
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name,l_name)
#     print("\nHello, " + formatted_name +"!")
# print("Thanks!")

# def city_country(city,country):
#     message = city.title() + ',' + country.title()
#     print(message)
# city_country('xchdkj','suygbxi')
# album_list = {}
# def make_album(singer,album,number = " "):
#     if number:
#         album_list[singer] = {album:number}
#     else:
#         album_list[singer] = album
# while True:
#     singer = input("Please tell me his name: ")
#     album = input("How about the album: ")
#     set = input("You can set 'q' to quit it or set 'n' to add number: ")
#     if set == 'q':
#         number = ' '
#         break
#     elif set == 'n':
#         number = input("Please spell number: ")
#     print(f"{singer},{album}")
#     make_album(singer.title(),album.title(),number)
#     print(album_list)
# print("the finally list is: " )
# print(album_list)
#向函数传递列表，访问一组用户时可以用这个算法思想
def greet_users(names):
    for name in names:
        msg = "Hello " + name.title() + " !"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
#在函数中修改列表
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following model have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['ipone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:],completed_models)#此时是禁止修改的
show_completed_models(completed_models)
#禁止修改列表（当需要保存副本时
# print_models(unprinted_designs[:],completed_models)
print(unprinted_designs)

def show_magicians(magicians_name):
    for magician_name in  magicians_name:
        print("The magicianers's name is: " + magician_name.title())
def make_great(magicians_name,add_great):
    while magicians_name:
        magician_name = magicians_name.pop()
        magician_name = "The Great " + magician_name
        add_great.append(magician_name)
        for a in add_great:
            print(a,end=", ")
magicians_name = ['scec','dsscec','sdecf','sdefce']
add_great = []
show_magicians(magicians_name)
make_great(magicians_name[:],add_great)
print("\n")
print(magicians_name)
































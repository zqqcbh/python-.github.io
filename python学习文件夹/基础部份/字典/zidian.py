alien_0 = {'color': 'green' , 'points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
alien_0['x_position'] = 0#添加元素
alien_0['y_position'] = 25
print(alien_0)
#创建字典
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 9
alien_1['x_position'] = 25
alien_1['y_position'] = 25
print(alien_1)
#修改字典值
print('The alien is' + alien_1['color'] +'.')
alien_1['color'] = 'yellow'
print('The alien is ' + alien_1['color'] + '.')
alien_1['speed'] = 'fast'
print(alien_1)
print("The alien's original X_position: " + str(alien_1['x_position']))
if alien_1['speed'] == 'medium':
    x_increment = 2
elif alien_1['speed'] == 'slow':
    x_increment = 1
else:
    x_increment = 3
alien_1['x_position'] = alien_1['x_position'] + x_increment
print('New X_position: ' + str(alien_1['x_position']))
print('\n')
print(alien_1)
del alien_1['points']#删除且永远消失
print(alien_1)
print('\n')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil': 'python',
    }
#自测
print('\n')
print('Sarah favorite language is ' + favorite_languages['sarah'].title() + '.')
people = {'first_name': 'Adam' , 'last_name' : 'Charles','city' : 'London'}
print(people['first_name'],people['last_name'],people['city'])
num = {'Swit': 6,'Huit': 3, 'Sham': 9, 'Mini': 0, 'Jack': 5}
print(num["Swit"],num['Huit'],num['Sham'],num['Mini'],num['Jack'])
zidian = {'python':'haha','c':'lala','java':'xixi','html':'lulu'}
print('Python: \n\t',zidian['python'],'\nC: \n\t',zidian['c'],
      '\nJava: \n\t',zidian['java'],'\nHTML: \n\t',zidian['html'])
#遍历字典
users_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in users_0.items():
    print('\nKey ' + key)
    print('Value ' + value)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')
#遍历字典中所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil': 'python',
    }
for name in favorite_languages:
    print(name.title())
    print('\n')
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
            print("  Hi! " + name.title() +
                  ",I see you favorite language is " + favorite_languages[name].title() + '.')
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
#按照顺序遍历（sorted
for name in sorted(favorite_languages.keys()):
    print(name.title() + "Thanks  you for your taking the poll!")
#遍历值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())
#词汇表
zidian = {'python':'haha','c':'lala','java':'xixi','html':'lulu'}
for language in zidian.keys():
    print("My language cover: " + language.title())
for ability in zidian.values():
    print("The ability cover: " + ability)
zidian['css'] = 'lolo'
zidian['js']  = 'lxlx'
for language in zidian.keys():
    print("My language cover: " + language.title())
for ability in zidian.values():
    print("The ability cover: " + ability)
for language, ability in zidian.items():
    print('The language ' + language.title() + 'cover :' + '\n\t' + ability.title())
    print(language)
    print(ability)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil': 'python',
    }
invers = ['lisa' , 'jodo' , 'sarah' , 'jen' , 'lee']
for inver in invers:
    if inver in favorite_languages.keys():
        print('Thank you for your join' + inver.title())
    else:
        print("I'sorry you can't join us, " + inver.title())
#嵌套
alien_0 = {'color':'green' , 'point': 5}
alien_1 = {'color':'red' , 'point':10}
alien_2 = {'color':'yellow' , 'point':15}

aliens = [alien_0 , alien_1 , alien_2]

for alien in aliens:
    print(alien)
print('\n')
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green' , 'points': 5 , 'speed' : 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))
#字典存储列表
pizza ={
    'crust': 'thick',
    'toppings':['mushrooms', 'extra cheese' ],
}
print("You ordered a " + pizza['crust'] +"-curst pizza" +
       'with the following topping: ')
for topping in pizza['toppings']:
    print('\t' + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward':['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name,languages in favorite_languages.items():
    print("\n" + name.title() +"'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
#字典储存字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location':'princeton',
    },
'mcurie':{
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
},

}
for username, user_info in users.items():
    print("\nUsername:" + username.title())
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
#自测·
print('\n')
people_0 = {'first_name': 'Adam' , 'last_name' : 'Charles','city' : 'London'}
people_1 = {'first_name': 'Jen' , 'last_name' : 'Lee' , 'city' : 'Empty'}
people_2 = {'first_name': 'Eric' , 'last_name': 'Liu', 'city': 'Honkong'}#这是玩家的详细信息
people0={}#建立一个空字典方便以后添加元素
people0['Adam'] = people_0#Adam是键，people是值，下面同理
people0['Jen'] = people_1
people0['Eric'] = people_2
for name,info in people0.items():
    full_name = info['first_name'] + ' ' + info['last_name']#全名
    location = info['city']
    print(full_name + ":")
    print(location + '\n')
print('\n')
pet = {}#建立空字典
pet_0 = {'pet':'cat','host':'Alm'}
pet_1 = {'pet':'dog','host':'Adam'}
pet_2 = {'pet':'pig','host':'Jen'}
pet['Aimi'] = pet_0
pet['Coco'] = pet_1
pet['Jiji'] = pet_2
for name,info in pet.items():
    print(name)
    print(info['pet'])
    print(info['host'] + '\n')

print('\n')
#字符转换
d1 = {"a": 1, "b" :2, "c": 3, "d" :4,"e": 5}
d2 = {v:k for k,v in d1.items()}
print(d2)

di = {}
while True:
    a = input("give: ")
    b = input("Give: ")
    di[a] = b
    print(di)




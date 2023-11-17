#两个文件合并
#重构
def greet_user():
    import json
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What your name? ")
        with open(filename, 'w') as j_obj:
            json.dump(username, j_obj)
            print("We will remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")
greet_user()
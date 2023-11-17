#把他们的用法分步了
import json
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            # print("Welcome back, " + username + "!")
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename) as j_obj:
        json.dump(username, j_obj)
    return username
def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll welcome you when you come back, " + username + "!")
greet_user()




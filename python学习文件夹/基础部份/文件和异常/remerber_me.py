import json
username = input("what your name? ")

filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We will remember you when you come back, " + username + "!")
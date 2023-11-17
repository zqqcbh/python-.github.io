import json
def in_number():
    numbers = input("What's your number？")
    filename = 'what_number.json'
    with open(filename, 'w') as j_obj:
        json.dump(numbers, j_obj)
def get_number():
    filename = "what_number.json"
    try:
        with open(filename) as k_obj:
            numbers0 = json.load(k_obj)
    except FileNotFoundError:
        print("We have't find this file")
    else:
        print("I guess you have input {}".format(numbers0))
in_number()
get_number()
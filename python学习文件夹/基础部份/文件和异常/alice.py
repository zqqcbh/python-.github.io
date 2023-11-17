# FileNotFoundError问题
filename = 'Alice in Wonderland.txt'
try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry,the file " + filename +"does not exist."
    print(msg)
else:
    words = contents.split()
    num_works = len(words)
    print("The file "+filename + "has about " + str(num_works) + " words.")





def read(filename):
    try:
        with open(filename) as read_l:
                content = read_l.read()
    except FileNotFoundError:
        pass
    else:
        print(content)
filenames = ['cats.txt','dogs.txt','dhwbd.txt']
for filename in filenames:
    read(filename)







def count_world(filename):
    """计算一个文件夹大概有多少单词"""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry,the file " + filename + "does not exist."#此处为pass时失败时一声不吭
        print(msg)
    else:
        words = contents.split()
        num_works = len(words)
        print("The file " + filename + "has about " + str(num_works) + " words.")
filename = 'Alice in Wonderland.txt'#当filename表示为一个列表时可以联合多个文件
count_world(filename)
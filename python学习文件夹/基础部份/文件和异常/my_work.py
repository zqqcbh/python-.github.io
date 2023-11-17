def work(filename):
    try:
        with open(filename, encoding='utf-8') as job_w:
            content = job_w.read()
    except FileNotFoundError:
        print("未找到您输入的文件")
    else:
        li = content.split()
        l1 = len(li)
        l2 = content.lower().count('kazan')
        print("这个文件共有{}个单词,其中kazan共出现了{}次".format(l1,l2))
filename = 'kazan.txt'
work(filename)

def add():
    while True:
        a = input("请输入第一个数:")
        b = input("请输入第二个数: ")
        try:
            c = int(a) + int(b)
            
        except ValueError:
            print("请输入正确的数字！")
        else:
            print(c)
        msg = input("是否继续？（q停止）")
        if msg == 'q':
            break
add()
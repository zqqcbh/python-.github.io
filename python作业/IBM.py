a = float(input('请输入身高的值(m):'))
b = int(input('请输入体重的值(kg):'))
BMT = b/(a**2)
print('用户BMT的值为:',BMT)
if BMT<18.5:
    print("偏瘦")
elif 18.5<BMT<24.9:
    print("正常")
else :
    print("超重")


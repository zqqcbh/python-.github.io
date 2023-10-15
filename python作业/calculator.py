first_nmuber = float(input("请告诉我第一个数/除数/减数: "))
message = input("请告诉我您想要进行的操作（1相加，2相减，3相乘，4相除）: ")
if message == "1":
    last_number = float(input("请告诉我另外一个数: "))
    num = first_nmuber + last_number
    print(f"{first_nmuber} + {last_number} = {num}")
elif message == "2":
    last_number = float(input("请告诉我被减数: "))
    num = first_nmuber - last_number
    print(f"{first_nmuber} - {last_number} = {num}")
elif message == "3":
    last_number = float(input("请告诉我被另一个数: "))
    num = first_nmuber * last_number
    print(f"{first_nmuber} * {last_number} = {num}")
elif message == "4":
    last_number = float(input("请告诉我被除数: "))
    num = first_nmuber/last_number
    print(f"{first_nmuber} / {last_number} = {num}")
else :
    print("输入错误，请重新输入")



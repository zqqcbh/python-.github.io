#ZeroDivisionError错务处理
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")#处理错误
print("Give me two number, and I will division them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't division by zero!")
    else:
        print(answer)




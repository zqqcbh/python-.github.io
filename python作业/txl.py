tx_table = {}
message = "You can spell 'q' to quit"#建表
for i in range(1,11):
    people = input("Please tell me about the name: ")
    print(message)
    number = input("Please tell me the number: ")
    if number == 'q':
        break
    tx_table[people.title()] = number
print(tx_table)
set = input("You can set your table now(add to adding,delete to deleting and create to creating): ")#进行删改操作
if set == 'add':#“改”操作
    people = input("Please tell me about the name: ")
    print(message)
    number = input("Please tell me the number: ")
    tx_table[people.title()] = number
if set == 'delete':
    de_table = input("Who will be deleted? Please tell me: ")
    de_table = de_table.title()
    print("I will delete " + tx_table.pop(de_table))
print(tx_table)
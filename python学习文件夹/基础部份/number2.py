# num1 = 0b101
# num2 = 0o17
# num3 = 0xaf
#
# print(num1,num2,num3)
# print(bin(num1),oct(num2),hex(num3))
# num4 = 1256
# print(bin(num4),oct(num4),hex(num4))
l = [1,3,4,6,8,9]
num1 = 2
num2 = 8

# C语言判断一个数字是否在数组中
# for(i =0;i<6;i++){
# #   if(l[i] == num1)
# #       {print("in");break;}
# # }
# if(i==6)
#   {print("not in")}
# }

print(num1 in l)
print(num2 in l)

if num1 in l:
    print("in")
else:
    print("not in")

# import random
# print(random.randint(1,51))


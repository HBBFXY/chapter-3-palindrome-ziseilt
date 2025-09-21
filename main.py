# 这里编写你的代码
num = input("请输入一个5位数：")
if len(num) != 5:
    print("输入错误，请确保输入的是5位数！")
else:
    if num == num[::-1]:
        print("{} 是回文数".format(num))
    else:
        print("{} 不是回文数".format(num))

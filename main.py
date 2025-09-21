# 这里编写你的代
num = input().strip()  # 不显示提示，直接读取输入

if len(num) != 5 or not num.isdigit():
    print("输入错误：请输入5位数字")
else:
    if num == num[::-1]:
        print(f"{num} 是回文数")
    else:
        print(f"{num} 不是回文数")

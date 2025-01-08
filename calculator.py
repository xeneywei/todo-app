def add(x, y):
    """加法函数"""
    return x + y

def subtract(x, y):
    """减法函数"""
    return x - y

def multiply(x, y):
    """乘法函数"""
    return x * y

def divide(x, y):
    """除法函数"""
    if y == 0:
        return "错误：除数不能为零"
    return x / y

# 主程序
print("欢迎使用简单计算器！")
print("请选择运算：")
print("1. 加法")
print("2. 减法")
print("3. 乘法")
print("4. 除法")

while True:
    # 获取用户输入
    choice = input("\n请输入运算选项(1/2/3/4)，按 q 退出：")
    
    # 检查是否退出
    if choice.lower() == 'q':
        print("感谢使用，再见！")
        break
    
    # 检查输入是否有效
    if choice not in ['1', '2', '3', '4']:
        print("无效的选择，请重新输入！")
        continue
    
    # 获取操作数
    try:
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))
    except ValueError:
        print("输入无效，请输入数字！")
        continue

    # 执行计算
    if choice == '1':
        print(f"\n{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"\n{num1} × {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, str):
            print(f"\n{result}")
        else:
            print(f"\n{num1} ÷ {num2} = {result}")
    
    print("\n" + "=" * 30) 
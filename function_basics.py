# 1. 最简单的函数
def say_hello():
    print("你好，世界！")

print("===== 简单函数调用 =====")
say_hello()

# 2. 带参数的函数
def greet(name):
    print(f"你好，{name}！")

print("\n===== 带参数的函数 =====")
greet("兮雅")

# 3. 带返回值的函数
def add_numbers(a, b):
    return a + b

print("\n===== 带返回值的函数 =====")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# 4. 带默认参数的函数
def greet_with_title(name, title="同学"):
    print(f"你好，{title} {name}")

print("\n===== 默认参数函数 =====")
greet_with_title("小明")  # 使用默认参数
greet_with_title("张老师", "老师")  # 覆盖默认参数

# 5. 多个返回值的函数
def calculate(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    return add, subtract, multiply

print("\n===== 多返回值函数 =====")
add_result, sub_result, mul_result = calculate(10, 5)
print(f"10 和 5 的运算结果：")
print(f"相加 = {add_result}")
print(f"相减 = {sub_result}")
print(f"相乘 = {mul_result}")

# 6. 带文档字符串的函数
def square(number):
    """
    计算一个数的平方
    参数:
        number: 要计算平方的数字
    返回:
        该数字的平方
    """
    return number ** 2

print("\n===== 带文档的函数 =====")
print(f"5的平方是：{square(5)}")
print(f"函数说明：\n{square.__doc__}")

# 7. 使用 *args 的函数（可变参数）
def sum_all(*numbers):
    return sum(numbers)

print("\n===== 可变参数函数 =====")
print(f"求和结果：{sum_all(1, 2, 3, 4, 5)}")

# 8. 使用 **kwargs 的函数（关键字参数）
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print("\n===== 关键字参数函数 =====")
print_info(name="兮雅", age=25, city="北京") 
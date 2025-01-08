# 1. if-elif-else 条件语句
print("===== if-elif-else 示例 =====")
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 2. for 循环
print("\n===== for 循环示例 =====")
# 遍历列表
fruits = ['苹果', '香蕉', '橙子']
print("水果清单：")
for fruit in fruits:
    print(f"- {fruit}")

# 使用 range
print("\n数字序列：")
for i in range(1, 5):
    print(f"数字: {i}")

# 3. while 循环
print("\n===== while 循环示例 =====")
count = 0
while count < 3:
    print(f"当前计数: {count}")
    count += 1

# 4. break 语句
print("\n===== break 示例 =====")
for i in range(1, 10):
    if i == 5:
        print("遇到 5，结束循环")
        break
    print(f"当前数字: {i}")

# 5. continue 语句
print("\n===== continue 示例 =====")
for i in range(1, 5):
    if i == 2:
        print("跳过 2")
        continue
    print(f"当前数字: {i}")

# 6. 嵌套循环
print("\n===== 嵌套循环示例 =====")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
    print("---")

# 7. 列表推导式
print("\n===== 列表推导式示例 =====")
squares = [x**2 for x in range(1, 5)]
print(f"1-4的平方: {squares}")

# 8. 条件表达式（三元运算符）
print("\n===== 条件表达式示例 =====")
age = 20
status = "成年" if age >= 18 else "未成年"
print(f"年龄 {age}: {status}")

# 9. while-else 语句
print("\n===== while-else 示例 =====")
num = 0
while num < 3:
    print(f"num = {num}")
    num += 1
else:
    print("循环正常结束")

# 10. for-else 语句
print("\n===== for-else 示例 =====")
for i in range(3):
    print(f"i = {i}")
else:
    print("循环完成")

# 11. 异常处理
print("\n===== try-except 示例 =====")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误：除数不能为零")
else:
    print(f"结果: {result}")
finally:
    print("异常处理结束") 
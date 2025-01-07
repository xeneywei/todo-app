# 定义一些变量
a = True
b = False
x = 5
y = 10

# 基础逻辑运算
print("==== 布尔值的逻辑运算 ====")
print(f"True AND False = {a and b}")
print(f"True OR False = {a or b}")
print(f"NOT True = {not a}")

print("\n==== 比较运算 ====")
print(f"{x} > {y} = {x > y}")
print(f"{x} < {y} = {x < y}")
print(f"{x} == {y} = {x == y}")
print(f"{x} != {y} = {x != y}")

print("\n==== 组合逻辑运算 ====")
print(f"{x} > 0 AND {x} < {y} = {x > 0 and x < y}")
print(f"{x} < 0 OR {x} < {y} = {x < 0 or x < y}") 
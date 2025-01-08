# 1. 数值类型
# 整数 (int)
age = 25
print(f"整数: age = {age}, 类型: {type(age)}")

# 浮点数 (float)
height = 1.75
print(f"浮点数: height = {height}, 类型: {type(height)}")

# 复数 (complex)
complex_num = 3 + 4j
print(f"复数: complex_num = {complex_num}, 类型: {type(complex_num)}")

# 2. 字符串类型 (str)
name = "兮雅"
message = '这是一个字符串'
multi_line = """这是一个
多行字符串"""
print(f"\n字符串: name = {name}, 类型: {type(name)}")
print(f"多行字符串:\n{multi_line}")

# 3. 布尔类型 (bool)
is_student = True
is_working = False
print(f"\n布尔值: is_student = {is_student}, 类型: {type(is_student)}")

# 4. 列表类型 (list) - 可变序列
fruits = ['苹果', '香蕉', '橙子']
mixed_list = [1, 'hello', True, 3.14]
print(f"\n列表: fruits = {fruits}, 类型: {type(fruits)}")
print(f"混合列表: mixed_list = {mixed_list}")

# 5. 元组类型 (tuple) - 不可变序列
coordinates = (10, 20)
mixed_tuple = (1, 'world', False)
print(f"\n元组: coordinates = {coordinates}, 类型: {type(coordinates)}")

# 6. 字典类型 (dict)
person = {
    'name': '兮雅',
    'age': 25,
    'is_student': True
}
print(f"\n字典: person = {person}, 类型: {type(person)}")

# 7. 集合类型 (set)
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, 'hello', 3.14}
print(f"\n集合: numbers = {numbers}, 类型: {type(numbers)}")

# 8. 空值 (None)
empty = None
print(f"\n空值: empty = {empty}, 类型: {type(empty)}")

# 9. 类型转换示例
print("\n类型转换示例:")
num_str = "123"
num_int = int(num_str)
print(f"字符串转整数: '{num_str}' -> {num_int}")

float_num = 3.14
int_num = int(float_num)
print(f"浮点数转整数: {float_num} -> {int_num}")

# 10. 变量的动态类型
print("\n变量的动态类型:")
x = 100
print(f"x = {x}, 类型: {type(x)}")
x = "hello"
print(f"x = {x}, 类型: {type(x)}")
x = [1, 2, 3]
print(f"x = {x}, 类型: {type(x)}") 
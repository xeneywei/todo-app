def main():
    # 获取用户输入
    name = input("请输入您的名字：")
    age = input("请输入您的年龄：")
    
    # 输出信息
    print(f"\n您好，{name}！")
    print(f"您今年 {age} 岁了。")
    
    # 计算明年年龄
    next_year_age = int(age) + 1
    print(f"明年您将会是 {next_year_age} 岁。")

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("错误：请输入有效的年龄数字！") 
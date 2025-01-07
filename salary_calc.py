def print_table_header(headers):
    # 打印表头
    print("\n" + "=" * 100)
    for header in headers:
        print(f"{header:<20}", end="")
    print("\n" + "=" * 100)

def print_table_row(columns):
    # 打印数据行
    for col in columns:
        print(f"{col:<20}", end="")
    print()

# 获取用户输入的目标营收
try:
    monthly_target = float(input("请输入月度营收目标（元）："))
except ValueError:
    print("输入无效，使用默认值200万")
    monthly_target = 2000000

# 基础参数设置
profit_rate = 0.8  # 80%的利润率
price_options = [1999, 2999, 3999, 4999]
monthly_lives = 12  # 每月12场直播

print(f"\n===== 课程销售目标分析 =====")
print(f"月度营收目标：{monthly_target:,.2f} 元")
print(f"实际利润率：{profit_rate * 100}%")
print(f"月度利润目标：{monthly_target * profit_rate:,.2f} 元")

# 定价方案分析表格
print("\n【定价方案分析】")
headers = ["课程定价", "所需销量(人)", "日均销量(人)", "预期毛收入", "预期净利润"]
print_table_header(headers)

for price in price_options:
    sales_needed = monthly_target / price
    daily_sales = sales_needed / 22
    gross_income = price * sales_needed
    net_income = gross_income * profit_rate
    
    row = [
        f"{price:,}元",
        f"{sales_needed:.0f}",
        f"{daily_sales:.1f}",
        f"{gross_income:,.2f}元",
        f"{net_income:,.2f}元"
    ]
    print_table_row(row)

# 直播场次分析表格
print("\n【直播场次分析】")
headers = ["课程定价", "每场直播人数", "每场直播营收", "转化率要求"]
print_table_header(headers)

for price in price_options:
    sales_per_live = (monthly_target / price) / monthly_lives
    revenue_per_live = sales_per_live * price
    # 假设每场直播观看人数500人
    conversion_rate = (sales_per_live / 500) * 100
    
    row = [
        f"{price:,}元",
        f"{sales_per_live:.1f}人",
        f"{revenue_per_live:,.2f}元",
        f"{conversion_rate:.1f}%"
    ]
    print_table_row(row)

# 建议方案
recommended_price = 2999
print(f"\n【建议方案】推荐定价：{recommended_price:,}元")
headers = ["指标", "目标值", "说明"]
print_table_header(headers)

monthly_sales = monthly_target / recommended_price
avg_live_sales = monthly_sales / monthly_lives

metrics = [
    ["月度总销量", f"{monthly_sales:.0f}人", "整月销售目标"],
    ["每场直播目标", f"{avg_live_sales:.1f}人", f"基于每月{monthly_lives}场直播"],
    ["场均销售额", f"{avg_live_sales * recommended_price:,.2f}元", "每场直播营收目标"],
    ["月度毛收入", f"{monthly_target:,.2f}元", "预期总营收"],
    ["月度净利润", f"{monthly_target * profit_rate:,.2f}元", f"按{profit_rate*100}%利润率"]
]

for row in metrics:
    print_table_row(row)

print("\n【注意事项】")
print("1. 以上分析基于每月12场直播计算")
print("2. 建议通过社群营销、会员裂变等方式辅助获客")
print("3. 可以考虑设置阶段性优惠价格刺激销量")
print("4. 建议设立销售激励机制提高团队积极性")
print("5. 转化率基于每场直播500人观看计算") 
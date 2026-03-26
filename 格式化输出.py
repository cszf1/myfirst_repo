# ==================== Python 格式化输出示例 ====================

a = 2
b = 3.9287
c = "python"

# 1. 传统 % 格式化
print("\n=== 传统 % 格式化 ===")
print("a=%06d" % a)                    # 整数 6 位，不足补 0
print("b=%.3f" % b)                    # 浮点数保留 3 位小数
print("c=%s" % c)                      # 字符串
print("输出百分数 a=%d%%" % (a*100))   # 百分号需要转义

# 2. str.format() 方法
print("\n=== str.format() 方法 ===")
print("a={:06d}".format(a))            # 整数 6 位，不足补 0
print("b={:.3f}".format(b))            # 浮点数保留 3 位小数
print("c={}".format(c))                # 字符串
print("输出百分数 a={}%".format(a*100))  # 百分号直接写
print("b={:+.3f}".format(b))           # 显示正负号

# 3. f-string (Python 3.6+) - 推荐使用
print("\n=== f-string (推荐) ===")
print(f"a={a:06d}")                    # 整数 6 位，不足补 0
print(f"b={b:.3f}")                    # 浮点数保留 3 位小数
print(f"c={c}")                        # 字符串
print(f"输出百分数 a={a*100}%")         # 表达式直接计算
print(f"b={b:+.3f}")                   # 显示正负号

# 4. 对齐和填充
print("\n=== 对齐和填充 ===")
print(f"左对齐：'{a:<10d}'")            # 左对齐，宽度 10
print(f"右对齐：'{a:>10d}'")            # 右对齐，宽度 10
print(f"居中对齐：'{a:^10d}'")          # 居中对齐，宽度 10
print(f"填充字符：'{a:*^10d}'")         # 居中对齐，用*填充

# 5. 数字格式化
print("\n=== 数字格式化 ===")
num = 1234567.89
print(f"千位分隔符：{num:,}")           # 1,234,567.89
print(f"百分比：{0.856:.2%}")          # 85.60%
print(f"科学计数法：{num:.2e}")         # 1.23e+06
print(f"二进制：{a:b}")                 # 10
print(f"十六进制：{255:x}")             # ff
print(f"八进制：{a:o}")                 # 2

# 6. 字符串格式化
print("\n=== 字符串格式化 ===")
name = "张三"
age = 25
print(f"姓名：{name}, 年龄：{age}")
print(f"姓名：{name:>10}")             # 右对齐
print(f"截取前 3 位：{'Hello World'[:3]}")

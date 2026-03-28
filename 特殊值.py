import math

def demonstrate_infinity():
    # 创建无穷大常量
    inf = float("inf")      # 正无穷大
    neg_inf = float("-inf") # 负无穷大

    # 无穷大的基本算术运算
    print("无穷大常量:")
    print("inf + inf =", inf + inf)           # 无穷大加无穷大仍为无穷大
    print("inf + 1 =", inf + 1)               # 无穷大加有限数仍为无穷大
    print("-inf * -66 =", -inf * -66)         # 负无穷大乘以负数得正无穷大
    print("-inf * inf =", -inf * inf)         # 正负无穷大相乘得负无穷大

    # 涉及无穷大的除法运算
    print("\n涉及无穷大的除法:")
    print("-inf / 100 =", -inf / 100)         # 无穷大除以有限数，符号保持不变
    print("inf / inf =", inf / inf)           # 无穷大除以无穷大未定义，结果为 NaN
    try:
        print("inf / 0.0 =", inf / 0.0)       # 无穷大除以零会抛出异常
    except ZeroDivisionError:
        print("inf / 0.0 会抛出 ZeroDivisionError 异常")

def demonstrate_nan():
    # 创建 NaN 常量
    nan = float("nan")    # NaN (Not a Number) 常量

    # NaN 的基本算术运算
    print("\nNaN 常量:")
    print("pos_inf + neg_inf =", float("inf") + float("-inf"))  # 正无穷大加负无穷大结果为 NaN
    print("nan ** 0 =", nan ** 0)                               # 任何数的 0 次方都等于 1（包括 NaN）

    # 将 NaN 与自身进行比较
    print("\n将 NaN 与自身比较:")
    print("nan == nan =", nan == nan)          # NaN 不等于自身（符合 IEEE 754 标准）

def demonstrate_math_functions():
    # 导入 math 模块
    import math

    # 创建无穷大和 NaN 常量（使用 math 模块的方式）
    inf = math.inf        # 正无穷大
    neg_inf = -math.inf   # 负无穷大
    nan = math.nan        # NaN

    # 使用 math 模块提供的判断函数
    print("\n使用 math 模块的函数:")
    print("math.isinf(inf) =", math.isinf(inf))       # 判断是否为无穷大
    print("math.isinf(neg_inf) =", math.isinf(neg_inf)) # 判断是否为无穷大
    print("math.isnan(nan) =", math.isnan(nan))       # 判断是否为 NaN
    print("math.isfinite(7.54) =", math.isfinite(7.54)) # 判断是否为有限数
    print("math.isfinite(inf) =", math.isfinite(inf))   # 无穷大不是有限数
    print("math.isfinite(nan) =", math.isfinite(nan))   # NaN 也不是有限数

# 调用函数演示各种情况
demonstrate_infinity()    # 演示无穷大相关操作
demonstrate_nan()         # 演示 NaN 相关操作
demonstrate_math_functions()  # 演示 math 模块的判断函数
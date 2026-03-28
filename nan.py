x = float('nan')
y = x

print(x is y)      # True（同一个对象）
print(x == y)      # False（NaN不等于任何值，包括它自己）

nan1 = float('nan')
nan2 = float('nan')

print(nan1 == nan2)  # False
print(nan1 is nan2)  # False（两个不同的 NaN 对象）
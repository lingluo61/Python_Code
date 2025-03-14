# 练习 4.5：100 万求和 创建⼀个包含数 1〜1 000 000 的列表，再使⽤
# min() 和 max() 核实该列表确实是从 1 开始、到 1 000 000 结束的。
# 另外，对这个列表调⽤函数 sum()，看看 Python 将 100 万个数相加需
# 要多⻓时间。

numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
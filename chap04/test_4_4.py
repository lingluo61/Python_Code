# 练习 4.4：100 万 创建⼀个包含数 1〜1 000 000 的列表，再使⽤⼀个
# for 循环将这些数打印出来。（如果输出的时间太⻓，按 Ctrl + C 停⽌
# 输出，或关闭输出窗⼝。）

numbers = list(range(1, 1000001))
for number in numbers:
    print(number)
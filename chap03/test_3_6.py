# 练习 3.6：添加嘉宾 你刚找到了⼀张更⼤的餐桌，可容纳更多的嘉宾
# 就座。请想想你还想邀请哪三位嘉宾。
# 以完成练习 3.4 或练习 3.5 时编写的程序为基础，在程序末尾添加函数
# 调⽤ print()，指出你找到了⼀张更⼤的餐桌。
# 使⽤ insert() 将⼀位新嘉宾添加到名单开头。
# 使⽤ insert() 将另⼀位新嘉宾添加到名单中间。
# 使⽤ append() 将最后⼀位新嘉宾添加到名单末尾。
# 打印⼀系列消息，向名单中的每位嘉宾发出邀请。

names = ['dave', 'bob', 'charlie']
print("find a bigger table")
names.insert(0, 'alice')
names.insert(2, 'bobby')
names.append('tom')
print(names)
# 练习 3.5：修改嘉宾名单 你刚得知有位嘉宾⽆法赴约，因此需要另外
# 邀请⼀位嘉宾。
# 以完成练习 3.4 时编写的程序为基础，在程序末尾添加函数调⽤
# print()，指出哪位嘉宾⽆法赴约。
# 修改嘉宾名单，将⽆法赴约的嘉宾的姓名替换为新邀请的嘉宾的
# 姓名。
# 再次打印⼀系列消息，向名单中的每位嘉宾发出邀请。

names = ['alice', 'bob', 'charlie']
print(f"{names[0].title()} can't come.")
names[0] = 'dave'
print(f"{names[0].title()} can come.")
print(f"{names[1].title()} can come.")
print(f"{names[2].title()} can come.")
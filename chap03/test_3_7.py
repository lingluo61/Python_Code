# 练习 3.7：缩短名单 你刚得知新购买的餐桌⽆法及时送达，因此只能
# 邀请两位嘉宾。
# 以完成练习 3.6 时编写的程序为基础，在程序末尾添加⼀⾏代码，
# 打印⼀条你只能邀请两位嘉宾共进晚餐的消息。
# 使⽤ pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为⽌。
# 每次从名单中弹出⼀位嘉宾时，都打印⼀条消息，让该嘉宾知道
# 你很抱歉，⽆法邀请他来共进晚餐。
# 对于余下两位嘉宾中的每⼀位，都打印⼀条消息，指出他依然在
# 受邀之列。
# 使⽤ del 将最后两位嘉宾从名单中删除，让名单变成空的。打印
# 该名单，核实名单在程序结束时确实是空的。

names = ['alice', 'dave', 'bobby', 'bob', 'charlie', 'tom']
print("allow two person")
name = names.pop()
print(f"sorry {name}")
name = names.pop()
print(f"sorry {name}")
name = names.pop()
print(f"sorry {name}")
name = names.pop()
print(f"sorry {name}")
print(names)
del names[0]
del names[0]
print(names)
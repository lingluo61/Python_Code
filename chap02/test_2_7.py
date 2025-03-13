#练习 2.7：删除⼈名中的空⽩ ⽤变量表⽰⼀个⼈的名字，并在其开头
#和末尾都包含⼀些空⽩字符。务必⾄少使⽤字符组合 "\t" 和 "\n" 各
#⼀次。
#打印这个⼈名，显⽰其开头和末尾的空⽩。然后，分别使⽤函数
#lstrip()、rstrip() 和 strip() 对⼈名进⾏处理，并将结果打印
#出来。

name = " Json\tNihao\nHello "
print(name)
name = name.lstrip()
print(name)
name = " Json\tNihao\nHello "
name = name.rstrip()
print(name)
name = " Json\tNihao\nHello "
name = name.strip()
print(name)
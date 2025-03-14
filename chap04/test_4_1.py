# 练习 4.1：⽐萨 想出⾄少三种你喜欢的⽐萨，将其名称存储在⼀个列
# 表中，再使⽤ for 循环将每种⽐萨的名称打印出来。
# 修改这个 for 循环，使其打印包含⽐萨名称的句⼦，⽽不仅仅是
# ⽐萨的名称。对于每种⽐萨都显⽰⼀⾏输出，如下所⽰。
# I like pepperoni pizza.
# 在程序末尾添加⼀⾏代码（不包含在 for 循环中），指出你有多
# 喜欢⽐萨。输出应包含针对每种⽐萨的消息，还有⼀个总结性的
# 句⼦，如下所⽰。
# I really love pizza!

pizzas = ['pepperoni', 'cheese', 'veggie']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I love pepperoni pizza")
print("I love cheese pizza")
print("I love veggie pizza")
print("I really love pizza!")
# Pythonの基本

# 標準出力
print("【標準出力】")
print("Hello, Python!")
print("")

# 演算
print("【演算】")
print(1 + 2)
print(1 / 3)
print("")

# データ型
print("【データ型】")
print(type(10))
print(type(2.5))
print(type("hello"))
print("")

# リスト
print("【リスト】")

num_list = [1, 2, 3, 4, 5]
print(num_list)
print(len(num_list))
print(num_list[1:2])
print(num_list[3:])
print(num_list[:3])
print(num_list[0:-1])

# if
print("【if】")
hungry = True
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")

# for
print("【for】")
for i in [1, 2, 3]:
    print(i)

# 関数
print("【関数】")


def hello():
    print("hello")


hello()


def hello(name):
    print("hello " + name)


hello("world")

print("【関数】")


class Man:
    def __init__(self, name):
        self.name = name
        print("init")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name)


man = Man("Ryu")
man.hello()
man.goodbye()

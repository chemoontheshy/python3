class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说：我 %d 岁。体重 %d ,在读%d年级" % (self.name, self.age, self.__weight))
        # %s是str,%d是int?


# p = people('chemo', 10, 30)
# p.speak()

class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说：我 %d 岁。在读%d年级。" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()

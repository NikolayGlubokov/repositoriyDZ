class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def info(self):
        print(f'{self.first, self.last, self.age}')


class Student(Human):
    def __init__(self, spec, group, rang, first, last, age):
        super().__init__(first, last, age)
        self.spec = spec
        self.group = group
        self.reit = rang

    def info(self):

        print(f'{self.spec, self.group, self.reit}', end=" ")
        super().info()


class Teacher(Human):
    def __init__(self, spec, exp, first, last, age):
        super().__init__(first, last, age)
        self.spec = spec
        self.exp = exp

    def info(self):
        print(f'{self.spec, self.exp}', end=" ")
        super().info()


class Graduate(Student):
    def __init__(self, topic, first, last, age, spec, group, reit):

        super().__init__(first, last, age, spec, group, reit)
        self.topic = topic

    def info(self):
        print(f'{self.topic}', end=" ")
        super().info()

group = [
    Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
    Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
    Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
    Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
    Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
    Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
]

for i in group:
    i.info()
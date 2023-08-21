from homework4 import num1, num2, num3, num4, number ,number1


class num5(num1, num2, num3, num4):
    def __init__(self,name,__age):
        num1.__init__(self, name)
        num2.__init__(self, __age)

    def print(self):
        num1.print(self)

    @property
    def __print1(self):
        return f'Возраст {self.__age}'
    @__print1.setter
    def age(self):
        return f'Возраст {self.__age}'


num1.print(number)
num2.print1(number1)

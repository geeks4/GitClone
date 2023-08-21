# инкапсуляция
# 1 капсула
# 2 уровни защиты
# 3 публичный,приватный,скрытый

class Bank:
    def __init__(self, name, age, money, password):
        self.__name = name
        self.__age = age
        self.__money = money
        self.__passw = password

    @property
    def data(self):
      return self.__name + ' имеет ' + self.__money + ' денег '
    @ data.setter
    def data(self, sentence):
       __name, rand, __money = sentence.split(' ')
       self.__name = __name
       self.__money = __money

    # def pname(self):
    #     print(self.__name, self.__money)

    @property
    def __ppas(self):
         return f'Пароль:{self.__passw}\nВозраст:{self.__age}'
    @__ppas.setter
    def password(self):
        return f'{self.__age} : {self.__passw}'

    # def print(self):
    #     print(f'Возраст:{self.__age}, Пароль:{self.__passw}')

beka = Bank('бека', 20, '0', '12345678987543')
print(beka.data)
print(beka.password)

# print(beka._money)
# beka._money = 123456789
# print(dir(Bank))
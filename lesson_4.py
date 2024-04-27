
class Human:
    height = 170
    gladness = 10


class Student(Human):
    gladness = 0


class Worker(Human):
    gladness = 100


nick = Student()
ann = Worker()
print(f'student - {nick.height}, {nick.gladness}')
print(f'student - {ann.height}, {ann.gladness}')


class GrandParent:
    height = 170
    age = 60
    gladness = 100


class Parent(GrandParent):
    age = 40


class Child(Parent):
    height = 110
    age = 10

    def __init__(self):
        print(self.age)
        print(self.height)
        print(self.gladness)


nick = Child()

class wow:

    def _hello(self):
        print('Hello')

    def __wow(self):
        print('Wow')


x = wow()
x._hello()
# x.__wow() ERROR
# x._Wow__wow() NOT RECOMMENDED


class A:
    hello = 'Hello'
    _hello = '_Hello'
    __hello = '__Hello'

    def __init__(self):
        self.world = 'world'
        self._world = '_world'
        self.__world = '__world'

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)


# A().printer()


class B(A):

    def printer_2(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)


# B().printer()


class Hello:

    def __init__(self):
        print('Hello')

class World(Hello):

    def __init__(self):
        super().__init__()
        # super().not_hello()
        print('Hello')


World()





class Computer:

    def __init__(self, model, *ards, **kwargs):
        super().__init__(*ards, **kwargs)
        self.memory = 128
        self.model = model

    def calculate(self):
        print('Calculating..')


class Display:

    def __init__(self, *ards, **kwargs):
        super().__init__(*ards, **kwargs)
        self.resolution = '4k'

    def display(self):
        print('I display image on the screen..')


class SmartPhone(Display, Computer):

    def print_info(self):
        print(self.model)
        print(self.memory)
        print(self.resolution)


phone = SmartPhone(model='SuperMax 2000')
phone.print_info()
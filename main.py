#
#
# print('Hello from PyCharm!')
#
# print('hello world!')
#
# print(
#     type(10)
# )
#
# class Student:
#     amount_of_students = 0
#     print('Hi! I am a student')
#
#     def __init__(self, height, name):
#         self.name = name
#         self.height = height
#         Student.amount_of_students +=1
#
#     def grow(self, value=1):
#         self.height += value
#
#     def __str__(self):
#         return f'I am a student. My name is {self.name}'
#
#
# john = Student(height=150, name='John')
# print(f'Johns height {john.height}')
# john.grow(20)
# print(f'Johns height after grow {john.height}')
# print(john)
#
# max = Student(height=190, name='Max')
# print(f'Maxs height {max.height}')
# print(max)
#
# print(f'We have {Student.amount_of_students} students')
#
# student = Student
#
# print(
#     type(student)
# )


import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to study...')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.gladness <=0:
            print('Depression...')
            self.alive = False
        elif self.progress < -0.5:
            print('Failed...')
            self.alive = False
        elif self.progress > 5:
            print('Passed!')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Progress - {self.progress}')

    def live(self, day):
        day = f'Day {day} of {self.name} life'
        print(f'{day:=^50}')
        cube = random.randint(1, 3)
        if cube == 1:
            self.to_study()
        elif cube == 2:
            self.to_sleep()
        elif cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

nick = Student(name='Sasha')
for day in range(1, 100000):
    if not nick.alive:
        break
    nick.live(day)
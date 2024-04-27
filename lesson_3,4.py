#
# class Human:
#
#     def __init__(self, name='Human'):
#         self.name = name
#
#
# class Auto:
#
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passenger(self, *humans):
#         for h in humans:
#             self.passengers.append(h)
#
#     def print_passengers_names(self):
#         if self.passengers:
#             print(f'Names passengers of {self.brand}:')
#             for p in self.passengers:
#                 print(p.name)
#         else:
#             print(f'There are no passengers in {self.brand}')
#
#
# kate = Human('Kate')
# nick = Human('Nick')
# car = Auto('Audi')
# car.add_passenger(kate, nick)
# car.print_passengers_names()


import random

class Human:

    def __init__(self, name, job= None, home= None, car= None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 100
        self.satiety = 100

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brand_list)

    def get_job(self):
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <=0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return

            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20
                self.shopping('fuel')
                return
            else:
                self.repair()
                return

            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4

    def shopping(self):
        pass

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def repair(self):
        self.car.strength += 100
        self.money -= 50

    def is_alive(self):
        if self.gladness < 0:
            print('Depression')
            return False
        if self.satiety < 0:
            print('Dead...')
            return False
        if self.money < -500:
            print('Bankrupt...')
            return False

    def days_index(self):
        pass

    def live(self):
        pass


class Home:

    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:


    def __init__(self, job_list):
        self.job = random.choice(job_list)
        self.salary = job_list[self.job]['salary']
        self.gladness.less = job_list[self.job]['gladness_less']


class Auto:

    def __init__(self, brand_list):
        self.brand = random.choice(brand_list)
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cannot drive!")
            return False

class Car:
    def __init__(self, color='', type='',year=''):
        self.color = color
        self.type = type
        self.year = year

    def car_start(self):
        print("Автомобиль заведен")

    def car_stop(self):
        print("Автомобиль заглушен")

    def car_year(self, year):
        self.year = year

    def car_type(self, type):
        self.type = type

    def car_color(self, color):
        self.color = color


lada = Car()
lada.car_start()
lada.car_stop()

lada.car_color('Белый')
print(lada.color)

lada.car_year('2008')
print(lada.year)

lada.car_type('Легковая')
print(lada.type)


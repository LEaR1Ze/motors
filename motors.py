


from msilib.schema import Property


class UniqueCars:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        
    def go(self):
        return "{} {} зі швидкістью {} рухаеться в Los Angeles.Поліцейська машина: {}\n".format(self.color,self.name,self.speed,self.is_police)
    def stop(self):
        return "{} {} їдучи зі швидкістью {} зупиниться біля Берліну.Поліцейська машина: {}\n".format(self.color,self.name,self.speed,self.is_police)
    def turn(self):
        return "{} {} рухаючись зі швидкістью {} поверне в сторону Пекіну.Поліцейська машина: {}".format(self.color,self.name,self.speed,self.is_police)
    def turnback(self):
        return "{} {} рухаючись зі швидкістью {} поверне назад в сторону Парижу.Поліцейська машина: {}".format(self.color,self.name,self.speed,self.is_police) 
class TownCar(UniqueCars):
    def work(self):
        a= 0
class SportCar(UniqueCars):
    def work(self):
        a= 0
class WorkCar(UniqueCars):
    def work(self):
        a= 0
class PoliceCar(UniqueCars):
    def work(self):
        a= 0
cars = [ 
UniqueCars("75 км/г", "Зелений", "Ауді", True),
UniqueCars("45 км/г", "Червоний", "Бмв", False),
UniqueCars("89 км/г", "Синій", "Мерседес", False),
UniqueCars("68 км/г", "Чорний", "Фольксваген", True)
]
for uniquecars in cars:
    uniquecars.go()
    uniquecars.stop()
    uniquecars.turn()
    uniquecars.turnback()

for num, uniquecars in enumerate(cars, start = 1):
     print("{} {}".format(num, uniquecars.go(), uniquecars.stop(), uniquecars.turn(),uniquecars.turnback()))
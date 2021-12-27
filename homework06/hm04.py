class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'текущая скорость автомобиля {self.name} равна {self.speed}'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущая скорость городского автомобиля {self.name} равна {self.speed}')
        if self.speed > 60:
            return f'текущая скорость автомобиля {self.name}  выше разрешенной'
        else:
            return f'текущая скорость {self.name} допустима для городского автомобиля'


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущая скорость рабочего автомобиля {self.name}, равна {self.speed}')
        if self.speed > 40:
            return f'текущая скорость автомобиля {self.name}  выше разрешенной'
        else:
            return f'текущая скорость {self.name} допустима для рабочей техники'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

bmw = SportCar(100, 'black', 'bmw', False)
lada = TownCar(70, 'black', 'lada', False)
honda = WorkCar(40, 'red', 'honda', False)
opel = PoliceCar(140, 'blue', 'opel', True)

print(honda.turn_left())
print(f'когда {lada.turn_right()}, тогда {bmw.stop()}')
print(f'{honda.go()} ее {honda.show_speed()}')
print(f'{honda.name} {honda.color}')
print(f'{bmw.name} это полицейская машина? {bmw.is_police}')
print(f'{opel.name} это полицейская машина? {opel.is_police}')
print(bmw.show_speed())
print(lada.show_speed())
print(opel.is_police)
print(opel.show_speed())

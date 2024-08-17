class Vehocle():
    _COLOR_VARIANTS = ('чёрный', 'белый', 'синий')
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color


    def get_model(self):
        print(f'Модель: {self.__model}')


    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')


    def get_color(self):
        print(f'Цвет: {self.__color}')


    def print_info(self):
        Sedan.get_model(self)
        Sedan.get_horsepower(self)
        Sedan.get_color(self)
        print(f'Владелец: {self.owner}')


    def set_color(self, new_color):
        if new_color.lower() in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehocle):
    pass


vehicle1 = Sedan('Федька', 'Toyota Mark IV', 600, 'чёрный')
vehicle1.print_info()

vehicle1.set_color('синИЙ')
vehicle1.set_color('РаДуЖнЫй')
vehicle1.owner = 'Васька'

vehicle1.print_info()
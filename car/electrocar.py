from car import carclass


class ElectroCar(carclass.CarClass):
    def __init__(self, brand, model, year, prob):
        super().__init__(brand, model, year, prob)
        self.battery = '100'

    def description_battery(self):
        print(f'Этот автомобиль имеет {self.battery} pfhzlf')
if __name__=='__main__':
    e_car=ElectroCar('Tesla1', 'T1', 2020, 100000)
    e_car.show_car()
    e_car.description_battery()
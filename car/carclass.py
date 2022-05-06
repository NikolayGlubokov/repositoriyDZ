class CarClass:
    def __init__(self, brand, model, year, prob):
        self.brand = brand
        self.model = model
        self.year = year
        self.prob = prob

    def show_car(self):
        print(f'{self.brand}, {self.model}, {self.year}, {self.prob}')

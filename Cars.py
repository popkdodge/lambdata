#!/usr/bin/env python

class Cars:
    
    def __init__(self, brand, year, model,price):
        self.brand = str(brand)
        self.year = int(year)
        self.model = model
        self.price = price
    def info(self):
        return print(f'This is a {self.year}, {self.brand} and it is price at {self.price}.')

class Porsche(Cars):
    def __init__(self, brand, year, model, price):
        super().__init__(brand, year, model, price)
        self.brand = "Porsche"
        self.price = 65000
    def website(self):
        print('https://www.porsche.com/usa/')
    
    def sound(self):
        print('https://www.porsche-frankfurt.de/portal/pics/hauptdomain/sounds/02_911_start_engine.mp3')


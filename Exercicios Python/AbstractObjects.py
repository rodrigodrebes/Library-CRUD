import math as mt
from abc import ABC, abstractmethod

class Forma(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Retangulo(Forma):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Forma):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return mt.pi * self.radius**2

    def perimeter(self):
        return 2 * mt.pi * self.radius

circulo = Circle(6)
print(circulo.area(), circulo.perimeter())

retangulo = Retangulo(7, 8)
print(retangulo.area(), retangulo.perimeter())

from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__(self, color):
        self.color = color
    @abstractmethod
    def obtenerArea(self):
        pass
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado
    def obtenerArea(self):
        return self.lado * self.lado
    def __str__(self):
        return f"Cuadrado(color={self.color}, lado={self.lado}, area={self.obtenerArea()})"

class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def obtenerArea(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
    def __str__(self):
        return f"Triangulo(color={self.color}, area={self.obtenerArea():.2f})"

class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio
    def obtenerArea(self):
        return math.pi * self.radio ** 2
    def __str__(self):
        return f"Redondo(color={self.color}, radio={self.radio}, area={self.obtenerArea():.2f})"